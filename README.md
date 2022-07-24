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
`tw_data.csv`をGoogle Driveにアップロードし、
Google Colabratory上で[retweert_regression.ipynb](retweert_regression.ipynb)を実行して下さい。<br>

予測値に対する考察は以下の通りです。<br>
![スクリーンショット 2022-07-24 114854](https://user-images.githubusercontent.com/81244428/180630728-5d303db2-dba8-417e-b508-908042cb3117.png)


とおくと、<br>
![スクリーンショット 2022-07-24 115353](https://user-images.githubusercontent.com/81244428/180630819-9cb13501-56b1-4c3d-9c60-5f53e11096ea.png)


となるので、<br>
![スクリーンショット 2022-07-24 115426](https://user-images.githubusercontent.com/81244428/180630832-35061004-574a-49d6-b097-fbadb1eb9024.png)


と表せます。<br>


同じ内容のtweetを別の主体が行ったと想定すると、今回の場合では`r:一定`となるので、
retweetのretweetが、retreet数にカウントされるにしても、されないにしても、<br>
![スクリーンショット 2022-07-24 120847](https://user-images.githubusercontent.com/81244428/180630842-7a93d23f-83b2-4075-93f5-2f7031a39e11.png)


となり、retweet数はtweet主体のfollower数によることが分かります。

今回はtweet内容によるretweet数の変化を分析したいので、以上より`retweet数 / (follower数 + 1)`を予測する値をします。<br>
ただし、０除算を防ぐため分母は`follower数 + 1`とします。<br>
