# All tokens inititalization

TT_INT 		= "INT"
TT_FLOAT 	= "FLOAT"
TT_PLUS 	= "PLUS"
TT_MINUS 	= "MINUS"
TT_MUL 		= "MUL"
TT_DIV 		= "DIV"
TT_LPAREN 	= "("
TT_RPAREN 	= ")"
DIGITS 		= "0123456789"
TT_EOF 		= "EOF"


# Token class
class Token:
	def __init__(self, type, value = None):
		self._type = type
		self._value = value
	
	def __repr__(self):
		if self._value == None:
			return f"{self._type}"
		else:
			return f"{self._type}:{self._value}"