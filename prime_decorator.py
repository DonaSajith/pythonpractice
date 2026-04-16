import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("execution_time:", end - start)
        return result
    return wrapper

@timer
def prime(num):
    if num <= 1:
        print(num, "is not a prime number")
    else:
        prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime==True:
            print(num, "is a prime number")
        else:
            print(num, "is not a prime number")
        return prime

num = int(input("Enter a number: "))
prime(num)

