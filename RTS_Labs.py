class myClass:

	def __init__():

	def aboveBelow(list,num):
		intAbv = 0
		intBel = 0
	
		i = 0
		while i < len(list):
			if (list[i] < num):
				intBel += 1
			elif(list[i] > num):
				intAbv +=1
			i += 1

		strOutput = str("Above: " + str(intAbv) + " Below: " + str(intBel))

		return strOutput

	def stringRotation(strIn, num):
			intSplit = len(strIn) - num
			strScoot = strIn[0:intSplit]
			strRot = strIn[intSplit:len(strIn)]
		
			out = strRot + strScoot
		
			return out
