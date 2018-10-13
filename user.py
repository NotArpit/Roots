from flask import Flask
from abc  import ABC, abstractmethod


class User():
	def __init__(self):
		self.__idNo
		self.__fruitW = {}
		self.__fruitN = {}

	def getID(self):
		return self.__id

	def getFruitW(self):
		return self.__fruitW

	def getFruitN(self):
		return self.__fruitN