# -*- coding: utf-8 -*-
from Components.Converter.Converter import Converter
from Components.Element import cached
from time import localtime

class gCWatch(Converter, object):
	def __init__(self, type):
		Converter.__init__(self, type)
		value = type.split(',')
		if value[0] == "sec":
			self.type = 1
		elif value[0] == "min":
			self.type = 2
		elif value[0] == "hour":
			self.type = 3
		self.__size = int(value[1])
		
	@cached
	def getSize(self):
		return self.__size
		
	size = property(getSize)

	@cached
	def getValue(self):
		if self.type == 1:
			time = self.source.time
			if time is None:
				return 0
			t = localtime(time)
			return t.tm_sec
		elif self.type == 2:
			time = self.source.time
			if time is None:
				return 0
			t = localtime(time)
			return t.tm_min
		elif self.type == 3:
			time = self.source.time
			if time is None:
				return 0
			t = localtime(time)
			c = t.tm_hour
			m = t.tm_min
			if c > 11:
				c = c - 12
			return (c * 5) + (m / 12)
		return 0

	value = property(getValue)
