def max_occurring_char(s):
    counts = {}
    max_char = None
    max_count = 0

    for ch in s:
        if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z') or ('0' <= ch <= '9'):
            if ch in counts:
                counts[ch] += 1
            else:
                counts[ch] = 1

            if counts[ch] > max_count:
                max_count = counts[ch]
                max_char = ch

    return max_char, max_count

text = "testing." #change this to any word
char, count = max_occurring_char(text)
print(f"Character: '{char}', Occurrence: {count}")
