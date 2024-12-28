height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

Bmi = weight / (height/100)**2

print("Your BMI is: ", Bmi)

if Bmi < 18.5:
    print("You are underweight.")
elif Bmi >= 18.5 and Bmi < 24.9:
    print("You are normal weight.")
elif Bmi >= 25 and Bmi < 29.9:
    print("You are overweight.")
elif Bmi >= 30 and Bmi < 34.9:
    print("You are obese.")
elif Bmi >= 35:
    print("you are severely obese")
else:
    print("you are extremely obese")