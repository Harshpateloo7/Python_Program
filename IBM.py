weight = input("Enter your weight in kg:")
weight =float(weight)

height = input("Enter your height in cm:")
height = int(height)

height_in_meters = height/100

bmi = weight / height_in_meters **2

print("BMI = %f " %bmi)
print("BMI = " + str(bmi))

