import os
import csv

py_bank_path=os.path. join('.','Resources','budget_data.csv')
with open (py_bank_path) as py_bank_data:
    budget_reader=csv.reader(py_bank_data,delimiter=',')
    csv.header=next(budget_reader)

    #total=0
    #sum_budget=0
    budget_list=[]
    for budget in budget_reader:
      #total+=1
      #sum_budget+=int(budget[1])
      budget_list.append(float(budget[1]))
      #print(budget[0])
      #print (total)
      #print (sum_budget)
      #print (a)

    print("Total months: "+ str(len(budget_list)))
    print("Total: " + str(sum(budget_list)))

    #a1=[int(data[1]) for data in budget_reader]

    #print (sum(a1))
   # print(len(a1))


#     result=[]
#     a=int(next(budget_reader)[1])
#     print(a)
#     for i in budget_reader:
#         print(i)
#         c=int(i[1])-a
#         a=int(i[1])
#         result.append(c)
#
# print(max(result))
    #print(a)
    change_list=[]
    for i in range(len(budget_list)-1):
        #print(i)
        #print(a[i])
        f=budget_list[i+1]-budget_list[i]
        change_list.append(f)

    average_change=(sum(change_list)/len(change_list))
    print ("Average change:" + str(average_change))
    print("Greatest Increase in Profits:" + str(max(change_list)))
    print("Greatest Decrease in Profits:" + str(min(change_list)))
