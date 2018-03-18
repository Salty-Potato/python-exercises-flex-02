word = 'bananas'

counts = {}
print(input('Pick a word: '))

for char in word:
    if char not in counts:
        counts[char] = 1
    else:
        counts[char] += 1

        