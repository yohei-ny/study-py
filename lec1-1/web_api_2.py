import urllib.request
import urllib.parse

API = "https://api.aoikujira.com/zip/xml/get.php"

values ={
  #httpメソッドで送るため?が含まれたgetで送っている　その中のfmtとznを使用している
  "fmt":"xml",
  "zn" :"1500042"
}
params =urllib.parse.urlencode(values)
#パラメータの受け取りvalueにあるのものを見つける
url =API +"?"+params
#パラメータの受け渡しからurlの後に？をつける
print("url=",url)
data =urllib.request.urlopen(url).read()
#データの読み込み
text =data.decode("utf-8")
print(text)