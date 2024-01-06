import pandas as pd
from pymystem3 import Mystem
from keras.utils import pad_sequences
from .apps import MlMvcConfig

def process_file_data(path, name_column):

    try:
        data_comments = pd.read_excel(path)[name_column]
        model = MlMvcConfig.model
        tokenizer = MlMvcConfig.tokenizer
        m = Mystem()
        lst_add_commentaries = []
        lst_add_score = []
        lst_add_mark = []

        for comment_index in range(len(data_comments)):
            if type(data_comments[comment_index]) == str:
                lst_lemm = m.lemmatize(data_comments[comment_index])
                prep = [word.strip(r'!?"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n').lower() for word in lst_lemm if word.isalpha()]
                sequence = tokenizer.texts_to_sequences([' '.join(prep)])
                sequence = pad_sequences(sequence, 64)
                score = model.predict(sequence)

                if score[[0]] > 0.9:
                    lst_add_commentaries.append(data_comments[comment_index])
                    lst_add_mark.append('Отрицательный')
                    lst_add_score.append(score)

                elif 0.9 > score[[0]] > 0.4:
                    lst_add_commentaries.append(data_comments[comment_index])
                    lst_add_mark.append('Нейтральный')
                    lst_add_score.append(score)

                else:
                    lst_add_commentaries.append(data_comments[comment_index])
                    lst_add_mark.append('Положительный')
                    lst_add_score.append(score)

        data = pd.read_excel(path)
        headers = list(data.columns.values)
        data.drop(headers, axis=1, inplace=True)
        data['Сообщение'] = lst_add_commentaries
        data['Класс'] = lst_add_mark
        data['Коэффициент'] = lst_add_score

        return data, True

    except Exception as ex:
        print("Error:", ex)
        return None, False
