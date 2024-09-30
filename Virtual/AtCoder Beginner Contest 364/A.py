n = int(input())

array = []
for _ in range(n): array.append(input())


answer = "Yes"

for i in range(1,n-1):
    if array[i-1] == "sweet" and array[i] == "sweet":
        answer = "No"

print(answer)
