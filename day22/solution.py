from collections import defaultdict

def gen(seed: int, iterations: int = 1) -> int:
    N = 16777216

    for _ in range(iterations):
        seed = (seed ^ (64 * seed)) % N
        seed = (seed ^ (seed // 32)) % N
        seed = (seed ^ (2048 * seed)) % N

    return seed

def generate_prices(seed: int, iterations: int = 2000) -> list:
    N = 16777216
    prices = []

    for _ in range(iterations):
        seed = (seed ^ (64 * seed)) % N
        seed = (seed ^ (seed // 32)) % N
        seed = (seed ^ (2048 * seed)) % N
        prices.append(seed % 10)

    return prices

def process_part1(filename: str) -> None:
    with open(filename) as file:
        seeds = [int(line) for line in file.readlines()]
    nums = [gen(seed, 2000) for seed in seeds]
    print(f"The sum is: {sum(nums)}")
    return

def process_part2(filename: str) -> None:
    with open(filename) as file:
        seeds = [int(line) for line in file.readlines()]
    hashmap = defaultdict(int)
    for seed in seeds:
        visited = set()
        prices = generate_prices(seed)
        diffs = [x - y for x, y in zip(prices[1:], prices)]
        for i in range(4, len(prices)):
            signal = tuple(diffs[i-4:i])
            if signal not in visited:
                visited.add(signal)
                hashmap[signal] += prices[i]
    best = max(hashmap.values())
    print("Best total price:", best)
    return

if __name__ == "__main__":
    process_part1("input.txt")
    process_part2("input.txt")
