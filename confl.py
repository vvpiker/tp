print(common line)

def hello(name: str) -> str:
    return f'Good day, {name}'


if __name__ == '__main__':
    name = input('Print your name here: ')
    res = hello(name)
    print(res)

