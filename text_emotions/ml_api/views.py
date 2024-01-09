from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework import generics, status
from .models import FileModel
from .serializer import FileSerializer
from .utils import process_file_data
from wsgiref.util import FileWrapper
from django.http import FileResponse
from rest_framework.parsers import FormParser, MultiPartParser
from django.forms.models import model_to_dict

# Create your views here.


class FileApiList(generics.ListAPIView):

    queryset = FileModel.objects.all()
    serializer_class = FileSerializer


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def upload_file(request):

    if request.method == 'POST':
        serialized_data = FileSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response({"response status": status.HTTP_201_CREATED, "data": serialized_data.data})
        else:
            return Response({"Result": status.HTTP_500_INTERNAL_SERVER_ERROR, "Error": serialized_data.errors})
    else:
        return Response({"This method is not allowed": status.HTTP_405_METHOD_NOT_ALLOWED})


@api_view(['PUT'])
@parser_classes([MultiPartParser, FormParser])
def process_file(request, pk=None):

    if request.method == 'PUT':

        file = FileModel.objects.get(id=pk)
        name_column = file.name_column
        file_path = file.file.path
        df = process_file_data(file_path, name_column)
        df.to_excel(file_path)
        file.status = True
        file.save()
        data = model_to_dict(file)
        serialized_data = FileSerializer(data=data)

        if serialized_data.is_valid():
            serialized_data.save()
            return Response({"response status": status.HTTP_200_OK, "data": serialized_data.data})

        return Response({"response status": status.HTTP_500_INTERNAL_SERVER_ERROR, 'error': serialized_data.errors})

    else:
        return Response({'This method is not allowed': status.HTTP_405_METHOD_NOT_ALLOWED})


@api_view(['GET'])
def download_file(request, pk=None):

    if request.method == 'GET':

        file = FileModel.objects.get(id=pk)
        document = open(file.file.path, 'rb')
        response = FileResponse(FileWrapper(document), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="%s"' % file.file.name
        return response

    else:
        return Response({'This method is not allowed': status.HTTP_405_METHOD_NOT_ALLOWED})
