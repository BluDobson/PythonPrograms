def edit_teams():
    file = open("teams.txt", "r")

    outfile = "This is a new line" + "\n"

    for line in range(1, 6):
        if line != 1:
            outfile += file.readline()
        else:
            file.readline()
    print(outfile)
    file = open("teams.txt", "w")
    file.write(outfile)
    file.close()

def read_teams():
    file = open("teams.txt", "r")
    lines = file.readlines()
    print(lines)
    file.close()

edit_teams()
read_teams()