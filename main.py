nums = []

while True:
    try:
        n = int(input())
    except ValueError:
        print("Вы должны ввести число")
        continue
    if n == 0:
        break
    nums.append(n)

print(max(nums, key=lambda x: sum(int(i) for i in str(x))))