import os
os.system("cls")
x= lambda a : a+10
y = lambda a, b : a*b
print(x(5))
print(y(4,6))
print("-----------------------------")

score_list = [34,5,6,7,8,10]

#build in function filter
filtered_score = filter(lambda score : score >=10,score_list)
print((list(filtered_score)))



def my_func(x):
    x("meta")
    x("roth")

my_func(lambda x : print(f"this is {x}"))    