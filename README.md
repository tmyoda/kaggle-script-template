Kaggle script build system template
===================================

# 説明
- kaggleのノートブックコンペ用
- base64エンコードしてソースまるごとノートブックへ

参考: https://zenn.dev/wakame/articles/20201114_kaggle_code_management

ノートブックに貼り付ける用のスクリプト生成コマンド
```
python build.py
```


# 使い方
1. `./easy_gold`を任意のプロジェクト名に変更
2. 同様に`setup.py`の`project_name`変数をプロジェクト名に変更
3. `./プロジェクト名`以下に好きなように学習・推論用のスクリプト作成
4. モデルをkaggle datasetsにアップロード
5. `build.py`を実行してスクリプトを生成
6. kaggle notebookに生成された`build/script.py`を貼り付けて提出

スクリプトの生成元は`script_template.py`なので、実行したいファイルが違う場合などは適宜修正


License is MIT.
