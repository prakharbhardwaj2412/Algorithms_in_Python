# The objective of code is to print maximum pairwise product in a array..!!

# !!!------"This is a naive algorithm which is correct but takes lot of time."-------!!!

# def max_pairwise_product(numbers):
#     n = len(numbers)
#     max_product = 0
#     for first in range(n):
#         for second in range(first + 1, n):
#             max_product = max(max_product,
#                 numbers[first] * numbers[second])
#
#     return max_product

# !!!------"This function does the same job in less time but does not satisfy all the test cases.------!!!"

# def max_pairwise_product(numbers):
#     n = len(numbers)
#     index = 0
#     for i in range(n):
#         if numbers[i]>numbers[index]:
#             index=i
#     # print(numbers[index])
#     if index == 0:
#         index2 = 1
#     else:
#         index2 = 0
#     for i in range (1, n):
#         if numbers[i] != numbers[index] and numbers[i] > numbers[index2]:
#             index2 = i
#     # print(numbers[index2])
#     return numbers[index] * numbers[index2]

# !!!------"This is compact logic where firstly the array is sorted using built-in sort() function and then the product is calculated.------!!!
def max_pairwise_product(numbers):
    n = len(numbers)
    numbers.sort()
    return numbers[-1]*numbers[-2]


# !!!------"FIrstly the user inputs the length of array in first line and then elements of array seperated by space"------!!!

# if __name__ == '__main__':
input_n = int(input())
input_numbers = [int(x) for x in input().split()]
print(max_pairwise_product(input_numbers))
