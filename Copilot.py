# this is a pthyon program to calculate the fibonacci sequence. Create the python code below to do this 
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = [0, 1]
        while len(fib_seq) < n:
            next_num = fib_seq[-1] + fib_seq[-2]
            fib_seq.append(next_num)
        return fib_seq

n = int(input("Enter the number of Fibonacci numbers to generate: "))
fibonacci_seq = fibonacci(n)
print(fibonacci_seq)
print ("go Yankees!")