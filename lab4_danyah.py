# Danyah Alarqaban | Lab 4 | Intro to Python
# Ticket 1
# Predict:
# Access granted: 17, 25, 13
# Too young: 11, 9
ages = [17, 25, 13, 11, 9]
for age in ages:
    if age >= 13:
        print(f"{age} - Access granted ✅")
    else:
        print(f"{age} - Too young ❌")

# EXPLAIN:
# The variable age holds one number from the list each time the loop runs.

# Ticket 2
# PREDICT:
# The loop will run once because keeps_checking starts as "yes".
# If the user types "no" after the first check, the loop stops.
keeps_checking = "yes"
while keeps_checking == "yes":
    age = int(input("Enter your age: "))
    if age >= 13:
        print("Access granted ✅")
    else:
        print("Too young ❌")
    keeps_checking = input("Check another age? (yes/no): ")
# EXPLAIN:
# A while loop is a good choice because we do not know how many times the user want to check an age.

# Ticket 3
# PREDICT:
# Without the break statement, the loop would never end.
while True:
    age = input("Enter an age or type 'stop': ")
    if age == "stop":
        break

    age = int(age)
    if age >= 13:
        print("Access granted ✅")
    else:
        print("Too young ❌")
# EXPLAIN:
# Ticket 2 keeps running while the answer is "yes."
# Ticket 3 keeps running forever until break is used when the user types "stop."

# Ticket 4
# PREDICT:
# The output is the same as Ticket 1, but now the checking is done by a function.
def can_access(age):
    return age >= 13

for age in ages:
    if can_access(age):
        print(f"{age} - Access granted ✅")
    else:
        print(f"{age} - Too young ❌")
# EXPLAIN:
# A function lets us reuse the same code instead of writing the if/else every time.

# Ticket 5 
# PREDICT : 
# --- StreamPass Signup Report ---
# Signup #1 | Age 22 — Access granted ✅
# Signup #2 | Age 10 — Too young ❌
# Signup #3 | Age 15 — Access granted ✅
# Signup #4 | Age 8 — Too young ❌
# Signup #5 | Age 19 — Access granted ✅
# Signup #6 | Age 13 — Access granted ✅
# Approved: 4 out of 6
def signup_reports(signups):
    approved = 0
    print("--- StreamPass Signup Report ---")

    for number, age in enumerate(signups, start=1):
        if can_access(age):
            print(f"Signup #{number} | Age {age} — Access granted ✅")
            approved += 1
        else:
            print(f"Signup #{number} | Age {age} — Too young ❌")

    print(f"Approved: {approved} out of {len(signups)}")


signups = [22, 10, 15, 8, 19, 13]
signup_reports(signups)

# EXPLAIN:
# I used variables, lists, functions, parameters, for loops,
# while loops, if/else statements, enumerate(), input(), break,
# comparison operators, and a counter variable.







            




   