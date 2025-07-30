def candy_distribution(t, test_cases):
    results = []
    for n in test_cases:
        # The number of valid (a > b) pairs is simply (n - 1) // 2
        results.append((n - 1) // 2)
    return results

# Example usage:
t = int(input())
test_cases = [int(input()) for _ in range(t)]
results = candy_distribution(t, test_cases)
for res in results:
    print(res)
