def selection_sort(alist):
    """The list is arranged in order of the highest in the percentage of similarity
    and returns only the highest 5 suggestions without the percentage
    """
    if len(alist) >= 5:
        n = 5
    else:
        n = len(alist)
    list_words = []
    for i in range(n):
        max = alist[i][0]
        maxposition = i
        for j in range(i + 1, len(alist)):
            if alist[j][0] > max:
                max = alist[j][0]
                maxposition = j
        alist[maxposition], alist[i] = alist[i], alist[maxposition]
        list_words.append(alist[i][1])
    return list_words
