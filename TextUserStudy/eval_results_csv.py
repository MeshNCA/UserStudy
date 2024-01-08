import pandas as pnd

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
    answer31 = int(row[f'Answer.question31'][-1])
    answer32 = int(row[f'Answer.question32'][-1])
    answer38 = int(row[f'Answer.question38'][-1])

    answer11 = int(row[f'Answer.question11'][-1])

    if answer11 == 1: # stained glass vase
        return False
    if answer31 == 1: # stained glass chair
        return False
    if answer32 == 1: # colorful crochet bunny
        return False
    if answer38 == 3: # patchwork leather bunny
        return False

    answer23 = int(row[f'Answer.question23'][-1])
    if answer23 != 1: # mug sandstone
        return False

    return True


for index, row in df.iterrows():
    if not (sanity_check(row)):
        print("Discarding row ", index + 1)
        continue
    for i in range(1, 51):
        # if i in [6, 22, 34]:
        #     continue

        url = row[f'Input.url{i}']
        image_name = url.split("/")[-1][:-4]
        answer = int(row[f'Answer.question{i}'][-1]) - 1
        method_scores[mapping[image_name][answer]] += 1

print(method_scores)

print(df['Answer.question50'])

# for i in range(1, 41):
