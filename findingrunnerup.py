if __name__ == '__main__':
    #n = int(input())
    #for i in range (0,n):
       # print(i*i)
   n = int(input("enter n"))
   arr = map(int, input().split()) 
   scores=list(arr)
   runner_up=-999
   Max_score=max(scores)
   for score in scores:
      if(score<Max_score and score>runner_up):
         runner_up=score
   print("the runner up is ",runner_up)
      
