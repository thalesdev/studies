import math
import decimal
class IEEEFloat:
	def __init__(self, dec,  precision=16):
		self.__precision = precision
		self.__mantissa = None
		self.__exponent = None
		self.__polarizer = None
		self.__signal = self.__get_signal(dec)
		self.__get_mantissa(abs(dec))
	def __get_mantissa_size(self):
		if self.__precision == 16:
			return 10
		elif self.__precision == 32:
			return 23
		elif self.__precision == 64:
			return 52
		elif self.__precision == 128:
			return 111
		elif self.__precision == 256:
			return 223
	def __get_expoent_size(self):
		if self.__precision == 16:
			return 5
		elif self.__precision == 32:
			return 8
		elif self.__precision == 64:
			return 11
		elif self.__precision == 128:
			return 16
		elif self.__precision == 256:
			return 32
		return 0
	def __poralize(self, ex):
		polarizer = (2**(self.__get_expoent_size()-1))-1
		self.__polarizer = polarizer
		return format(polarizer + ex,   "0{}b".format(self.__get_expoent_size()))
		#return str(ex + polarizer) 
	def __get_signal(self,dec):
		return "0" if dec>0 else "1" # Retorna o bit de sinal baseado no valor em decimal
	def __get_mantissa(self, dec):
		integer_part = math.floor(dec)
		float_part = float("0."+str(dec).split(".")[-1])
		if dec == 0:
			pass
		else:
			bin_integer = format(integer_part, "0b")
			bin_float = ""
			count=0
			while(float_part != 0 and count < self.__get_mantissa_size()):
				float_part_aux = str(float_part*2)
				bin_float += float_part_aux.split(".")[0]
				float_part = float("0."+str(float_part_aux).split(".")[-1])
				count+=1
			p = len(bin_integer)
			spExp = 0 
			int_float = bin_integer+","+bin_float
			for j in range(len(int_float)):
				if int_float[j] == "1":
					spExp= ((-1)**( 1 if (p-j)<0 else 2 ))*(abs(p-j)-1)
					self.__exponent = self.__poralize(spExp)
					break
			mantissa = ""
			#print(int_float,spExp)
			for bit in int_float[abs(p-spExp):]:
				if bit != ",":
					mantissa += bit	
			self.__mantissa = mantissa
	def decimal(self):
		sum=0
		for v,j in enumerate(self.__mantissa):
			sum+= float(int(j)*(2**(-int(v)-1)))
		return(((-1)**int(self.__signal))*(sum+1)*(2**(  int(self.__exponent,2) - self.__polarizer   )))
	def __str__(self):
		return "IEE 754 {}bit float: {}".format( self.__precision,(self.__signal+self.__exponent+self.__mantissa+ ("0"*(self.__get_mantissa_size() - len(self.__mantissa)))))
a = IEEEFloat(-0.0001,128)
print(a.decimal(),a)