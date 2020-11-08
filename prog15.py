def print_dict(dict):
    for key in dict:
        print('{0}  {1}'.format(key,dict[key]))


if __name__=='__main__':
    print("tu jestem")

    samolot={'n':'pasazerki','typ':'oeing'}

    print_dict(samolot)


def calculator(a,b,op):
    if op =="+":
        return a+b
    elif op=="-":
        return a-b
    elif op=="*":
        return a*b
    elif op=="/":
        return a/b
    else:
        print("wybierz cos innego")
    raise AssertionError('nieznane dzialanie')


d=calculator(10,5,"/")
print(d)
