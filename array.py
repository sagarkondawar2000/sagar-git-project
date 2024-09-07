array = [10, 20, 30]
element_to_insert = 40
index_to_insert = 2

array.insert(index_to_insert, element_to_insert)
print(array)  # Output: [10, 20, 40, 30]

##Manual process

array = [10, 20, 30]
element_to_insert = 40
index_to_insert = 2

# Create a new array with the desired length
new_array = [None] * (len(array) + 1)

# Copy elements from the original array up to the insertion point
for i in range(index_to_insert):
    new_array[i] = array[i]

# Insert the new element
new_array[index_to_insert] = element_to_insert

# Copy the remaining elements from the original array
for i in range(index_to_insert, len(array)):
    new_array[i + 1] = array[i]

print(new_array)  # Output: [10, 20, 40, 30]






#############
a=[1,2,3,4,5]
print(a[3])
element_to_insert=45
index_to_insert=2
a.insert(3,45)
print(a.index(45))
del a[4]
for element in a:
    print(element)