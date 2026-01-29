"""
program that simulates a simple voting system. 
Allow users to vote for different candidates and display the results.

"""

# define a list of canditate names 
candidates =['Alice','Bob','Charlie']

# initialize a dictionary to store votes for each candidate 
votes = {}
for candidate in candidates:
    # adding List in dictionary initilize all votes to 0 
    votes[candidate] = 0

# voting Process 
while True:
    # User to vote name of Candidates 
    choice = input("Enter the name of the candidate you want to vote for: ")

    # check if the casditate is valid 
    if choice in votes:
        votes[choice]+=1
        print ("Vote Recorded.")
    else:
        print("Invalid Candidate. Please Try Again.")

    # ask if user want continue voting 
    continue_voting = input("Do you want to continue voting? (Yes/No): ")
    if continue_voting.lower()!="yes":
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