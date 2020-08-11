# Uses python3
import sys

# def lcm_naive(a, b):
#     for l in range(1, a*b + 1):
#         if l % a == 0 and l % b == 0:
#             return l
#
#     return a*b

# This is the function to calculate gcd(a,b)
def gcd_algo(a, b):
    if b == 0:
        return a
    a, b = b, a % b
    return gcd_algo(a, b)

# In this function we calculate the lcm of a,b
# We use the identity a * b = gcd(a,b) * lcm(a,b)
def lcm(a, b):
    return (a * b)//gcd_algo(a, b)


if __name__ == '__main__':
    # input = sys.stdin.read()
    num = input()
    a, b = map(int, num.split())
    print(lcm(a, b))

