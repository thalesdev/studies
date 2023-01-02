import math
import functools as ft


class Matrix:
	def __init__(self, array, *args, dtype=None):
		self._array = array if dtype is None else self.__astype__(array, dtype)
		self._dtype = dtype
		self._shape = len(array[0]), len(array[1])
		self._limsp = 0
		self._liminf = 0

	@property
	def shape(self):
		try:
			return len(self._array[0]), len(self._array[1])
		except:
			return 0, 0

	def dot(self, b):
		self._array = [[sum(el_a * el_b for el_a, el_b in zip(row_a, col_b))
		                for col_b in zip(*b)] for row_a in self]

	def __astype__(self, array, dtype):
		return map(lambda e: map(lambda el: dtype(el) if not isinstance(el, dtype) else el, e), array)

	def astype(self, dtype):
		self._array = self.__astype__(self._array, dtype)
		return self

	def __mul__(self, other):
		self._array = [[a_el * b_el for a_el, b_el in zip(a_row, b_row)] for a_row, b_row in zip(self, other)]
		return self

	def __pow__(self, power, modulo=None):
		if power > 1:
			return self * self.__pow__(power - 1)
		return self

	def __empty__lines__(self):
		return sum(1 if not sum(e for e in row) else 0 for row in self)

	def __empty__cols(self):
		pass

	def sla(self):
		print(self.__empty__lines__())

	def __iter__(self):
		return self._array.__iter__()

	def __str__(self):
		return str(list(map(lambda e: list(e), self)))
