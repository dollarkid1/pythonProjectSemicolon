weight = eval(input("Enter your Weight\n"))
height = eval(input("Enter your Height\n"))

KILOGRAMS_PER_POUNDS = 0.45359237
METERS_PER_INCH = 0.0254

weightInKilograms = weight * KILOGRAMS_PER_POUNDS
heightInMeters = height * METERS_PER_INCH
bmi = weightInKilograms / (heightInMeters * heightInMeters)

print("BMI is ", format(bmi, '.2f'))
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
