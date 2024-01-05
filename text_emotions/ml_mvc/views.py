from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from .models import FileModel
from .forms import ProcessFileForm
from .utils import process_file_data
from wsgiref.util import FileWrapper
def upload_file(request):
    if request.method == 'POST':
        form = ProcessFileForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            return render(request, 'process_file.html', {'form' : form})
        else:
            return render(request, 'index.html')
    else:
        form = ProcessFileForm()
        return render(request, 'upload_file.html', {'form' : form})


def proc_file(request):

    if request.method == 'PUT':

        obj = FileModel.objects.all().last()
        df = process_file_data(obj.file, obj.name_column)
        df.to_excel(obj.file.path)
        obj.status = True
        obj.save()
        return render(request, 'download.html')

    else:
        return None


def download_file(request):
    file = FileModel.objects.all().last().file
    document = open(file.path, 'rb')
    response = FileResponse(FileWrapper(document), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="%s"' % file.name
    return response


def about(request):
    return render(request, 'about.html')
