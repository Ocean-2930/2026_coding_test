def checker(participant, complete):
    dct = {}

    for n in participant:
        if n not in dct:
            dct[n] = 1
        else:
            dct[n] += 1

    for n in complete:
        dct[n] -= 1

    for k, v in dct:
        if v == 0:
            continue

        return k