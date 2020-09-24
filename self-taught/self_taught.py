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



# def squared(x):
#     """ Takes an int and returns it multiplied by 2.
#     :param x: int.
#     :return: x multiplied by 2.
#     """
#     return x ** 2


# def print_string(string):
#     """ Prints the string passed in.
#     :param string: str.
#     """
#     print(string)

# print_string("Testing: 1, 2, 3.")


# def add_mult(a,b,c,x=100,z=1000):
#     """ Returns the result of two optional params
#     multiplied by the addition of 3 required params.
#     :param a: int.
#     :param b: int.
#     :param c: int.
#     :param x: int.
#     :param z: int.
#     :return: int.
#     """
#     return a + b + c * x * z


# def convert(string):
#     """ Converts passed in str to int.
#     :param string: str.
#     :return: string converted to int.
#     """
#     try:
#         return float(string)
#     except ValueError:
#         print("Could not convert the string to a float.")