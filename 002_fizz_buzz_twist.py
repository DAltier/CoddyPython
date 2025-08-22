print("Welcome to FizzBuzz!")
def fizzbuzz(n):
    if n % 21 == 0:
        return "FizzBuzz"
    elif n % 7 == 0:
        return "Buzz"
    elif n % 3 == 0:
        return "Fizz"
    elif "3" in str(n):
        return "Almost Fizz"
    else:
        return str(n)

n = int(input())
for i in range(1, n+1):
    value = fizzbuzz(i)
    print(value)