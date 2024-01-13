from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.


class FileModel(models.Model):

    name_file = models.CharField(max_length=255, verbose_name="Название файла")
    author_file = models.CharField(max_length=255, blank=True, verbose_name="Автор файла")
    name_column = models.CharField(max_length=255, null=False, verbose_name="Название колонки")
    file = models.FileField(upload_to="files_ml_api/", validators=[FileExtensionValidator(['xlsx'])], verbose_name="Файл")
    status = models.BooleanField(default=False, blank=True, verbose_name="Статус обработки")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    def __str__(self):
        return self.name_file
