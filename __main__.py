from scripts import search_pairs, get_zeros, get_multi_alphabet_sum

if __name__ == '__main__':
    # 1ая задача
    array, k = [0, 51, 14, 4, 41, -3, 43, 85, 39, 81, 98, 68, 59, 79, 87, 7,
                58, 4, 10, 73, 32, 34, 26, 56, 8, 25, 54, 61, 31, 50, 100, 85], 51
    print(f'Уникальные пары: {search_pairs(array=array, k=k)}')
    # 2ая задача
    file_path = 'names.txt'
    print(f'Сумма равна: {get_multi_alphabet_sum(file_path)}')
    # 3ья задача
    n = 12
    print(f'Количество нулей в {n}! : {get_zeros(n)}')
