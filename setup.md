# 一番最初に一回だけやること

## Macでpython3系のインストール
## Homebrewがインストールされている前提
`brew install python3`

## python仮想環境設定ツールのインストール
`pip3 install virtualenv`

## (任意の開発用ディレクトリで)仮想環境の作成
ex) `virtualenv <virtualenv name>`
`virtualenv venv`
## pip listした時にWARNINGが出るので設定ファイルを作成して以下を書き込む
```
vi venv/pip.conf
-----
[list]
format=columns
-----
```

## 仮想環境の起動
`source venv/bin/activate`

## 必要なライブラリのインストール(python3系で作成した仮想環境内なのでpipでOK)
`pip install requests twitter`
## インストールされていることの確認
`pip list`

## tokenなどの設定
`vi twitter_conf.py`

## 仮想環境の終了
`deactivate`


# 作業するごとにやる手順

## 仮想環境の起動
`source venv/bin/activate`

## 仮想環境の終了
`deactivate`
