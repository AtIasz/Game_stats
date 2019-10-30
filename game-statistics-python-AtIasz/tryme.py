def soryegeton(listli):
    sorye = False
    while sorye == False:
        sorye = True
        for obj in range(len(listli) - 1):
            if listli[obj] > listli[obj + 1]:
                temp = listli[obj]
                listli[obj] = listli[obj + 1]
                listli[obj + 1] = temp
                sorye = False
    return listli