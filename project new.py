

# Calculate the daily calorie needs for an older lady
# based on the Harris-Benedict equation

def calculate_daily_calorie_needs(age, weight, height, gender, activity_level):
    if gender == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == 'female':
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        print("Invalid gender")
        return None
    
    if activity_level == 'sedentary':
        caloric_needs = bmr * 1.2
    elif activity_level == 'lightly active':
        caloric_needs = bmr * 1.375
    elif activity_level == 'moderately active':
        caloric_needs = bmr * 1.55
    elif activity_level == 'very active':
        caloric_needs = bmr * 1.725
    else:
        print("Invalid activity level")
        return None
    
    return caloric_needs

# Example usage
age = 70
weight = 60 # kg
height = 160 # cm
gender = 'female'
activity_level = 'lightly active'

daily_calorie_needs = calculate_daily_calorie_needs(age, weight, height, gender, activity_level)
print("Daily calorie needs:", daily_calorie_needs)
# Define the recommended daily intake for an older lady's balanced diet plan
# Define recommended daily intake for different nutrients
RECOMMENDED_INTAKE = {
    'calories': 1600, 
    'protein': 46, 
    'fat': 20, 
    'carbs': 130, 
    'fiber': 25, 
    'sugar': 20,
    'sodium': 2300,
    'potassium': 4700,
    'calcium': 1200,
    'vitamin_d': 800,
    'vitamin_c': 75,
    'vitamin_a': 700,
}

# Define a function to calculate the recommended daily intake based on age and gender
def calculate_intake(age, gender):
    intake = RECOMMENDED_INTAKE.copy()
    if gender == 'female':
        intake['calories'] -= 200
        intake['protein'] -= 5
        intake['sodium'] -= 300
        intake['calcium'] += 200
        intake['vitamin_d'] += 400
    if age >= 51:
        intake['fiber'] += 2
        intake['vitamin_d'] += 200
        intake['calcium'] += 200
        intake['vitamin_b12'] += 1.5
    return intake

# Define a function to recommend a well-balanced diet based on the user's current intake
def recommend_diet(current_intake, age, gender):
    # Calculate the recommended daily intake based on age and gender
    recommended_intake = calculate_intake(age, gender)

    # Calculate the percentage of recommended intake for each nutrient
    percentages = {}
    for nutrient in recommended_intake:
        percentage = (current_intake.get(nutrient, 0) / recommended_intake[nutrient]) * 100
        percentages[nutrient] = percentage

    # Recommend foods to eat based on which nutrients are lacking
    recommendations = []
    if percentages['protein'] < 100:
        recommendations.append('lean protein sources such as chicken, fish, and tofu')
    if percentages['fat'] < 100:
        recommendations.append('healthy fats such as nuts, seeds, and avocado')
    if percentages['carbs'] < 100:
        recommendations.append('complex carbohydrates such as whole grains and fruits')
    if percentages['fiber'] < 100:
        recommendations.append('fiber-rich foods such as vegetables and legumes')
    if percentages['sugar'] > 100:
        recommendations.append('limiting added sugars such as candy and soda')
    if percentages['sodium'] > 100:
        recommendations.append('limiting sodium-rich foods such as processed meats and packaged snacks')
    if percentages['potassium'] < 100:
        recommendations.append('foods rich in potassium such as bananas and sweet potatoes')
    if percentages['calcium'] < 100:
        recommendations.append('calcium-rich foods such as dairy products and leafy greens')
    if percentages['vitamin_d'] < 100:
        recommendations.append('vitamin D-rich foods such as fatty fish and fortified dairy products')
    if percentages['vitamin_c'] < 100:
        recommendations.append('foods high in vitamin C such as citrus fruits and bell peppers')
    if percentages['vitamin_a'] < 100:
        recommendations.append('foods high in vitamin A such as carrots and sweet potatoes')

import random

# Create lists of food items for each food group
grains = ["oatmeal", "whole wheat bread", "brown rice", "quinoa", "whole grain pasta"]
vegetables = ["spinach", "broccoli", "carrots", "sweet potatoes", "tomatoes"]
fruits = ["blueberries", "apples", "bananas", "strawberries", "oranges"]
dairy = ["low-fat milk", "greek yogurt", "low-fat cheese"]
protein = ["salmon", "chicken breast", "eggs", "tofu", "beans"]

# Define daily serving recommendations for each food group
grains_servings = 3
vegetables_servings = 3
fruits_servings = 2
dairy_servings = 3
protein_servings = 4

