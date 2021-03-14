import lexer

# main loop
while True:
	text = input("hearth > ")
	result, error = lexer.main(text)
	if error: print("ERROR:", error.asString())
	else: print(result)