answer = 0
n = int(input())
array = input()
for i in range(n-2):
    if array[i:i+3] == "#.#": answer += 1
print(answer)
