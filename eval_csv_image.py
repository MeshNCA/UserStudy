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

with open("image_questions.txt", "r") as f:
    data = f.readlines()
    for r in data:
        s = r.strip().split(" ")
        mapping[s[0]] = (s[1], s[2], s[3], s[4])




for index, row in df.iterrows():
    for i in range(1, 41):

        url = row[f'Input.url{i}']
        image_name = url.split("/")[-1][:-4]
        answer = int(row[f'Answer.question{i}'][-1]) - 1
        method_scores[mapping[image_name][answer]] += 1

print(method_scores)

# for i in range(1, 41):