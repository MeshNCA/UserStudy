import pandas as pnd

csv_file = "results.csv"

df = pnd.read_csv(csv_file)

method_scores = {
    "meshnca": 0,
    "text2mesh": 0,
    "diffrd": 0,
    "ondemand": 0
}

mapping = {

}

with open("questions.txt", "r") as f:
    data = f.readlines()
    for r in data:
        s = r.strip().split(" ")
        mapping[s[0]] = (s[1], s[2], s[3], s[4])


def sanity_check(row):
    answer6 = int(row[f'Answer.question6'][-1])
    answer22 = int(row[f'Answer.question22'][-1])
    answer34 = int(row[f'Answer.question34'][-1])

    return answer6 == 2 and answer22 == 1 and answer34 == 2


for index, row in df.iterrows():
    if not(sanity_check(row)):
        print("Discarding row ", index + 1)
        continue
    for i in range(1, 41):
        if i in [6, 22, 34]:
            continue
        url = row[f'Input.url{i}']
        image_name = url.split("/")[-1][:-4]
        answer = int(row[f'Answer.question{i}'][-1]) - 1
        method_scores[mapping[image_name][answer]] += 1

print(method_scores)

# for i in range(1, 41):