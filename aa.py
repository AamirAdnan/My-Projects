# arr=[1,2,34,55,666]
# runner_up=-999
# high=max(arr)
# for score in arr:
#     if(score<high and score>runner_up):
#         runner_up=score
# print(runner_up) 
#test 
# a=int(input())
# for a in range (0,a):
#     x,y=[int(i) for i in input().split()]
#     if(x>y):
#         print("SECOND")
#     elif(y>x):
#         print("FIRST")
#     else:
#         print("ANY")
# for a in range (0,a):
#     x,y=[int(i) for i in input().split()]
#     print(x,y)
import random
print(random.random())
print(random.randint(1,100))
print(random.randrange(0,10,2))
n=random.sample(range(1,20),5)
print(n)
c=["butter chicken",'biryani','mess']
print(random.choice(c))