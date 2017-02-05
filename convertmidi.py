import base64
mid_file = "output.mid"
print "mid64='''\\\n" + base64.encodestring(open(mid_file, 'rb').read()) + "'''"
