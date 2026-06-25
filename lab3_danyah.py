# Danyah Alarqaban | Lab 3 | Intro to Python
#Ticket 1
username="danyah123"
#Predict: I think the character count will be 9
print(len(username))
#Explain: The len() function returns the number of characters in a string.
#Ticket 2
#Predict: d and 3
print(username[0])
print(username[len(username)-1])
#explain the index 0 is the first character in the string and the index -1 is the last character in the string. 
#Ticket 3
# Predict: Yes, both lines look the same but the first line is a string and the second line is a list.
print("Welcome to Loop, @" + username + "!")
print(f"Welcome to Loop, @{username}!")
#explain : f-strings are easier because you don't have to use concatenation signs and variables
# Ticket 4
# PREDICT: I think it will cause an error.

# username[0] = "X"  # run this, it breaks on purpose

# ERROR: TypeError: 'str' object does not support item assignment

print(username.upper())

# EXPLAIN: Strings are immutable, which means their individual letters cannot be changed.
# Explain : Stings are immutable, meaning that they cannot be changed after they are created. The upper() method returns a new string with all characters in uppercase, but it does not modify the original string.
# Ticket 5
feed=["First day at loop", " learning python is fun", "Having fun coding"]
#PREDICT: 3 and "First day at loop"
print(len(feed))
print(feed[0])  
#  Explain : Index 0 is used to get the first item in a list
#Ticket 6
# Predict: 3
feed.append("Just posted a new photo")
print(feed)
# Explain: The fourth item is index3 because the first item start at index 0
# Ticket 7
# Predict: "First day at loop" get removed, rest sorted alphabetically
feed.pop(0)
feed.sort()
print(feed)
# Explain The pop() removes first item. sort() put them in alphabetical order.
#Ticket 8
profile = {
"username": username,
"followers": 200,
"verified" : False
}
# Predict: 200 and error
print(profile["followers"])
profile[0] #run this, it breaks on purpose
# ERROR: KeyError: 0
# EXPLAIN: Dictionaries uses keys (names), not number indexes like lists.
# Ticket 9
profile["followers"] = profile["followers"] + 50
profile["bio"] = "I love coding"
print(profile)
# PREDICT: None
print(profile.get("age"))
# Explain: The get () is safer because it does not crash if the key is missing.
# Ticket 10
# PREDICT: @danyah123 has 250 followers and 3 posts. Top post: (one caption)
print(f"@{profile['username']} has {profile['followers']} followers and {len(feed)} posts. Top post: {feed[0]}")
# Explain: This line uses both a dictionary (profile) and a list (feed) to build this line.

