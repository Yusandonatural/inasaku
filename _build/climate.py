# -*- coding: utf-8 -*-
"""気象庁「アメダス日別平年値(1991-2020年)」から、地点ごとの平年値ファイルを書き出す。

  climate/<観測所番号>.json … その地点の日別平年値(気温0.1℃・降水量0.1mm、366日ぶん)
  amedas-chiten-data.html    … 地点マスタ(都道府県|地点名,緯度,経度,標高,観測所番号;…)

使い方:
  1. 気象庁の平年値ダウンロードページから normal_amedas_daily.zip を取得して展開
     https://www.data.jma.go.jp/stats/data/mdrr/normal/
  2. 日平均気温(要素0500)と日合計降水量(要素4000)の行だけを集める
       grep -h -E '^25,[ 0-9]+, *(0500|4000),' area*/*.csv > extract.txt
  3. python3 climate.py extract.txt jma_station_active.csv

日別平年値が30年ぶん揃っていない地点(新設・移設された観測所)は、計算できないので外します。
"""
import csv, io, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT  = os.path.join(ROOT, "climate")
MST  = os.path.join(ROOT, "amedas-chiten-data.html")
DIM  = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
OFF  = [0]
for _d in DIM[:-1]:
    OFF.append(OFF[-1] + _d)

# 観測所番号の上2桁 → 都道府県(北海道は支庁)
AREA = {"11":"宗谷","12":"上川","13":"留萌","14":"石狩","15":"空知","16":"後志","17":"オホーツク",
        "18":"根室","19":"釧路","20":"十勝","21":"胆振","22":"日高","23":"渡島","24":"檜山",
        "31":"青森","32":"秋田","33":"岩手","34":"宮城","35":"山形","36":"福島","40":"茨城",
        "41":"栃木","42":"群馬","43":"埼玉","44":"東京","45":"千葉","46":"神奈川","48":"長野",
        "49":"山梨","50":"静岡","51":"愛知","52":"岐阜","53":"三重","54":"新潟","55":"富山",
        "56":"石川","57":"福井","60":"滋賀","61":"京都","62":"大阪","63":"兵庫","64":"奈良",
        "65":"和歌山","66":"岡山","67":"広島","68":"島根","69":"鳥取","71":"徳島","72":"香川",
        "73":"愛媛","74":"高知","81":"山口","82":"福岡","83":"大分","84":"長崎","85":"佐賀",
        "86":"熊本","87":"宮崎","88":"鹿児島","91":"沖縄","92":"沖縄","93":"沖縄","94":"沖縄"}
ORDER = ["宗谷","上川","留萌","石狩","空知","後志","オホーツク","根室","釧路","十勝","胆振","日高",
         "渡島","檜山","青森","秋田","岩手","宮城","山形","福島","茨城","栃木","群馬","埼玉","東京",
         "千葉","神奈川","長野","山梨","静岡","愛知","岐阜","三重","新潟","富山","石川","福井",
         "滋賀","京都","大阪","兵庫","奈良","和歌山","岡山","広島","島根","鳥取","徳島","香川",
         "愛媛","高知","山口","福岡","大分","長崎","佐賀","熊本","宮崎","鹿児島","沖縄"]


def read_normals(path):
    """要素0500(日平均気温)と4000(日合計降水量)を、地点ごとの366日配列にする。"""
    T, P = {}, {}
    for line in io.open(path, encoding="utf-8", errors="replace"):
        f = [x.strip() for x in line.rstrip("\n").split(",")]
        if len(f) < 8:
            continue
        stn, el, mon, vals = f[1], f[2], int(f[6]), f[7:]
        tgt = T if el == "0500" else (P if el == "4000" else None)
        if tgt is None:
            continue
        arr = tgt.setdefault(stn, [None] * 366)
        for d in range(DIM[mon - 1]):
            i = d * 2
            if i + 1 >= len(vals):
                break
            if vals[i + 1] == "8" and vals[i] != "":       # RMK 8 = 平年値あり
                arr[OFF[mon - 1] + d] = int(vals[i])
    return T, P


