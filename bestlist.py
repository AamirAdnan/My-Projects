
if __name__ == '__main__':

    N = int(input("enter how many oprations you want to perform in the list"))
    arr=[]
    for i in range(N):
        user_input=input().split()
        if user_input[0]=="insert":
            arr.insert(int(user_input[1]), int(user_input[2]))
        elif user_input[0]=="print":
            print(arr)
        elif user_input[0]=="remove":
            arr.remove(user_input[1])
        elif user_input[0]=="append":
            arr.append(user_input[1])
        elif user_input[0]=="sort":
            arr.sort
        elif user_input[0]=="pop":
            arr.pop()
        elif user_input[0]=="reverse":
            arr.reverse()
