final_dict = {'This' : 4, 'is' : 2 , 'my' : 2, 'homework' : 8, 'for' : 3, 'my' : 2, 'class' : 5}

print('The original dictionary is : ', final_dict)

f = 2

fre = 0

for f in final_dict:
    if final_dict[f] == f:
        fre = fre + 1

print('Frequency of f is :', fre)