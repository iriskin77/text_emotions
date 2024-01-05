import json
from django.apps import AppConfig
from keras.models import load_model
from keras.preprocessing.text import Tokenizer, tokenizer_from_json
from pathlib import Path

class MlApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ml_api"

    abs_path = Path(__file__).resolve().parent.parent

    model = load_model(rf"{abs_path}/texts_emotions/model/best_model_LSTM10000_2.h5")

    with open(rf'{abs_path}/texts_emotions/model/tokenizer_json.json') as file:
        data = json.load(file)
        tokenizer = tokenizer_from_json(data)
