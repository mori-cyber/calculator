# در برنامه ماشین حساب قابلیت های زیر را بیفزایید:
# factorial - tan - cot - تبدیل رادیان به درجه برای توابع مثلثاتی
# برنامه ای بنویسید که سه عدد دریافت نماید و مشخص نماید که آیا می توان مثلثی رسم کرد که اضلاع آن برابر این سه عدد باشند یا خیر. راهنمایی: در ریاضیات، قضیه‌ای‌ است که بیان می‌دارد در هر مثلث اندازهٔ هر ضلع از مجموع اندازهٔ دو ضلع دیگر کوچکتر است.
# برنامه ای بنویسید که با دریافت وزن و قد فرد، شاخص BMI را برای آن فرد محاسبه نماید، و با توجه به مقادیر موجود در شکل زیر، در مورد چاق یا لاغر بودن فرد پیام مناسب چاپ نماید.

import math

a=int(input('enter first number:'))
b= int(input('enter second number:'))
c= str(input('enter a operation:'))


if c== '+':
    print('result is:',a+b)
elif c=='*':
    print('result is:',a*b)
elif c == '/':
    print('result is:',a/b)
elif c == '-':
    print('result is:',a-b)
elif c== '%':
    print('result  first number is:',a/100 ,"\nresult second number is:",b/100)
elif c == 'tan':
    print('tan result is:',math.tan(a), math.tan(b))
elif c== 'cot':
    print('cot result is:',pow(math.tan(a),-1),  pow(math.tan(b) ,-1))
elif c=='fact':
    x = 1
    for i in range(2,a+1):
        x*=i
    print('factorial result is:',x)   
        
    




