# Define a function called `qan_tic`
def qan_tic(): # (1)
  tic = "QAN.AX" # (2)
  print(tic) # (3)
  return tic # (4)
# Call the function
qan_tic() # (5)

#class attempt:
def even_numbers(numbers):
  even = []
  for num in numbers:
     if num % 2 == 0:
        even.append(num)
  return even
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 22, 23, 25, 29, 30, 31]
result = even_numbers(numbers)
print(result)

# class attempt2
lst = [2,3,12,14,20,21,25,13,15]
new_lst = [x**2 for x in lst if x**2>150]
print(f'the new list with value of square greater than 150 is {new_lst}')


#y_example1
#y_example2
#y_example3

