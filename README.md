# JASMINE Developer's Guide

このリポジトリは JASMINE のソフトウェアチームで開発をするために必要な情報をまとめたドキュメントを提供します. 環境構築のメモ, つまづいたこと, チュートリアルや役立つ情報などを追加していただけるとありがたいです.


## 自分の計算機でドキュメントを表示する

ドキュメントは `Python` の `mkdocs` というパッケージを使用して作成しています. テンプレートとして `material` を使用しています. `pip` 等を使用して以下のパッケージをインストールすることでドキュメントをコンパイルできるようになります.

```
mkdocs==1.2.3
mkdocs-bootstrap4==0.1.5
mkdocs-git-committers-plugin==0.2.2
mkdocs-img2fig-plugin==0.9.3
mkdocs-material==8.1.4
mkdocs-material-extensions==1.0.3
```

`material` についての詳細は以下のページを参照してください.

- [Material for MkDocs][material]

自分の計算機でドキュメントを表示するためには以下のコマンドを実行してください.

``` console
$ mkdocs serve
```

ローカルのディレクトリにドキュメントが生成されます. また, 計算機のローカル環境ででウェブサーバが起動します. ブラウザで `localhost:8000` にアクセスすることでドキュメントを閲覧できます. 閲覧が完了したら `Ctrl-c` でプロセスを終了させてください.


## ドキュメントを追加する
ドキュメントは Markdown 形式で記述してください. Markdown 形式については「Markdown チートシート」等で検索するか, 以下のリンクを参照してください. GitHub Flavored Markdown の機能はほぼ使えるはずです.

- [Markdown 記法チートシート - Qiita][cheetsheet]

ドキュメントは `docs/` 以下に作成してください. 作成したら忘れずに `mkdocs.yml` を編集してください. `mkdocs.yml` はドキュメントの設定ファイルです. 末尾に `nav` から始まるセクションがあります. 一部を以下に示します.

``` yaml
nav:
  - トップページ: index.md
  - はじめに:
    - startup/setup.md
    - startup/guideline.md
```

`nav` にはドキュメントのツリー構造が示されています. `docs/` からみた相対パスを追加することでドキュメントに新しいページを追加できます. `docs/sample/hogehoge.md` をトップレベルのメニューに追加する場合は以下のように編集します.

``` yaml
nav:
  - トップページ: index.md
  - はじめに:
    - startup/setup.md
    - startup/guideline.md
  - sample/hogehoge.md
```

`#見出し` を適切に記述していればリンク文字列は自動で設定されます. 見出しと違う文字列をリンクに設定したい場合は以下のように記述してください.

``` yaml
nav:
  - トップページ: index.md
  - はじめに:
    - startup/setup.md
    - startup/guideline.md
  - fugafuga: sample/hogehoge.md
```

## ドキュメント追加の手順

ドキュメントを追加するまでの手順を示します. まずは作業をするためのブランチを作成してください. ここでは `new/hogehoge` というブランチ名にしました. ブランチ名はないように合わせて適切に設定してください.

``` console
$ git checkout -b new/hogehoge
```

ドキュメントファイルを `docs` に追加します. 他のページからリンクを張る場合には対応するページも編集してください. `mkdocs.yml` を編集してドキュメントにページを登録することも忘れないでください. ドキュメントの作成中は適切に `commit` や `push` をして不慮の事故に備えてください.

`mkdocs serve` を実行して自分のブラウザでドキュメントを表示してください. コンソールにエラーが表示されていないか, またドキュメントが適切に表示されていることを確認してください.

ドキュメントの追加が完了したら `git push` をして GitHub で `develop` ブランチに pull request を送ってください. pull request が承認されたら管理人が GitHub Pages に反映させます. 最新のドキュメントが以下の URL で公開されるようになります.

- https://github.com/JASMINE-Mission/devguide/


[material]: https://squidfunk.github.io/mkdocs-material/
[cheetsheet]: https://qiita.com/Qiita/items/c686397e4a0f4f11683d
[ghpage]: https://github.com/JASMINE-Mission/devguide/
