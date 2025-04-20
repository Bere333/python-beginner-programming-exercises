def fizz_buzz():
    # ✅↓ Write your code here ↓✅
    for num in range(101):
        if (num % 3 == 0) & (num % 5 == 0):
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

# ❌↓ DON'T CHANGE THE CODE BELOW ↓❌
fizz_buzz()
