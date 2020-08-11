# Thw below function is based on naive algorithm which takes more time to compute element in series
# def calc_fib(n):
#     if (n <= 1):
#         return n
#
#     return calc_fib(n - 1) + calc_fib(n - 2)
#
# n = int(input())
# print(calc_fib(n))

# the below function uses another approach to compute nth element of the series.
def calc_fib(n):
    F = []
    F.insert(0, 0)
    F.insert(1, 1)
    for i in range(2, n+1):
        F.insert(i, F[i-1]+F[i-2])
    return F[n]
n = int(input())
print(calc_fib(n))
