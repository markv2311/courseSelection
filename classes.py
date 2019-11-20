
canTake =[]
classes = [150, 161, 162, 231, 241, 251, 260, 300, 303, 304, 307, 353, 385, 355, 461, 475, 480]
taken = []
final = []
x = 1
while x != 0:
	x = int(raw_input("What classes have you taken? (Enter 0 to exit). "))
	if x == 0:
		print 'Thanks for using!'
	elif x in classes:
		print 'This is in the system'
		taken.append(x)
		print 'Class: %s' %x
		print ' '
		if x == 161:
			canTake.extend((241,162))
		if x == 162:
			canTake.extend((303, 304, 307, 231))
		if x == 231:
			canTake.extend((353, 355))
		if x == 241:
			canTake.append(241)
		if x == 353:
			canTake.append(385)
		if x == 150:
			canTake.append(260)
		if 303 in taken and 304 in taken and 307 in taken:
			canTake.append(475)
			if 231 in taken:
				canTake.append(461)
		if x in canTake:
			canTake.remove(x)
	else:
		print 'This is not in the system: %s'%x

for i in canTake:
	if i not in final:
		final.append(i)
for x in taken:
	if x in final:
		final.remove(x)
print ' '
print 'You can take these classes: '
for p in range(len(final)):
	print final[p]
