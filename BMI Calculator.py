def get_user_input():
    print("Welcome to BMI Calculator!\n")
    
    unit_system = input("Choose units - (1) Metric (kg, meters) or (2) Imperial (lbs, feet): ")

    if unit_system == "1":
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in meters (m): "))
        bmi = weight / (height ** 2)
    elif unit_system == "2":
        weight = float(input("Enter your weight in pounds (lbs): "))
        height = float(input("Enter your height in feet (ft): "))
        # Convert to metric before calculation
        weight = weight * 0.453592
        height = height * 0.3048
        bmi = weight / (height ** 2)
    else:
        print("Invalid input. Please restart and choose 1 or 2.")
        return

    display_bmi_result(bmi)

def display_bmi_result(bmi):
    print(f"\nYour BMI is: {bmi:.2f}")
    
    if bmi < 18.5:
        print("→ You are Underweight 😕")
    elif 18.5 <= bmi < 24.9:
        print("→ You have a Normal weight 🙂")
    elif 25 <= bmi < 29.9:
        print("→ You are Overweight 😐")
    else:
        print("→ You are Obese 😟")

if __name__ == "__main__":
    get_user_input()
