"""
Description of the Task:
Create a Python program that simulates a simple voting system. 
Allow users to vote for different candidates and display the results.

Instructions:
Define a list of candidate names.
Initialize a dictionary to store the votes for each candidate, with candidate names as keys and initial vote counts as values.
Display the list of candidates to the user.
Prompt the user to enter the name of the candidate they want to vote for.
Update the vote count for the selected candidate in the dictionary.
Repeat steps 4-5 until the user decides to stop voting.
Display the final vote count for each candidate.

Learning Objective:
Practice working with lists, dictionaries, and loops in Python.
Understand how to collect and process user input.
Learn how to display formatted output.

"""

"""
program that simulates a simple voting system. 
Allow users to vote for different candidates and display the results.

"""

# define a list of canditate names 
candidates = ['Alice','Bob','Charlie']

# initialize a dictionary to store votes for each candidate 
votes = {}
for candidate in candidates:
    votes[candidate] = 0    # adding List in dictionary initilize all votes to 0 

# voting Process 
while True:
    choice = input("Enter the name of the candidate you want to vote for: ")    # User to vote name of Candidates 

    # check if the casditate is valid 
    if choice in votes:
        votes[choice] += 1
        print ("Vote Recorded.")
    else:
        print("Invalid Candidate. Please Try Again.")

    # ask if user want continue voting 
    continue_voting = input("Do you want to continue voting? (Yes/No): ")
    if continue_voting.lower() != "yes":
        break

# display final result 
print("\nFinal Vote Count:")

for canditate,count in votes.items():
    print(f"{candidate}: {count} votes")

"""
Enter the name of the candidate you want to vote for: Alice
Vote Recorded.
Do you want to continue voting? (Yes/No): yes  
Enter the name of the candidate you want to vote for: David 
Invalid Candidate. Please Try Again.
Do you want to continue voting? (Yes/No): yes      
Enter the name of the candidate you want to vote for: Charlie
Vote Recorded.
Do you want to continue voting? (Yes/No): No

Final Vote Count:
Charlie: 1 votes
Charlie: 0 votes
Charlie: 1 votes
"""