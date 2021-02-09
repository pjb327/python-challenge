# hi
import os
import csv

PyPoll_csv = os.path.join("Resources/election_data.csv")
output = ".Analysis/output.txt"

can_dict = {"Candidate": [], "Vote Percent": [], "Votes": []}
v_count = 0
count = 0
v_percent = 0
winner = ""
each_can = []


with open(PyPoll_csv, newline = "") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csv_reader)
    for x in csv_reader:
        count = count + 1
        can_dict["Candidate"].append(x[2])
        if x[2] not in can_dict["Candidate"]:
            can_dict["Candidate"].append(x[2])
    for y in can_dict["Candidate"]:
        can_dict["Votes"].append(each_can.count(y))
    for z in can_dict["Votes"]:
        v_percent = (z/count) * 100
        can_dict["Vote Percent"].append(round(v_percent, 3))
    v_win = max(can_dict["Votes"])
    v_index = can_dict["Votes"].index(v_win)
    winner = can_dict["Candidate"][v_index]
            # if x[2] in can_dict['Candidate']:
        #     can_dict['Votes'] = can_dict['Votes'] + 1
        # else:
        #     can_dict['Candidate'].append(x[2])
        #     can_dict['Votes'].append(1)
# for i in can_dict['Candidate']:
#     index = can_dict['Candidate'].index(i)
print("Financial Analysis")
print(f"Total Votes: {count}")
for a in can_dict["Candidate"]:
    index = can_dict["Candidate"].index(a)
    print(f"{a}: {can_dict['Vote Percent'][index]}% ({can_dict['Votes'][index]})")
print(f"Winning candidate: {winner}")

with open('output.txt', 'w') as text:
    text.write(f"Financial Analysis\nTotal Votes: {count}\nWinning candidate: {winner}")
    for b in can_dict["Candidate"]:
        bndex = can_dict["Candidate"].index(b)
        print(f"{b}: {can_dict['Vote Percent'][bndex]}% ({can_dict['Votes'][bndex]})")