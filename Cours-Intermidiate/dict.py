dict0 = { 'name' : 'Abdellah', 'age' : 18,}
print(dict0)
dict0['email'] = 'abdo@gmail.com'
print(dict0)
del dict0['email'] # dict0.popitem() => remove last item
print(dict0)

try:
    print(dict0['lastname'])
except:
    print('ERREUR')

for key in dict0.keys() :
    print(key)
for value in dict0.values() :
    print(value)

for key , value  in dict0.items() :
    print(f"{key} => {value}")