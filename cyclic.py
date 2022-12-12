def rotate_array(arr,n):
    x = arr[n-1]
    for i in range(n-1, 0,-1):
        arr[i] = arr[i-1]
    arr[0]= x   
arr = [1, 2,3,4,5]     
n = len(arr)    
print("Array to be rotated : ", arr)
rotate_array(arr, n)
print("cyclically rotated array ", arr)