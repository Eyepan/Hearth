from lexer import *

# Node class
class Node:
	def __init__(self, token, left = None, right = None):
		self._left = left
		self._token = token
		self._right = right

	def __repr__(self):
		if self._left == None or self._right == None:
			return f"{self._token}"
		return f"({self._left}, {self._token}, {self._right})"


class Parser:
	def __init__(self, tokens):
		self._tokens = tokens
		self._currentToken = None
		self._tokenIndex = -1
		self.advance()

	def advance(self):
		self._tokenIndex += 1
		if self._tokenIndex < len(self._tokens):
			self._currentToken = self._tokens[self._tokenIndex]
		else:
			self._currentToken = Token(TT_EOF)

	def factor(self):
		tok = self._currentToken
		if tok._type in (TT_INT, TT_FLOAT):
			self.advance()
			return Node(tok)

	def term(self):
		left = self.factor()
		while self._currentToken._type in (TT_MUL, TT_DIV):
			operatorToken = self._currentToken
			self.advance()
			right = self.factor()
			left = Node(operatorToken, left, right)

		return left

	def expr(self):
		left = self.term()

		while self._currentToken._type in (TT_PLUS, TT_MINUS):
			operatorToken = self._currentToken
			self.advance()
			right = self.term()
			left = Node(operatorToken, left, right)

		return left

	def parse(self):
		result = self.expr()
		return result


