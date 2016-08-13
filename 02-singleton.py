#! C:\\Python27\ Python
# -*- coding: utf-8 -*-

# using new type class
__metaclass__ = type


class Singleton:
	'''
	class level single instance
	'''
	_instance = None


	def __init__(self):
		'''
		must exist, will be called after __new__ 
		'''
		pass


	def __new__(cls, *args, **kwargs):
		'''
		customize new operator for this class, when trying to new an object of this class,
		it always return the single instance
		'''
		if cls._instance is None:
			cls._instance = super(Singleton, cls).__new__(cls, args, kwargs)

		return cls._instance




class Singleton2:
	'''
	class decorator, making other class to Singleton
	'''
	def __init__(self, cls):
		self._cls = cls

	def __call__(self):
		'''
		make the instance of  
		'''
		raise TypeError('Singletons must be accessed through "Instance()".')

	def __instancecheck__(self, inst):
		return isinstance(inst, self._cls)

	def instance(self):
		try:
			return self._instance
		except:
			self._instance = self._cls()
			return self._instance


@Singleton2
class TestCls:
	'''
	class has been decorated to singleton
	TestCls will be not class anymore, it becomes an instance of Singleton2
	'''
	def __init__(self):
		pass

	def test(self, param=''):
		print 'test function, param:', param



if __name__ == '__main__':

	obj1 = Singleton()
	print obj1
	obj2 = Singleton()
	print obj2
	print obj1 == obj2
		

	#obj3 = TestCls()
	obj4 = TestCls.instance()
	print obj4

	obj5 = TestCls.instance()
	print obj5
	print obj5 == obj4

	print '1 > '
	obj5.test('obj5')
	
	print '2 > '
	print type(TestCls)
	print isinstance(obj5, TestCls)
	print isinstance(TestCls, Singleton2)

	print '3 > '
	ss = Singleton2(TestCls)
	print type(ss)
	print isinstance(ss, Singleton2)