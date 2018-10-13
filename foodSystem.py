from flask import Flask
from abc  import ABC, abstractmethod


class foodSystem(ABC):
	def __init__(self, userList=[], priceList = []):
		self.__users =  userList
		self.__priceList = priceList
		
	@property 
	def getUsers:
		return self.__users

	@property 
	def getPrices:
		return self.__priceList

