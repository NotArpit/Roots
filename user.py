from flask import Flask
from abc  import ABC, abstractmethod
from trade import *


class User():
	def __init__(self):
		self.__idNo = 0
		self.__fruitW = {}
		self.__fruitH = {}

	def getID(self):
		return self.__idNo

	def getFruitW(self):
		return self.__fruitW

	def getFruitH(self):
		return self.__fruitH

	def addFruitW(self, produce, quantity):
		self.__fruitW[produce] = quantity

	def addFruitH(self, produce, quantity):
		self.__fruitH[produce] = quantity
