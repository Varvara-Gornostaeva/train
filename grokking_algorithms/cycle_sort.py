# http://algolab.valemak.com/cycle

def cycle(data):
    # Проходим по массиву в поиске циклических круговоротов
    for cycleStart in range(0, len(data) - 1):
        value = data[cycleStart]

        # Ищем, куда вставить элемент
        pos = cycleStart
        for i in range(cycleStart + 1, len(data)):
            if data[i] < value:
                pos += 1

        # Если элемент уже стоит на месте, то сразу
        # переходим к следующей итерации внешнего цикла
        if pos == cycleStart:
            continue

        # В противном случае, помещаем элемент на своё
        # место или сразу после всех его дубликатов
        while value == data[pos]:
            pos += 1
        data[pos], value = value, data[pos]

        # Циклический круговорот продолжается до тех пор,
        # пока на текущей позиции не окажется её элемент
        while pos != cycleStart:

            # Ищем, куда переместить элемент
            pos = cycleStart
            for i in range(cycleStart + 1, len(data)):
                if data[i] < value:
                    pos += 1

            # Помещаем элемент на своё место
            # или сразу после его дубликатов
            while value == data[pos]:
                pos += 1
            data[pos], value = value, data[pos]

    return data


# O(n2 / 2)
if __name__ == "__main__":
    print(cycle([5, 3, 6, 2, 11]))