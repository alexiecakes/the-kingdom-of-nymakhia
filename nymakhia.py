# The Kingdom of Nymakhia
import textwrap

class Room:
	hasPlayer = False

	def __init__(self, name, sdesc, ldesc):
		self.name = name
		self.sdesc = sdesc
		self.ldesc = ldesc
	
	def n(self):
		try:
			self.hasPlayer = False
			self.n.hasPlayer = True
			print "Moving north to %s" % self.n.name
		except AttributeError:
			print "There is nothing for you that way."
			
	def look(self):
		print "-" * 42
		print self.name.center(42, " ")
		print "-" * 42
		print ""
		print textwrap.fill(self.ldesc, 42)
		print ""
		
	def glance(self):
		print self.sdesc + "\n"
		
throne = Room("The Ruins of the Sunset Throne", "These are the ruins of a once great sandstone throneroom.", "Insert ldesc here")
throne.hasPlayer = True

s = raw_input()
if s.lower() == 'look' or s.lower() == 'l':
	throne.look()
elif s.lower() == 'glance' or s.lower() == 'gl':
	throne.glance()
else:
	print "What?"