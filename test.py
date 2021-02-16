#!/usr/bin/python3

def avg(*args):
	sum = 0
	count = 0
	if not args: 
		return sum

	else:
		for arg in args: 
			if type(arg)==list or type(arg)==tuple:
				for elem in arg: 
					sum+=elem
					count += 1

			else:
				sum+=arg
				count+=1
	
		return sum/count
		

if __name__=="__main__":
	control = ""
	args = []
	cnt = 0
	while control!='#':
		
		args.append(control)
		cnt += 1
	print(f"You gave {cnt} values")
	
	
	avg_res = avg(args)
	print(avg_res)
