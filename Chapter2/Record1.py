user = {}


def client():
    for i in range(3):
        name = input('enter name')
        age = int(input('enter age'))
        user[name] = age


def use():
    print(user)


def print_details():
    client()
    use()


print_details()
