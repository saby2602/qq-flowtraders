##################################################################################
##################################################################################
## Template file for problem 2. 						##
## First, fill in your answer logic below					##
##################################################################################
#                                LOGIC GOES BELOW                     		#
##################################################################################
#
#
#
#
#
##################################################################################
##################################################################################
## Fill in function 								##
## findSecondMeasurement(firstMeasurement, standardDeviation)		 	##
## below. It takes in input firstMeasurement, standardDeviation			##
## and returns expected value of second measurement 				##
##                                                                          	##
## You only have to fill in the math function where indicated     		##
##                                                                          	##
## You can run this template file to see the output of your function	    	##
## for standardDeviation = 3 and firstMeasurement = 105				## 
## Simply run: `python problem1b_template.py`                            	##
## You should see the output printed once your program runs.                	##
##                                                                          	##
## DO NOT CHANGE ANYTHING ELSE BELOW. ONLY FILL IN THE LOGIC.      		##
##                                                                          	##
## Good Luck!                                                               	##
##################################################################################
##################################################################################
import math
def calprob( first, stdev, mean) :
	ans =  (1 / (stdev * math.sqrt(2*math.pi)))
	power = ((first-mean)*(first-mean))/(2*stdev*stdev);
	ans*= math.exp(-power)
	return ans

def findSecondMeasurement(firstMeasurement, standardDeviation):
	lisa = 110
	susan = 90
	plisa = calprob(firstMeasurement,standardDeviation,lisa)
	psusan = calprob(first,sd,susan)
	nplisa = plisa/(plisa+psusan)
	npsusan = psusan/(plisa+psusan)
	secondMeasurement = lisa*nplisa + susan*npsusan
	return round(secondMeasurement, 2)

if __name__ == "__main__":
	standardDeviation = 3
	firstMeasurement = 105
	print('For First Measurement %.2f, standard deviation %.2f, Expected second measurement: %.2f'%(firstMeasurement, standardDeviation\
		,findSecondMeasurement(firstMeasurement, standardDeviation)))
