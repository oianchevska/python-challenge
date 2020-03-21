# Import Dependencies
import os
import csv

# Open and read csv file
file_path = os.path.join(".", "Resources", "election_data.csv")

with open(file_path) as election_data:

    reader = csv.reader(election_data, delimiter=',')

    # Skip the header
    header = next(reader)

    # Calculate the total number of votes and for each candidate
    total_voter = 0
    candidate = dict()
    for data in reader:
        total_voter += 1
        candidate[data[2]] = candidate.get(data[2], 0) + 1

# Use lambda to retrieve data as a sorted list
can = candidate.items()
can = sorted(can, reverse=True, key=lambda x: x[1])

# Export the results to a text file and print to the terminal
with open("Result.txt", "w") as pypoll_result:

    pypoll_result.write("Election Results" + "\n")
    pypoll_result.write("-" * 25 + "\n")
    pypoll_result.write("Total Votes: " + str(total_voter) + "\n")
    pypoll_result.write("-" * 25 + "\n")

    print("Election Results")
    print('-' * 25)
    print("Total Votes: " + str(total_voter))
    print('-' * 25)

    for c in can:
        s = f"{c[0]}: {c[1]/total_voter*100:.3}% ({c[1]})"
        pypoll_result.write(s + "\n")
        print(s)

    pypoll_result.write("-" * 25 + "\n")
    pypoll_result.write("Winner: " + str(can[0][0]) + "\n")
    pypoll_result.write("-" * 25 + "\n")

    print("-" * 25)
    print("Winner: " + str(can[0][0]))
    print("-" * 25)