sum_of_number = []
while True:
    user_number = int(input())
    if len(sum_of_number) == 0 and user_number == 0:
        sum_of_number.append(user_number)
        break
    if len(sum_of_number) == 0 or (len(sum_of_number) > 0 and sum(sum_of_number) != 0):
        sum_of_number.append(user_number)
        if sum(sum_of_number) == 0:
            break
    else:
        break
print(sum(i * i for i in sum_of_number))
