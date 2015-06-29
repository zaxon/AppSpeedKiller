'''
	@author jiankangxin@gmail.com
'''

from utils import cmd_or_shell

class tool_manager(object):

	def __init__(self):

		self.result_path = None

	@staticmethod
	def execute(cmd, func):
		'''
			speed test tools executer, data_parser should be used as call_back
		'''
		if not tool_manager.checker():
			return
		func(''.join(cmd_or_shell.os_system_sync(cmd)))

	@staticmethod
	def checker():
		'''
		'''
		#TODO rule 1 os version CHECKER
		return True

	@staticmethod
	def get_adb_version():
		return adb('version')[0]
