# Nested IF Statements
# A nested IF statement is an IF statement that is inside another IF statement.


# Example of a nested IF statement
age = 20
balance = 1000

if age >= 18: # if age is greater than or equal to 18, then do the code below
    if balance > 500: # if balance is greater than 500, then do the code below
        print("You can access alcahole!")
    else: # if the above condition is false, then do the code below
        print("Not enough money!")
else: # if the above condition is false (first if condition), then do the code below
    print("You are too young to access alcahole!")

# -----------------------------------------------------------------------------------

# Example of nested IF statement: Movie Ticket Check
age = 16
has_permission = True
money = 300

if age >= 18:  # Check if person is adult
    if money >= 250:  # Check if person has enough money
        print("You can buy a movie ticket!")
    else:
        print("You don't have enough money for the ticket!")
else:  # Person is under 18
    if has_permission:  # Check if parent permission is given
        if money >= 250:
            print("You can buy a movie ticket with permission!")
        else:
            print("You need more money, even with permission!")
    else:
        print("You cannot watch the movie, too young and no permission!")

