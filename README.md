## Описание

API для нейросети, которая определяет тональность комментариев.
Сслыка на репозиторий с нейросетью: <code>[LSTM_model](https://github.com/iriskin77/model_sent_analysis)</code>

Детальное описание API можно посмотреть на swagger:

 + http://127.0.0.1:8080/api/v1/swagger/ 

## Как это работает

Набор api позволяют загружать файл, просматривать загруженные файлы, а также скачивать. Кроме того, по API можно
определить тональность комментариев, которые содержаться в файле.

+ GET api/v1/fileslist/
+ GET api/v1/fileslist/<int:pk>/
+ GET api/v1/download_file/<int:pk>
+ POST api/v1/upload_file/
+ PUT api/v1/process_file/<int:pk>/

Визуально это выглядит следующим образом:

![](https://github.com/iriskin77/text_emotions/blob/master/images/api_model.png)

Результаты работы:

Файл до обработки:

![](https://github.com/iriskin77/text_emotions/blob/master/images/before_model.png)

Файл после обработки:

![](https://github.com/iriskin77/text_emotions/blob/master/images/res_model.png)

## Как это использовать

1) Добавить файл через POST запрос: 
 + http://127.0.0.1:8080/api/v1/upload_file/ 
+ Например, это можно сделать через Postman:
  
![](https://github.com/iriskin77/text_emotions/blob/master/images/postman_upfile.png)

В качестве ответа будет Json с id файла

   ```json
    {
    "response status": 201,
    "data": {
        "id": 13,
        "name_file": "Текст для обработки",
        "author_file": "",
        "name_column": "Сообщение",
        "file": "/media/files_ml_api/Test.xlsx",
        "status": false,
        "date": "2024-01-16T09:07:48.903831Z"
    }
}
  ```

2) Использовать PUT запрос, чтобы обработать файл: 
 + http://127.0.0.1:8080/api/v1/process_file/<int:pk>


3) Использовать GET запрос, чтобы скачать файл:
 + http://127.0.0.1:8080/api/v1/download_file/<int:pk>

## Как установить

+ Клонировать репозиторий: git clone

+ Использовать команду docker-compose build

+ Использовать команду docker-compose up

После этого будет создать docker контейнер на порту 8080:

http://127.0.0.1:8080

