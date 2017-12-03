import random as r
from feste import *

r.seed(42);
daysn = 24;

#h = [0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,1,0,0];

h = getCalendar();

def blocchi(h,f):
	r = [0]*len(h);
	r[0]=h[0]+f[0];
	b = [];
	for i in range(1,len(h)):
		if(h[i]+f[i]>0):
			r[i]=r[i-1]+1;
		else:
			if(r[i-1]!=0):
				b.append(r[i-1])
	return b;

def score(h,f,daysn):
	r = blocchi(h,f);
	if(len(r)>=3) and sum(f)==daysn:
		s = sum([i * i for i in r])
		l = len(r)
		return s+l;
	else:
		return 0;

def generateF(h,daysn):
	f = [0]*len(h);
	while(daysn>0):
		idx = r.randint(0,len(h)-1);
		if h[idx]==0 and f[idx]==0:
			f[idx]=1
			daysn = daysn-1
	return f;

def crossingOver(f1,f2):
	c = r.randint(0,len(f1)-1);
	return f1[:c]+f2[c:]

def mutation(f,rate):
	for i in range(0,rate):
		c = r.randint(0,len(f)-1);
		q = r.randint(0,len(f)-1);
		box = f[c]
		f[c] = f[q]
		f[q] = box

	return f;

def init(h,daysn,popN):
	pop = [0]*popN
        perf = [0]*popN
        for i in range(0,popN):
                pop[i] = generateF(h,daysn)
                perf[i] = score(h,pop[i],daysn)
	return pop,perf;

def simulation(h,pop,perf,popN):
	#pop = [x for _,x in sorted(zip(perf,pop))]
	perf,pop = zip(*sorted(zip(perf, pop)))
	pop = list(pop)
	perf = list(perf)
	top = pop[popN/2:]
	for i in range(0,popN/2-1):
		a = r.choice(top)
		b = r.choice(top)
		pop[i] = mutation(crossingOver(a,b),3);
	
	for i in range(0,popN):
		perf[i] = score(h,pop[i],daysn)
	#print perf
	return pop,perf

pop,perf = init(h,daysn,200)
for i in range(0,5000):
	pop,perf = simulation(h,pop,perf,10)

print h
print pop[-1]
print perf[-1]

getDayName(pop[-1])
