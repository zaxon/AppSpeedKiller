'''
	base class for all tools, extends this class!
	@author jiankangxin@gmail.com, 2015-6-14
'''
import abc
import utils.cmd_or_shell
from tool_manager import tool_manager

class common_tool(object):

	def __init__(self):
		'''
		'''

	@abc.abstractmethod
	def parse_data(self, data_bundle):
		pass

	def set_common_command(self, tester_info):
		self.set_command('%s %s ' % (self.get_command(), tester_info.package_name))

	def set_command(self, command):
		self.command = command
		self.tool_manager = tool_manager

	def get_command(self):
		return self.command

	def set_os_min_v(self, os_min_version):
		self.min_os_version = os_min_version

	def set_os_max_v(self, os_max_version):
		self.max_os_version = os_max_version

	def get_os_min_v(self):
		return self.min_os_version

	def get_os_max_v(self):
		return self.max_os_version

	def get_tool_manager(self):
		return self.tool_manager

	def execute(self, func):
		self.tool_manager.execute(self.get_command(), func)