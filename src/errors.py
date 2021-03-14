# Errors class

class Error:
	def __init__(self, errorName, details):
		self._errorName = errorName
		self._details = details

	def asString(self):
		return f'{self._errorName}: {self._details}\n'

# Errors, inheriting from the Error class
class IllegalCharacterError(Error):
	def __init__(self, details):
		super().__init__('Illegal Character Error', details)

