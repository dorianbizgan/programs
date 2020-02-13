def main():


	j = int(input("Enter lower limit: "))
	k = int(input("Enter upper limit: "))

	cache = {} #initializing a cache


	#cache[key] = val | How to check dictionary 
	for i in range(j, k + 1):
		dummy = i
		count = 1
		while dummy != 1:
			if dummy in cache:
				count += cache[dummy] - 1
				#print("HI")
				break
			if (dummy % 2) == 0:
				dummy = (dummy>>1)
				count += 1
			else:
				dummy = ((3 * dummy) + 1)
				count += 1


		
		cache[i] = count
				
	#	print("Value:",original,"Cycles:",cache[original])
	#	print()



	"""for i in cache:
		print("Key",i,"Value",cache[i])
	"""
	#print(cache)
	print(max(cache.values()))
	

main()

