import pandas as pd
from pymystem3 import Mystem
from keras.utils import pad_sequences
from .apps import MlMvcConfig

def process_file_data(path: str, name_column: str):

    try:
        data_comments = pd.read_excel(path)[name_column]
        model = MlMvcConfig.model
        tokenizer = MlMvcConfig.tokenizer
        m = Mystem()
        commentaries = []
        score = []
        marks = []

        for comment_index in range(len(data_comments)):
            if type(data_comments[comment_index]) == str:
                lst_lemm = m.lemmatize(data_comments[comment_index])
                prep = [word.strip(r'!?"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n').lower() for word in lst_lemm if word.isalpha()]
                sequence = tokenizer.texts_to_sequences([' '.join(prep)])
                sequence = pad_sequences(sequence, 64)
                score = model.predict(sequence)

                if score[[0]] > 0.9:
                    commentaries.append(data_comments[comment_index])
                    marks.append('Отрицательный')
                    score.append(score)

                elif 0.9 > score[[0]] > 0.4:
                    commentaries.append(data_comments[comment_index])
                    marks.append('Нейтральный')
                    score.append(score)

                else:
                    commentaries.append(data_comments[comment_index])
                    marks.append('Положительный')
                    score.append(score)

        data = pd.read_excel(path)
        headers = list(data.columns.values)
        data.drop(headers, axis=1, inplace=True)
        data['Сообщение'] = commentaries
        data['Класс'] = marks
        data['Коэффициент'] = score

        return data, True

    except:

        return None, False


