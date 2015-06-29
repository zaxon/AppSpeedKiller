'''
	plugin conf for speed tester tools,  class loader should be used for better taste
	@author jiankangxin@gmail.com, 2015-6-14
'''

from plugins.gfxinfo import gfxinfo

plugin_list = {}

#plugin 1, gfxinfo

gfxinfo = gfxinfo()
plugin_list[gfxinfo.TAG] = gfxinfo