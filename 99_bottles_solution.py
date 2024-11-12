#! python3

# a program that prints out every line to the song "99 bottles of beer on the wall"

num_bottles = 99

while num_bottles > 1:
    print(f"{num_bottles} bottles of beer on the wall, {num_bottles} bottles of beer. ")
    num_bottles -= 1
    if num_bottles == 1:
        print(
            f"Take one down and pass it around, {num_bottles} bottle of beer on the wall."
        )
    else:
        print(f"Take one down and pass it around, {num_bottles} bottles of beer on the wall.")

print(f"{num_bottles} bottle of beer on the wall, {num_bottles} bottle of beer.")
print(f"Take one down and pass it around, no more bottles of beer on the wall.")
print("No more bottles of beer on the wall, no more bottles of beer. ")
print("Go to the store and buy some more, 99 bottles of beer on the wall.")
