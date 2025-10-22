def words_containing(file,substring):
    contain = []
    sub = substring
    with open(file, 'r', encoding="utf-8") as file:
        for word in file:
            w = word.split()
            for words in w:
                if sub in words:
                    contain.append(words)
    return contain

test = words_containing('test.txt', 'the')
print(test)
