'''
	@author jiankangxin@gmail.com, 2015-6-14
'''

#INIT PATH
import sys
sys.path.append('utils')
sys.path.append('plugins')
sys.path.append('plugin_conf')
sys.path.append('interfaces')

from plugins.get_gfxinfo import get_gfxinfo
from interfaces import speed_killer_interface


if __name__ == '__main__':
	ski = speed_killer_interface.speed_killer_interface('com.baidu.searchbox')
	cmd_list = ['GET_GFXINFO']
	ski.run(cmd_list)
	