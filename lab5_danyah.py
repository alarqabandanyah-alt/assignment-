# ============================================================
# Lab 5 - WEEK 5 : The VibeCheck Bug Hunt
# ============================================================
# Name: Danyah Alarqaban
#
# Your job: fix every bug so the file run with NO errors
# and prints the correct output (see the lab sheet).
# ============================================================


# ------------------------------------------------------------

# PART 1: - A function that greets a user
# ------------------------------------------------------------

# BUG 1 FIXED: Added the missing colon 
def send_vibe():
    print("VibeCheck says: good energy only")

# BUG 2 FIXED: Indented the print statement
def welcome_user():
    print("Welcome to VibeCheck!")


# ------------------------------------------------------------
# PART 2 - A function that uses a variable
# ------------------------------------------------------------

def show_mood():
    mood = "hyped"
    # BUG 3 FIXED: Corrected the variable name
    print(f"Today's mood is {mood}")


# ------------------------------------------------------------
# PART 3 - A function with parameters
# ------------------------------------------------------------

def make_shoutout(name,mood):
    return f"{name} is feeling {mood} today!"


# ------------------------------------------------------------
# PART 4 - A function that counts hype points
# ------------------------------------------------------------

def count_hype(likes, shares):
    # BUG 4 FIXED: Add instead of subtract
    total = likes + shares
    return total


def final_message():
    print("Thanks for using VibeCheck!")


# ============================================================
# RUNNING THE CODE
# ============================================================

send_vibe()
welcome_user()
show_mood()

# BUG 6 FIXED: Wrapped in print()
print(make_shoutout("Jordan", "creative"))

# BUG 7 FIXED: Added the missing second argument
print(make_shoutout("Alex", "chill"))

# BUG 8 FIXED: Changed "ten" to the number 10
print(count_hype(10, 5))

# BUG 5 FIXED: Moved this call after the function definition
final_message()





