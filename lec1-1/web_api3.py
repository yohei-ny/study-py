import urllib.request as req
import urllib.parse as parse
import sys
sys.argv
# sys.argvはコマンドライン引数を扱い条件に応じた引数を使用できるようなる

if len(sys.argv) <=1:
  print("USAGE: hyakuniisyu.py(keyward)")
  sys.exit()
keyward =sys.argv[1]
# sys.argv[0]には調べた使用したファイル名が入る

API ="https://api.aoikujira.com/hyakunin/get.php"
query ={
  "fmt":"ini",
  "key":keyward
}
params =parse.urlencode(query)
url =API +"?"+params
print("url =",url)
with req.urlopen(url) as r:
  b =r.read()
  data =b.decode("utf-8")
  print(data)