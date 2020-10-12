import urllib.request
#モジュールのインストール
url ="https://uta.pw/shodou/img/28/214.png"
#保存したいurlの読み込み
savename ="test3.png"
#保存する名前
mem =urllib.request.urlopen(url).read()
#データの読み込みが行えた場合において保存される
#ファイルのダウンロード読み込み
with open(savename,mode="wb") as f:
  #open関数でファイルを開く
  f.write(mem)
  # witeがデータの保存
  print("保存しました")