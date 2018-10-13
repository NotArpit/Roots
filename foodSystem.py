from flask import Flask

class foodSystem(object):
	def __init__(self):
		self.__users = []
		self._priceList = {}
		

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
