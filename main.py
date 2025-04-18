# 1. Create a Dictionary 
print("\n1.================================")

push_ups = {

    "exercise": "Push Ups",
    "sets": 3,
    "reps": 15,
    "notes": "Keeps your back straight, hands shoulder_width apart"

}
print(push_ups)

# 2. Accessing Dictionary keys
print("\n2.================================")

# print out keys from the dictionary
print(push_ups["exercise"])
print(push_ups["sets"])
print(push_ups["reps"])
print(push_ups["notes"])


# 3.Accessing Dictionary keys
print("\n3.================================")

# update the sets of the exercise
push_ups["sets"] = 5

# delete node with del
del push_ups["notes"]

# add the key back
push_ups["workout_note"] = "Keep your back straight, hands shoulder_width apart"

# print out the dictionary
print(push_ups)


# 4. Accessing nested data
print("\n4.================================")
# - Add the nested dictionary below
workout_plan = {
    "Push-ups": {
        "sets": 3,
        "reps": 15,
        "notes": "Keep your back straight, hands shoulder_width apart"

    },
    "Squats": {
        "sets": 4,
        "reps": 12,
        "notes": "Go as long as you can, while maintaining proper form"
    },
    "Plank": {
        "sets": 2,
        "reps": "Hold for 60 seconds",
        "notes": "Engage your core and keep your body in a straight line.",

    },
    "Lunges": {
        "sets": 3,
        "reps": 10,
        "notes": "Each leg. Step forward and lower your body until your front knee iss at 90-degree angle."
    },
    "Bicep Curls": {
        "sets": 3,
        "reps": 12,
        "notes": "Use dumbbells, keep your elbows close to your body."
    }
}
# Accessing Lunges notes
print(workout_plan["Lunges"]["notes"])


# 5. Iterating over a dictionary 
print("\n5.================================")
for key, value in workout_plan.items():
    print(f"{key.upper()}:{value}")
print("\n=================================")