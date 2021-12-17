weight = int(input('Enter the weight in kilograms :'))
height = float(input('Enter the height in meters :'))

bmi = weight / height**2

print ('your bmi =' , bmi)

if bmi < 18.5 :
    print ('underweight')

elif bmi >= 18.5 and bmi <= 24.9 :
    print ('normal')

elif bmi >= 25 and bmi <= 29.9 :
    print ('overweight')

elif bmi >= 30 and bmi <= 34.9 :
    print ('obese')

elif bmi >= 35 :
    print ('extremely obese')