import circle
import square


figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
	"""	Представляет собой функцию для вычисления периметра или или площади круга или квадрата, 
	используя внешние модули и динамически выполняя код, который зависит от введёных 
	пользователем данных.

		Параметры: а)fig (строка): Название фигуры
				   b)func (строка): Название функции, которую нужно выполнить
				   с)size (список): Список чисел, представляющих размеры фигуры

		Возвращаемое значение: Функция calc не возвращает никакое значение.
		  Она просто выводит результат вычисления на экран с помощью функции print.
	"""			
	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)



