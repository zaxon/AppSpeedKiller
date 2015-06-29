'''
	@author jiankangxin@gmail.com, 2015-6-14
'''

from common_tool import common_tool

class gfxinfo(common_tool):

	TAG = 'GET_GFXINFO'
	NEED_COMMON_COMMAND = True

	def __init__(self):
		super(common_tool, self).__init__()
		self.set_command('adb shell dumpsys gfxinfo')
		self.set_os_min_v(17)
		self.set_os_max_v(None)

	def parse_data(self, data_bundle):
		print data_bundle
