import json
import random

def load_json(location):

    with open(location, encoding="utf8") as f:
        data = json.load(f)

    return data

def random_number(max_int):
    return random.randint(0, max_int)

sample_texts = load_json("data/meeting-transcript-summarization-dataset/test.json")

show_text = sample_texts[random_number(len(sample_texts))]["dialogue"]