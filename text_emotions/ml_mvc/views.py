from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from .models import FileModel
from .forms import ProcessFileForm
from .utils import process_file_data
from wsgiref.util import FileWrapper
from django.core.paginator import Paginator


def upload_file(request):
    if request.method == 'POST':
        form = ProcessFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            files = FileModel.objects.all().order_by('-date')
            return render(request, 'list_files.html', {'list_files': files})
        else:
            return render(request, 'upload_file.html', {'form': form})
    else:
        form = ProcessFileForm()
        return render(request, 'upload_file.html', {'form': form})


def process_file(request, pk):

    files = FileModel.objects.all().order_by('-date')
    obj = FileModel.objects.get(id=pk)
    data, status = process_file_data(obj.file, obj.name_column)
    paginator = Paginator(files, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if status:
        data.to_excel(obj.file.path)
        obj.status = True
        obj.save()
        return render(request, 'list_files.html', {'list_files': files, 'page_obj' : page_obj})
    else:
        pass


def download_file(request, pk):

    file = FileModel.objects.get(id=pk).file
    document = open(file.path, 'rb')
    response = FileResponse(FileWrapper(document), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="%s"' % file.name
    return response


def show_list_files(request):
    files = FileModel.objects.all().order_by('-date')
    paginator = Paginator(files, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'list_files.html', {'list_files': files, 'page_obj': page_obj})


def about(request):
    return render(request, 'about.html')


def show_api(request):
    pass
