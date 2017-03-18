NORTH= 90
SOUTH= 270
EAST= 0
WEST= 180

class Robot: 
	def __init__ (self, bearing = NORTH ,x=0, y=0): #default direction, FYI, is North
		self.bearing = bearing
		self.x= x
		self.y = y

	@property
	def coordinates(self):
		return (self.x, self.y)

	def turn_right(self):
		self.bearing = (self.bearing-90) % 360 #Yay! Negative modulus!

	def turn_left(self):
		self.bearing = (self.bearing+90) % 360 #if we are going left we turn 90 degrees, unit circle

	def advance(self):
		if self.bearing == NORTH: #if we are going forward, facing north, y+1
			self.y+=1
			#self.coordinates = (self.x,self.y) 
			#NB: The previous line and 'self.coordinates' line could be combined.
		if self.bearing == SOUTH: #if we are going forward, facing south, y-1
			self.y-=1
			#self.coordinates = (self.x,self.y)
		if self.bearing == EAST: #if we are going forward, facing east, x+1
			self.x+=1
			#self.coordinates = (self.x,self.y)
		if self.bearing == WEST: #if we are going forward, facing west, x-1
			self.x-=1
			#self.coordinates = (self.x,self.y)

	def simulate(self, pathString):
		listString = list(pathString) #turn string into list of letters
		for step in listString: #'translate' list of strings into movements
			if step =="R":
				self.turn_right()
			if step == "L":
				self.turn_left()
			if step =="A":
				self.advance()

class Luftrobot(Robot):
	def __init__ (self, bearing = NORTH ,x=0, y=0, altitude= 0): #default direction, FYI, is North
		Robot.__init__(self,bearing, x, y)
		self.altitude = altitude
	
	@property
	def coordinates(self):
		return (self.x, self.y, self.altitude)

	def warp(self, distance):
		for i in range(distance):
			self.advance()
	
	def goback(self): #reverse of advance
		if self.bearing == NORTH: #if we are going forward, facing north, y+1
			self.y-=1
			#self.coordinates = (self.x,self.y) 
			#NB: The previous line and 'self.coordinates' line could be combined.
		if self.bearing == SOUTH: #if we are going forward, facing south, y-1
			self.y+=1
			#self.coordinates = (self.x,self.y)
		if self.bearing == EAST: #if we are going forward, facing east, x+1
			self.x-=1
			#self.coordinates = (self.x,self.y)
		if self.bearing == WEST: #if we are going forward, facing west, x-1
			self.x+=1
			#self.coordinates = (self.x,self.y)
	def ascend(self):
		self.altitude+=1
	def descend(self):
		self.altitude-=1
	def simulate(self, pathString):
		listString = list(pathString) #turn string into list of letters
		for step in listString: #'translate' list of strings into movements
			if step =="R":
				self.turn_right()
			if step == "L":
				self.turn_left()
			if step =="A":
				self.advance()
			if step == "U":
				self.ascend()
			if step =="D":
				self.descend()



