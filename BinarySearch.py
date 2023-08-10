def binary_search(arr,low,high,search):
    if high>=low:
        mid=(high+low)//2
        if arr[mid]==search:
            return mid
        elif arr[mid]>search:
            return binary_search(arr,low,mid-1,search)
        else:
            return binary_search(arr,mid+1,high,search)
    else:
        return -1
arr=[]
n=int(input("enter how many element you want to add in list"))
for i in range(n):
    m=int(input("enter the element"))
    arr.append(m)
search =int(input("enter the element you want to search"))
result=binary_search(arr,0,len(arr)-1,search)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

