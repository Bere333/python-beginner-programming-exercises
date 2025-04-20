# ✅↓ Write your code here ↓✅
def number_of_bottles():
    for bottles in range(100):
        if bottles == 0:
            print(f"No more bottles of milk on the wall, no more bottles of milk.\nGo to the store and buy some more, 99 bottles of milk on the wall.")
        else:
            print(f"{bottles} bottles of milk on the wall, {bottles} bottles of milk.\nTake one down and pass it around,  {bottles - 1} bottles of milk on the wall.")
number_of_bottles()
        