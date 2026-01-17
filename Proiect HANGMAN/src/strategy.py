from collections import Counter


def choose_best_letter(candidates, tried_letters):
    counter = Counter()

    for word in candidates:
        unique_letters = set(word)
        for ch in unique_letters:
            if ch not in tried_letters:
                counter[ch] += 1

    if not counter:
        return None

    return counter.most_common(1)[0][0]
