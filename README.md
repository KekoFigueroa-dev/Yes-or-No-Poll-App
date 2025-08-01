# Yes or No Voting App

A simple Python console application for running a yes/no poll with multiple voters. Prevents duplicate voting, handles non-standard answers, and provides admin-only access to detailed results.

## Features

- Custom yes/no poll question
- Configurable number of voters
- Prevents duplicate votes by name
- Accepts "yes", "y", "no", "n" (case-insensitive)
- Handles non-yes/no answers gracefully
- Announces poll winner or tie
- Admin password required to view detailed results
- Fun ASCII voting sheet at the end

## Usage

1. **Clone the repository:**
   ```
   git clone https://github.com/KekoFigueroa-dev/Yes-or-No-Poll-App.git
   ```
2. **Navigate to the project directory:**
   ```
   cd Yes-or-No-Poll-App
   ```
3. **Run the app:**
   ```
   python voterapp.py
   ```

## Example

```
Welcome to my Yes or No Voting App!
This app allows you to vote on a simple yes or no question.
What yes/no issue would you like to vote on? Should soda be banned for young children?
How many people will be voting? 3
Please set a password for the poll: admin123
Enter your Full Name: John Smith
Please enter your vote for the issue: Should soda be banned for young children?
What do you think Yes or No? yes
Thank you for voting, John Smith!
...
```

## License