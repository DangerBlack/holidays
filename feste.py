import datetime

def getCalendar():
	YEAR = 2018
	h = [0]*366;
	for i in range(0,366):
		d = datetime.date(YEAR, 1, 1) + datetime.timedelta(i - 1)
		if d.weekday()>=5:
			h[i] = 1

	#capodanno
	h[0] = 1
	#befana
	h[6] = 1
	#liberazione
	h[115] = 1
	#1maggio
	h[122] = 1
	#2giugno
	h[153] = 1
	#15agosto
	h[227] = 1
	#2 november
	h[305] = 1
	#8 dec
	h[342] = 1
	#25 dec
	h[359] = 1
	#26 dec
	h[360] = 1
	
	#pasqua 2018
	h[91] = 1
	h[92] = 1
	return h;

def getDayName(f):
	YEAR = 2018;
	for i in range(0,366):
		if f[i]==1:
                	d = datetime.date(YEAR, 1, 1) + datetime.timedelta(i - 1)
                	print d

