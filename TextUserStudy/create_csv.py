import pandas as pnd
import random
import numpy as np

num_questions = 50
df = pnd.DataFrame(columns=["exp_id", "question"] + [f"url{i}" for i in range(1, num_questions + 1)])

base_url = "https://raw.githubusercontent.com/MeshNCA/UserStudy/main/TextUserStudy/questions"


# p10_armadillo.png


def create_row(id):
    exp_id = id
    question = "Choose the option that better matches the following description: An Image of an \"Object\" made of \"Reference Material\"."

    selection_set = {}
    mesh_names = ["bunny", "alien", "chair", "mug", "vase"]
    texture_names = [
        "bark", "cactus", "colorful crochet", "feathers", "jelly beans",
        "marble", "moss", "patchwork leather", "sandstone", "stained glass"
    ]
    options = [f"{t}_{m}" for t in texture_names for m in mesh_names]

    options.remove("feathers_alien")
    options.remove("moss_bunny")
    options.remove("bark_bunny")
    options.remove("stained glass_chair")

    selected_options = np.random.choice(options, num_questions - 4, False)
    urls = [f"{base_url}/{s}.png" for s in selected_options]

    urls.insert(9, f"{base_url}/moss_bunny.png")  # option 1
    urls.insert(21, f"{base_url}/feathers_alien.png")  # option 3
    urls.insert(30, f"{base_url}/stained glass_chair.png")  # not option 1
    urls.insert(43, f"{base_url}/bark_bunny.png")  # option 2

    # urls[5] = f"{base_url}/p12_armor.png" # 2
    # urls[21] = f"{base_url}/p14_mobius.png" # 1
    # urls[33] = f"{base_url}/p6_springer.png" # 2

    row = [exp_id, question] + urls

    return row


for i in range(1):
    df.loc[i] = create_row(i)

df.to_csv("questions.csv", index=False)
