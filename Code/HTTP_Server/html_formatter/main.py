f = open('html.txt', 'r')
for line in f:
    if(line != ""):
        line = line.replace("","")
        line = line.replace("\n","")
        line = line.replace("\r","")
        line = "html += \'" + line + "\'"
        print(line)
