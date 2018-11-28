import sys

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
  reload(sys)
  sys.setdefaultencoding(defaultencoding)


## html chinese utf-8  <meta charset="utf-8">
