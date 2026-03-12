file = open("numbers.csv", "r")
content = file.readlines()
#print(content)
file.close()
sum = 0
for row in content:
    if row.strip():
        sum += int(row.strip())
print(sum)
