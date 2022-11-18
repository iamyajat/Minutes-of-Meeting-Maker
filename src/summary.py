from simplet5 import SimpleT5

model = SimpleT5()
model.load_model("t5", "./assets/model", use_gpu=False)


def get_mom(text, progress_bar):
    dialogues = text.split("\n")
    points = []
    i = 0
    while i < len(dialogues):
        chunk = ""
        while (len(chunk) + len(dialogues[i])) <= 400:
            chunk = chunk + "\n" + dialogues[i]
            i = i + 1
            if i >= len(dialogues):
                break
        if len(chunk) == 0 and i < len(dialogues) and len(dialogues[i]) > 400:
            chunk = dialogues[i]
            i = i + 1
            print("here")
        points.append(summarize(chunk)[0])

        progress_bar.progress((i / len(dialogues)))
        print(f"Chunk {i} done out of {len(dialogues)}")

        if(i >= len(dialogues)):
            break 

    return points


def summarize(text):
    return model.predict(text)