def fill(a, need=360):
    """わずかな欠測を前後から線形で埋める。足りなければ None。"""
    if a is None or sum(1 for x in a if x is not None) < need:
        return None
    a = list(a)
    idx = [i for i, x in enumerate(a) if x is not None]
    for i in range(len(a)):
        if a[i] is not None:
            continue
        lo = max([j for j in idx if j < i], default=None)
        hi = min([j for j in idx if j > i], default=None)
        if lo is None:   a[i] = a[hi]
        elif hi is None: a[i] = a[lo]
        else:            a[i] = int(round(a[lo] + (a[hi] - a[lo]) * (i - lo) / float(hi - lo)))
    return a


def old_prefs():
    """既存の地点マスタから (地点名, 緯度, 経度) → 都道府県 を拾う(支庁の割り当てを保つため)。"""
    try:
        s = io.open(MST, encoding="utf-8").read()
        txt = re.search(r'<pre id="amd-data"[^>]*>(.*?)</pre>', s, re.S).group(1).strip()
    except Exception:
        return {}
    o = {}
    for blk in txt.split("~"):
        i = blk.find("|")
        if i <= 0:
            continue
        pref = blk[:i]
        for it in blk[i + 1:].split(";"):
            a = it.split(",")
            if len(a) >= 3:
                o[(a[0], round(float(a[1]), 3), round(float(a[2]), 3))] = pref
    return o


PAGE = '''<!doctype html>
<html lang="ja"><head><meta charset="utf-8"><title>アメダス地点データ</title></head>
<body>
<div style="max-width:760px;margin:0 auto;padding:24px 16px;font-family:sans-serif;line-height:1.9;color:#333">
<h2 style="font-size:18px;margin-bottom:10px">アメダス地点データ</h2>
<p style="font-size:14px">「自然栽培の米作り 一年目の教科書」の工程表ツールが読み込むデータです。気温を観測している現役のアメダス%d地点の、地点名・緯度・経度・標高・観測所番号。出典: 気象庁「地点データ」。</p>
<pre id="amd-data" style="white-space:pre-wrap;word-break:break-all;font-size:11px;color:#666">%s</pre>
</div>
</body></html>
'''


def main(extract, stations):
    T, P = read_normals(extract)
    rows = [r for r in csv.DictReader(io.open(stations, encoding="utf-8-sig"))
            if r["Temperature"] == "1" and r["End Date"] == "9999-99-99"]
    prefs = old_prefs()

    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    for f in os.listdir(OUT):
        if f.endswith(".json"):
            os.remove(os.path.join(OUT, f))

    by_area, skipped = {}, []
    for r in rows:
        no   = r["Station Number"]
        name = r["Station Name(Kanji)"]
        lat  = round(float(r["Latitude_Precipitation(degree)"]), 3)
        lon  = round(float(r["Longitude_Precipitation(degree)"]), 3)
        alt  = r["Altitude_Precipitation(m)"]
        t = fill(T.get(no))
        if t is None:
            skipped.append(no + " " + name)
            continue
        p = fill(P.get(no), need=300)
        io.open(os.path.join(OUT, no + ".json"), "w", encoding="utf-8").write(
            json.dumps({"t": t, "p": p}, separators=(",", ":")))
        pref = prefs.get((name, lat, lon)) or AREA.get(no[:2])
        if not pref:
            skipped.append(no + " " + name + "(都道府県不明)")
            os.remove(os.path.join(OUT, no + ".json"))
            continue
        by_area.setdefault(pref, []).append(
            "%s,%s,%s,%s,%s" % (name, ("%g" % lat), ("%g" % lon), alt, no))

    packed = "~".join(p + "|" + ";".join(by_area[p]) for p in ORDER if p in by_area)
    n = sum(len(v) for v in by_area.values())
    io.open(MST, "w", encoding="utf-8").write(PAGE % (n, packed))
    return n, skipped, len(packed)


if __name__ == "__main__":
    n, sk, ln = main(sys.argv[1], sys.argv[2])
    print("地点: %d ／ マスタ %d 文字 ／ climate/*.json を書き出しました" % (n, ln))
    print("平年値が足りず除外: %d" % len(sk))
    for s in sk:
        print("  -", s)
