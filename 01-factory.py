# #!C:\Python27 python
# -*- coding: utf-8 -*-

# 使新式类
__metaclass__ = type



class AbstractFactory:
     def build_product(self, p_type):        
         raise NotImplementError("AbstractFactory")


class AbstractProduct:
	'''
	AbstractProduct class 
			
	'''
	def __init__(self, p_type, p_params):
		self._type = p_type
		self._params = p_params
	
	@property
	def pro_type(self):
		return self._type

	@pro_type.setter
	def set_type(self, p_type):
		self._type = p_type

	@property
	def pro_params(self):
		return self._params

	@pro_params.setter
	def set_params(self, p_params={}):
		self._params = p_params

	def show_info(self):
		raise NotImplementError("AbstractProduct.show_info")

	
class ProductA(AbstractProduct):
	'''
	Concrete Product A
	'''
	p_id = 1

	def __init__(self, name):
		AbstractProduct.__init__(self, 'PA', {'name': name, 'pid': ProductA.p_id})
		ProductA.p_id += ProductA.p_id


	def show_info(self):
		infos = {
			'type': self._type,
			'name': self._params['name'],
			'pid' : self._params['pid'],
		}

		return 'type: %(type)s, name: %(name)s, pid: %(pid)d' % infos


class ProductB(AbstractProduct):
	'''
	Concrete Product B
	'''
	def __init__(self, name, price=1.0):
		AbstractProduct.__init__(self, 'PB', {'name': name, 'price': price})


	def show_info(self):
		infos = {
			'type': self._type,
			'name': self._params['name'],
			'price' : self._params['price'],
		}

		return 'type: %(type)s, name: %(name)s, pid: %(price)f' % infos


	@property
	def pro_price(self):
		return self._params['price']


class FactoryBeijing(AbstractFactory):
	"""
	Concrete Creator in Beijing
	"""
	def __init__(self):
		super(FactoryBeijing, self).__init__()
		self._product = []

	def build_product(self, p_type):  
		pro_inst = None

		if p_type == 'PA':
			pro_inst = ProductA('A Product')
		elif p_type == 'PB':
			pro_inst = ProductB('B Product', 99.00)

		if not pro_inst:
			self._product.append(pro_inst)

		return pro_inst


		

if __name__ == '__main__':

	factory = FactoryBeijing()
	
	p1 = factory.build_product('PA')
	p2 = factory.build_product('PB')
	p3 = factory.build_product('PA')

	print 'p1>', p1.show_info()
	print 'p2>', p2.show_info()
	print 'p3>', p3.show_info()

	p3.pro_params['name'] = 'new name'

	print 
	print 'p2> type: {0}, price: {1}'.format(p2.pro_type, p2.pro_price)
	print 'p3> type: {0}, params: {1}'.format(p3.pro_type, p3.pro_params)