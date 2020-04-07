#python program for doing insertion sort

def InsertionSort(arr):

    for i in range(1, len(arr)):
        key=arr[i]

        j=i-1
        while j >=0 and key < arr[j]:
            arr[j+1]=arr[j]
            j=j-1

        arr[j+1] = key

# Driver code to test above 
arr = [10,15,12,14,19] 
InsertionSort(arr) 
print ("Sorted array is:") 
for i in range(0,len(arr)): 
    print ("%d" %arr[i])             