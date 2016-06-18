#Program to extract messages made by Antara and me for use with IBM Watsons personalit insights engine

txtfile = "antaraplusme.txt"

f = open(txtfile, "r")

antara = open("antara.txt", "w")
mani = open("mani.txt", "w")

isAnt = True

cnt = 0
for line in f:
	#cnt += 1
	#if cnt > 15:
	#	break
	if "Antara Majumdar" in line:
		isAnt = True
		continue
	elif "Manikandan Sundararajan" in line:
		isAnt = False
		continue

	if isAnt == True and [ord(c) for c in line] != [10]:
		print line
		antara.write(line)
	elif isAnt == True:
		continue
	elif isAnt == False and [ord(c) for c in line] != [10]:
		print line
		mani.write(line)
	elif isAnt == False:
		continue

f.close()
antara.close()
mani.close()