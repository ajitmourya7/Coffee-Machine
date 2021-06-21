stay = True
number_list = []
while stay:
    number = input()
    if len(number) == 1 and number == ".":
        print(min(number_list))
        stay = False
    else:
        number_list.append(float(number))
