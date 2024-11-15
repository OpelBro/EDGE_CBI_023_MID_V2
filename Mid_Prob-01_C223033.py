def fibonacci(n):
    # Edge case for non-positive n
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    # Initialize the first two terms
    fib_sequence = [0, 1]
    
    # Loop to generate the Fibonacci sequence up to n terms
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    
    return fib_sequence

# Take user input for the number of terms
try:
    n = int(input("Enter the number of Fibonacci terms you want to generate: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        fib_seq = fibonacci(n)
        print(f"The Fibonacci sequence up to {n} terms is:")
        print(fib_seq)
except ValueError:
    print("Please enter a valid integer.")
