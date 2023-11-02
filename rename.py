newName = input("[+] enter the new name : ")
newName = f'"{newName}"'
with open('/data/data/com.termux/files/home/.zshrc','r') as file:
    allLines = []
    pos= 0
    for i, line in enumerate(file):
        if "TNAME=" in line:
            pos = i
        allLines.append(line)
    allLines[pos] = f"TNAME={newName}" + "\n"
with open('/data/data/com.termux/files/home/.zshrc','w') as file:
    file.writelines(allLines)
print("Updated sucessfully restart to see changes")
