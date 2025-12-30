def intersection(list1, list2):
    result = []

        for i in range(len(list1)):
        found = False
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                found = True
                break
        if not found:
            result.append(list1[i])

    for i in range(len(list2)):
        found = False
        for j in range(len(list1)):
            if list2[i] == list1[j]:
                found = True
                break
        if not found:
            result.append(list2[i])

    return result

list1 = [4, 5, 2, 3, 1, 6]
list2 = [8, 7, 6, 9, 4, 5]

print(intersection(list1, list2))
