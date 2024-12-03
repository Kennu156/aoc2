with open('input.txt', 'r') as file:
    data = file.readlines()

for line in data:
    numbers = line.split()
    if len(numbers) == 2: 
        numbers = sorted(map(int, numbers), reverse=True) 
        pair = (numbers[0] - numbers[1])

print(pair)
