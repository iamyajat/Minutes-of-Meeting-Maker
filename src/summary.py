from simplet5 import SimpleT5

model = SimpleT5()
model.load_model(
    "t5", "./assets/t5-epoch-9-train-loss-0.517-val-loss-1.9625", use_gpu=False
)


def summarize(text):
    return model.predict(text)
