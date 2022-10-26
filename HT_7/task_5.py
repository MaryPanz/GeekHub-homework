from collections import Counter


words = "dadddsfgh"
print(f"The word {words} consists of")
#counts = Counter(letter for letter in words)
counts = {}
for letter in words:
    counts.setdefault(letter,0)
    counts[letter] += 1

for key in counts:
    if counts[key] > 1:
        print("%d letter/number %s" % (counts[key], key))
    else:
        print("0 double occurences for %s" % key)
