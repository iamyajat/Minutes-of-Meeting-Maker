from simplet5 import SimpleT5

model = SimpleT5()
model.load_model(
    "t5", "./assets/model", use_gpu=False
)


def summarize(text):
    return model.predict(text)
