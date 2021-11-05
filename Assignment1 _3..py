w = float(input())
h = float(input())
##########################################################
BMI = w/(w+h)
##########################################################
if BMI<18.5:
    print('under weight')
elif 18.5<BMI and BMI<24.9:
    print('normal')
elif BMI>25 and BMI<29.9:
    print('over weight')
elif 24.9<BMI and BMI<30:
    print('obese')
elif 35<BMI :
    print('extermely obes')
#############################################################