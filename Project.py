import random 
import math
import copy #needed to import this because my IBS manipulates deep copy of generated array


def generateList():
    x = random.randint(1, 100000)
    y = random.randint(1, 10)
    list1 = []
    for i in range(0,x):
    	if(i == 0):
    		list1.append(1)
    	else:
    		list1.append(list1[i-1] + y)
    return list1
    # if x >= y:
    #     return range(0, x, y)
    # else: 
    #     return range(0, y, x)
def generateIncreasingList():
	x = random.randint(80000,100000)
	list1 = []
	for i in range(0, x):
		if(i == 0):
			list1.append(1)
		else:
			list1.append(list1[i-1] + random.randint(1, x))
	return list1


def adaptive(array, key):
	arr = array
	
	left = 0
	right = len(array) - 1
	counter = 0
	iteration = 0
	while(left!=right and arr[left] <= key <= arr[right]):
		#comp
		iteration += 1
		counter+=1;
		BSmedIsSmaller = False #boolean value switched on if bs bound is smaller than IS bound
		rangeInterp = 0 #range of interp new bound
		rangeBS = 0
		interpNext = left + (((key - arr[left]) * (right - left))// (arr[right] - arr[left]))#inter formula
		BSNext = (right + left)// 2

		#print('interp : %d, bs : %d'%(interpNext, BSNext))
		##---- COMPARE BOUNDARIES BUT IF KEY IS HAPPENED TO BE ONE OF THE BOUNDARIES OF BS OR IS, WE JUST USE THAT AS OUR ANSWER-----------------
		if(key == arr[interpNext]):
			#comp 
			counter+=1
			print('key found using IS\nthe index of the key is %d\nin adaptive, this took us %d accesses\nand %d iterations\n'%(interpNext, counter, iteration))
			return interpNext
		if(arr[BSNext] == key):
			#comp
			counter+=2
			print('key found using BS\nthe index of the key is %d\nint adaptive this took us %d accesses\nand %d iterations\n'%(BSNext, counter,iteration))
			return BSNext
		#find BS boundary
		if(key < arr[BSNext]):
			counter += 3
			rangeBS = (BSNext - 1) - left 
		elif(key > arr[BSNext]):
			counter + 4
			rangeBS = right-(BSNext + 1)
		#comp since only one is accessed, we increase counter by 1
		
		#find IS boundary
		if(key < arr[interpNext]):
			counter += 1
			rangeInterp = (interpNext - 1) - left

		elif(key > arr[interpNext]):
			counter += 2
			rangeInterp = right - (interpNext + 1)
		
		#print('BSBOUND: %d INTERP BOUND: %d' %(rangeBS, rangeInterp))
	
		##################compare bsbound and interpbound and change left and right accordingly
		if(rangeInterp > rangeBS):
			BSmedIsSmaller = True
		if(BSmedIsSmaller):
			#print('BS bound is smaller!!')
			
			if(key > arr[BSNext]):
				left = BSNext + 1
				counter += 1
			else:
				right = BSNext - 1
				
		elif(not(BSmedIsSmaller)):
			#print('IS bound is smaller or is the same as BS!!')
			if(key > arr[interpNext]):
				counter += 1
				left = interpNext + 1
			elif(key < arr[interpNext]):
				
				right = interpNext -1
		#because two comparison in each if or elseif and only one branch out of the two can be accessed in each loop
		#print('the new bounds are %d, %d' %(left, right))
		
		#print(counter)	
		
		
	if(key == arr[left]):
		counter += 1
		print('key found in last loop at %d with %d accesses' %(left, counter))
		return left
	print('key not found')
	return -1


#ex = generateIncreasingList()
ex = generateIncreasingList() ####switch this between generateList() to generateIncreasingList() to test 
keytofind = ex[random.randint(2, len(ex)-2)]
print('the randomly generated list is %d long and elements range from 1 to %d\nand the key to find is %d\n'%(len(ex), ex[-1], keytofind))

adaptive(ex, keytofind) #selecting random number from 1 to len of arr
#adaptive([1,3,5,7,9,11,13,15],11)
#adaptive([1,2,55,77,99,100,102,104,200,206,400,560,760,761,777,888,919,929,999,1000,2000,2002,5000,5232,5300,5322,5400,10000,50000,670000], 5300)

def interpolationbinary(array, key):
	iteration = 0
	theta = 2
	s = 2
	arr = copy.copy(array)
	arr[0]= 0 #set the first element as 0 
	n = len(arr) - 1#current boundary were working with 
	arr.append(arr[n] + 1) #add a arr[n] + 1 at the end of list
	left = 0
	right = n + 1
	counter = 0
	y = (key - arr[left])/(arr[right] - arr[left])#fraction	
	while(arr[left] <= key <= arr[right] and left!=right):
		counter += 1
		iteration += 1
		if(n >= s):
			leftHat = max(left + math.ceil((n * y) - theta*math.sqrt((n * y)*(1-y))), left + 1)
			rightHat = min(left + math.floor((n * y) + theta*math.sqrt((n * y)*(1-y))), right - 1)
			#print('lefthat:%d righthat:%d' %(leftHat, rightHat))
			if(arr[leftHat] == key):
				counter += 1
				print('key found at leftHat key: %d\nin IBS, this took us %d accesses\nand %d iterations\n' %(leftHat,counter,iteration))
				return leftHat
			elif(arr[rightHat] == key):
				counter += 2
				print('key found at rightHat key: %d\nin IBS, this took ys %d accesses\nand %d iterations\n' %(rightHat, counter, iteration))
				return rightHat
			elif(key < arr[leftHat]):
				counter += 3
				right = leftHat 
			elif(arr[leftHat] < key < arr[rightHat]):
				counter += 4
				left = leftHat 
				right = rightHat 
			elif(arr[rightHat] < key):
				counter += 5
				left = rightHat 
			n = right - left - 1

			y = (key - arr[left])/(arr[right] - arr[left])
		if(True):
			mid = (left + right)//2
			if(arr[mid] == key):
				counter += 1
				print('key found at mid using BS key: %d\nin IBS, this took us %d accesses\nand %d iterations\n' %(mid,counter,iteration))
				return mid
			elif(key<arr[mid]):
				counter += 2
				right = mid
			elif(key>arr[mid]):
				counter += 3
				left = mid
			n = right - left - 1
			y = (key - arr[left])/(arr[right] - arr[left])
			if(n == 0):
				print('key not found')
				return
	# if(key == arr[left]):
	# 	print('key found in last loop')	
	# 	return left
	print('key not found')
	return -1

#interpolationbinary([1,2,55,77,99,100,102,104,200,206,400,560,760,761,777,888,919,929,999,1000,2000,2002,5000,5232,5300,5322,5400,10000,50000,670000], 5300)
#interpolationbinary([0, 4, 15, 24, 31, 35, 44, 48, 57, 67, 82, 100, 116, 132, 134, 158, 172, 184, 187, 201, 226, 251, 270, 301, 334,337, 344, 374, 393, 427, 428], 6000)
interpolationbinary(ex, keytofind)
#interpolationbinary([1,3,5,7,9,11,13,15],11)
def thirdAlg(array, key):
	intArr = array
	bsArr = array #two separate copies for easier readability and debugging
	intLeft = 0
	intRight = len(array) - 1
	bsLeft = 0
	bsRight = len(array) - 1
	counter = 0 
	iteration = 0

	#simply have two separate trackers of low and high for both IS AND BS for easy readability and debugging
	while(intArr[intLeft] <= key <= intArr[intRight] and bsArr[bsLeft] <= key <= bsArr[bsRight] ):
		counter += 2
		iteration += 1
		intMid = intLeft + (((key - intArr[intLeft]) * (intRight - intLeft))// (intArr[intRight] - intArr[intLeft]))

		bsMid = (bsRight + bsLeft)// 2
		if(key == intArr[intMid]):
			counter += 1
			print('key found using IS\nthe index of the key is %d\nin the third combined algorithm, it took us %d accesses\nand %d iterations\n'%(intMid, counter, iteration))
			return intMid
		elif(key > intArr[intMid]):
			counter += 2
			intLeft = intMid + 1
		elif(key < intArr[intMid]):
			counter += 3
			intRight = intMid - 1

		if(key == bsArr[bsMid]):
			counter += 1
			print('key found using BS\nthe index of the key is %d\nin the third combined algorithm, it took us %d accesses\nand %d iterations\n'%(bsMid, counter,iteration))
			return bsMid 
		elif(key < bsArr[bsMid]):
			counter += 2
			bsRight = bsMid - 1
		elif(key > bsArr[bsMid]):
			counter += 3
			bsLeft = bsMid + 1 

	if(key == intArr[intLeft]):
		counter += 1
		print('key found in last loop of IS after it has exitted\nthe index of the key is %d\nin the third combined algorithm, it took us %d accesses\nand %d iterations\n'%(intLeft, counter,iteration))
		return intLeft
	print('key not found')
	return -1

thirdAlg(ex, keytofind)
#thirdAlg([1,3,5,7,9,11,13,15],11)