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
### Prepare Data
以下のコマンドを実行し、twitterから情報を取得します。情報は`tw_data.csv`として保存されます。<br>
```
$ python twitter_api.py
```
csvの各列は、tweet内容、retweet数、tweet主体のfollower数 となっています。<br>
尚、twitter APIの認証キーや情報の取得の仕方は[こちら](https://norari-kurari-way.com/twitter_api_tweets_data/)の記事を参考にしました。

###  Train
取得したtwitterのデータを使用してBERTを訓練します。<br>
入力はtweet内容の文字列、予測する値は、`retweet数 / (follower数 + 1)`とします。<br>


とおくと、


となるので、


と表せます。


同じ内容のtweetを別の主体が行ったと想定すると、今回の場合では`r:一定`となるので、
retweetのretweetが、retreet数にカウントされるにしても、されないにしても、


となり、retweet数はtweet主体のfollower数によることが分かります。

今回はtweet内容によるretweet数の変化を分析したいので、`retweet数 / (follower数 + 1)`を予測する値をします。<br>
ただし、０除算を防ぐため分母は`follower数 + 1`とします。
