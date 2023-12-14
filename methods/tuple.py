# country = ("spain","india","nepal","bang", "odisha", "kerala") #these() brackets are use for tuple thses() tuples are non editable
# print(type(country))
# print(len(country))
# print(country[0])
# print(country[-1])
# print(country[-2])
# import time
# t = time.strftime('%H:%M:%S')
# hour = int(time.strftime('%H'))
# hour = int(input("enter hour : "))
# print(hour)
# if ( hour>0 and hour<12):
#     print("good morning sir")
# elif (hour>=12 and hour<17):
#     print("good afternoon")
# else:
#     print("good night")
ques = [
    ["what is the name of the vitamin provided by the sun","vitamin a","vitamin b", "vitamin c","vitamin d",4],
    ["what is the name of the vitamin provided by the sun","vitamin a","vitamin b", "vitamin c","vitamin d",4],
    ["what is the name of the vitamin provided by the sun","vitamin a","vitamin b", "vitamin c","vitamin d",4],
    ["what is the name of the vitamin provided by the sun","vitamin a","vitamin b", "vitamin c","vitamin d",4],
    ["what is the name of the vitamin provided by the sun","vitamin a","vitamin b", "vitamin c","vitamin d",4],
    ["what is the name of the vitamin provided by the sun","vitamin a","vitamin b", "vitamin c","vitamin d",4],
    ["what is the name of the vitamin provided by the sun","vitamin a","vitamin b", "vitamin c","vitamin d",4],
    ["what is the name of the vitamin provided by the sun","vitamin a","vitamin b", "vitamin c","vitamin d",4],
    ]
levels = [1000,2000,3000,5000,10000,20000,40000,80000,100000]
money = 0
for i in range(0,len(ques)):
    question = ques[i]
    print(f"\n\n the question for rs.{levels[i]}")
    print(f"a.{question[1]}               b.{question[2]}")
    print(f"c.{question[3]}               d.{question[4]}")
    reply = int(input("enter correct answer in btw (1-4) or press 0 to exit: \n"))
    if (reply == 0):
        money = levels[i-1]
        break
    if (reply == question[5]):
        print(f"your answer is correct, you have won {levels[i]}")
        if (i == 4):
            money = 10000
        elif (i == 6):
            money = 40000
        elif(i == 8 ):
            money = 100000
    else:
        print("your answer is wrong")
        break
print(f"the total amount you won is {money}")