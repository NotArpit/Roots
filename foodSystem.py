from flask import Flask

class foodSystem(object):
	trade_id = 0
	def __init__(self):
		self.__users = []
		self._priceList = {}
		self.__tradeList = {}
		self.__tradeDetailsW = {}
		self.__tradeDetailsH = {}

	def getUsers(self):
		return self.__users

	def getPrices(self):
		return self.__priceList

	def addPriceList(self, produce, price):
		self._priceList[produce] = price

	def getPriceList(self):
		return self._priceList

	def addUsers(self, user):
		return self.__users.append(user)

	def getTradeList(self):
		return self.__tradeList

	def addTradeList(self, title, quantityW, itemW):
		self.__tradeList[itemW] = quantityW
		trade_id += 1
