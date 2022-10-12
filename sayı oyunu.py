import random
number=[]
digit = [1,2,3,4,5,6,7,8,9]
r1 = random.randint(0,8)
number.append(digit[r1])
digit.remove(digit[r1])

digit.append(0)
r2 = random.randint(0,8)
number.append(digit[r2])
digit.remove(digit[r2])

r3 = random.randint(0,7)
number.append(digit[r3])
digit.remove(digit[r3])

#print(number)
td_number = str(number[0]) + str(number[1]) + str(number[2])
#789print(td_number)

won = False
while not won:
    my_number = str(input("Guess:"))
    assert len(my_number) == 3 
    my_digits = [int(my_number[0]),int(my_number[1]),int(my_number[2])]
    #print(my_digits)
    
    arti_Sayisi = 0
    eksi_Sayisi = 0
    
    if number[0] == my_digits[0]:
        arti_Sayisi += 1
    elif number[0] == my_digits[1]:
        eksi_Sayisi += 1
    elif number[0] == my_digits[2]:
        eksi_Sayisi += 1
    
    if number[1] == my_digits[0]:
        eksi_Sayisi += 1
    elif number[1] == my_digits[1]:
        arti_Sayisi += 1
    elif number[1] == my_digits[2]:
        eksi_Sayisi += 1
        
    if number[2] == my_digits[0]:
        eksi_Sayisi += 1
    elif number[2] == my_digits[1]:
        eksi_Sayisi += 1
    elif number[2] == my_digits[2]:
        arti_Sayisi += 1
        
    if arti_Sayisi > 0:
        print("+" + str(arti_Sayisi))
    if eksi_Sayisi > 0:
        print("-" + str(eksi_Sayisi))
    if arti_Sayisi + eksi_Sayisi == 0:
        print(0)
     
    if my_number == td_number:
        print("Correct Guess!")
        print("The Answer : " + td_number)
        won = True

 
