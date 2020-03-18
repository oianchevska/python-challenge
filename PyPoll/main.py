import os
import csv

file_path=os.path.join(".","Resources","election_data.csv")
with open (file_path) as election_data:
    reader=csv.reader(election_data,delimiter=',')
    header=next(reader)
    print(header)

    total_voter=0
    candidate=dict()

    for data in reader:
        total_voter+=1
        #print(data)

        candidate[data[2]]=candidate.get(data[2],0)+1
    print(candidate)

    for c in candidate.items():
        print(c)


