def find_anagrams(word, candidates):
    list = []
    for cand in candidates:
        if sorted(word.lower()) == sorted(cand.lower()) and word.lower() != cand.lower():
            list.append(cand)
    return list


