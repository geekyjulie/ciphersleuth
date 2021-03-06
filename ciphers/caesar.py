import math
import random
import os
import wsgiref.handlers
#import json
from django.utils import simplejson as json
import sys

#Sourced from http://inventwithpython.com/cipher.py
class CaesarCipherTool:
	# Caesar Cipher
	# made some modifications to source
	def __init__(self, mode, message):
		self.mode = mode
		self.message = message
		self.name = 'caesar'
	MAX_KEY_SIZE = 26
	key = 0
	'''
	def getKey(self,num):
		#while True:
		
		print('Enter the key number (1-%s)' % (self.MAX_KEY_SIZE))
		if (key >= 1 and key <= self.MAX_KEY_SIZE):
			self.key = key
			return key
	'''
	def display(self):
		return self.mode + " " + self.message + " " + self.key

	def storekey(self,num):
		self.key=int(num)
		
	def getTranslatedMessage(self):
		if self.mode[0] == 'd':
			self.key = -self.key
		translated = ''
		for symbol in self.message:
			if symbol.isalpha():
				num = ord(symbol)
				num += self.key
				if symbol.isupper():
					if num > ord('Z'):
						num -= 26
					elif num < ord('A'):
						num += 26
				elif symbol.islower():
					if num > ord('z'):
						num -= 26
					elif num < ord('a'):
						num += 26
				translated += chr(num)
			else:
				translated += symbol
		return translated
#def main():
#	toolbox = CipherToolbox()
#	mod = toolbox.getMode()
#	print(mod)
#	mes = toolbox.getMessage()
#	print(mes)
#	caesar = CaesarCipherTool(mod,mes)
#	toolbox.tools.append(caesar)
#	caesar.getKey()
#	print(caesar.key)
#	cipher = caesar.getTranslatedMessage()
#	print(cipher)
	
#if __name__ == '__main__':
  #main()
