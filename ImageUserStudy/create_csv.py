import pandas as pnd
import random
import numpy as np

num_questions = 40
df = pnd.DataFrame(columns=["exp_id", "question"] + [f"url{i}" for i in range(1, num_questions + 1)])

base_url = "https://raw.githubusercontent.com/MeshNCA/UserStudy/main/ImageUserStudy/questions"
# p10_armadillo.png

def create_row(id):
    exp_id = id
    question = "Which option better matches the style of the reference image?"

    selection_set = {}
    mesh_names = ["mobius", "bunny", "dragon", "armor", "armadillo", "springer"]
    options = [f"p{i}_{m}" for i in range(1, 25) for m in mesh_names]

    # options.remove("p12_armor")
    # options.remove("p14_mobius")
    # options.remove("p6_springer")

    selected_options = np.random.choice(options, num_questions, False)
    urls = [f"{base_url}/{s}.png" for s in selected_options]

    # urls[5] = f"{base_url}/p12_armor.png" # 2
    # urls[21] = f"{base_url}/p14_mobius.png" # 1
    # urls[33] = f"{base_url}/p6_springer.png" # 2

    row = [exp_id, question] + urls

    return row


for i in range(40):
    df.loc[i] = create_row(i)

df.to_csv("questions.csv", index=False)
