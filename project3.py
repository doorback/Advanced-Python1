# 1)
def is_alive(health):
 if health < 0:
     return False
 else:
     return True

#2
m1 = int(input('You need to enter the real number of the month you were born: '))
if (m1 == 1):
    print ("You were born in January")
else:
    if m1 ==2:
        print ("You were born in February")
    else:
        if m1 ==3:
            print ("You were born in March")
        else:
            if m1 ==4:
                print("You were born in April")
            else:
                if m1 ==5:
                    print("You were born in May")
                else:
                    if m1 ==6:
                        print("You were born in June")
                    else:
                        if m1==7:
                            print("You were norn in July")
                        else:
                            if m1 == 8:
                                print("You were born in August")
                            else:
                                if m1 == 9:
                                    print("You were born in September")
                                else:
                                    if m1 == 10:
                                        print("You were born in October")
                                    else:
                                        if m1 ==11:
                                            print("You were born in November")
                                        else:
                                            if m1==12:
                                                print("You were born in December")

if m1>2 and m1<6:
    print ("Birds sang beautiful songs")
else:
    if m1>5 and m1<9:
        print ("The sun shine brighter than ever")
    else:
        if m1>8 and m1<12:
            print ("The harvest was incredible")
        else:
            print ("White snow fell outside the window")

#3
l, u, p, d = 0, 0, 0, 0
s = "R@m@_f0rtu9e$"
capitalalphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallalphabets = "abcdefghijklmnopqrstuvwxyz"
specialchar = "$@_"
digits = "0123456789"
if (len(s) == 8):
    for i in s:

        # counting lowercase alphabets
        if (i in smallalphabets):
            l += 1

            # counting uppercase alphabets
        if (i in capitalalphabets):
            u += 1

            # counting digits
        if (i in digits):
            d += 1

            # counting the mentioned special characters
        if (i in specialchar):
            p += 1
if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(s)):
    print("Valid Password")
else:
    print("Invalid Password")