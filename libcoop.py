class Ledfade:
	def __init__(self, *args, **kwargs):
		if 'start' in kwargs:
			self.start = kwargs.get('start')
		if 'end' in kwargs:
			self.end = kwargs.get('end')
		if 'action' in kwargs:
			self.action = kwargs.get('action')
		self.transit = self.end - self.start

	def ledpwm(self, p):
		c = 0.181+(0.0482*p)+(0.00323*p*p)+(0.0000629*p*p*p)
		if c < 0.0:
			return 0
		if c > 0.0 and c <= 100.0:
			return c
		elif c > 100.0:
			return 100

	def update(self, now):
		if self.action == 'sunrise':
			return self.ledpwm(((now - self.start) / self.transit) * 100)
		elif self.action == 'sunset':
			return self.ledpwm(100 - ((now - self.start) / self.transit) * 100)
