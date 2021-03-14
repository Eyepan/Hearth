# Importing all errors
from errors import *
from tokens import *
# Lexer class 

class Lexer:
	def __init__(self, text):
		self._text = text
		self._pos = -1
		self._currentChar = None
		self.advance()

	def advance(self):
		self._pos += 1
		if self._pos < len(self._text):
			self._currentChar = self._text[self._pos]
		else:
			self._currentChar = None

	def makeTokens(self):
		tokens = []

		while self._currentChar != None:
			if self._currentChar in ' \t':
				self.advance()
			elif self._currentChar in DIGITS:
				tokens.append(self.makeNumber())
			elif self._currentChar == '+':
				tokens.append(Token(TT_PLUS))
				self.advance()
			elif self._currentChar == '-':
				tokens.append(Token(TT_MINUS))
				self.advance()
			elif self._currentChar == '*':
				tokens.append(Token(TT_MUL))
				self.advance()
			elif self._currentChar == '/':
				tokens.append(Token(TT_DIV))
				self.advance()
			elif self._currentChar == '(':
				tokens.append(Token(TT_LPAREN))
				self.advance()
			elif self._currentChar == ')':
				tokens.append(Token(TT_RPAREN))
				self.advance()
			elif self._currentChar == '^':
				tokens.append(Token(TT_EXP))
				self.advance()


			# SERIOUSLY BAD CODE, SHOULD REMOVE AFTER A PROPER EXIT FUNCTION IS PLACED
			elif self._currentChar == 'x':
				print("Exiting Hearth")
				exit()
			else:
				return [], IllegalCharacterError(f" '{self._currentChar}' ")
		return tokens, None
	
	
	def makeNumber(self):
		number = ''
		dotCount = 0
		while self._currentChar != None and self._currentChar in DIGITS + '.':
			if self._currentChar == '.':
				if dotCount == 1: break
				dotCount += 1
				number += '.'
			else:
				number += self._currentChar
			self.advance()
		if dotCount == 0: return Token(TT_INT, int(number))
		else: return Token(TT_FLOAT, float(number))

def main(text):
	lexer = Lexer(text)
	tokens, errors = lexer.makeTokens()
	return tokens, errors