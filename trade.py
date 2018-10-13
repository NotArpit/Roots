from flask import Flask
from abc  import ABC, abstractmethod


class Trade():
	def __init__(self):
		self.__idNo = 0
		self.__tradesH = {}
		self.__tradesW = {}

	def getID(self):
		return self.__idNo

	def addTrade(self, tyoe, produce, quantity):
		if type == 'WANT':
			self.__tradesW[produce] = quantity
		elif type == 'HAVE':
			self.__tradeH[produce] = quantity