# import & set path for csv file
import os
import csv

pypoll_csv = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

# create variables, lists, & dictionaries to store information
total_count = 0
candidate_list = []
candidate_count = {}
candidate_votes = []
candidate_percentage = []
winner = ""
winning_votes = 0
cleaned_data = []

with open(pypoll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

# total number of votes cast
    for row in csvreader:
        total_count = total_count + 1

# compile complete list of candidates and their total votes received
        candidate = row[2]
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            candidate_count[candidate] = 0
            candidate_count[candidate] = candidate_count[candidate] + 1
        else:
            candidate_count[candidate] = candidate_count[candidate] + 1

# percentage of votes each candidate received    
    for key, value in candidate_count.items():
        candidate_votes.append(value)
        votes = candidate_count[candidate]
        percentage = round((int(value) / total_count * 100), 3)
        candidate_percentage.append(percentage)

# winner based on popular vote
        if (value > winning_votes):
            winning_votes = value
            winner = key

# clean data for easier display
    cleaned_data = zip(candidate_list, candidate_percentage, candidate_votes)
    cleaned_data = list(cleaned_data)

# print analysis to terminal
print("Election Results")
print("-----------------------------------------")
print(f'Total Votes: {str(total_count)}')
print("-----------------------------------------")
for i in cleaned_data:
    print(f'{i[0]}: {i[1]}% ({i[2]})')   
print("-----------------------------------------")
print(f'Winner: {winner}')
print("-----------------------------------------")

# export analysis as text file
output_file = os.path.join("..", "PyPoll", "Analysis", "PyPoll_Analysis.csv")
with open(output_file, "w", newline="") as datafile:
    csvwriter = csv.writer(datafile)
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["----------------------------------------"])
    csvwriter.writerow([f'Total Votes: {str(total_count)}'])
    csvwriter.writerow(["----------------------------------------"])
    for i in cleaned_data:
        csvwriter.writerow([f'{i[0]}: {i[1]}% ({i[2]})'])
    csvwriter.writerow(["----------------------------------------"])
    csvwriter.writerow([f'Winner: {winner}'])
    csvwriter.writerow(["----------------------------------------"])