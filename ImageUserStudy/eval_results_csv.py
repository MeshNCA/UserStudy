import pandas as pnd
import numpy as np

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
    return True
    answer6 = int(row[f'Answer.question6'][-1])
    answer22 = int(row[f'Answer.question22'][-1])
    answer34 = int(row[f'Answer.question34'][-1])

    return answer6 == 2 and answer22 == 1 and answer34 == 2


print(len(df['WorkerId']))
print(len(df['WorkerId'].unique()))

duplicate_workers = duplicate_names = df['WorkerId'][df['WorkerId'].duplicated(keep=False)]
duplicate_workers = duplicate_workers.unique()

for worker_id in duplicate_workers:
    sub_df = df[df['WorkerId'] == worker_id]
    first_submission = sub_df['SubmitTime'].min()
    df.loc[(df['WorkerId'] == worker_id) & (
            df[
                'SubmitTime'] > first_submission), 'Reject'] = "You've submitted more than one HIT. Only your first submission is accepted."
    # print(sub_df[['AcceptTime', 'SubmitTime']])

# df.loc[df['WorkTimeInSeconds'] > 200]

df.loc[df['Reject'].isna(), 'Approve'] = 'x'
df.to_csv("rejections.csv")

df = df[df['Reject'].isna()]

# df = df[~df['WorkerId'].isin(duplicate_workers)]


# df = df[df['WorkTimeInSeconds']  200]


for index, row in df.iterrows():
    if not (sanity_check(row)):
        print("Discarding row ", index + 1)
        continue
    for i in range(1, 41):
        if i in [6, 22, 34]:
            pass
        url = row[f'Input.url{i}']
        image_name = url.split("/")[-1][:-4]
        answer = int(row[f'Answer.question{i}'][-1]) - 1
        method_scores[mapping[image_name][answer]] += 1

# print(df[['AcceptTime', 'SubmitTime']])


total = sum(method_scores[k] for k in method_scores)
proportions = {k: method_scores[k] / total for k in method_scores}
print(total)

errors = {k: np.sqrt(proportions[k] * (1.0 - proportions[k]) / (total)) for k in proportions}

precentage = {k: f"{100 * method_scores[k] / total:2.1f}%" for k in method_scores}
errors = {k: f"{100 * errors[k]:1.1f}%" for k in method_scores}

print(precentage, errors)

# print(df['WorkTimeInSeconds'].sort_values())
