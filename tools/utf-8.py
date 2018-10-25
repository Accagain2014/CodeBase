import sys

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
  reload(sys)
  sys.setdefaultencoding(defaultencoding)