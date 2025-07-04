with open ("test.txt") as reader:
    count = 0
    for line in reader:
        count = count + 1
print(count)
