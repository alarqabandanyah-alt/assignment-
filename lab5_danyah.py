# ============================================================
# Lab 5 - WEEK 5 : The VibeCheck Bug Hunt
# ============================================================
# Name: Danyah Alarqaban
#
# Your job: fix every bug so the file runs with NO errors
# and prints the correct output.
# ============================================================


# ------------------------------------------------------------
# PART 1: A function that greets a user
# ------------------------------------------------------------

# Predict: I think this function will print a VibeCheck message.
def send_vibe():
    print("VibeCheck says: good energy only")


# Predict: I think this function will welcome the user.
def welcome_user():
    print("Welcome to VibeCheck!")


# ------------------------------------------------------------
# PART 2: A function that uses a variable
# ------------------------------------------------------------

# Predict: I think this will print that today's mood is hyped.
def show_mood():
    mood = "hyped"
    print(f"Today's mood is {mood}")


# ------------------------------------------------------------
# PART 3: A function with parameters
# ------------------------------------------------------------

# Predict: I think this will return the person's name and mood.
def make_shoutout(name, mood):
    return f"{name} is feeling {mood} today!"


# ------------------------------------------------------------
# PART 4: A function that counts hype points
# ------------------------------------------------------------

# Predict: I think this will add likes and shares together.
def count_hype(likes, shares):
    total = likes + shares
    return total


# Predict: I think this will print a thank-you message.
def final_message():
    print("Thanks for using VibeCheck!")


# ============================================================
# RUNNING THE CODE
# ============================================================

send_vibe()
welcome_user()
show_mood()

# Predict: I think this will say Jordan is feeling creative today.
print(make_shoutout("Jordan", "creative"))

# Predict: I think this will say Alex is feeling chill today.
print(make_shoutout("Alex", "chill"))

# Predict: I think this will print 15.
print(count_hype(10, 5))

# Predict: I think this will print a thank-you message.
final_message()





