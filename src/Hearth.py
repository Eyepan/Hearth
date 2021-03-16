from tokens import *
from lexer import *
from parse import *

class Hearth:
	def __init__(self):
		print("WELCOME TO HEARTH v0.0.2")

	def mainLoop(self):
		while True:
			self._text = input("hearth > ")
			self._lexer = Lexer(self._text)

			# get the tokens
			self._tokens = self._lexer.getTokens()
			if len(self._tokens) > 0: 
				print(self._tokens)


				# pass the tokens to the parser to get an ast
				parser = Parser(self._tokens)
				ast = parser.parse()
				print(ast)

				# pass the ast to the interpreter to get a result