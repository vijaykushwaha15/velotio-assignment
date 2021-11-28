def checkSubset(list1, list2, m, n):
    i = 0
    j = 0
    count=0
    for i in range(n):
        for j in range(m):
            if(list2[i] == list1[j]):
                count +=1
        # if not present in list1
        if (j == m):
            return 0
      
    # If all present in list1
    if (count==n):
        return 1
  
      
input_string = input("Enter a array element separated by space ")
array1  = input_string.split(" ")

input_string = input("Enter a array element separated by space ")
array2  = input_string.split(" ")
m = len(array1)
n = len(array2)
# calling function  
if(checkSubset(array1, array2, m, n)):
    print("array2 is subset of array1 ")
else:
    print("array2 is not a subset of array1")    

