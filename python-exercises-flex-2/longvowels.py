def longvowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    monkey = ''
    for c in word:
        for vowel in vowels:
            if c == vowel:
                monkey += (vowel*4)
        monkey += c
    return monkey
exercise = 'long poop'
tom = 'short poop'
print(longvowels(exercise))
    
    
    
    
    
    