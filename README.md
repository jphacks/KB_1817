# サンプル（プロダクト名）

[![Product Name](image.png)](https://www.youtube.com/watch?v=G5rULR53uMk)

## 製品概要
### Tipping × Tech

### 背景（製品開発のきっかけ、課題等）
####現状の課題
- お年寄りや妊婦さんに席を譲る、目の不自由な方に声をかける、道に落ちていたゴミを拾う...世の中には個人レベルですることができる **”いいこと”** がたくさんあるはず！
- でも日本人の「誰かがやってくれる精神」「目立ちたくない精神」が邪魔をして積極的に **”いいこと”** をしづらい！
- かといって、「お前がいいことをしろよ」「最近の若者は...」のような **ネガティブな動機で”いいこと”をしたくはない！**
- もっと**ポジティブに（積極的に）”いいこと”をして欲しい！**
####ではどうするか
- **現実世界での”いいこと”に投げ銭で「いいね！」をしよう！**

### 製品説明（具体的な製品の説明）

### 特長

#### 1. 周りにいるちゃりんユーザーをGoogleMap上に表示させる

#### 2. 投げ銭できる

#### 3. 投げ銭を受け取ることができる

### 解決出来ること
この製品を利用することによって最終的に解決できることについて記載をしてください。

### 今後の展望
#### 現在の問題点
- ブラウザで動くWebアプリなのでリアルタイム性が低い
- 投げ銭はアプリ内のポイントでしかないため、ユーザーにとっての価値が低い

#### ではどうしていきたいか
- 最終的にはブロックチェーンの技術を用いてGPSで位置情報を取ることなくサーバーレスで動くサービスにしたい
- 投げ銭自体もBitCoinやEthereumなどの仮想通貨で決済できるようにして、価値のある投げ銭にしたい


## 開発内容・開発技術
### 活用した技術
#### API・データ

* 位置情報取得：[Geolocation API](https://developer.mozilla.org/ja/docs/Web/API/Geolocation/Using_geolocation)
* Map表示：[Google Maps API](https://cloud.google.com/maps-platform/?hl=ja)

#### フレームワーク・ライブラリ・モジュール
* Webアプリフレームワーク：Flask(Python)
* サーバー：Heroku
* BootStrap3


### 独自開発技術（Hack Dayで開発したもの）
#### 2日間に開発した独自の機能・技術
* 投げ銭機能
* 位置情報を取得して近くにいる他ユーザーをMapに表示
