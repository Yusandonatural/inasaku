# -*- coding: utf-8 -*-
"""共通の枠（ヘッダー・ヒーロー・フッター）。各ページはこれを使って組み立てる。"""

SITE = "自然栽培の米作り 一年目の教科書"
TAGLINE = "家族で食べるお米を、自然栽培で作る。"

# 見出し用のしっぽり明朝（Google Fonts）
FONTS = ("""<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@400;600;700&display=swap">""")
BASE = "https://inasaku.yusando.com/"
BMC = "quietsheep"   # https://buymeacoffee.com/quietsheep

NAV = [
    ("index.html",   "教科書トップ"),
    ("sagyou.html",  "作業の手順"),
    ("hinshu.html",  "品種を選ぶ"),
    ("nouki.html",   "農機具と予算"),
    ("genjou.html",  "稲作の現状"),
    ("rekishi.html", "稲作の歴史"),
]

MARK = ('<svg class="mark" viewBox="0 0 32 32" aria-hidden="true">'
        '<circle cx="16" cy="16" r="15" fill="#265536"/>'
        '<path d="M16 25V12" stroke="#f0d789" stroke-width="1.8" stroke-linecap="round"/>'
        '<path d="M16 13c0-3.4 2.3-6 5.4-6.6C21.1 9.9 19 12.4 16 13Z" fill="#f0d789"/>'
        '<path d="M16 16c-3 0-5.3-2.3-5.8-5.4C13 11.2 15.2 13.2 16 16Z" fill="#8fc7a3"/>'
        '<path d="M16 19.5c3 0 5.3-2.3 5.8-5.4-2.8.6-5 2.6-5.8 5.4Z" fill="#8fc7a3"/>'
        '</svg>')

def nav(page):
    out = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == page else ""
        out.append('<a href="%s"%s>%s</a>' % (href, cur, label))
    return '<nav class="navlinks" aria-label="サイト内">' + "".join(out) + "</nav>"


def topbar(page):
    return ('<header class="topbar"><div class="topbar-in">'
            '<a class="brand" href="index.html">%s<span class="txt">一年目の教科書</span></a>'
            '<span class="bar-tag">%s</span>%s'
            '</div></header>' % (MARK, TAGLINE, nav(page)))


SUPPORT = '''<section class="supportband"><div class="wrap">
<p class="support-line">お役に立ったと思われた方は、ぜひ<a href="https://buymeacoffee.com/{bmc}" target="_blank" rel="noopener noreferrer">コーヒーを一杯ご馳走してください</a>。いただいたぶんは、品種データの拡充とサーバー費用にあてます。</p>
</div></section>'''.replace("{bmc}", BMC)


FOOT = '''<footer class="sitefoot"><div class="wrap">
<div class="foot-grid">
<div>
<h4>この教科書について</h4>
<p class="foot-tag">家族で食べるお米を、自然栽培で作る。</p>
<p style="margin:0">農薬・化学肥料・除草剤を使わない米づくりの道しるべ。一年目の方が、田んぼ探しから稲刈りまでを一人でやりきれることを目指してまとめています。</p>
</div>
<div>
<h4>ページ</h4>
<ul>%s</ul>
</div>
<div>
<h4>このサイトのもと</h4>
<ul>
<li><a href="https://www.youtube.com/watch?v=jaX9OwiZDI0" target="_blank" rel="noopener">動画版（YUSANDO CHANNEL）</a></li>
<li><a href="https://github.com/Yusandonatural/inasaku" target="_blank" rel="noopener">ソースコード（GitHub）</a></li>
</ul>
</div>
</div>
<div class="foot-btm">
<p class="disclaimer" style="margin:0">本サイトに掲載している作業時期・日数・出穂予定日・収穫予定日・収量・費用などの数値は、一般的な知見と公開されている統計に基づく<b>目安</b>であり、正確性・完全性を保証するものではありません。実際の生育は、地域・ほ場の条件・品種・種子の由来・その年の気象によって大きく変動します。作業にあたっては、ご自身のほ場の観察を最優先とし、必要に応じて地域の農業普及指導センター・JA・経験ある生産者にもご相談ください。掲載価格は調査時点のもので、変動します。</p>
<p style="margin:14px 0 0">© 自然栽培の米作り 一年目の教科書</p>
</div>
</div></footer>''' % "".join('<li><a href="%s">%s</a></li>' % (h, l) for h, l in NAV)


def nextnav(items):
    """items: [(kicker, title, href), ...]"""
    s = '<div class="nextnav">'
    for k, t, h in items:
        s += '<a href="%s"><div class="k">%s</div><div class="t">%s</div></a>' % (h, k, t)
    return s + "</div>"


def page(fname, title, desc, body, page_key=None, extra_head=""):
    key = page_key or fname
    html = '''<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{base}{fname}">
<meta property="og:type" content="article">
<meta property="og:url" content="{base}{fname}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:site_name" content="{site}">
<meta name="twitter:card" content="summary_large_image">
{fonts}
<link rel="stylesheet" href="assets/site.css">
{extra}
</head>
<body>
{top}
{body}
{support}
{foot}
</body>
</html>
'''.format(title=title, desc=desc, base=BASE, fname=("" if fname == "index.html" else fname),
           site=SITE, fonts=FONTS, extra=extra_head, top=topbar(key), body=body, support=SUPPORT, foot=FOOT)
    return html
