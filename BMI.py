w = input('請輸入體重：')
h = input('請輸入身高：')
w = float(w)
h = float(h)
h = h / 100
bmi = w / (h * h)
print('BMI=', bmi)
if bmi < 18.5:
	print('過輕')
elif bmi >= 18.5 and bmi < 24:
	print('正常範圍')
elif bmi >= 24 and bmi < 27:
	print('過重')
elif bmi >= 27 and bmi < 30:
	print('輕度肥胖')
elif bmi >= 30 and bmi < 35:
	print('中度肥胖')
elif bmi >= 35:
	print('重度肥胖')
	