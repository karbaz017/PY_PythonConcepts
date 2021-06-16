# numbers = [1,2,5,7,4,12,7,0]
# largest = numbers[0]
# for number in numbers:
#     if number > largest:
#         largest = number
# print(f"Largest No: {largest}")

# 2D Lists

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# matrix[0][1] = 20
# print(matrix[0][1])
# for row in matrix:
#     for item in row:
#         print(item)

# numbers = [3, 4, 1, 6, 1, 7]
# numbers.append(20)
# numbers.insert(0, 10)
# numbers.remove(6) #it removes a item if it exists in list and gives error of not exist in list
# numbers.clear() #empty the list
# numbers.pop() #removes the last element from list
# print(numbers)
# print(numbers.index(6)) # gives index of item if it exist else gives error
# print( 6 in numbers) # gives True if it exist in list and False if not exist in list
# print(numbers.count(1))
# numbers.sort() #sorts list in ascending order
# numbers.reverse() # reverses the items in list
# numbers2 = numbers.copy() # copies the list
# print(numbers)
# unique = []
# for item in numbers:
#     if item not in unique:
#         unique.append(item)
# print(numbers)
# print(unique)
