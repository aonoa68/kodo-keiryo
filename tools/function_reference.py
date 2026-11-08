# -*- coding: utf-8 -*-
"""各回の「この回で使った関数」の表の素。

  関数名: (すること, （）の中に入れるもの, 表に出す例, 実行して確かめる式)

4つめが None のときは、3つめの例をそのまま実行して確かめる。
例を直したら tools/verify_examples.R で実行確認し、
tools/build_function_tables.py で各 .Rmd の表を作り直してから
全16本を再レンダリングすること。
"""

FUNCTIONS = {
    'library': (
        'パッケージを読み込む',
        'パッケージ名。**引用符なし**',
        'library(tidyverse)',
        None),
    'install.packages': (
        'パッケージを入れる（最初の1回だけ）',
        'パッケージ名。**引用符あり**（`library()` と逆）',
        'install.packages("tidyverse")',
        'TRUE'),
    'c': (
        '複数の値を1つに束ねる',
        '束ねたい値を `,` で並べる',
        'c(85, 72, 91)',
        None),
    'summary': (
        '要約を表示する',
        'データフレーム，または分析結果',
        'summary(iris)',
        None),
    'str': (
        'データの構造（型と中身）を表示する',
        'データフレーム',
        'str(iris)',
        None),
    'glimpse': (
        '列名・型・中身をざっと見る',
        'データフレーム',
        'glimpse(msleep)',
        None),
    'head': (
        '先頭の数行を取り出す',
        'データ, 行数（省略すると6行）',
        'head(iris, 3)',
        None),
    'nrow': (
        '行数を数える',
        'データ',
        'nrow(msleep)',
        None),
    'ncol': (
        '列数を数える',
        'データ',
        'ncol(msleep)',
        None),
    'length': (
        '要素の個数を数える',
        'ベクトル（列）',
        'length(iris$Sepal.Length)',
        None),
    'print': (
        '結果を表示する。行数を指定できる',
        'データ, `n = 行数`（`n = Inf` で全行）',
        'print(msleep, n = Inf)',
        None),
    'View': (
        'RStudioで表として開く',
        'データ（**V は大文字**）',
        'View(msleep)',
        'TRUE'),
    'help': (
        'ヘルプを出す（`?` と同じ）',
        '関数名，または `package = "パッケージ名"`',
        'help(package = "ggplot2")',
        'TRUE'),
    'example': (
        'ヘルプの Examples を実行する',
        '関数名',
        'example(sd)',
        'TRUE'),
    'saveRDS': (
        '結果を1つファイルに保存する',
        '保存するもの, ファイル名',
        'saveRDS(result, "result.rds")',
        'saveRDS(iris, file.path(tempdir(), "x.rds"))'),
    'readRDS': (
        '保存した結果を読み込む',
        'ファイル名',
        'readRDS("result.rds")',
        '{f <- file.path(tempdir(), "y.rds"); saveRDS(iris, f); readRDS(f)}'),
    'display.brewer.all': (
        'ColorBrewerの色の組を一覧表示する',
        '**何も入れません**',
        'display.brewer.all()',
        'RColorBrewer::display.brewer.all()'),
    'is.na': (
        '欠損値かどうか調べる',
        '列。`!is.na()` で「欠損でない」',
        'filter(msleep, is.na(vore))',
        None),
    'mean': (
        '平均',
        '数値の列。欠損があるときは `na.rm = TRUE`',
        'mean(iris$Sepal.Length)',
        None),
    'sd': (
        '標準偏差',
        '数値の列。欠損があるときは `na.rm = TRUE`',
        'sd(iris$Sepal.Length)',
        None),
    'var': (
        '分散',
        '数値の列',
        'var(iris$Sepal.Length)',
        None),
    'median': (
        '中央値',
        '数値の列',
        'median(iris$Petal.Length)',
        None),
    'min': (
        '最小値',
        '数値の列',
        'min(msleep$sleep_total)',
        None),
    'max': (
        '最大値',
        '数値の列',
        'max(msleep$sleep_total)',
        None),
    'sum': (
        '合計',
        '数値の列',
        'sum(iris$Sepal.Length)',
        None),
    'sqrt': (
        '平方根',
        '数値',
        'sqrt(16)',
        None),
    'round': (
        '四捨五入する',
        '数値, 桁数（省略すると整数）',
        'round(3.14159, 2)',
        None),
    'scale': (
        '平均0・標準偏差1に標準化する',
        '数値の列。**行列が返る**点に注意',
        'scale(iris$Sepal.Length)',
        None),
    'rep': (
        '同じ値をくり返す',
        'くり返す値, `each =` または `times =`',
        'rep(1:3, each = 2)',
        None),
    'numeric': (
        '数値を入れる空の入れ物を作る',
        '長さ（個数）',
        'numeric(10)',
        None),
    'seq_along': (
        '1から長さまでの連番を作る',
        'ベクトル',
        'seq_along(c(5, 8, 2))',
        None),
    'paste': (
        '文字列をつなげる',
        'つなげる値。`sep =` で区切り文字',
        'paste("A", "B", sep = "-")',
        None),
    'factor': (
        'カテゴリ（水準つき）に変える',
        '元の列, `levels =`（順序）, `labels =`（表示名）',
        'factor(mtcars$am, labels = c("AT", "MT"))',
        None),
    'matrix': (
        '数値を行列の形に並べる',
        '値, `nrow =`, `byrow = TRUE`（横に詰める）',
        'matrix(c(16, 4, 10, 10), nrow = 2, byrow = TRUE)',
        None),
    'list': (
        '複数のものをまとめて1つにする',
        'まとめたいもの',
        'list(c("A群", "B群"), c("はい", "いいえ"))',
        None),
    'tibble': (
        '表をその場で作る',
        '`列名 = 値` を並べる',
        'tibble(id = 1:3, score = c(5, 7, 9))',
        None),
    'as.data.frame': (
        'データフレームに変換する',
        '表や行列',
        'as.data.frame(table(mtcars$cyl))',
        None),
    'unname': (
        '名前（ラベル）を外す',
        '名前の付いた値',
        'unname(c(a = 1, b = 2))',
        None),
    'rownames': (
        '行の名前を取り出す',
        '行列・データフレーム',
        'rownames(mtcars)',
        None),
    'set.seed': (
        '乱数を毎回同じにする',
        '整数（何でもよい）',
        'set.seed(123)',
        None),
    'rnorm': (
        '正規分布の乱数を作る',
        '個数, `mean =`（既定0）, `sd =`（既定1）',
        'rnorm(50, mean = 10, sd = 2)',
        None),
    'system.time': (
        '実行にかかった時間を測る',
        '測りたい処理',
        'system.time(mean(1:1000000))',
        None),
    'lm': (
        '回帰直線を当てはめる',
        '`y ~ x` の形の式',
        'lm(Petal.Length ~ Sepal.Length, data = iris)',
        None),
    'aggregate': (
        'グループごとに集計する（R本体の関数）',
        '`値 ~ グループ`, `data =`, `FUN =`',
        'aggregate(weight ~ group, data = PlantGrowth, FUN = mean)',
        None),
    'where': (
        '型で列を選ぶ',
        '判定する関数（`is.numeric` など）',
        'across(where(is.numeric), mean)',
        'mtcars |> summarise(across(where(is.numeric), mean))'),
    'read.csv': (
        'CSVファイルを読み込む（R本体の関数）',
        'ファイルのパス。`read_csv()` と違い，空欄は欠損にならない',
        'read.csv("msleep.csv")',
        '{f <- file.path(tempdir(), "t.csv"); write.csv(head(iris), f, row.names = FALSE); read.csv(f)}'),
    'read_csv': (
        'CSVファイルを読み込む',
        'ファイルのパス（引用符あり）。文字化けには `locale =`',
        'read_csv("data/my_data.csv")',
        'TRUE'),
    'locale': (
        '文字コードなどの読み取り設定',
        '`encoding = "CP932"` など',
        'locale(encoding = "CP932")',
        None),
    'read_excel': (
        'Excelファイルを読み込む',
        'ファイルのパス, `sheet =`（シート名か番号）',
        'read_excel("data/my_data.xlsx", sheet = 1)',
        'TRUE'),
    'filter': (
        '**行**を絞り込む',
        'データ, 残す行の条件。`,` で並べると「かつ」',
        'filter(msleep, sleep_total >= 12)',
        None),
    'select': (
        '**列**を選ぶ',
        'データ, 残す列名。頭に `-` で除外',
        'select(msleep, name, vore)',
        None),
    'mutate': (
        '列を作る・書き換える',
        'データ, `新しい列名 = 計算式`',
        'mutate(msleep, sleep_min = sleep_total * 60)',
        None),
    'arrange': (
        '並び替える',
        'データ, 基準にする列。降順は `desc()` で包む',
        'arrange(msleep, desc(sleep_total))',
        None),
    'desc': (
        '降順にする',
        '列名（`arrange()` の中だけ）',
        'arrange(msleep, desc(bodywt))',
        None),
    'starts_with': (
        'その文字で始まる列を選ぶ',
        '文字列（`select()` の中だけ）',
        'select(msleep, starts_with("sleep"))',
        None),
    'everything': (
        '残りの全部の列',
        '**何も入れません**',
        'select(msleep, name, everything())',
        None),
    'group_by': (
        'グループに分ける',
        'データ, 分ける基準の列',
        'group_by(msleep, vore)',
        None),
    'summarise': (
        'グループごとに1行にまとめる',
        'データ, `新しい列名 = 集計の式`',
        'summarise(msleep, 平均 = mean(sleep_total))',
        None),
    'n': (
        'そのグループの件数',
        '**何も入れません**（`n()` と書く）',
        'summarise(msleep, 件数 = n())',
        None),
    'count': (
        '件数を数えて表にする',
        'データ, 数える基準の列',
        'count(msleep, vore)',
        None),
    'across': (
        '複数の列に同じ処理をかける',
        '列の選び方, かける関数',
        'across(where(is.numeric), mean)',
        'mtcars |> summarise(across(where(is.numeric), mean))'),
    'pull': (
        '1列をベクトルとして取り出す',
        'データ, 列名',
        'pull(mtcars, mpg)',
        None),
    'pivot_longer': (
        '横長の表を縦長にする',
        'データ, `cols =`, `names_to =`, `values_to =`',
        'pivot_longer(d, cols = c(before, after), names_to = "時点", values_to = "値")',
        None),
    'pivot_wider': (
        '縦長の表を横長にする',
        'データ, `names_from =`, `values_from =`',
        'pivot_wider(dl, names_from = 時点, values_from = 値)',
        None),
    'ggplot': (
        'グラフの土台を作る',
        '`data =` データ, `aes()` で軸の割り当て',
        'ggplot(iris, aes(x = Sepal.Length, y = Petal.Length))',
        None),
    'aes': (
        '列をグラフの要素に割り当てる',
        '`x =`, `y =`, `color =`, `fill =` など',
        'aes(x = Species, y = Petal.Length)',
        'ggplot(iris, aes(x = Species, y = Petal.Length))'),
    'geom_point': (
        '点を描く（散布図）',
        '`size =`・`color =` など見た目（省略可）',
        'geom_point(size = 2)',
        'gp + geom_point(size = 2)'),
    'geom_jitter': (
        '点を少しずらして描く（重なり防止）',
        '`width =`, `height =`',
        'geom_jitter(width = 0.1)',
        'gb + geom_jitter(width = 0.1)'),
    'geom_histogram': (
        'ヒストグラムを描く',
        '`binwidth =` か `bins =`（**省略すると30本**で注意が出る）',
        'geom_histogram(binwidth = 0.3)',
        'gh + geom_histogram(binwidth = 0.3)'),
    'geom_boxplot': (
        '箱ひげ図を描く',
        '見た目の指定（省略可）',
        'geom_boxplot()',
        'gb + geom_boxplot()'),
    'geom_bar': (
        '件数を数えて棒グラフにする',
        '`y` は書かない（Rが数える）',
        'geom_bar()',
        'ggplot(iris, aes(Species)) + geom_bar()'),
    'geom_col': (
        '値をそのまま棒の高さにする',
        '`aes(y = 値)` が必要',
        'geom_col()',
        'ggplot(ms, aes(vore, m)) + geom_col()'),
    'geom_errorbar': (
        'エラーバーを描く',
        '`aes(ymin =, ymax =)`, `width =`',
        'geom_errorbar(aes(ymin = m - s, ymax = m + s), width = 0.2)',
        'ggplot(ms, aes(vore, m)) + geom_col() + geom_errorbar(aes(ymin = m - s, ymax = m + s), width = 0.2)'),
    'geom_smooth': (
        '回帰直線・曲線を重ねる',
        '`method = "lm"` で直線。`se = FALSE` で帯を消す（既定は出る）',
        'geom_smooth(method = "lm", se = FALSE)',
        'gp + geom_smooth(method = "lm", se = FALSE)'),
    'geom_line': (
        '点を線で結ぶ',
        '`aes(group =)` でどれを結ぶか',
        'geom_line(aes(group = id))',
        'ggplot(dl, aes(時点, 値)) + geom_line(aes(group = id))'),
    'geom_hline': (
        '横線を引く',
        '`yintercept =`（線の高さ）',
        'geom_hline(yintercept = 0)',
        'gp + geom_hline(yintercept = 0)'),
    'stat_summary': (
        '集計した値を図に描く',
        '`fun =`（集計関数）, `geom =`（描き方）',
        'stat_summary(fun = mean, geom = "point")',
        'gb + stat_summary(fun = mean, geom = "point")'),
    'labs': (
        'タイトルや軸ラベルを付ける',
        '`title =`, `x =`, `y =`, `color =`, `fill =`',
        'labs(title = "花びらの長さ", x = "種", y = "長さ (cm)")',
        'gb + labs(title = "花びらの長さ", x = "種", y = "長さ (cm)")'),
    'theme_bw': (
        '白地に枠線の見た目にする',
        '**何も入れません**（`base_family =` でフォント指定可）',
        'theme_bw()',
        'gp + theme_bw()'),
    'theme_minimal': (
        '枠線を減らした見た目にする',
        '**何も入れません**',
        'theme_minimal()',
        'gp + theme_minimal()'),
    'theme_classic': (
        '軸だけの見た目にする',
        '**何も入れません**',
        'theme_classic()',
        'gp + theme_classic()'),
    'theme_dark': (
        '暗い背景の見た目にする',
        '**何も入れません**',
        'theme_dark()',
        'gp + theme_dark()'),
    'theme': (
        '細かい見た目を個別に変える',
        '`axis.text = element_text(...)` など',
        'theme(axis.text = element_text(size = 12))',
        'gp + theme(axis.text = element_text(size = 12))'),
    'element_text': (
        '文字の設定',
        '`size =`, `family =`, `angle =`',
        'element_text(size = 12, angle = 45)',
        'gp + theme(axis.text = element_text(size = 12, angle = 45))'),
    'scale_color_brewer': (
        '点や線の色をColorBrewerの組にする',
        '`palette = "Dark2"` など',
        'scale_color_brewer(palette = "Dark2")',
        'gc + scale_color_brewer(palette = "Dark2")'),
    'scale_fill_brewer': (
        '塗りつぶしの色をColorBrewerの組にする',
        '`palette = "Set2"` など',
        'scale_fill_brewer(palette = "Set2")',
        'gf + scale_fill_brewer(palette = "Set2")'),
    'scale_color_manual': (
        '点や線の色を自分で決める',
        '`values = c(...)`',
        'scale_color_manual(values = c("#1B9E77", "#D95F02", "#7570B3"))',
        'gc + scale_color_manual(values = c("#1B9E77", "#D95F02", "#7570B3"))'),
    'scale_fill_manual': (
        '塗りつぶしの色を自分で決める',
        '`values = c(...)`',
        'scale_fill_manual(values = c("#66C2A5", "#FC8D62", "#8DA0CB"))',
        'gf + scale_fill_manual(values = c("#66C2A5", "#FC8D62", "#8DA0CB"))'),
    'scale_x_discrete': (
        'x軸の目盛りの表示を変える',
        '`labels = c(...)`',
        'scale_x_discrete(labels = c("セトサ", "バーシ", "バージ"))',
        'gb + scale_x_discrete(labels = c("セトサ", "バーシ", "バージ"))'),
    'facet_wrap': (
        'グループごとに図を分ける',
        '`~ 列名`',
        'facet_wrap(~ Species)',
        'gp + facet_wrap(~ Species)'),
    'coord_flip': (
        '縦と横を入れ替える',
        '**何も入れません**',
        'coord_flip()',
        'gb + coord_flip()'),
    'ggsave': (
        '図をファイルに保存する',
        'ファイル名, `width =`, `height =`, `dpi =`（既定300）。図を省くと直前の図',
        'ggsave("plot.png", width = 6, height = 4)',
        'ggsave(file.path(tempdir(), "plot.png"), plot = gp, width = 6, height = 4)'),
    'table': (
        '度数を数えてクロス表を作る',
        '1つまたは2つの列',
        'table(mtcars$cyl, mtcars$am)',
        None),
    'xtabs': (
        '式でクロス表を作る',
        '`~ 列 + 列`, `data =`',
        'xtabs(~ cyl + am, data = mtcars)',
        None),
    'prop.table': (
        '度数を割合に直す',
        '表, `1`（行ごと）か `2`（列ごと）',
        'prop.table(tab, 1)',
        None),
    'cor': (
        '相関係数を計算する',
        '2つの数値の列。欠損は `use = "complete.obs"`',
        'cor(iris$Sepal.Length, iris$Petal.Length)',
        None),
    'cor.test': (
        '相関係数の検定',
        '2つの数値の列',
        'cor.test(iris$Sepal.Length, iris$Petal.Length)',
        None),
    'chisq.test': (
        'カイ二乗検定',
        'クロス表。2×2では既定で連続性の補正が入る（`correct = FALSE` で外す）',
        'chisq.test(tab)',
        None),
    'fisher.test': (
        'フィッシャーの正確確率検定',
        'クロス表',
        'fisher.test(tab)',
        None),
    't.test': (
        't検定',
        '`数値 ~ グループ, data =` または2つの列。既定は**ウェルチ**。対応ありは `paired = TRUE`',
        't.test(mpg ~ am, data = mtcars)',
        None),
    'var.test': (
        '2群の分散が等しいかの検定',
        '2つの数値の列',
        'var.test(mpg ~ am, data = mtcars)',
        None),
    'aov': (
        '分散分析をする',
        '`数値 ~ グループ`, `data =`',
        'aov(weight ~ group, data = PlantGrowth)',
        None),
    'anova': (
        '結果を分散分析表にする',
        '`aov()` や `lm()` の結果',
        'anova(lm(weight ~ group, data = PlantGrowth))',
        None),
    'oneway.test': (
        '等分散を仮定しない一元配置分散分析',
        '`数値 ~ グループ`, `data =`, `var.equal =`',
        'oneway.test(weight ~ group, data = PlantGrowth)',
        None),
    'bartlett.test': (
        '等分散性を検定する',
        '`数値 ~ グループ`, `data =`',
        'bartlett.test(weight ~ group, data = PlantGrowth)',
        None),
    'shapiro.test': (
        '正規性を検定する',
        '数値の列',
        'shapiro.test(PlantGrowth$weight)',
        None),
    'TukeyHSD': (
        '多重比較（Tukey法）',
        '`aov()` の結果',
        'TukeyHSD(aov(weight ~ group, data = PlantGrowth))',
        None),
    'pairwise.t.test': (
        '総当たりのt検定',
        '数値の列, グループ, `p.adjust.method =`（既定 `"holm"`）',
        'pairwise.t.test(PlantGrowth$weight, PlantGrowth$group)',
        None),
}

# 表に載せない（knitr の設定やコピーボタンの実装で出てくるだけのもの）
NOISE = ['cat', 'file.exists', 'for', 'function', 'geom_xxx', 'if', 'readLines', 'requireNamespace', 'return', 'set', 'while']
