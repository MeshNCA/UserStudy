import pandas as pnd
import numpy as np

csv_file = "results.csv"

df = pnd.read_csv(csv_file)

method_scores = {
    "meshnca": 0,
    "text2mesh": 0,
    "xmesh": 0,
}

mapping = {

}

with open("questions.txt", "r") as f:
    data = f.readlines()
    for r in data:
        s = r.strip().split(" ")
        target = r[:-25]
        mapping[target] = (s[-3], s[-2], s[-1])


def sanity_check(row):
    return True
    answer31 = int(row[f'Answer.question31'][-1])
    answer32 = int(row[f'Answer.question32'][-1])
    answer38 = int(row[f'Answer.question38'][-1])

    answer11 = int(row[f'Answer.question11'][-1])
    answer25 = int(row[f'Answer.question25'][-1])

    if answer11 == 1:  # stained glass vase
        return False
    if answer31 == 1:  # stained glass chair
        return False
    if answer32 == 1:  # colorful crochet bunny
        return False
    if answer38 == 3:  # patchwork leather bunny
        return False

    if answer25 == 3:
        return False

    # answer23 = int(row[f'Answer.question23'][-1])
    # if answer23 != 1: # mug sandstone
    #     return False

    return True

# import matplotlib.pyplot as plt
# plt.hist(df['WorkTimeInSeconds'], bins=30)
# plt.show()

print(df[df['WorkTimeInSeconds'] < 200]['WorkerId'])

df = df[df['WorkTimeInSeconds'] > 200]


for index, row in df.iterrows():
    if not (sanity_check(row)):
        print("Discarding row ", index + 1)
        continue
    for i in range(1, 51):
        # if i in [11, 31, 32, 38, 25]:
        #     pass

        url = row[f'Input.url{i}']
        image_name = url.split("/")[-1][:-4]
        answer = int(row[f'Answer.question{i}'][-1]) - 1
        method_scores[mapping[image_name][answer]] += 1



total = sum(method_scores[k] for k in method_scores)
proportions = {k: method_scores[k] / total for k in method_scores}
print(total)

errors = {k: np.sqrt(proportions[k] * (1.0 - proportions[k]) / (total)) for k in proportions}

precentage = {k: f"{100 * method_scores[k] / total:2.1f}%" for k in method_scores}
errors = {k: f"{100 * errors[k]:1.1f}%" for k in method_scores}

print(precentage, errors)

# print(df['WorkTimeInSeconds'].sort_values())