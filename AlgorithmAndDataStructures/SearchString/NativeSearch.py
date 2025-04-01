def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    positions = []

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            positions.append(i)

    return positions

text = "ABABABABCABABD"
pattern = "ABAB"
print(naive_search(text, pattern))