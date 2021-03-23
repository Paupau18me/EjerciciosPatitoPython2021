txt = map(str, input().split(' '))
for word in txt:
    if 'a' in word and 'e' in word and 'i' in word and 'o' in word and 'u' in word:
        print(word)
