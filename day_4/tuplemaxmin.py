# tupled_list = [
#     ('V', 62), ('VI', 68),
#     ('VII', 72), ('VIII', 70),
#     ('IX', 74), ('X', 65)
# ]
# maxed_value = max(tupled_list, key = lambda x: x[1]) # function for maximun
# minimun_value = min(tupled_list, key = lambda x: x[1]) # function for manimum
# print("Maximun and minimun values are: ", maxed_value[1], minimun_value[1])





tupled_list = [ # tuple with list
    ('XII', {"blash": 90}), ('VI', {"zero": 68}),
    ('VII', {"whos": 72}), ('VIII', {"random": 70}),
    ('IX', {"gsf": 74}), ('X', {"asd":65})
]

sorted_array = sorted(tupled_list, key = lambda x: [
    i for i in x[1].keys()]) # function for sort
print(sorted_array,"----------->")
maxed_value = max(sorted_array, key = lambda x: [
    i for i in x[1].keys()]) # function for maximun
minimun_value = min(sorted_array, key = lambda x: [
    i for i in x[1].keys()]) # function for manimum
print("Maximun and minimun values are: ", [
    n for i,n in maxed_value[1].items()],
    [n for i,n in minimun_value[1].items()
])
