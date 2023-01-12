# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime




   

def compute_age(bday):

    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(bday, "%Y-%m-%d")
    today = datetime.now()

  
    years = today.year - birthdate.year

    
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    kg = pounds * 0.45359237
    return kg


def cm_from_in(inches):
    cm = inches * 2.54
    return cm


def body_mass_index(weight, height):
    bmi = weight / (height ** 2) * 10000
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender.upper() == "F":
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    
    elif gender.upper() == "M":
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
        
    else:
        print("ERROR")
    return bmr


def main():
    
    gender = input("What is your gender? (M or F): ")
    bday = input("Enter your birthday (YYYY-MM-DD): ")
    pounds = float(input("Enter your weight in U.S. pound: "))
    inches = float(input("Enter in your height in U.S. inches: "))
    

   
    years = compute_age(bday)
    kg = kg_from_lb(pounds)
    cm = cm_from_in(inches)
    bmi = body_mass_index(kg, cm)
    bmr = basal_metabolic_rate(gender, kg, cm, years)
    
    

    # Print the results for the user to see.
    print(f"Age (years): {years}")
    print(f"Weight (kg): {kg:.2f}")
    print(f"Height (cm): {cm:.1f}")
    print(f"Body mass index: {bmi:.1f}")
    print(f"Basal metabolic rate (kcal/day): {bmr:.0f}")    


# Call the main function so that
# this program will start executing.
main()


