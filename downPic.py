#-*-coding:utf-8-*-
##########################
#		Author:Hejunjie			 #
#		Time:2017:4:13 20:17 #
##########################
import requests

url = 'http://img1.gamersky.com/image2014/12/20141201why_1/image'

def downloadPic(imageUrl,filePath):
	r = requests.get(imageUrl)
	with open(filePath,"wb") as code:
		code.write(r.content)
		code.fclose()

for num in range(1,20):
	filePath = 'C:\\Users\\455\\Desktop\\test\\image%s.jpg' %num
	downloadPic(url+'0'*(3-len(str(num)))+str(num)+'.jpg',filePath)
	print 'have saved %s' %filePath
