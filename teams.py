# Randomly partition people into teams.
# Copyright © 2014 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.

# Given a team size n and a number m of team members,
# print out the teams one per line. If m is
# not evenly divisible by n, assign the "extra" members
# evenly to other teams.

from random import randrange

# Team size
n = int(input("Team size? "))

# Number of participants
m = int(input("Number of participants? "))

# Given a list of participants, return
# teams as a list of lists of participants.
def make_teams(participants):
    # Set up counts and accumulator.
    teams = []
    l = len(participants)
    residue = l % n

    # Loop over teams.
    for _ in range(l // n):
        # Set up accumulator.
        members = []
        
        # Check for an extra person that needs a team.
        team_size = n
        if residue > 0:
            team_size += 1
            residue -= 1
        
        # Loop over team members.
        for _ in range(team_size):
            i = randrange(len(participants))
            members += [participants[i]]
            del participants[i]
        
        # Remember the new team.
        teams += [members]

    return teams
            
    
# Produce the teams.
teams = make_teams(list(range(1, m + 1)))

# Print the team list.
print("Teams")
participant_index = [0] * m
for i in range(len(teams)):
    print(str(i + 1) + ":", end='')
    for p in teams[i]:
        print(" " + str(p), end='')
        participant_index[p - 1] = i + 1
    print()

print()

# Print the participant index.
print("Participants")
for i in range(m):
    print(str(i + 1) + ": ", participant_index[i])
