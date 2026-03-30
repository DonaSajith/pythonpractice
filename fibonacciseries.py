n = int(input("Enter the number of terms: "))
fib_series = []
a, b = 0, 1

for i in range(n):
    fib_series.append(a)
    a, b = b, a + b

print("Fibonacci series:", fib_series)