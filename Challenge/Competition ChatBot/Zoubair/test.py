dict = {
    'a1':[1,2,3,1],
    "a2" :[0,5,1,1]

 }
# print(list(dict))
# # print(dict[list(dict)[0]])
# t = [0 for t in range(4) ]
# for i in range(len(list(dict))):
    
#     for j in range(len(dict[list(dict)[0]])):
#         t[j] += dict[list(dict)[i]][j]

# # sum1 = [dict[list(dict)[i]][j] for i in range(len(dict)) for j in range(len(dict[list(dict)[0]]))]
# print(t)
# def stock(data):
#     file = open("data.csv","a")
   
#     t = [0 for t in range(4) ]
#     for i in range(len(list(data[1]))):
#         for j in range(len(data[1][list(data[1])[0]])):
#             t[j] += data[1][list(data[1])[i]][j]
#     file.write(f"{data[0]};{list(data[1])};{t}\n")
#     file.close()

# r = ['Q',{
#     "a1":[1,2,3,0],
#     "a2":[1,2,3,0],
#     "a3":[1,2,3,0],
#     "a4":[1,2,3,0]
# }]
# stock(r)
# stock(r)
# q_num = 0
# def get_info():
#     global q_num
#     q_num += 1
#     return [list(dict)[q_num],dict[list(dict)[q_num]]]

# print(get_info())
final_tab = [1,6,2,4]
def best_filier():
    return final_tab.index(max(final_tab))
print(best_filier())