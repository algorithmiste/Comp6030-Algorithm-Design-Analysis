import random

boy_names = [
	'Noah','Liam','Mason','Jacob','William','Ethan','James','Alex','Michael','Benjamin','Elijah','Daniel','Aiden','Logan','Matthew','Lucas','Jacskon','David','Oliver','Jayden','Joseph','Gabriel','Sammuel','Carter','Anthony','John','Dylan','Luke','Henry','Andrew',
]
girl_names = [
	'Emma','Olivia','Sophia','Ava','Isabella','Mia','Abigail','Emily','Charlotte','Harper','Madison','Amelia','Elizabeth','Sofia','Evelyn','Avery','Chloe','Ella','Grace','Victoria','Aubrey','Scarlett','Zoey','Addison','Lily','Lillian','Natalie','Hannah','Aria','Layla',
]

#----------------------------------------------------------------------
class Person(object):
	def __init__(self, name):
		self.name = name
		self.mate = None
		self.propose_idx = 0
		self.preference = []

	def prefers(self, p1, p2):
		if p1 not in self.preference:
			print(p1, 'is not in the preference list.')
			return None
		if p2 not in self.preference:
			print(p2, 'is not in the preference list.')
			return None
		if self.preference.index(p1) < self.preference.index(p2):
			return True
		return False

	def set_preference(self, persons, order=None):
		self.preference = persons.copy()
		if order is None:
			random.shuffle(self.preference)

	def __str__(self):
		return '{:10} {}'.format(self.name, [p.name for p in self.preference])

#----------------------------------------------------------------------
class Pair(object):
	def __init__(self, man, woman):
		self.man = man
		self.woman = woman


	def __str__(self):
		return '({}, {})'.format(str(self.man), str(self.woman))

#----------------------------------------------------------------------
def print_list(L):
	for x in L:
		print(x)

#----------------------------------------------------------------------
def print_arrangement(pairs):
	for p in pairs:
		print(p[0])
		print(p[1])
		print()

#----------------------------------------------------------------------
def init(m, w, seed=None):
	random.seed(seed)
	men = [ persons(i) for i in m ]
	women = [ Person(i) for i in w ]
	for i in men:
		i.set_preference(women)		
	for i in women:
		i.set_preference(men)
	return men, women

#----------------------------------------------------------------------
def random_arrangement(m, w, seed=None):
	random.seed(seed)
	men = [ Person(i) for i in m ]
	women = [ Person(i) for i in w ]
	for i in men:
		i.set_preference(women)		
	for i in women:
		i.set_preference(men)
	idx = list(range(len(men)))
	random.shuffle(idx)
	pairs = []
	for i in range(len(idx)):
		men[i].propose_idx = idx[i]
		men[i].mate = women[idx[i]]
		women[idx[i]].mate = men[i]
		pairs.append((men[i], women[idx[i]]))
	return men, women, pairs

#----------------------------------------------------------------------



