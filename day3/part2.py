from typing import List

def max_joltage(bank: str, num_digits: int) -> int:
    n = len(bank)
    result: List[str] = []
    start = 0

    while len(result) < num_digits:
        # how many digits we still need
        remaining = num_digits - len(result)
        # the furthest we can pick from
        end = n - remaining + 1
        # pick the largest digit in bank
        max_digit = max(bank[start:end])
        # find the first occurrence
        idx = bank.index(max_digit, start, end)
        result.append(max_digit)
        start = idx + 1

    return int("".join(result))


# --- read input ---
with open("input.txt") as f:
    banks = [line.strip() for line in f if line.strip()]

total = 0
for bank in banks:
    total += max_joltage(bank, 12)

print("Total output joltage (12-digit per bank):", total)
