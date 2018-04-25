
def get_codes():
	fname='code.txt'
	code=[]
	for line in open(fname,'r').readlines():
		line=line.rstrip().lstrip()
		if not line: continue
		if line[0]=='#': continue
		code.append(line)
	return code

def str2date(str_date):
	from datetime import date
	y,m,d=[int(x) for x in str_date.split('-')]
	return date(y,m,d)