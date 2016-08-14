# !C:\Python27 python
# -*- coding: utf-8 -*-

# new type class
__metaclass__ = type


class AbstractBuilder:
 
	def __init__ (self):
		self._process_list = []
	
	def feasibility(self):
		raise NotImplementError("AbstractBuilder")

	def bid(self):
		raise  NotImplementError("AbstractBuilder")

	def requirement(self):
		raise NotImplementError("AbstractBuilder")

	def design(self):
		raise NotImplementError("AbstractBuilder")

	def program(self):
		raise NotImplementError("AbstractBuilder")
	
	def test(self):
		raise NotImplementError("AbstractBuilder")

	def deployment(self):
		raise NotImplementError("AbstractBuilder")

	def maintenance(self):
		raise NotImplementError("AbstractBuilder")
	
	def show_process(self):
		for process in self._process_list :
			print '>', process


class ConcreteBuilder(AbstractBuilder):

	def feasibility(self):
		self._process_list.append('feasibility analyze')
		print 'feasibility analyze'

	def bid(self):
		self._process_list.append('project bid')
		print 'project bid'

	def requirement(self):
		self._process_list.append('requirement analyze')
		print 'requirement analyze'

	def design(self):
		self._process_list.append('project design')
		print 'project design'

	def program(self):
		self._process_list.append('project program')
		print 'project program'

	def test(self):
		self._process_list.append('project test')
		print 'project test'

	def deployment(self):
		self._process_list.append('project deployment')
		print 'project deployment'

	def maintenance(self):
		self._process_list.append('project maintenance')
		print 'project maintenance'


class Project(object):
	'''
	concrete project
	'''
	def __init__(self, builder):
		super(Project, self).__init__()
		self._builder = builder


	def construct(self):
		self._builder.feasibility()
		self._builder.bid()
		self._builder.requirement()
		self._builder.design()
		self._builder.program()
		self._builder.test()
		self._builder.deployment()
		self._builder.maintenance()
			


if __name__ == '__main__':
	builder = ConcreteBuilder()
	project = Project(builder)

	project.construct()