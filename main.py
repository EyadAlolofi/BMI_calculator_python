def calculate_bmi():
    weight = float(input("Enter your weight (in kg): "))
    height = float(input("Enter your height (in meters): "))

    bmi = (weight / height) ** 2
    interpretation = interpret_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f} - {interpretation}")


def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


calculate_bmi()