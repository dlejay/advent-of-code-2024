from collections import Counter

L1 = []
L2 = []

with open("input.txt") as file:
    for line in file:
        num1, num2 = map(int, line.split())
        L1.append(num1)
        L2.append(num2)

L1.sort()
L2.sort()

dist = sum(abs(x - y) for x, y in zip(L1, L2))

print(f"Total distance is {dist}")

count = Counter(L2)

similarity = sum(i * count[i] for i in L1)

print(f"Similarity score is {similarity}")


