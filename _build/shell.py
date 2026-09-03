# -*- coding: utf-8 -*-
"""共通の枠（ヘッダー・ヒーロー・フッター）。各ページはこれを使って組み立てる。"""

SITE = "自然栽培の米作り 一年目の教科書"
BASE = "https://yusandonatural.github.io/inasaku/"
BMC = "__BMC_ID__"   # Buy Me a Coffee のユーザー名が決まったら置換する

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

# 原案のオリジナルSVG。棚田を重ねた曲線の帯と、低い陽。
HERO_ART = '''<svg class="hero-art" viewBox="0 0 1440 300" preserveAspectRatio="xMidYMax slice" aria-hidden="true" focusable="false">
<defs>
<linearGradient id="t1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3f7a52"/><stop offset="1" stop-color="#356847"/></linearGradient>
<linearGradient id="t2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2f6644"/><stop offset="1" stop-color="#28563a"/></linearGradient>
<linearGradient id="t3" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#245034"/><stop offset="1" stop-color="#1b3e28"/></linearGradient>
<linearGradient id="t4" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#17361f"/><stop offset="1" stop-color="#0e2716"/></linearGradient>
<linearGradient id="wat" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#f0d789" stop-opacity=".00"/><stop offset=".5" stop-color="#f0d789" stop-opacity=".34"/><stop offset="1" stop-color="#f0d789" stop-opacity=".00"/></linearGradient>
</defs>
<circle cx="1128" cy="70" r="46" fill="#f0d789" opacity=".92"/>
<circle cx="1128" cy="70" r="86" fill="#f0d789" opacity=".10"/>
<path d="M0 118 C210 92 372 130 566 122 C782 113 936 74 1140 88 C1268 97 1360 112 1440 108 L1440 300 L0 300Z" fill="url(#t1)"/>
<path d="M0 122 C210 96 372 134 566 126 C782 117 936 78 1140 92 C1268 101 1360 116 1440 112" fill="none" stroke="url(#wat)" stroke-width="2.4"/>
<path d="M0 166 C186 142 350 178 560 166 C784 153 950 122 1156 136 C1276 144 1364 158 1440 154 L1440 300 L0 300Z" fill="url(#t2)"/>
<path d="M0 170 C186 146 350 182 560 170 C784 157 950 126 1156 140 C1276 148 1364 162 1440 158" fill="none" stroke="url(#wat)" stroke-width="2.2"/>
<path d="M0 214 C168 194 344 226 552 212 C782 197 966 168 1172 182 C1288 190 1370 202 1440 198 L1440 300 L0 300Z" fill="url(#t3)"/>
<path d="M0 218 C168 198 344 230 552 216 C782 201 966 172 1172 186 C1288 194 1370 206 1440 202" fill="none" stroke="url(#wat)" stroke-width="1.8"/>
<path d="M0 262 C150 246 348 272 546 260 C778 246 980 218 1188 230 C1298 236 1374 246 1440 242 L1440 300 L0 300Z" fill="url(#t4)"/>
<g stroke="#f0d789" stroke-width="1.5" stroke-linecap="round" opacity=".5" fill="none">
<path d="M92 300v-42"/><path d="M92 268c-9-6-13-15-13-24 8 3 13 12 13 24Z" fill="#f0d789" stroke="none" opacity=".55"/>
<path d="M92 278c9-6 13-16 13-25-8 3-13 13-13 25Z" fill="#f0d789" stroke="none" opacity=".55"/>
<path d="M126 300v-32"/><path d="M126 276c-7-5-10-12-10-19 6 2 10 9 10 19Z" fill="#f0d789" stroke="none" opacity=".45"/>
<path d="M1338 300v-38"/><path d="M1338 272c8-5 12-14 12-22-7 3-12 11-12 22Z" fill="#f0d789" stroke="none" opacity=".45"/>
</g>
</svg>'''


def nav(page):
    out = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == page else ""
        out.append('<a href="%s"%s>%s</a>' % (href, cur, label))
    return '<nav class="navlinks" aria-label="サイト内">' + "".join(out) + "</nav>"


def topbar(page):
    return ('<header class="topbar"><div class="topbar-in">'
            '<a class="brand" href="index.html">%s<span class="txt">一年目の教科書</span></a>%s'
            '</div></header>' % (MARK, nav(page)))


SUPPORT = '''<section class="band alt"><div class="wrap read">
<div class="support-box">
<h3>この教科書は無料で公開しています</h3>
<p>取材・データ整備・ツールの開発と更新は、すべて自費でやっています。役に立ったと感じていただけたら、コーヒー一杯分から応援していただけると励みになります。いただいたぶんは、品種データの拡充とサーバー費用にあてます。</p>
<a class="bmc" href="https://www.buymeacoffee.com/{bmc}" target="_blank" rel="noopener noreferrer"><span>☕</span><span>コーヒーを一杯おごる</span></a>
<p class="support-note">Buy Me a Coffee のページへ移動します（別タブで開きます）。<br>もちろん、応援なしでもすべての内容をお使いいただけます。</p>
</div>
</div></section>'''.replace("{bmc}", BMC)


FOOT = '''<footer class="sitefoot"><div class="wrap">
<div class="foot-grid">
<div>
<h4>この教科書について</h4>
<p style="margin:0">農薬・化学肥料・除草剤を使わない米づくりの道しるべ。一年目の方が、田んぼ探しから稲刈りまでを一人でやりきれることを目指してまとめています。</p>
</div>
<div>
<h4>ページ</h4>
<ul>%s</ul>
</div>
<div>
<h4>発行</h4>
<ul>
<li><a href="https://yusando.com" target="_blank" rel="noopener">株式会社悠三堂</a></li>
<li><a href="https://yusando.com/pages/inasaku-kyokasho" target="_blank" rel="noopener">悠三堂サイト内の同ページ</a></li>
<li><a href="https://github.com/Yusandonatural/inasaku" target="_blank" rel="noopener">ソースコード（GitHub）</a></li>
</ul>
</div>
</div>
<div class="foot-btm">
<p class="disclaimer" style="margin:0">本サイトに掲載している作業時期・日数・出穂予定日・収穫予定日・収量・費用などの数値は、一般的な知見と公開されている統計に基づく<b>目安</b>であり、正確性・完全性を保証するものではありません。実際の生育は、地域・ほ場の条件・品種・種子の由来・その年の気象によって大きく変動します。作業にあたっては、ご自身のほ場の観察を最優先とし、必要に応じて地域の農業普及指導センター・JA・経験ある生産者にもご相談ください。掲載価格は調査時点のもので、変動します。</p>
<p style="margin:14px 0 0">© 株式会社悠三堂</p>
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
           site=SITE, extra=extra_head, top=topbar(key), body=body, support=SUPPORT, foot=FOOT)
    return html
