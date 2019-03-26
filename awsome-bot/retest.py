import re
#rule=r'([收买有求].*网)[^(球|拍)]'
rule=r'([收买有求租(有.*转让)].*网)(?![球拍上吧址])'
print(re.match(rule,'求一个网'))

