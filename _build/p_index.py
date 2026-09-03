# -*- coding: utf-8 -*-
"""index.html にヒーローと共通ヘッダー／フッターをかぶせる。
   工程表ツールの中身（#inasaku-kyokasho）はそのまま残す。"""
import io, os, re
import shell

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, "index.html")

HERO = '''<section class="hero">
<div class="hero-in">
<div class="eyebrow">◎ 農薬・化学肥料・除草剤 不使用</div>
<h1>一年目から、<br>ちゃんとお米は<span class="accent">穫れます</span>。</h1>
<p class="sub">自然栽培で米を一年つくりきるための教科書です。田んぼ探しから種籾の準備、代かき、除草、稲刈りまで。最寄りのアメダス観測地点を選べば、その土地の実測気温から、あなたの田んぼの作業暦をつくります。</p>
<div class="hero-cta">
<a class="btn btn-p" href="#tool">工程表をつくる</a>
<a class="btn btn-g" href="sagyou.html">作業の手順を読む</a>
</div>
<div class="hero-stats">
<div><b>916</b><span>連動するアメダス地点</span></div>
<div><b>13</b><span>工程の解説</span></div>
<div><b>28</b><span>品種の適性判定</span></div>
<div><b>5年</b><span>実測気温で計算</span></div>
</div>
</div>
''' + shell.HERO_ART + '''
</section>

<section class="band"><div class="wrap">
<div class="sec-head">
<div class="kicker">CONTENTS</div>
<h2>知りたいところから読んでください</h2>
<p>順番に読む必要はありません。まず工程表をつくって自分の田んぼの日付を出し、そこから必要なページに飛ぶのが早道です。</p>
</div>
<div class="grid g3">
<a class="card" href="#tool"><span class="ico">📅</span><h3>工程表をつくる</h3><p>最寄りのアメダス地点・品種・田植え日を選ぶと、もみまきから秋起こしまでの予定日が並びます。印刷とカレンダー取り込みに対応。</p><span class="more">つくる →</span></a>
<a class="card" href="sagyou.html"><span class="ico">🌱</span><h3>作業の手順</h3><p>13の工程を、目的・手順・コツ・つまずきやすい点の順に。塩水選から稲刈りの適期判断まで。</p><span class="more">読む →</span></a>
<a class="card" href="hinshu.html"><span class="ico">🌾</span><h3>品種を選ぶ</h3><p>28品種を出穂期・積算温度・耐冷性・いもち病抵抗性で比較。その土地の気温で登熟しきる品種の選び方。</p><span class="more">選ぶ →</span></a>
<a class="card" href="nouki.html"><span class="ico">🛠</span><h3>農機具と予算</h3><p>1反なら約9万円、3反で約84万円。実売価格と中古相場、そして借りて済ませる方法。</p><span class="more">見積もる →</span></a>
<a class="card" href="genjou.html"><span class="ico">📊</span><h3>日本の稲作の現状</h3><p>作付面積・担い手・米価・生産費。令和の米騒動と2026年の価格反落まで、公的統計で。</p><span class="more">知る →</span></a>
<a class="card" href="rekishi.html"><span class="ico">📜</span><h3>日本の稲作の歴史</h3><p>稲作の伝来から1959年の除草剤導入、そして自然農法の系譜まで。出典つきの年表。</p><span class="more">たどる →</span></a>
</div>
</div></section>
'''


def build():
    s = io.open(P, encoding="utf-8").read()

    # すでに適用済みなら何もしない
    if 'class="topbar"' in s:
        return None

    # 1) 共通CSSを読み込む
    s = s.replace('<style>html,body{margin:0;padding:0;background:#f7f9f6;}</style>',
                  '<link rel="stylesheet" href="assets/site.css">')

    # 2) ヘッダーとヒーローを本文の先頭に差し込む
    s = s.replace('<body>\n<div id="inasaku-kyokasho">',
                  '<body>\n' + shell.topbar("index.html") + "\n" + HERO + '\n<div id="inasaku-kyokasho">')

    # 3) 断片が持っていた旧ヘッダーは、ヒーローと重複するので隠す
    s = s.replace('<div class="app-head">', '<div class="app-head" hidden>')

    # 4) 断片の旧フッターは隠し、共通フッターを </body> の直前に置く
    s = s.replace('<div class="app-foot">', '<div class="app-foot" hidden>')
    assert "class=\"support-box\"" not in s, "応援セクションが重複します"
    s = s.replace("</body>", shell.SUPPORT + "\n" + shell.FOOT + "\n</body>")

    io.open(P, "w", encoding="utf-8").write(s)
    return len(s)
