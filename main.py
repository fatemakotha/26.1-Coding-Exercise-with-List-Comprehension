#EXAMPLE 1
numberssss = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
resultss = [number for number in numberssss if number % 2 == 0]
print(resultss)

#EXAMPLE 2:
import csv
with open("file1.txt") as file1:
    file_1_data = file1.readlines()
    print(file_1_data)
with open("file2.txt") as file2:
    file_2_data = file2.readlines()
    print(file_2_data)

result = [int(num) for num in file_1_data if num in file_2_data]
print(result)

