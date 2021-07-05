names = ["Ayo","Ade","Ada"]
for var in enumerate (names):
    print(var)
names = ["Ayo","Ade","Ada"]
for index, name in enumerate(names):
    print("name=(),index=()".format (name,index))


name= "John Marwood Cleese"
first,middle,last=name.split()
transformed= last+','+first+' '+middle
print(transformed)
print(name)
print(first)
print(middle)

ip_address= "127.0.0.1"
first,second,third,last=ip_address.split(".")
new=first+''+second+""+third+""+last
print(last)
print(third)
print(first)
print(new)
print(ip_address.split("."))