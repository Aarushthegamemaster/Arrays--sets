import array as arr
array1 = arr.array('i', [1,3,5,7,9,7,5,3])
print("Original array:"+str(array1))
print("The number of occurences of the number 3 in the array is:"+str(array1.count(3)))
array1.reverse()
print("The array reversed:")
print(str(array1))