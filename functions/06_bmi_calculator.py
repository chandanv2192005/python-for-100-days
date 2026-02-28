# Full Example — BMI Calculator with Functions

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def bmi_checker():
    print("--- BMI Calculator ---")
    try:
        weight = float(input("Enter weight (kg): "))
        height = float(input("Enter height (m): "))
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)
        print(f"Your BMI: {bmi}")
        print(f"Category: {category}")
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")

if __name__ == "__main__":
    # Note: bmi_checker() requires user input. 
    # To run it manually, uncomment the line below and run: python3 06_bmi_calculator.py
    # bmi_checker()
    
    # Demonstration with fixed values for automated verification:
    test_w, test_h = 70, 1.75
    test_bmi = calculate_bmi(test_w, test_h)
    print(f"Test BMI (70kg, 1.75m): {test_bmi}")
    print(f"Test Category: {get_bmi_category(test_bmi)}")
