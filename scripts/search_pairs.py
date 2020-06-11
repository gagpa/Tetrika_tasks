def search_pairs(array: list, k: int) -> list:
    """
    Находит пары чисел из массива array, сумма которых равна числу k
    array - массив целых чисел,
    k - требуемая сумма.
    """
    pairs = []
    array.sort()
    array = list(filter(lambda digit: digit <= k, array))
    while array and len(array) > 1:
        l_dig = array[0]
        r_dig = array[-1]
        sum_digs = sum((l_dig, r_dig))
        if sum_digs > k:
            array.remove(r_dig)
        elif sum_digs < k:
            array.remove(l_dig)
        else:
            pairs.append((l_dig, r_dig))
            array.remove(l_dig)
            array.remove(r_dig)
    return pairs
