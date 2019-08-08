cn=input('Enter Name=')
units=eval(input('Enter no. of units consumed='))
dc=50
if units>500:
    charge=3000+dc
elif units>100 and units<=200:
    charge=500+dc
elif units>200 and units<=300:
    charge=650+dc
elif units>300 and units<=500:
    charge=800+dc
else:
    charge=0+dc
print('Name=',cn)
print('Units used=',units)
print('charges=',charge)
