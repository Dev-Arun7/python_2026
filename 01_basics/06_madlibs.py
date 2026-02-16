# Madlibs game - a fun way to practice string concatenation and user input
# The user will be prompted to enter various words (nouns, verbs, adjectives, etc.) 
# and then those words will be inserted into a pre-defined story template to create a funny story.

# Get user input for the madlibs
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
adjective3 = input("Enter one more adjective: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
verb1 = input("Enter a verb: ")
verb2 = input("Enter another verb: ")

print(f"Today I went to the zoo and saw a {adjective1} {noun1} jumping up and down in its tree. ")
print(f"He {verb1} {adjective2}ly through the large tunnel that led to its {adjective3} {noun2}.")
print(f"I got some peanuts and passed them through the cage to a gigantic gray {noun1} towering above my head. ")
print(f"Feeding that animal made me hungry. I went to get a {adjective1} scoop of ice cream. It filled my stomach. ")
print(f"Afterwards I had to {verb2} {adjective2} to catch our bus. ")
print("When I got home I {verb1} my mom for a {adjective3} day at the zoo.")    
print("The end!")