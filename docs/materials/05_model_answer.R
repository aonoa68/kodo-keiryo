# ============================================================
# 行動計量学（行動科学分析法入門）
# 第5回　データの加工(1)：dplyr　演習1〜3　模範解答
#
# 使い方：全選択（Ctrl + A）→ Ctrl + Enter（Macは Cmd + A → Cmd + Enter）
#
# ※ 実行すると，コンソールの表示が途中で切れます（「# ℹ 21 more rows」など）。
#    エラーではありません。読み方は資料の「4. filter()」の中の
#    「コンソールの表示の読み方」を見てください。
#    全部見たいときは，行の最後に |> print(n = Inf) を足します。
# ============================================================

library(tidyverse)

# 使うのは msleep（哺乳類の睡眠データ，83種）。ggplot2に付属しています。


# ------------------------------------------------------------
# 演習1：filter() の練習
# ------------------------------------------------------------

# 1. 雑食動物（vore == "omni"）だけ
msleep |>
  filter(vore == "omni")

# 2. 体重（bodywt）が 100 kg 以上
msleep |>
  filter(bodywt >= 100)

# 3. 草食（vore == "herbi"）かつ総睡眠時間（sleep_total）が 8 時間以上
msleep |>
  filter(vore == "herbi", sleep_total >= 8)

# 条件を2つ並べるときは , でつなぎます。& でも同じです。
#   filter(vore == "herbi" & sleep_total >= 8)

# 注意：vore には欠損値（NA）があります。
# vore == "omni" は，NAの行について TRUE でも FALSE でもなく NA を返すので，
# filter() はその行を落とします。つまり「NAの動物は結果に出てこない」ことになります。
sum(is.na(msleep$vore))   # 7件

# 問：欠損7件は，1 で取り出した雑食20件に入っていますか。
#     入っていません。vore が NA の行は vore == "omni" の判定が NA になり，
#     filter() は TRUE でない行を落とすためです。
#     「omni でない」という条件（vore != "omni"）でも同じく拾われません。
#     欠損だけを見たいときは filter(is.na(vore)) と書きます。
msleep |> filter(is.na(vore)) |> select(name, sleep_total)


# ------------------------------------------------------------
# 演習2：select() の練習
#   動物名・食性・総睡眠時間・体重の4列だけを選ぶ
# ------------------------------------------------------------

msleep_small <- msleep |>
  select(name, vore, sleep_total, bodywt)

msleep_small

# 逆に「要らない列を捨てる」書き方もできます（列名に - を付けます）。
msleep |>
  select(-genus, -order, -conservation, -sleep_rem, -sleep_cycle, -awake, -brainwt)

# 今回はどちらも同じ結果になります。元のデータでこの4列が
# name → vore → sleep_total → bodywt の順に並んでいるためです。
# select() は書いた順に列を並べるので，順番を変えたいときは正の指定を使います。
#   msleep |> select(bodywt, name)   # bodywt が先に来る


# ------------------------------------------------------------
# 演習3：mutate() の練習
#   覚醒時間の割合（awake / 24）の列を足し，大きい順に並べて上位10行
# ------------------------------------------------------------

msleep |>
  select(name, awake) |>
  mutate(awake_ratio = awake / 24) |>
  arrange(desc(awake_ratio)) |>
  head(10)

# arrange() は小さい順が既定なので，大きい順にするには desc() で包みます。
# desc() を忘れると「いちばんよく寝る動物」が並びます。見比べてみてください。
msleep |>
  select(name, awake) |>
  mutate(awake_ratio = awake / 24) |>
  arrange(awake_ratio) |>
  head(10)

# 問：上位に並ぶのはどんな動物ですか。sleep_total と見比べて気づいたことは。
#     awake はほぼ「24 - sleep_total」です（83件中81件が合計ちょうど24時間。
#     Pilot whale と Common porpoise の2件だけ24.05になっています）。
#     そのため awake_ratio が大きい動物は，そのまま睡眠時間が短い動物です。
#     上位は キリン（0.92）・ゴンドウクジラ・ウマ・ノロジカ・ロバ の順で，
#     大型の草食動物と海生の動物が並びます。
#     awake_ratio は sleep_total から決まる値なので，新しい情報は増えていません。
#     それでも「1日のうちどれだけ起きているか」という割合にすると，
#     動物どうしを比べやすくなります。
msleep |>
  select(name, sleep_total, awake) |>
  mutate(awake_ratio = awake / 24) |>
  arrange(desc(awake_ratio)) |>
  head(5)
