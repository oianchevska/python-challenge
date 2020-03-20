import os
import csv


def max_d(d):
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]

file_path=os.path.join(".","Resources","election_data.csv")


with open (file_path) as election_data:

    reader=csv.reader(election_data,delimiter=',')
    header=next(reader)
    #print(header)

    total_voter=0
    candidate=dict()

    for data in reader:
        total_voter+=1

        candidate[data[2]]=candidate.get(data[2],0)+1

    #print(candidate)
    fun=max_d(candidate)

can=candidate.items()
can=sorted(can,reverse=True,key=lambda x:x[1])

with open("Result.txt","w") as pypoll_result:
    pypoll_result.write("Election Results"+"\n")
    pypoll_result.write ("-"*20+ "\n")
    pypoll_result.write("Total Votes: "+ str(total_voter)+ "\n")
    pypoll_result.write("-"*20+ "\n")



    print("Election Results")
    print('-'*20)
    print("Total Votes: " + str(total_voter))
    print('-'*20)

    for cand in can:
    #print(cand[0]+ ":" , str(round((cand[1]/total_voter)*100,3)) + "%", cand[1])
        s=f"{cand[0]}: {cand[1]/total_voter*100:.3}% ({cand[1]})"
        pypoll_result.write(s + "\n")

        print(s)

    #print(candidate)
    #print(total_voter)
    #for c in candidate.items():
        #print(c)
    pypoll_result.write("-" * 20 + "\n")
    pypoll_result.write("Winner: " + fun+ "\n")
    pypoll_result.write("-" * 20 + "\n")
    print("-"*20)
    print("Winner: " + fun)
    print("-" * 20)




