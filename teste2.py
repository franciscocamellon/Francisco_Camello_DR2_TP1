def ex7_rotation(str1):
    str2=''
    i = (len(str1)//2)+1
    print(i)
    aux = str1[:i]
    print(aux)
    # str1[:i] = str1[i:]
    aux2 = str1[i:]
    print(aux2)
    # str1[i:] = aux
    aux3 = aux2 + aux
    print(aux3)
    # return print(str2)

s= 'otorrinolaringologista'
ex7_rotation(s)