# Generate a random selection of food items from each food group
grains_selection = random.sample(grains, grains_servings)
vegetables_selection = random.sample(vegetables, vegetables_servings)
fruits_selection = random.sample(fruits, fruits_servings)
dairy_selection = random.sample(dairy, dairy_servings)
protein_selection = random.sample(protein, protein_servings)

# Print out the daily diet plan
print("Daily Diet Plan:")
print("Grains: ", grains_selection)
print("Vegetables: ", vegetables_selection)
print("Fruits: ", fruits_selection)
print("Dairy: ", dairy_selection)
print("Protein: ", protein_selection)
import datetime

def monitor_exercise():
    today = datetime.date.today()
    print("Today's date:", today)
    
    # Ask for input of exercise duration in minutes
    exercise_duration = int(input("Enter exercise duration in minutes: "))
    
    # Set the recommended exercise duration for the day (30 minutes for elderly)
    recommended_duration = 30
    
    # Calculate the difference between recommended and actual exercise duration
    exercise_diff = exercise_duration - recommended_duration
    
    # Check if the exercise duration meets the recommended duration
    if exercise_duration >= recommended_duration:
        print("Great job! You have met the recommended exercise duration for the day.")
    else:
        print(f"You need to exercise for {abs(exercise_diff)} more minutes to meet the recommended exercise duration for the day.")
        
monitor_exercise()


# set the target daily exercise goal in minutes
target_exercise_goal = 30

# create an empty list to store exercise logs
exercise_logs = []

def log_exercise(duration):
    """Logs a completed exercise session with the given duration."""
    timestamp = datetime.datetime.now()
    exercise_logs.append((timestamp, duration))
    print(f"Logged {duration} minutes of exercise at {timestamp}.")

def get_total_exercise_today():
    """Returns the total minutes of exercise logged today."""
    today = datetime.date.today()
    total = 0
    for log in exercise_logs:
        log_date = log[0].date()
        if log_date == today:
            total += log[1]
    return total

def get_average_exercise_per_week():
    """Returns the average minutes of exercise per week, over the last 4 weeks."""
    now = datetime.datetime.now()
    one_week_ago = now - datetime.timedelta(weeks=1)
    four_weeks_ago = now - datetime.timedelta(weeks=4)
    total = 0
    count = 0
    for log in exercise_logs:
        log_date = log[0].date()
        if four_weeks_ago <= log[0] <= one_week_ago:
            total += log[1]
            count += 1
    if count == 0:
        return 0
    else:
        return total / count

# example usage:
log_exercise(20) # logs a 20-minute exercise session
log_exercise(40) # logs a 40-minute exercise session
print("Total exercise today:", get_total_exercise_today())

print("Average exercise per week:", get_average_exercise_per_week())


import datetime

# Define function for scheduling checkups
def schedule_checkup(last_checkup):
    # Check if it's been more than 6 months since the last checkup
    six_months_ago = datetime.datetime.today() - datetime.timedelta(days=180)
    if last_checkup < six_months_ago:
        # Schedule a new checkup
        next_checkup = last_checkup + datetime.timedelta(days=180)
        print("It's time to schedule your next checkup for", next_checkup.strftime('%m/%d/%Y'))
    else:
        print("You don't need to schedule a checkup yet.")

# Example usage
last_checkup = datetime.datetime(2022,2, 1)#change date when u checkup
schedule_checkup(last_checkup)

 
import datetime

# Function to calculate the duration of sleep
def calculate_sleep_duration(start_time, end_time):
    duration = end_time - start_time
    return duration.seconds // 3600  # Convert seconds to hours

# Function to check if the old lady got sufficient sleep
def is_sufficient_sleep(duration):
    if duration >= 7:
        return True
    else:
        return False

# Get the current date and time
now = datetime.datetime.now()

# Get the sleep start and end times from the user
sleep_start = datetime.datetime.strptime(input("Enter sleep start time (in HH:MM format): "), "%H:%M")
sleep_end = datetime.datetime.strptime(input("Enter sleep end time (in HH:MM format): "), "%H:%M")

# Calculate the duration of sleep
sleep_duration = calculate_sleep_duration(sleep_start, sleep_end)

# Check if the old lady got sufficient sleep
if is_sufficient_sleep(sleep_duration):
    print("Good job! You got enough sleep.")
else:
    print("You need to sleep for at least 7 hours to stay healthy.")

