#!/usr/bin/python
#This is and application which whows the content of "see also" on Wikipedia
#IT must work recursively

#first, we have to upload Wikipedia
import wikipedia

#we need warnings as well:
import warnings

#
import time

warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

#marking sites witch were already seen:
visited = set()

#Maximum time allowed:
MaxTimeAllowed = 50  #seconds

#From which page we start:
try:
	startingPoint = raw_input("Enter the phrase you want to start with: \n")
except Exception:
	print ("Error! Phrase unavailable")
#	print str(Exception)
	exit(1)
#print(startingPoint)
try:
	startingPage = wikipedia.page(startingPoint)
except Exception:
	print ("Error! Starting Page can't be reached")
#	print str(Exception)
	exit(1)
#the seeAlso part:
try:
	seeAlso = startingPage.section("See also")
except Exception:
	print ("Error! 'See Also' section can't be reached")
#	print str(Exception)
	exit(1)

#the list of "seeAlso"
try:
	list = {s.strip() for s in seeAlso.splitlines()}	
except Exception:
	print ("Error! List can not be generated")
#	print str(Exception)
	exit (1)

#looping thorugh the list

while len(list) != 0 :
	start = time.time()	
	for i in list.copy():
		if (time.time() - start) >MaxTimeAllowed:
			print ("IT takes too long!")
			break
		if wikipedia.page(i).url not in visited:
			visited.add(wikipedia.page(i).url)
			try:
				seeAlso = wikipedia.page(i).section("See also")
			except Exception:#wikipedia.exceptions as e:
				print ("Error in 'See Also section!'")
#				print str(Exception)
				list.remove(i)
				pass

			try:
				list.update({s.strip() for s in seeAlso.splitlines()})

			except Exception:
				print("Unable to update the list!")
#				print str(Exception)
				pass

			try:
				print('{}: {}'.format(i, wikipedia.page(i).url))
			except Exception:
				print ("This one is unavailable, sorry!")
#				print str(Exception)
				pass

		else:
			 continue
	if (time.time() - start) > MaxTimeAllowed:
		print("definietelt too long!")
		break

print ("And that is all")
exit ()



