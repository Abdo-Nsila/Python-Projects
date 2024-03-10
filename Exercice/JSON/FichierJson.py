import json


# Methode json :
# file_location  = "JSON\\file.json"
# ptr_json = open(file_location , 'r' , encoding='utf-8')
# content = json.load(ptr_json)
# print((content['nom']['Bac1'][0]['Ahmed Bac1']))
# ptr_json.close()


# Pure methods :
# f = open("JSON\\file.json", 'r' , encoding='utf-8')
# chaine = f.read()
# print(chaine)
# f.close()








data = {
    "nom": {"Ts" : [{"Ahmed Ts" : 80} ,{"Amine Ts" : 90},{"Ayman Ts" : 100}],
            "Bac1" : [{"Ahmed Bac1" : 80},{"Amine Bac1" : 90},{"Ayman Bac1" : 100}],
            "Bac2" : [{"Ahmed Bac2" : 80},{"Amine Bac2" : 90},{"Ayman Bac2" : 100}]
            },
    "prénom": "mouhcine",
    "age": 37
}

# Methode json 
# ptr_json = open("JSON\\file2.json" , 'w' , encoding='utf-8')
# json.dump(data , ptr_json)
# ptr_json.close()



# Pure methods :
# f = open("JSON\\file2.json", 'w' , encoding='utf-8')
# f.write(str(data))
# f.close()