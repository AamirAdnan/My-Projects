if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores=list(arr)
    Max_score=max(scores)
    Runner_up=-1111
    for i in scores:
        if(i>Runner_up and i<Max_score):
            Runner_up=i
    print(i)