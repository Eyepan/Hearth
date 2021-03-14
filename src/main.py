import lexer

# main loop
while True:
	text = input("HEARTH > ")
	result, error = lexer.main(text)
	if error: print("ERROR:", error.asString())
	else: print(result)