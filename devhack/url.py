import os

a = os.listdir()

final = []

for i in a:
    final.append(i.replace(" ", "%20"))

f = open("urls.txt", "w")

for i in final:
    f.write(f"https://github.com/DSC-KIIT/certificates/raw/master/devhack/{i}\n")

f.close()