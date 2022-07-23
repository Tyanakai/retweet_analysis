# retweet analysis with BERT
tweet内容から、どれだけretweetされるかを予測するBERTモデルを訓練します。
<br>
## Usage
###  Installation
デプロイする環境下で以下のコマンドを入力して下さい。
```
$ git clone https://github.com/Tyanakai/tweet_analysis.git
$ cd tweet_analysis
```
```
$ pip install -r requirements.txt
```
### Execution
以下のコマンドを実行し、twitterから情報を取得します。情報は`tw_data.csv`として保存されます。<br>
csvの列はtweet内容、retweet数、tweet主体のfollower数 となっています。
```
$ python twitter_api.py
```

###  train model
