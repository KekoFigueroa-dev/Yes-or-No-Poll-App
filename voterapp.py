#Voter app
# 1. Print a welcome message and explain the poll
print("Welcome to my Yes or No Voting App!")
print("This app allows you to vote on a simple yes or no question.")
# 2. Define the question to be voted on, number 
question = input(str("What yes/no issue would you like to vote on? "))
vote_number = int(input(str("How many people will be voting? ")))
poll_pwd = input(str("Please set a password for the poll: "))

# 3 Create a Dictionary to hold the voters and the votes
yes = 0
no = 0
results = {}

#Simulate voting trough a loop
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
        print(f"thank you for voting, {name}!")

#debugging print(results)
print("Current voting results:")
for voter, vote in results.items():
    print(f"{voter}: {vote}")