arr=[1,2,34,55,666]
runner_up=-999
high=max(arr)
for score in arr:
    if(score<high and score>runner_up):
        runner_up=score
print("The runner up will be",runner_up) 