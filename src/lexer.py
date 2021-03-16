from tokens import *

# Lexer class

class Lexer:
	def __init__(self, text):
		self._text = text
		self._tokens = []
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
		while self._currentChar != None:

			# checking for blank spaces and tabs
			if self._currentChar in ' \t':
				self.advance()

			# checking if the current token is a digit
			if self._currentChar in DIGITS + '.':
				self._tokens.append(self.makeNumber())

			elif self._currentChar == '+':
				self._tokens.append(Token(TT_PLUS))
				self.advance()
			
			elif self._currentChar == '-':
				self._tokens.append(Token(TT_MINUS))
				self.advance()
			
			elif self._currentChar == '*':
				self._tokens.append(Token(TT_MUL))
				self.advance()
			
			elif self._currentChar == '/':
				self._tokens.append(Token(TT_DIV))
				self.advance()

			elif self._currentChar == '(':
				self._tokens.append(Token(TT_LPAREN))
				self.advance()

			elif self._currentChar == ')':
				self._tokens.append(Token(TT_RPAREN))
				self.advance()

			# Super good code, I'm proud of it ;)

			elif self._text == 'quit':
				print("EXITING HEARTH")
				exit()

			else:
				print(" " * (self._text.find(self._currentChar) + 9) + "^")
				print(f"ILLEGAL CHARACTER {self._currentChar} in position {self._text.find(self._currentChar)}")
				self._tokens.clear()
				break
		
		return self._tokens


	def makeNumber(self):
		number = ''		# number as a string

		# while the current character is still a digit or a decimal point, add the character to the number string
		while self._currentChar != None and self._currentChar in DIGITS + '.':
			number += self._currentChar
			self.advance()

		if '.' in number:
			return Token(TT_FLOAT, float(number))
		else:
			return Token(TT_INT, int(number))

	def getTokens(self):
		return self.makeTokens()

