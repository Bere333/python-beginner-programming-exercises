import random

def get_randomInt():
	# ✅↓ Write your code here ↓✅
	# Esta vez, el rango de números comienza en 1 y termina en 12
	random_numbers = random.randrange(1, 13)
	return random_numbers

# ❌ ↓ DON'T CHANGE THE CODE BELOW ↓ ❌
print(get_randomInt())
