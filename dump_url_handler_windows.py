from _winreg import OpenKey, EnumValue, EnumKey, HKEY_CLASSES_ROOT

handlers = []

hkcrKey = OpenKey(HKEY_CLASSES_ROOT, "")
try:
	i = 0
	while 1:
		keyName = EnumKey(hkcrKey, i)
		keyHandle = OpenKey(HKEY_CLASSES_ROOT, keyName)
		try:
			j = 0
			while 1:
				valueName = EnumValue(keyHandle, j)
				if valueName[0] == 'URL Protocol':
					handlers.append(keyName)
				j = j + 1

		except WindowsError:
			pass
		i = i + 1
except WindowsError:
	pass

for handler in sorted(handlers):
	print handler
