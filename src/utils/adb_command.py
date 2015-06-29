import cmd_or_shell 

#TODO adb Terminal should be used here
def adb_shell(command):
	return cmd_or_shell.os_system_sync('adb shell %s' % (command))

def adb(command):
	return cmd_or_shell.os_system_sync('adb %s' % (command))
