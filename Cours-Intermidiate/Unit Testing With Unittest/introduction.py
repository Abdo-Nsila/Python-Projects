import json

# dict0 = {"i1":12,
#          "i2":True,
#          "i3":"ahmed",
#          "i4":[1,2,3,4,5],
#          }

# d = json.dumps(dict0 , indent=20)
# print(d)
# with open("data.json","w") as f :
#     f.write(d)
# d = json.loads(d)
# print(d)

class User :

        def __init__(self,name,age) :
                self.name = name
                self.age = age
                
            # getters_____________
            # setter______________
class User1 :

        def __init__(self,name,age) :
                self.name = name
                self.age = age
                
            # getters_____________
            # setter______________

obj = User1("Ali",20)
# def encoding(o) :
#     if isinstance(o,User) :
#            return {"name":o.name,"age":o.age,"type":o.__class__.__name__}
#     else :
#            raise "Awdiiiiiiiiiii !"
    
# # d = json.dumps(encoding(obj))
# d = json.dumps(obj,default=encoding)
# print(d)
                

# from json import JSONEncoder

# class UserEncoder(JSONEncoder) :
#        def default(self,obj) :
#             if isinstance(obj,User) :
#                 return {"name":obj.name,"age":obj.age,"type":obj.__class__.__name__}
#             return JSONEncoder.default(self,obj)


# ue = UserEncoder().encode(obj)
# print(ue)









def fact(n) :
        if n == 1 :
            return 1 # break
        return n * fact(n-1)


print(fact(2))



