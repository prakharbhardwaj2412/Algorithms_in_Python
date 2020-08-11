# Uses python3
import sys

# THis is a naive algorithm wich takes more time for large inputs and so it is not efficient
# def gcd_naive(a, b):
#     current_gcd = 1
#     for d in range(2, min(a, b) + 1):
#         if a % d == 0 and b % d == 0:
#             if d > current_gcd:
#                 current_gcd = d
#
#     return current_gcd

# The below function is based on euclidean algorithm
# Eculidean Algorithm states that gcd(a, b) = gcd(b, a%b)
def gcd_algo(a, b):
    if b == 0:
        return a
    a, b = b, a % b
    return gcd_algo(a, b)


# if __name__ == "__main__":
# input = sys.stdin.read()
num = input()
a, b = map(int, num.split())
print(gcd_algo(a, b))
