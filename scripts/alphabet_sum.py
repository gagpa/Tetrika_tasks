alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

cache_names = {}


def get_multi_alphabet_sum(path: str) -> int:
    """Прочитывает информацию из файла. Преобраует информацию в список и сортирует её.
    Затем находит все алфавитные суммы. Суммирует полученные значения из списка"""
    text = __get_content(path)
    names = text.replace('"', '').split(',')
    names.sort()
    multi_alphabet_sums = [(i + 1) * __calculate_alphabet_sum(name) for i, name in enumerate(names)]
    sum_multi_sums = sum(multi_alphabet_sums)
    return sum_multi_sums


def __calculate_alphabet_sum(name: str) -> int:
    """Проверяет в словаре cache_names наличие данных по ключу name,
     если нет, то вычисляет алфавитную сумму и записывает её в cache_names."""
    letter_places = []
    if name in cache_names.keys():
        alphabet_sum = cache_names[name]
    else:
        for letter in name:
            place = alphabet.index(letter) + 1
            letter_places.append(place)
        alphabet_sum = sum(letter_places)
        cache_names[name] = alphabet_sum
    return alphabet_sum


def __get_content(path) -> str:
    """Читает информацию из локального файла"""
    with open(path, 'r') as file:
        text = file.read()
    return text
