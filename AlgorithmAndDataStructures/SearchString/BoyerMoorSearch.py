def boyer_moore_search(text, pattern):
    def bad_char_heuristic(pattern):
        bad_char = {}
        for i in range(len(pattern)):
            bad_char[pattern[i]] = i
        return bad_char

    n = len(text)
    m = len(pattern)
    bad_char = bad_char_heuristic(pattern)
    positions = []
    s = 0  # сдвиг

    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            positions.append(s)
            s += (m - bad_char.get(text[s + m], -1)) if s + m < n else 1
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))

    return positions

# Пример использования
text = "ABAAABCD"
pattern = "ABC"
print(boyer_moore_search(text, pattern))  # [4]
