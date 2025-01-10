#! python3
# Chinese puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm.
# How many rabbits and how many chickens do we have?

# brute force approach

heads = 150
legs = 396

for head in range(0, heads + 1):
    chicken_heads = heads - head
    rabbit_heads = head

    chicken_legs = chicken_heads * 2
    rabbit_legs = rabbit_heads * 4

    if chicken_legs + rabbit_legs == legs:
        print(f'Chickens: {chicken_heads}, rabbits: {rabbit_heads}')
    else:
        continue

# non-routine logic
# there are 150 animals total

heads = 150
legs = 396

animals_total = 150
# each animal has minimum 2 legs, chickens have 2 legs and rabbits 2+2 legs
# if all animals were chickens we would have 300 legs total but we have 96 extra legs
all_chickens_legs = heads * 2
print(all_chickens_legs)
# each pair of extra legs belongs to a rabbit or each rasbbit contributs 2 extra legs to the leg count
extra_legs = legs - all_chickens_legs
print(extra_legs)
# number of rabbits = number of extra legs / 2
num_rabbits = extra_legs / 2
# number of chickens = 150 - rabbits
num_chickens = 150 - num_rabbits
print(f'Chickens: {int(num_chickens)}, rabbits: {int(num_rabbits)}')