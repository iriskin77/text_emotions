from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import File
from .serializer import FileSerializer
from .utils import process_file_data
from wsgiref.util import FileWrapper
from django.http import FileResponse
# Create your views here.

class FileApiList(generics.ListAPIView):

    queryset = File.objects.all()
    serializer_class = FileSerializer


@api_view(['POST'])
def upload_file(request):
    if request.method == 'POST':
        serialized_data = FileSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response({"Result": 201, "Data": serialized_data.data})
        else:
            return Response({"Result": 500, "Error": serialized_data.errors})

    else:
        return Response({"This method is not allowed": 405})


@api_view(['PUT'])
def process_file(request, pk=None):

    if request.method == 'PUT':

        obj = File.objects.get(id=pk)
        name_column = obj.name_column
        file_path = obj.file.path
        data, status = process_file_data(file_path, name_column)

        if status:
            data.to_excle(file_path)
            obj.status = True
            obj.save()
            return Response(status=204)

        return Response(status=500)

    else:
        return Response({'This method is not allowed': 405})


@api_view(['GET'])
def download_file(request, pk=None):

    if request.method == 'GET':

        obj = File.objects.get(id=pk)
        document = open(obj.file.path, 'rb')
        response = FileResponse(FileWrapper(document), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="%s"' % obj.file.name
        return response

    else:
        return Response({'This method is not allowed': 405})
