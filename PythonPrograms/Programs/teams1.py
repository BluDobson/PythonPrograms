def write_teams():
    file = open("teams.txt", "w")
    teams = ["Team 1: Chelsea", "Team 2: Manchester United", "Team 3: Liverpool", "Team 4: Arsenal", "Team 5: Manchester City"]
    for i in teams:
        file.write(f"{i}\n")
    file.close()

def read_teams():
    file = open("teams.txt", "r")

    outfile = ""
    lines = file.readlines()
    outfile = outfile + lines[0]
    outfile = outfile + lines[3]
    print(outfile)

write_teams()
read_teams()