# Функция, которая подсчитывает число покупателей, попадающих в каждую группу, если нумерация ID сквозная и
# начинается с 0. На вход функция получает целое число n_customers (количество клиентов).

def num_group_all_cust(n_customers: int):
    count_cust = {}  # dict represent how many customers (value) is in the group (key)
    for i in range(n_customers):
        # s = sum([int(j) for j in str(i)])  # this way easier
        s = 0  # it's much faster
        while i != 0:
            s += i % 10
            i //= 10
        count_cust[s] = count_cust.get(s, 0) + 1
    return count_cust

# Функция, аналогичная первой, если ID начинается с произвольного числа. На вход функция получает целые числа:
# n_customers (количество клиентов) и n_first_id (первый ID в последовательности).


def num_group_cust(n_customers: int, n_first_id:int):
    count_cust = {}  # dict represent how many customers (value) is in the group (key)
    n_last_id = n_first_id + n_customers
    for i in range(n_first_id, n_last_id):
        s = 0
        while i:
            s, i, = s + i % 10, i // 10
        count_cust[s] = count_cust.get(s, 0) + 1
    return count_cust  # if u don't need whole list better make it as generator


if __name__ == '__main__':
    import timeit

    print(timeit.timeit("num_group_all_cust(99999)", setup="from __main__ import num_group_all_cust", number=1))
    print(num_group_all_cust(99999))
    print(timeit.timeit("num_group_cust(9000000, 99999)", setup="from __main__ import num_group_cust", number=1))
    print(num_group_cust(9000000, 99999))

# Считаю такой алгоритм распределения клиентов по группам не рациональнен, так как они распрелены
# "нормально", а значит в одних группах людей будет значительно больше чем в других. Лучше распределять по последней
# цифре в ID (или нескольким последним цифрам в зависимости от того сколько групп необходимо). Тогда клиенты будут
# распределены равномерно
