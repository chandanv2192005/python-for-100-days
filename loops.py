# break — exits the loop immediately
for i in range(10):
    if i == 5:
        break
    else:
        print(i)

# Output: 0 1 2 3 4
# continue — skips current iteration, keeps going
for i in range(10):
    if i % 2 == 0:
        continue # skip even numbers
    else:
        print(i)
# Output: 1 3 5 7 9