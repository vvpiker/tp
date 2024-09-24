print(common line)

def hello(name: str) -> str:
    return f'Good day, {name}'

if __name__ == '__main__':
    name = input('Print your name here: ')
    f = open('output.txt', 'w')
    res = hello(name)
    f.write(res)
    f.close()
