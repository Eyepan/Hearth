# CONSTANTS
DIGITS = '1234567890'

# Tokens
TT_INT		= 'INT'
TT_FLOAT    = 'FLOAT'
TT_PLUS     = 'PLUS'
TT_MINUS    = 'MINUS'
TT_MUL      = 'MUL'
TT_DIV      = 'DIV'
TT_LPAREN   = 'LPAREN'
TT_RPAREN   = 'RPAREN'

# Token Class
class Token:
	def __init__(self, type, data = None):
		self._type = type
		self._data = data

	def __repr__(self):
		if self._data: 
			return f'{self._type}:{self._data}'
		return f'{self._type}'
