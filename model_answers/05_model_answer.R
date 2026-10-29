# ============================================================
# 行動計量学（行動科学分析法入門）
# 第5回　データの加工(1)：dplyr　演習1〜3　模範解答
#
# 使い方：全選択（Ctrl + A）→ Ctrl + Enter（Macは Cmd + A → Cmd + Enter）
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


# ------------------------------------------------------------
# 演習2：select() の練習
#   動物名・食性・総睡眠時間・体重の4列だけを選ぶ
# ------------------------------------------------------------

msleep_small <- msleep |>
  select(name, vore, sleep_total, bodywt)

msleep_small

# 列の順番は書いた順になります。
# 「この4列以外を捨てる」と書くこともできます（結果は同じではありません。
#  下は列の並びが元のままになります）。
#   msleep |> select(name, vore, sleep_total, bodywt)


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

# awake は「24 - sleep_total」なので，awake_ratio が大きい動物は
# そのまま睡眠時間が短い動物です。上位は キリン（0.92）・ゴンドウクジラ・ウマ・
# ノロジカ・ロバ の順で，大型の動物が並びます。
