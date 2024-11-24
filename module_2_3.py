my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
my_list_len = len(my_list)
adres = 0
while adres < my_list_len:
    my_list_adr = int(my_list[adres])
    if my_list_adr > 0:
        adres += 1
        print(my_list_adr)
    else:
        adres += 1
        if my_list_adr < 0:
            break