import time
import datetime

# Set stress management goals
goal_minutes = 30

# Keep track of stress management time
stress_mgmt_time = 0

# Loop to simulate stress management activity
while True:
    # Prompt user to enter stress management activity time in minutes
    activity_time = int(input("Enter stress management activity time in minutes (0 to exit): "))
    
    # Exit loop if user enters 0
    if activity_time == 0:
        break
    
    # Add activity time to total stress management time
    stress_mgmt_time += activity_time
    
    # Check if goal has been met
    if stress_mgmt_time >= goal_minutes:
        # If goal has been met, print message and break out of loop
        print("Congratulations, you have met your stress management goal!")
        break
    
    # Print remaining time to reach goal
    remaining_time = goal_minutes - stress_mgmt_time
    print("You still need to do", remaining_time, "minutes of stress management activity today.")

   
import datetime

def record_social_activity():
    # Record social activity for the day
    today = datetime.date.today()
    activity = input("What social activities did you participate in today? ")
    with open("social_activity_log.txt", "a") as log_file:
        log_file.write(f"{today}: {activity}\n")

def view_social_activity():
    # View recorded social activities
    with open("social_activity_log.txt", "r") as log_file:
        for line in log_file:
            print(line)

# Main program
while True:
    print("1. Record social activity")
    print("2. View recorded social activity")
    print("3. Exit")
    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        record_social_activity()
    elif choice == "2":
        view_social_activity()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Try again.")
def avoid_alcohol(age, drinks_per_week):
    if age > 65 and drinks_per_week > 0:
        print("Please consider reducing or avoiding alcohol consumption.")
    else:
        print("You are within safe alcohol consumption limits.")

# Example usage
avoid_alcohol(70, 2)  # Output: Please consider reducing or avoiding alcohol consumption.
avoid_alcohol(60, 1)  # Output: You are within safe alcohol consumption limits.
import datetime

# Define a function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Define a function to check if a person is underweight, normal, overweight or obese
def check_bmi_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi < 25:
        return "normal weight"
    elif 25 <= bmi < 30:
        return "overweight"
    else:
        return "obese"

# Define a function for the balanced diet plan
def balanced_diet():
    # Include all the food items that an elderly person should consume
    diet = {
        "fruits": ["apples", "bananas", "oranges", "grapes"],
        "vegetables": ["spinach", "carrots", "broccoli", "sweet potatoes"],
        "protein": ["beans", "chicken", "fish", "eggs"],
        "dairy": ["milk", "yogurt", "cheese"],
        "whole grains": ["brown rice", "whole wheat bread", "oatmeal"],
    }
    return diet

# Define a function for exercise routine
def exercise_routine():
    # Include exercises that are beneficial for elderly persons
    exercises = ["walking", "swimming", "cycling", "yoga"]
    return exercises

# Define a function for setting medication reminders
def set_alarm():
    # Set an alarm for medication reminders
    alarm_time = input("Enter the time for medication reminder (HH:MM AM/PM): ")
    alarm_time = datetime.datetime.strptime(alarm_time, "%I:%M %p")
    return alarm_time

# Define a function for stress management
def stress_management():
    # Include stress-relieving activities
    activities = ["meditation", "deep breathing exercises", "listening to music", "reading"]
    return activities

# Define a function for avoiding smoking and alcohol
def avoid_smoking_alcohol():
    # Advise against smoking and alcohol consumption
    print("Smoking and alcohol consumption are harmful to health. Please avoid them.")

# Define a function for social activities
def social_activities():
    # Suggest social activities that elderly persons can engage in
    activities = ["playing board games with friends and family", "attending community events", "joining a hobby group"]
    return activities

# Call the functions
weight = 70 # in kilograms
height = 1.6 # in meters
bmi = calculate_bmi(weight, height)
bmi_category = check_bmi_category(bmi)
print("Your BMI is:", bmi)
print("Your BMI category is:", bmi_category)

diet_plan = balanced_diet()
print("Your balanced diet plan is:", diet_plan)

exercise_plan = exercise_routine()
print("Your exercise routine includes:", exercise_plan)

medication_reminder = set_alarm()
print("Your medication reminder is set for:", medication_reminder)

stress_relief_activities = stress_management()
print("Your stress-relief activities include:", stress_relief_activities)

avoid_smoking_alcohol()

social_activities = social_activities()
print("Your suggested social activities include:", social_activities)


    
