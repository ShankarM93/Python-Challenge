#Creating path file and CSV files
import os
import csv

#Setting file path
file = os.path.join("C:\\Users\\Admin\\Desktop\\Python-Challenge\\Pypoll\\\Resources\\election_data.csv")

# Opening the CSV
with open(file, newline='') as csvfile:

    # CSV reader specifiing the delimiter and variable that holds contents within the file
    csvreader = csv.reader(csvfile, delimiter=',')

    # Reading the first row (header)
    csv_header = next(csvreader)

    candidate_list = [candidate[2] for candidate in csvreader]
    
# Calculating total votes 
total_votes = len(candidate_list)

# Creating candiate list nd vote counts
canditates_info = [[candidate,candidate_list.count(candidate)] for candidate in set(candidate_list)]

# Sorting the list so that the first candidate becomes the winner 
canditates_info = sorted(canditates_info, key=lambda x: x[1], reverse=True)

# Printing Results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate in canditates_info:
    percent_votes = (candidate[1] / total_votes) * 100
    print(f'{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})')

print("-------------------------")
print(f"Winner: {canditates_info[0][0]}")
print("-------------------------")


#  Printing the  election results to text file 
filepath = os.path.join('.', 'Resources', 'PyPoll_Results.txt')
with open(filepath, "w") as text_file:
    print("Election Results", file=text_file)
    print("-------------------------", file=text_file)
    print(f"Total Votes: {total_votes}", file=text_file)
    print("-------------------------", file=text_file)

    for candidate in canditates_info:
        percent_votes = (candidate[1] / total_votes) * 100
        print(f'{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})', file=text_file)

    print("-------------------------", file=text_file)
    print(f"Winner: {canditates_info[0][0]}", file=text_file)
    print("-------------------------", file=text_file)
