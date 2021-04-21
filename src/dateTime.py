class dateTime:
	def __init__(self, year=0000, month=00, day=00, hour=00, minute=00, second=00):
		self.year = year
		self.month = month
		self.day = day
		self.hour = hour
		self.minute = minute
		self.second = second

	def getYear(self):
		return self.year

	def getMonth(self):
		return self.month

	def getDay(self):
		return self.day

	def getHour(self):
		return self.hour

	def getMinute(self):
		return self.minute

	def getSecond(self):
		return self.second
