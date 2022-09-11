import math

# 1)
a = int(input("Enter a: "))
b = int(input("Enter b: "))
h = int(input("Enter h: "))
S = ((math.pow(a,2)+b)*h) / ((2*(a-b))+4)
print ('Firstanswer : ' + str("S={0:.2f}".format(S)))

# 2)
q = int(input("Enter q: "))
w = int(input("Enter w: "))
a = math.sqrt(math.cos(2*w)+math.sin(4*w) + math.sqrt(math.pow(math.e,q) + math.pow(math.e,(-q))))
b = math.pow(((math.pow(math.e,(-q))) + math.pow(math.e,q)),3) * math.pow((math.sin(4*w) + math.cos(2*w) - 2), 2)
H = a/b
print ('Second answer: ' + str("H={0:.2f}".format(H)))

# 3)
#1
a=2
b=1
c = math.pow(math.pow(a,b),a) + math.pow(a,math.pow(a,b)) - math.pow(a,4)
print('Third(1) task answer is: ' + str("c={0:.2f}".format(c)))

#2
a=1
b=4
c=3
p = math.pow(((1/math.tan(b))+6), 1/3) + math.sqrt((math.pow((a+1),3))/4*b-2*c)
print('Third(2) task answer is: ' + str("p={0:.2f}".format(p)))

#3
q = 3
w = 0.2
e = 5*q*w / math.pow(q,3) + math.exp(math.pow(q,2)) + math.sqrt(math.pow(1/math.sin(w),2) - math.pow(w,2))
print('Third(3) task answer is: ' + str("e={0:.2f}".format(e)))

#4
q=3
w=5
e= math.sqrt(math.fabs(w))+(math.pow(math.atan(math.log(q)),3) / math.pow(q,w) - w +1 )
print('Third(4) task answer is: ' + str("e={0:.2f}".format(e)))

#5
q=3
w=1
e=2
i = math.pow(4,(q*w)) - math.pow(q,(q*w)) + math.pow((q*w),e)
print('Third(5) task answer is: ' + str("i={0:.2f}".format(i)))

#6
q=2
w=2
e=1
i =( 4*math.fabs(q) - q*w*math.pow(e,2) )/( q+math.exp(w*q)-2*w*e)
print('Third(6) task answer is: ' + str("i={0:.2f}".format(i)))

#7
q=0.8
w=0.1
e=4
i = math.pow((1-q + (1/math.atan(q-7*w)))/(4*q*e-math.pow(math.log(w),2)),1/5)
print('Third(7) task answer is: ' + str("i={0:.2f}".format(i)))

#8
q=3
w=1
e=3
i= 2*3*4/(math.pow(math.sin(q),3) + math.pow(math.tan(w),3)) - math.sqrt(math.pow(e,(q-w)))
print('Third(8) task answer is: ' + str("i={0:.2f}".format(i)))

#9
q=4
i= math.pow(math.log(q-3),4)+math.pow(2,q)*math.pow(math.sin(3*q),2)
print('Third(9) task answer is: ' + str("i={0:.2f}".format(i)))

#10
q=2
w=2
e=1
i = math.sqrt(0.6*q*w*e)+math.pow(math.pow(w,q),2) - math.exp(math.sin(2*math.pow(q,2)))
print('Third(10) task answer is: ' + str("i={0:.2f}".format(i)))

#11
q=0.5
w=2
i = (math.asin(math.pow(q,3)) - 6) / (8*(math.cos(4*w)-math.sin(4*q)))
print('Third(11) task answer is: ' + str("f={0:.2f}".format(i)))

#12
q=2
w=1
e=3
i = ((math.fabs(math.log(math.pow(q,3))) + math.exp(2*q)) / (q+3.4)) - (math.pow((1/math.tan(3/q*w*e)),3))
print('Third(12) task answer is: ' + str("i={0:.2f}".format(i)))