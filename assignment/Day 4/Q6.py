prices = [105, 110, 108, 112, 115, 116, 114]

window = 3

for i in range(len(prices) - window + 1):
    avg = sum(prices[i:i+window]) / window
    print(f"Day {i+1} average = {avg:.2f}")