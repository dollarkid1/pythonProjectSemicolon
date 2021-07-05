records=[]

def get_name_age():
    name= input("enter a name")
    age=input("enter an age")

    return name,age


def collect_and_store_name_age(memory):
    name,age = get_name_age()
    memory.append((name,age))

for _ in range(3):
    collect_and_store_name_age(records)
    print(records)
