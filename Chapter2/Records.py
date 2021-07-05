

"""for i in range (3):
    name=input('enter name')
    age=int(input('enter age'))
    user[name]=age
print(user)"""

user={}
def client():
    for i in range(3):
        name = input('enter name')
        age = int(input('enter age'))
        user[name] = age
    print(user)

client()
