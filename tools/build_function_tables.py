# -*- coding: utf-8 -*-
"""各回の .Rmd にある「この回で使った関数」の節を作り直す。

使い方（リポジトリ直下で）:
    python3 tools/build_function_tables.py

そのあと docs/materials で全16本を再レンダリングすること。
関数の説明・例は tools/function_reference.py にある。
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from function_reference import FUNCTIONS, NOISE          # noqa: E402

MATERIALS = os.path.join(os.path.dirname(HERE), "docs", "materials")
LESSONS = ["01", "02", "03", "04", "05", "06", "07",
           "08", "09", "10", "11", "12", "13", "14", "15"]
HEADING = "## この回で使った関数"

PIPE_NOTE = """
パイプ `|>` は関数ではなく記号です。`データ |> 関数()` と書くと，
データがその関数の**1つめの（）の中身**として渡されます。
"""

# 第5回だけ、dplyr の引用符の話を添える
QUOTE_BOX = """
> **引用符を付けるか迷ったら**
>
> - **列名そのもの**を指すとき … 引用符**なし**（`select(name)`，`arrange(sleep_total)`）
> - **中身の値**と比べるとき … 文字なら引用符**あり**（`filter(vore == "carni")`）
> - 数値と比べるときは引用符なし（`filter(sleep_total >= 12)`）
"""


def functions_in(text):
    """出てくる順に関数名を返す。

    実行するチャンク ```{r} と、実行しないコード例 ```r の両方を見る。
    引用ブロック（行頭の >）の中にあるものも拾う。
    """
    plain = re.sub(r"(?m)^(\s*)>\s?", r"\1", text)
    blocks = re.findall(r"^\s*```\{r[^}]*\}\n(.*?)^\s*```", plain, re.S | re.M)
    blocks += re.findall(r"^\s*```r\n(.*?)^\s*```", plain, re.S | re.M)
    code = "\n".join(blocks)
    code = re.sub(r"#.*", "", code)              # コメントを外す
    code = re.sub(r'"[^"\n]*"', '""', code)      # 文字列の中身を外す
    found, seen = [], set()
    for m in re.finditer(r"\b([A-Za-z.][A-Za-z0-9._]*)\s*\(", code):
        name = m.group(1)
        if name in NOISE or name in seen:
            continue
        seen.add(name)
        found.append(name)
    return found


def section_for(key, text):
    names = functions_in(text)
    unknown = [n for n in names if n not in FUNCTIONS]
    if unknown:
        raise SystemExit(
            f"{key}.Rmd: tools/function_reference.py に無い関数: {unknown}")

    sample = next((n for n in names if n not in ("library", "help", "example")),
                  "mean")
    link = "#help" if key == "02" else "02.html#help"
    rows = "\n".join(
        "| `{0}()` | {1} | {2} | `{3}` |".format(n, *FUNCTIONS[n][:3])
        for n in names)

    return (
        HEADING + "\n\n"
        "出てきた順に並べています。**（）の中に何を入れるか**を確かめたいときに見てください。\n\n"
        "::: {.fn-table}\n\n"
        "| 関数 | すること | （）の中に入れるもの | 例 |\n|---|---|---|---|\n"
        + rows + "\n\n:::\n"
        + (PIPE_NOTE if "|>" in text else "")
        + (QUOTE_BOX if key == "05" else "")
        + f"\n> **もっと詳しく知りたいときは** `?関数名` と実行してください（例：`?{sample}`）。\n"
        + "> 右下の **Help** タブに，その関数の説明と，（）に書ける項目が全部出ます。\n"
        + f"> 読み方は **[第2回「ヘルプの読み方」]({link})** にまとめてあります。\n"
        + "\n---\n\n")


def main():
    for key in LESSONS:
        path = os.path.join(MATERIALS, key + ".Rmd")
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        block = section_for(key, text)

        if HEADING in text:                      # 既にある節を差し替える
            start = text.index(HEADING)
            m = re.search(r"\n## ", text[start + 5:])
            if m is None:
                raise SystemExit(f"{key}.Rmd: 節の終わりが見つからない")
            end = start + 5 + m.start() + 1
            text = text[:start] + block + text[end:]
        else:                                    # 「本日のまとめ」の前に入れる
            anchor = "## 本日のまとめ"
            if text.count(anchor) != 1:
                raise SystemExit(f"{key}.Rmd: 「本日のまとめ」が1つではない")
            text = text.replace(anchor, block + anchor)

        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"{key}.Rmd  {len(functions_in(text))} 関数")


if __name__ == "__main__":
    main()
