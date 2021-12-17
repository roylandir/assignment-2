num_of_stu = int(input('please inter number of students :'))
sum = 0
min = 21
max = 0

for i in range (num_of_stu) :
    score = int(input('please inter Enter a score : ' ))

    sum = score + sum
    if score > max :
        max = score

    elif score < min :
        min = score


print ('The grade point average for' , num_of_stu , 'students is: ' ,  sum / num_of_stu )
print ('The lowest class score : ' , min , '\n Maximum class score : ' , max )