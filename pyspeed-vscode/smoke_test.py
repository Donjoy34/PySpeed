def my_func():
    return sum(range(1000))


def another_func():
    values = [i * 2 for i in range(50)]
    return len(values)


if __name__ == "__main__":
    print(my_func())
    print(another_func())
