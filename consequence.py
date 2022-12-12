def conseq_num(arr,n):
 maximum_num = 0 
 count = 0
 arr.sort() 
x = []
x.append(arr[0])
for i in range(1,n):
  if (arr[i]!=arr[i-1]):
      x.append(arr[i])
for i in range(len(x)):
   if (i>0 and x[i]==x[i-1]+1):
      count+=1
   else: count = 1
   maximum_num = max(maximum_num,count)
return maximum_num
arr = [1, 9, 3, 10, 4, 20, 2]
n = len(arr)
print(conseq_num(arr,n)
      
