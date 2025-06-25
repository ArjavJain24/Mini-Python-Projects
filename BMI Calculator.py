def bmi_calculator():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    bmi = weight / (height ** 2)
    print(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        print("You are Underweight.")
    elif 18.5 <= bmi < 25:
        print("You are Normal weight.")
    elif 25 <= bmi < 30:
        print("You are Overweight.")
    else:
        print("You are Obese.")

bmi_calculator()
