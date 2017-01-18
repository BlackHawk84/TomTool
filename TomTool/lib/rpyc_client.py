import rpyc

import features


class rpyc_client:

	itemsgroup = [['gate1','global','stackers','incubator1'],['gate1','global','stackers','incubator1','incubator2'],['gate1','global','stackers','incubator1','incubator2','incubator3']]
	activeConnection = False

	def __init__(self, host,port,numIncs):
			self.rpyc_connector = rpyc.connect(host, port)
			self.rpyc_app = self.rpyc_connector.root.get_application()
			self.activeConnection = True
			self.groups = rpyc_client.itemsgroup[numIncs-1]

	def get_activeConnection(self):
		return self.activeConnection
	
	def rpyc_get(self, name):
		return self.rpyc_app.pool[name].get_value()

	def rpyc_set(self,value):
		if not(bool(self.currentFeat['readonly'])):
			return self.rpyc_app.pool[self.currentFeat['name']].set_value(value)
		else:
			return False


	def rpyc_set_direct(self, name, value):
		return self.rpyc_app.pool[name].set_value(value)
	
	def rpyc_get_group(self):
		return self.groups

	def rpyc_set_features_list(self,group):
		#Function: Definition of Features list 
 		self.featuresList = []
		for item in features.fitems[group]:
			self.featuresList.append(item['name'])
		return self.featuresList

	def rpyc_set_current_feature(self,groupIndex,featIndex):
		self.currentFeat = features.fitems[groupIndex][featIndex]
		return self.currentFeat

	def rpyc_get_current_feature(self):
		return self.currentFeat

	def rpyc_set_current_feature_by_search(self,name):
		j = 0
		for key1, group in features.fitems.items():
			i=0
			for feat in group:
				if feat['name'] == str(name):
					self.currentFeat = feat					
					return [self.currentFeat,j,i]
				i=i+1
			j = j+1
