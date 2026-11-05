# -*- coding: utf-8 -*-
"""tools/function_reference.py に書いた「例」を全部Rで実行して、動くことを確かめる。

使い方（リポジトリ直下で）:
    python3 tools/verify_examples.py

失敗が0件でなければ、例を直すこと。
例を直したら、これを通してから build_function_tables.py を動かす。
"""
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from function_reference import FUNCTIONS          # noqa: E402

# 例の中で使う材料。ファイルやRStudioが要るものは実行式を "TRUE" にして飛ばす。
PREAMBLE = r'''
suppressMessages(library(tidyverse))
gp  <- ggplot(iris, aes(x = Sepal.Length, y = Petal.Length))
gb  <- ggplot(iris, aes(x = Species, y = Petal.Length))
gh  <- ggplot(iris, aes(x = Sepal.Length))
gc  <- ggplot(iris, aes(Sepal.Length, Petal.Length, color = Species))
gf  <- ggplot(iris, aes(Species, fill = Species))
ms  <- msleep |> filter(!is.na(vore)) |> group_by(vore) |>
  summarise(m = mean(sleep_total), s = sd(sleep_total))
tab <- table(mtcars$cyl, mtcars$am)
d   <- tibble(id = 1:3, before = c(5, 6, 7), after = c(7, 8, 9))
dl  <- d |> pivot_longer(cols = c(before, after),
                         names_to = "時点", values_to = "値")
x   <- rnorm(100)

fails <- character(0)
chk <- function(name, q) {
  r <- tryCatch({
    v <- suppressMessages(suppressWarnings(eval(q, envir = globalenv())))
    if (inherits(v, "ggplot")) invisible(ggplot_build(v))
    else invisible(capture.output(print(v)))
    "OK"
  }, error = function(e) paste("ERROR:", conditionMessage(e)))
  if (r != "OK") {
    fails <<- c(fails, name)
    cat(sprintf("  %-20s %s\n", name, r), file = stderr())
  }
}
'''

EPILOGUE = r'''
cat("\n==== 失敗:", length(fails), "件 ====\n", file = stderr())
if (length(fails)) quit(status = 1)
'''


def main():
    lines = [PREAMBLE]
    for name in sorted(FUNCTIONS):
        _, _, example, test = FUNCTIONS[name]
        code = example if test is None else test
        if code == "TRUE":          # ファイルやRStudioが要るので実行しない
            continue
        lines.append("chk(%s, quote(%s))" % (_r_string(name), code))
    lines.append(EPILOGUE)

    with tempfile.NamedTemporaryFile("w", suffix=".R", delete=False,
                                     encoding="utf-8") as fh:
        fh.write("\n".join(lines))
        path = fh.name
    try:
        r = subprocess.run(["Rscript", "--vanilla", path],
                           stdout=subprocess.DEVNULL)
        return r.returncode
    finally:
        os.unlink(path)


def _r_string(s):
    return '"%s"' % s.replace("\\", "\\\\").replace('"', '\\"')


if __name__ == "__main__":
    sys.exit(main())
