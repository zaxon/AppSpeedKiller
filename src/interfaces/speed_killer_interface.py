'''
	@author jiankangxin@gmail.com, 2015-6-14
'''

from plugin_conf import conf
from tester_info import interface_data

class speed_killer_interface(object):

	def __init__(self, package_name):
		'''
		'''
		#init plugin_list
		self.tester_info = None
		self._init(package_name)

	def run(self, tool_list):
		'''
		'''
		for plugin_name in tool_list:
			if self.plugin_list.has_key(plugin_name):
				if self.plugin_list[plugin_name].NEED_COMMON_COMMAND == True:
					self.plugin_list[plugin_name].set_common_command(self.tester_info)
				self.plugin_list[plugin_name].execute(self.plugin_list[plugin_name].parse_data)


	def _init(self, arg1):
		'''
		'''
		self.tester_info = interface_data()
		self.tester_info.set_package_name(arg1)
		self.plugin_list = conf.plugin_list