def create_phone_number(n):
    phone_number = "("
    counter = 0
    for number in n:
        if (counter < 2):
            phone_number += str(number)
        elif(counter == 2):
            phone_number += str(number) + ") "
        elif(counter <5):
            phone_number += str(number)
        elif (counter == 5):
            phone_number += str(number)+ "-"
        else:
            phone_number += str(number) 
        counter += 1
    return phone_number