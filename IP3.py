q = int(input('Enter 1st number: '))
w = int(input('Enter 2nd number: '))
e = int(input('Enter 3th number: '))
if q>w:
    if q>e:
        z=q
else:
    if w>e:
        z=w
    else:
        z=e
if q<w:
    if q<e:
        x=q
else:
    if w<e:
        x=w
    else:
        x=e
print('Biggest number is: ' + str(z))
print('Smallest number is: ' + str(x))