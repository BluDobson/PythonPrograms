def write_teams():
    file = open("teams.txt", "w")

    team1 = "Team 1: Chelsea" + "\n"
    team2 = "Team 2: Manchester United" + "\n"
    team3 = "Team 3: Liverpool" + "\n"
    team4 = "Team 4: Arsenal" + "\n"
    team5 = "Team 5: Manchester City" + "\n"

    file.write(team1)
    file.write(team2)
    file.write(team3)
    file.write(team4)
    file.write(team5)

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