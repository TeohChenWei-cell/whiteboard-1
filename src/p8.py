def Anagrams(s1, s2):
    f1 = {}
    f2 = {}

    for ch in s1:
        if ('a' <= ch.lower() <= 'z'):
            ch = ch.lower()
            if ch in f1:
                f1[ch] += 1
            else:
                f1[ch] = 1

    for ch in s2:
        if ('a' <= ch.lower() <= 'z'):
            ch = ch.lower()
            if ch in f2:
                f2[ch] += 1
            else:
                f2[ch] = 1

    if len(f1) != len(f2):
        return False

    for key in freq1:
        if key not in f2 or f1[key] != f2[key]:
            return False

    return True
