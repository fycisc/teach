# -*- coding: utf-8 -*-
__author__ = 'feiyicheng'
import urllib2
import string

deltatime = 5

classes = [
	('http://mis.teach.ustc.edu.cn/querystubykcbjh.do?tag=jg&kcbjh=011X1902&xnxq=20142&kczw=Java%C8%ED%BC%FE%BF%AA%B7%A2%BB%F9%B4%A1',100,'java'
	 , 'http://mis.teach.ustc.edu.cn/xkgcinsert.do?xnxq=20142&kcbjbh=011X1902&kcid=2599&kclb=0&kcsx=4&cxck=0&zylx=01&gxkfl=null&xlh=1&sjpdm=35&kssjdm=null', '011X1902'),
	('http://mis.teach.ustc.edu.cn/querystubykcbjh.do?tag=jg&kcbjh=011X1901&xnxq=20142&kczw=Java%C8%ED%BC%FE%BF%AA%B7%A2%BB%F9%B4%A1',60,'java'
	 , 'http://mis.teach.ustc.edu.cn/xkgcinsert.do?xnxq=20142&kcbjbh=011X1901&kcid=2599&kclb=0&kcsx=4&cxck=0&zylx=01&gxkfl=null&xlh=1&sjpdm=25&kssjdm=null', '011X1901'),
	('http://mis.teach.ustc.edu.cn/querystubykcbjh.do?tag=jg&kcbjh=022X2601&xnxq=20142&kczw=%CC%EC%CC%E5%CE%EF%C0%ED%B8%C5%B9%DB',200,'天体物理概观'
	 , 'http://mis.teach.ustc.edu.cn/xkgcinsert.do?xnxq=20142&kcbjbh=022X2601&kcid=5326&kclb=0&kcsx=4&cxck=0&zylx=01&gxkfl=null&xlh=1&sjpdm=55&kssjdm=null','022X2601'),
	('http://mis.teach.ustc.edu.cn/querystubykcbjh.do?tag=jg&kcbjh=103X0101&xnxq=20142&kczw=%B4%AB%CD%B3%BD%A1%C9%ED',30,'传统健身'
	 , 'http://mis.teach.ustc.edu.cn/xkgcinsert.do?xnxq=20142&kcbjbh=103X0101&kcid=4707&kclb=0&kcsx=4&cxck=0&zylx=01&gxkfl=null&xlh=1&sjpdm=15&kssjdm=null','103X0101'),
	('http://mis.teach.ustc.edu.cn/querystubykcbjh.do?tag=jg&kcbjh=601X3401&xnxq=20142&kczw=%B5%E7%D7%D3%D0%C5%CF%A2%BC%EC%CB%F7',100,'电子信息检索'
	 , 'http://mis.teach.ustc.edu.cn/xkgcinsert.do?xnxq=20142&kcbjbh=601X3401&kcid=5184&kclb=0&kcsx=4&cxck=0&zylx=01&gxkfl=null&xlh=1&sjpdm=44&kssjdm=null','601X3401'),
	('http://mis.teach.ustc.edu.cn/querystubykcbjh.do?tag=jg&kcbjh=103X2901&xnxq=20142&kczw=%C9%E7%BD%BB%CE%E8%B5%B8(%C4%D0%B2%BD)',28,'社交舞蹈'
	 , 'http://mis.teach.ustc.edu.cn/xkgcinsert.do?xnxq=20142&kcbjbh=103X2901&kcid=4734&kclb=0&kcsx=4&cxck=0&zylx=01&gxkfl=null&xlh=1&sjpdm=44&kssjdm=null HTTP/1.1','103X2901'),
]

headers = [
	('Host', 'mis.teach.ustc.edu.cn'),
	('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
	('Cookie','JSESSIONID=08181E4764EE884E408DE31431817598; __utma=63887786.691193098.1419693077.1421477665.1421675729.11; __utmz=63887786.1419693077.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _gscu_1103646635=19159380twnlr411'),
	('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.3.18 (KHTML, like Gecko) Version/8.0.3 Safari/600.3.18'),
	('Accept-Language','zh-cn'),
	('Accept-Encoding','gzip, deflate'),
	('Connection','keep-alive'),
]

inserturlsample = 'http://mis.teach.ustc.edu.cn/xkgcinsert.do?xnxq=20142&kcbjbh=011X1901&kcid=2599&kclb=0&kcsx=4&cxck=0&zylx=01&gxkfl=null&xlh=1&sjpdm=25&kssjdm=null'
opener = urllib2.build_opener()
opener.addheaders = headers
# content = opener.open(inserturlsample).read()
# print(content)
# print(content.find('<td class="bg5" align="center" width="10%">'+ str(101) +'</td>'))

