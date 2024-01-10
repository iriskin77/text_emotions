#### Описание

API для нейросети, которая определяет тональность комментариев.
Сслыка на репозиторий с нейросетью: <code>[LSTM_model](https://github.com/iriskin77/model_sent_analysis)</code>

#### Как это работает

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

#### Как установить
