def multiplier(number):
	"""
	二乗した数字を返す
	"""
	return number ** 2


def string(strings):
	"""
	引数に文字列を入力すると、文字列を返す
	"""
	print(str(strings))


def add_number(a, b=5, c=10):
	"""
	引数をすべて足したものを出力
	"""
	return a + b + c, a - b - c
result1, result2 = add_number(2)
print(result1, result2)


def division(integer):
	"""
	整数を2で割ったものを返す
	"""
	return int(int(integer) / 2)

def miltiplication(integer):
	"""
	divisionの戻り値を乗算したものを返す
	"""
	return division(integer) * 4
result = miltiplication(6)
print(result)


def float_numbers(float_number):
	"""
	数字を入力
	数字以外を入力すると、エラーを返す
	"""
	try:
		return float(float_number)
	except (NameError, TypeError, ValueError) as e:
		print('数字を入力してください')

