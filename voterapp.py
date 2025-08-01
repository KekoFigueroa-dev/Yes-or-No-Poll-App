#Voter app

# Welcome
print("Welcome to my Yes or No Voting App!")
print("This app allows you to vote on a simple yes or no question.")

# Poll Setup
question = input("What yes/no issue would you like to vote on? ")
vote_number = int(input("How many people will be voting? "))
poll_pwd = input("Please set a password for the poll: ")

# Vote Tracking
yes = 0
no = 0
results = {}

# Voting Loop
for i in range(vote_number):
    name = input("Enter your Full Name: ").title().strip()
    if name in results.keys():
        print("You have already voted!")
    else:
        print("Please enter your vote for the issue: " + question)
        choice = input("What do you think Yes or No? ").lower().strip()
        if choice == "yes" or choice == "y":
            choice = 'yes'
            yes += 1
        elif choice == "no" or choice == "n":
            choice = 'no'
            no += 1
        else:
            print("That is not a valid choice, but We guess its your choice.")
        results[name] = choice
        print(f"Thank you for voting, {name}!")

# Voter List
print(f"The following {vote_number} people voted:")
for voter in results.keys():
    print(f"{voter}")

# Poll Results
print(f"On the following issue: {question}")
if yes > no:
    print(f"Yes won with {yes} votes! to {no} votes for No.")
elif no > yes:
    print(f"No won with {no} votes! to {yes} votes for Yes.")
else:
    print(f"It's a tie! Both Yes and No received {yes} votes.")

print("")

# Admin Results Access
user_type = input("Are you a voter or an admin?, enter admin password to access the voter results: ").lower().strip()

if user_type == poll_pwd:
    print("Access granted. Here are the voting results:")
    for voter, vote in results.items():
        print(f"{voter}: {vote}")
    print(f"Total Yes votes: {yes}")
    print(f"Total No votes: {no}")    
else:
    print("Access denied. You are not authorized to view the results.")

# Goodbye
print("Thank you for using the Voting App! Goodbye!")

# Voting Sheet ASCII Art
print("""
    ________________
   |                |
   |  VOTING SHEET  |
   |________________|
   |                |
   |  Yes:  [ ]     |
   |  No:   [ ]     |
   |________________|
""")