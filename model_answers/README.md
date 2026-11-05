# 演習の模範解答（未公開分の置き場）

このフォルダは **`docs/` の外**にあります。mkdocs は `docs/` の中しか公開しないので、
ここに置いてあるファイルはサイトに出ません。URLを推測されても404になります。

**方針：授業が終わった回から順に公開する。**

## 公開の手順（1回分）

第NN回の授業が終わったら、次の4つを行います。

1. **ファイルを移す**

   ```sh
   git mv model_answers/NN_model_answer.R docs/materials/NN_model_answer.R
   ```

2. **`docs/index.md` の各回の表に、リンクを1つ足す**

   第2回・第3回と同じ形式です。

   ```
   ... ・ [Rmd](materials/NN.Rmd)<br>[演習の模範解答](materials/NN_model_answer.R) |
   ```

3. **`docs/materials/NN.Rmd` の演習の最後に、模範解答の節を足す**

   第3回（`03.Rmd`）の「### 模範解答」をそのままコピーして番号を変えます。

   ```markdown
   ### 模範解答

   演習1〜N の解答例を置いてあります。自分で解いたあとに見てください。

   **→ [第NN回 演習の模範解答（`.R` ファイル）](NN_model_answer.R)**

   > ブラウザで中身が表示されます。保存するときは右クリック →「リンク先を別名で保存」。
   > RStudioで開いて，**全選択して `Ctrl + Enter`** で実行して確かめてください。
   ```

4. **再レンダリングして公開**

   ```sh
   cd docs/materials && Rscript -e 'rmarkdown::render("NN.Rmd", quiet=TRUE)'
   cd ../.. && git add -A && git commit && git push origin main
   mkdocs gh-deploy --force --site-dir /tmp/kodo-keiryo-build
   ```

   再レンダリングしたら、**HTMLからbase64画像を1枚デコードして目で見ること。**
   `ragg` が読めていないと図の日本語がすべて □ になりますが、grep では検出できません。

   **ビルド先は必ず Dropbox の外にすること。** `site/` を Dropbox 内に置くと、
   mkdocs が書いた直後に Dropbox が古い版へ巻き戻し、競合コピーを作ることがある。
   2026/11/01 にこれで第5回の古い資料が一度公開された。

## 公開済み

| 回 | 公開日 |
|---:|---|
| 2 | 第2回の実施後 |
| 3 | 2026/10/29 |
| 4 | 2026/11/01 |

## 未公開（このフォルダ）

| 回 | 内容 | 公開予定 |
|---:|---|---|
| 5 | filter・select・mutate | 11/6 の授業後 |
| 6 | 集計・エラーバー・count | 11/13 の授業後 |
| 8 | 相関・cor.test・相関行列 | 11/27 の授業後 |
| 9 | クロス集計・カイ二乗／フィッシャー・積み上げ棒 | 12/4 の授業後 |
| 10 | t検定（対応なし） | 12/11 の授業後 |
| 11 | 対応のあるt検定・pivot_longer | 12/18 の授業後 |
| 13 | 一元配置分散分析・Bartlett・η² | 1/8 の授業後 |
| 14 | Tukey HSD・総合レポート | 1/22 の授業後 |

第7・12・15回は習熟度確認テストの回で演習がありません
（問題と解答例はテスト実施後に各回のページへ掲載する、と資料に書いてあります）。

## 「この回で使った関数」の表

各回の表は**手で書いていない**。素は次の3つ（リポジトリ直下 `tools/`）。

| ファイル | 役割 |
|---|---|
| `function_reference.py` | 107関数の「すること／（）の中身／例」の辞書 |
| `build_function_tables.py` | 各 `.Rmd` の「この回で使った関数」の節を作り直す |
| `verify_examples.py` | 辞書の「例」を全部Rで実行して動くか確かめる |

関数が出てくる順は、各 `.Rmd` のコードから自動で拾っている
（実行チャンク ```{r} と、実行しないコード例 ```r の両方。引用ブロックの中も見る）。
**辞書に無い関数が資料に出てくると、`build_function_tables.py` が
その関数名を出して止まる。**

直し方：

```bash
# 1. tools/function_reference.py を編集する
python3 tools/verify_examples.py          # 例が動くか確かめる（失敗0件にする）
python3 tools/build_function_tables.py    # 各 .Rmd の表を作り直す
# 2. docs/materials で全16本を再レンダリング
# 3. mkdocs gh-deploy --force --site-dir /tmp/kodo-keiryo-build
```

辞書に書いた既定値（`t.test()` はウェルチ、`head()` は6行など）は
`formals()` で実機確認したもの。推測で書き足さないこと。

ヘルプの読み方は第2回の `{#help}` 節にまとめてあり、各回の表から
`02.html#help` でリンクしている。**この節の見出しの `{#help}` を消すと
全14回のリンクが切れる。**

## コードの「コピー」ボタン

各回の HTML に出るコピーボタンの実体は `_includes/site-extras.html`（リポジトリ直下）。
このファイルには関数表のCSSも入っている。
各 `.Rmd` の末尾の `copy-button` チャンクが `file.exists()` で読み込んでいる。

- ボタンや表の見た目を変えるときは `_includes/site-extras.html` を直して**全16本を再レンダリング**する
  （HTML に埋め込まれるので、ファイルだけ直しても反映されない）
- YAML の `includes: after_body:` は**使わないこと**。学生が `.Rmd` だけダウンロードして
  Knit したとき、pandoc が「not found」で停止する。チャンク経由なら黙って何もしない

## 作成時の確認

全ファイルを R 4.6.1 で実行し、エラーが出ないこと、
コメントに書いた数値が実際の出力と一致することを確認済みです（2026/10/29）。
