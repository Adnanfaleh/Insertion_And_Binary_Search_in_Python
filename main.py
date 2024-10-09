array = [1, 2, 4, 5, 6, 7, 8]
n = len(array)
x = int(input("Enter the number you want to search for: "))

#linear_Search_Python_Code:
'''
def linearSearch(array, x, n):
    for i in range(0, n):
        if (array[i] == x):
            return i;
    return -1; # Return -1 if the number is not found
    

result = linearSearch(array, x, n)

if(result == -1):
    print('Number is not found')
else:
    print('Number is at index ', result+1 , 'in the array');
    
'''
#-------------------------------------------------------------------------------------

#Binary_Search_Python_Code: 
'''
def BinarySearch(array, x, n):
    mid = n // 2  
    if (x < array[mid]):
        for i in range(0, mid):
            if array[i] == x:
                return i
    elif (x > array[mid]):
        for i in range(mid, n):
            if (array[i] == x):
                return i
    elif x == array[mid]:
        return mid
    return -1  # Return -1 if the number is not found

result = BinarySearch(array, x, n)

if result == -1:
    print('Number is not found')
else:
    print('Number is at index', result + 1, 'in the array')
'''