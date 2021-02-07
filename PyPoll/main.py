# hi
import os
import csv

PyPoll_csv = os.path.join("Resources/election_data.csv")
output = ".Analysis/output.txt"

can_dict = {}
v_count = 0
count = 0
v_percent = 0
winner = ""

with open(PyPoll_csv, newline = "") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csv_reader)