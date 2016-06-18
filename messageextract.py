import sys, subprocess, re, base64, logging, time

class Extract(object):

	def __init__(self, filename):
		self.filename = 'messages.htm'
		self.tidied = 'tidied' + self.filename + 'l'
		self.extractmessages()

	def extractmessages(self):
		p = subprocess.call(["ls", "-l"])
		time.sleep(1)
		p = subprocess.call(['tidy', self.filename, '>', self.tidied])
		time.sleep(1)
		p = subprocess.call(["ls", "-l"])
		print "File has been extracted"
		f = open(self.tidied, 'r')
		cnt = 0
		for line in f:
			if cnt > 25:
				break
			print line
			cnt += 1
		f.close()
	 	p = subprocess.call(['rm', self.tidied])
	 	p = subprocess.call(["ls", "-l"])

if __name__ == '__main__':
	
