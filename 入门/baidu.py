from urllib import request

def visit_baidu():
 URL = "http://www.baidu.com"
 # open the URL
 req = request.urlopen(URL)
 # read the URL
 html = req.read()
 # decode the URL to utf-8
 html = html.decode("utf_8")
 print(html)

if __name__ == '__main__':
 visit_baidu()