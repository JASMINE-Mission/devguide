# 環境構築
参考として環境構築手順の一例を示す.


## 開発環境の構築
Ubuntu 20 LTS に入っていた `python` を用いる.

``` console
$ python3 -V
Python 3.8.10
```


`pip` が入っていなかったのでインストール.

``` console
$ sudo apt install python3-pip
```

`python` のモジュールを `pip --user` でインストールしていく.

``` console
$ pip3 install --user ホゲホゲ
```
`ホゲホゲ` の部分は, 適宜必要なものを追加するようにしてるけれど, 現時点では以下.

```
docopt matplotlib scipy opencv-python selenium pyvirtualdisplay pyFFTW skyfield pexpect seaborn pandas numpy-quaternion numba openpyxl tqdm pyinstaller
```

以下の 2 つのモジュールは `pip` では入らなかったので, `github` より入れました.

``` console
# ソースを展開するディレクトリに移動(たとえば, $HOME/srcdir)
$ wget https://github.com/astropy/astropy-helpers/archive/master.zip
$ mv master.zip astropy-helpers-master.zip
$ unzip   astropy-helpers-master.zip
$ cd astropy-helpers-master
$ python3 setup.py install --user

$ cd ..
$ wget https://github.com/ericmandel/pyds9/archive/master.zip
$ mv master.zip pyds9-master.zip
$ unzip pyds9-master.zip
$ cd pyds9-master
$ python3 setup.py install --user
```

以上で, python の環境が整った.


## 開発ツールの整備
GitHub と Slack を使えるようにする.

- GitHub:  https://github.com/JASMINE-Mission
    - ユーザ登録をして用いる.
- Slack : http://jasminesimulation.slack.com
    - 招待してもらって登録ユーザになって参加する.

git コマンドが使えるように

``` console
$ sudo apt install git
```

ここまでで, チームメンバーとして最低限のスタートライン.


## 開発コードの取得
まずは repository をとってくる. 作業ディレクトリで以下を実行する.

```
$ git clone https://github.com/JASMINE-Mission/telescope_baseline
```

そうすると, telescope_baseline というディレクトリができているので

``` console
$ cd telescope_baseline
```

開発ブランチで作業するために以下を実行.

``` console
$ git checkout develop
```

ここで, 作業ディレクトリは以下のようになっている.

```
├── MANIFEST.in
├── README.md
├── examples
│   └── photometry_example.py
├── miyakawa_test_message.txt
├── setup.py
├── src
│   └── telescope_baseline
│       ├── __init__.py
│       ├── data この下にたくさんのファイル, データ
│       └── photometry
│           ├── Hw_coeff.py
│           ├── __init__.py
│           └── convmag.py
└── tests
    └── photometry
        ├── Hw_coeff_test.py
        └── convmag_test.py
```


## パッケージのインストール
開発するパッケージを `python` 環境から使えるようにする.

``` console
$ python3 setup.py install --user
```

ここまでで, 既存コードが使えるはず.
作業ディレクトリには以下の新しいディレクトリができる.

```
build/もとの src の下にあったものと幾つかのファイル
dist/telescope_baseline-0.1.0-py3.8.egg
src/telescope_baseline.egg-info/幾つかのファイル
```


## 新機能実装のための準備
今回は新しいコードを追加するので, 新しいブランチを作成する.
新しいコードとして, これまで中心推定精度の見積に用いていたコードとしたい.
中心推定のコードの構成は新しく整理しなおすべきと考えるが,
とりあえず最新版のものをベースに考える.

そこで, PSF の作成プログラムの中で呼び出していたモジュールの中で,
一番下層 (基本？) になっている望遠鏡データの読み込みをしているところにしてみる.
そうすると, `Telescope` の class 定義部分になります. このコードを書いたのは
私ではないけれど, 私はEFLを使わないので無効化しています.

新しくブランチを作成する. ブランチ名を `def_tele_class` としよう.

``` console
$ git branch def_tel_class
```

新しくできたブランチでの作業開始

``` console
$ git checkout def_tel_class
```

ディレクトリ構成は新しいブランチ作成では変化してなさそう.
