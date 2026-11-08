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


# ------------------------------------------------------------
# 演習4（発展）：自分の関心のあるデータで同じことをやる
# ------------------------------------------------------------

# この演習は「自分で選んだデータでやる」ものなので、唯一の正解はありません。
# ここでは例として penguins を選んだ場合を示します。
# 自分が選んだデータの名前と列名に読み替えて見てください。
# 手順は変わりません。変わるのはデータ名と列名だけです。

# どんなデータがあるかは data() で一覧が出ます。
#   data()
#   ?penguins          # 選んだデータの説明を読む
#   is.data.frame(penguins)   # TRUE ならこの演習に使えます

# penguins は R 4.5 以降に標準で入っているデータです（読み込み不要）。
# msleep と違い「ふつうのデータフレーム」なので、そのまま打つと344行流れます。
glimpse(penguins)


# 1. 種ごとに body_mass の件数・平均・標準偏差
penguins |>
  group_by(species) |>
  summarise(
    n    = n(),
    mean = mean(body_mass, na.rm = TRUE),
    sd   = sd(body_mass,   na.rm = TRUE)
  )

# 結果（四捨五入）
#   Adelie    152  3700.7  458.6
#   Chinstrap  68  3733.1  384.3
#   Gentoo    124  5076.0  504.1
#
# msleep のときと書き方は変わりません。列名とデータ名を入れ替えただけです。


# 2. エラーバー付きの棒グラフ
mass_summary <- penguins |>
  group_by(species) |>
  summarise(
    mean_mass = mean(body_mass, na.rm = TRUE),
    sd_mass   = sd(body_mass,   na.rm = TRUE)
  )

ggplot(mass_summary, aes(x = species, y = mean_mass, fill = species)) +
  geom_col() +
  geom_errorbar(aes(ymin = mean_mass - sd_mass, ymax = mean_mass + sd_mass),
                width = 0.2) +
  scale_fill_brewer(palette = "Set2") +
  labs(title = "ペンギンの種ごとの体重（平均±SD）",
       x = "種", y = "体重 (g)") +
  theme_bw()

# Gentoo だけ平均が 1.4kg ほど重く（5076g vs 3701g）、
# 平均±SD の範囲が Adelie・Chinstrap と重なりません。


# 3. 島ごとの件数を多い順に
penguins |>
  count(island, sort = TRUE)

# 結果   Biscoe 168 ／ Dream 124 ／ Torgersen 52


# 問1：なぜそのデータを選んだか
#      ここは人それぞれです。「ペンギンが好きだから」で構いません。
#      大事なのは、選んだあとに ?penguins を読んで
#      「何を、どうやって測ったデータなのか」を確かめることです。
#      penguins は、南極・パーマー諸島の3つの島で2007〜2009年に
#      測定された成鳥の記録です（Gorman, Williams & Fraser 2014）。
#      ?penguins にこの説明が書いてあります。


# 問2：欠損があったか。na.rm = TRUE の前と後でどう変わったか
#      penguins には body_mass に2件、sex に11件の欠損があります。
#      na.rm = TRUE を付けずに種ごとの平均を出すと、こうなります。
penguins |>
  group_by(species) |>
  summarise(mean = mean(body_mass))
#      Adelie NA ／ Chinstrap 3733.1 ／ Gentoo NA
#
#      3種のうち2種だけが NA になりました。なぜ Chinstrap だけ数値が出るのか
#      body_mass の欠損が2件あり、その2件がどちらも Chinstrap 以外の種だからです。
#      平均は、欠損が1つでも混ざると NA になります。裏を返すと、
#      欠損が1つも無いグループだけは数値が出ます。
#      確かめ方：
penguins |>
  group_by(species) |>
  summarise(欠損の数 = sum(is.na(body_mass)))
#      Adelie 1 ／ Chinstrap 0 ／ Gentoo 1
#
#      「一部のグループだけ NA」という出方をしたら、
#      そのグループに欠損が入っていると考えてください。


# 参考：sex ごとに集計すると現れる行
penguins |>
  group_by(sex) |>
  summarise(n = n(), mean = mean(body_mass, na.rm = TRUE))

#      female 165 ／ male 168 ／ <NA> 11 の3行が出ます。
#      <NA> の11件は「性別が記録されていない個体」で、第2節の msleep の
#      vore と同じです。group_by() は欠損を黙って捨てず、1つのグループとして見せます。
#      iris では全部の列が埋まっているので、この行は出ませんでした。


# 問3：グループごとの件数の差は何を表すか
#      例：「Biscoe島がいちばんペンギンの多い島」と言えるか
#      言えません。この168という数は「Biscoe島で調査された個体の数」であって、
#      島にいるペンギンの数ではありません。島ごとに何羽捕まえて測ったかは
#      調査する側の都合で決まります。
#      第3回で iris の3種がどれも50本ずつだったのと同じで、
#      件数は「自然界の割合」ではなく「データの取り方」を表しています。
