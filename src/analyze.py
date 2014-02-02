#Useful Libraries
import numpy as np
import pickle as p

#Data Library
import datacode.feature_dict as dc



class Task:
	def __init__(self, name, data):
		self.name = name
		self.data = data


class TaskManager:
	def __init__(self, data, tasks = []):
		self.data = data
		self.tasks = tasks


if __name__ == "__main__":
	dataHolder = dc.Data(codebook = dc.HC144D)
	dataHolder.createRefs()
	dataHolder.loadData("../h144d.dat")
	# print "Indices of V1 at", dataHolder.index("V1")
	# print "Feature Description of V1 is ", dataHolder.feature("V1")
	# print "Our Raw Data is ", dataHolder.data
	print dataHolder.lookUp(var = "V10")
	print dataHolder.lookUp(desc = "DUID")