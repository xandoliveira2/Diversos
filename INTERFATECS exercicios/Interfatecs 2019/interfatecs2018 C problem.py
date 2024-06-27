def main(): #problema C
	entrada = input().split(' ')
	med1 = int(entrada[0])
	med2 = int(entrada[1])
	med3 = int(entrada[2])
	if med1<=med2 and med1<=med3:
		print(med1)
	elif med2<=med1 and med2<=med3:
		print(med2)
	else:
		print(med3)
main()