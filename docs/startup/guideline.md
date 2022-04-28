# 開発ガイドライン

このページではコードを開発するときの指針としていくつかのルールを記述します. 以下のルールは必ず従わなければいけないものではありませんが, コードの体裁がしっちゃかめっちゃかにならないための指針として提示します. 書き方に迷ったときなどは以下のルールを参考にしてください.


## Python 開発のガイドライン
このセクションでは Python で開発をするときの指針をまとめます.
コードの一例を以下に示します.

``` python linenums="1"
--8<-- "examples/example.py"
```


### shebang!
必須ではありませんが, コードの冒頭部に以下の 2 行を記述することを推奨します.

``` python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
```

1 行目を書いておくとコード単体で実行したときに os が `/usr/bin/env python` で実行される Python を起動するようになります. 計算機内に複数の Python 環境がある場合に「いつも使用しているもの」が起動されるようになります.

2 行目はコードが UTF-8 で書かれていることを宣言します. コード内に複数バイト文字列 (日本語など) が含まれていてもエラーが出なくなります (たぶん).


### インデント
`Python` ではインデントを使用して論理的なブロックを構成します. インデントは慣習としてスペース 4 つを使用します. JASMINE の開発でもこの方式に従います. タブ文字を使用しないように気をつけてください.

!!! tip
    `emacs` であれば `indent-tab-mode` を `nil` に設定してください. 空白周りの挙動は `whitespace-mode` を導入すると便利です.


### 文字列
文字列はシングルクオート `''` で囲ってください. `Python` ではシングルクオートとダブルクオートで囲われた文字列を区別しませんが, どちらかに統一しておいたほうが良いでしょう.


### 関数名/変数名
関数や変数の名前は動作がわかるよう簡潔に定義してください. 関数名や変数名は基本的に小文字でスネークケース (`some_fantastic_function`) を採用してください. 意味が明らかに明確な場合やスコープが限られる場合を除いて 1 文字の変数名 (`a`, `x`, `_`, ...) や内容がよくわからない変数名 (`temp`, `tmp`, `hoge`,...) は避けてください.

Python ではクラスの名前はキャメルケース (`SomeFantasticClass`) をもちいることが多いようです. 強い理由がなければこの方針に従ってください.


### コメント
主要な関数には必ず定形のコメント (ドキュメント) を付けてください. ドキュメントの付け方にはいくつか流儀がありますが, [Google Python Style Guide][google] が簡潔なのでこれに従うのがよいと思います. 以下に簡単な例を示しました. 定形でドキュメントを記載することで, ドキュメント生成自動化ツール (Sphinx 等) で処理できます.

``` python
def some_function(arg1,arg2):
    """ 関数の機能を 1 行で要約して記述

    1 行では書けない詳細や重要な注意を記述する (optional).

    Args:
      arg1: 引数 1 の説明
      arg2: 引数 2 の説明

    Returns:
      戻り値の説明
    """
    ...
```

- [Google Python Style Guide][google]
- [Documenting Python Code: A Complete Guide - Real Python][documenting]

[google]: https://google.github.io/styleguide/pyguide.html
[documenting]: https://realpython.com/documenting-python-code/


### テスト
主要な関数には必ずテストを作成するようにしてください. テストを作成することで, 開発が進みプロジェクトが大きくなっても, コードが健全であることを保証できます. テストを記述する必要性やテストの書き方については別のページに記載しています. 以下のページをご参照ください.

- [テスト開発の指針](./test.md)


### linter/formatter
コードを機械的にチェックするためのツールを紹介します.

`yapf` は Google が開発している Python の formatter です. コードを解析して標準的ではないコードを修正してくれます. `pip` 経由でインストールできます. 詳細については [GitHub のページ][yapf] を参照してください.

``` console
$ pip install yapf

$ yapf your_python_code.py    # フォーマットしたコードを標準出力に表示
$ yapf -d your_python_code.py # -d, --diff オプションで変更した差分を表示
$ yapf -i your_python_code.py # -i, --in-place オプションでコードを直接編集
```

pull request を送る前にこのツールを使用して体裁を整えておくことを推奨します.

`pylint` は Python コードをより強力にチェックするためのツールです. 同じく `pip` 経由でインストールできます. [詳細なマニュアル][pylint]が整備されているので詳細はそちらを参照してください.

``` console
$ pip install pylint

$ pylint your_python_code.py # ドキュメントなどを含めたコードの評価が表示される
```

`yapf` と違ってドキュメントがきちんと書かれているか, 余計なモジュールを import していないかなどもチェック &amp; 評価してくれます. モジュール単位でのチェックもしてくれるようなので pull request を送る前やバージョンリリース前にはこのツールを使用してチェックしておくことを推奨します.

!!! info
    `pylint` モジュール間の依存関係を確認するなどかなり細かいところまでチェックしてくれすようです. 採点はかなり厳しいので常に満点をキープすることを目指す必要はないと思います.

[yapf]: https://github.com/google/yapf
[pylint]: https://pylint.pycqa.org/en/latest/
