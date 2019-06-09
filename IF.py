rain = input('今天有沒有下雨: ')
if rain == '有':
	print('請帶雨傘')
	print('宅在家裡')
age = input('請輸入年齡: ')
age = int(age)
if age >= 20:
	print('你可以投票')
else:
	print('你不能投票')
if age < 13:
	print('國小')
elif age >= 13 and age < 18:
	print('國高中')
elif age >=18 and age < 22:
	print('大學')
else:
	print('社會人')	