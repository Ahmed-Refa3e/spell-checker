def remove_punctuation(text):
    """
    remove punctuation from the words
    """
    my_list = []
    for word in text:
        if word[0] in "*-_.&()?!^`~,":
            word = word[1:]

        if len(word) == 0:
            continue

        if word[-1] in "*-_.&()?!^`~,":
            word = word[:-1]

        my_list.append(word)

    return my_list
