# ============================================================
# 行動計量学（行動科学分析法入門）
# 第6回　データの加工(2)：集計と要約統計量　演習1〜3　模範解答
#
# 使い方：全選択（Ctrl + A）→ Ctrl + Enter（Macは Cmd + A → Cmd + Enter）
# ============================================================

library(tidyverse)


# ------------------------------------------------------------
# 演習1：グループ別集計
#   種ごとに Petal.Length の平均・標準偏差・サンプルサイズ
# ------------------------------------------------------------

iris |>
  group_by(Species) |>
  summarise(
    n    = n(),
    mean = mean(Petal.Length),
    sd   = sd(Petal.Length)
  )

# 結果（小数第2位まで）
#   setosa      n = 50   mean = 1.46   sd = 0.17
#   versicolor  n = 50   mean = 4.26   sd = 0.47
#   virginica   n = 50   mean = 5.55   sd = 0.55
#
# n() は「そのグループの行数」を数える関数で，中に何も書きません。
# どの種も50本ずつなので，サンプルサイズの偏りはありません。
# 一方でSDは setosa だけ極端に小さく，3倍以上の開きがあります。
# （このばらつきの違いは第13回でもう一度出てきます）


# ------------------------------------------------------------
# 演習2：集計結果のグラフ化（エラーバー付き棒グラフ）
# ------------------------------------------------------------

# まず集計
petal_summary <- iris |>
  group_by(Species) |>
  summarise(
    mean_petal = mean(Petal.Length),
    sd_petal   = sd(Petal.Length)
  )

petal_summary

# グラフ
ggplot(petal_summary, aes(x = Species, y = mean_petal, fill = Species)) +
  geom_col() +
  geom_errorbar(aes(ymin = mean_petal - sd_petal,
                    ymax = mean_petal + sd_petal), width = 0.2) +
  labs(title = "種ごとの花びらの長さ（平均±SD）",
       x = "種", y = "花びらの長さ (cm)") +
  theme_bw()

# geom_col() は「集計済みの値をそのまま高さにする」ための関数です。
# geom_bar() は自分で数えてしまうので，ここでは使いません。
#
# エラーバーが何を表すかは，図を見せる前に決めて明記してください。
#   ±SD   … データそのもののばらつき（今回）
#   ±SE   … 平均値の推定の不確かさ（SD / sqrt(n)）
#   95%CI … 平均値の信頼区間
# 同じ図でも幅がまったく変わるので，書かないと読めません。


# ------------------------------------------------------------
# 演習3：count() の応用
#   食性（vore）ごとのサンプルサイズを多い順に。NA は除く
# ------------------------------------------------------------

msleep |>
  filter(!is.na(vore)) |>
  count(vore, sort = TRUE)

# 結果
#   herbi 32 ／ omni 20 ／ carni 19 ／ insecti 5   （合計76）
#
# filter(!is.na(vore)) を忘れると NA が5番目のカテゴリとして7件出てきます。
# 下と見比べてください。
msleep |>
  count(vore, sort = TRUE)

# sort = TRUE は「n の多い順に並べる」指定です。付けないと vore の順（アルファベット順）
# になります。count() は group_by() + summarise(n = n()) の近道です。
