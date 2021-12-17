sum = 0

while True :
    number = input ('inter number or exit : ')

    if number == 'exit' :
        print ('sum = ' , sum)
        break
    else :
        sum = int(number) + sum