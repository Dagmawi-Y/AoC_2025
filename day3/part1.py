with open("input.txt") as f:
    banks = [line.strip() for line in f if line.strip()]

total = 0

for bank in banks:
    max_joltage = 0
    n = len(bank)
    
    # try all pairs of positions i < j
    for i in range(n):
        for j in range(i + 1, n):
            joltage = int(bank[i] + bank[j])
            if joltage > max_joltage:
                max_joltage = joltage
    
    total += max_joltage

print("Total output joltage:", total)
