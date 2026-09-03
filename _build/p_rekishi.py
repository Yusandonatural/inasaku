# -*- coding: utf-8 -*-
import shell, chart

BODY_TOP = '''
<section class="pagehead"><div class="wrap">
<div class="kicker">HISTORY</div>
<h1>日本の稲作の歴史</h1>
<p>いまあたりまえに見える田んぼの風景は、三千年ちかい試行錯誤の積み重ねです。自然栽培は「昔に戻る」ことではありませんが、農薬も化学肥料もなかった時代に人が何をどうやっていたかを知っておくと、自分の田んぼで起きることの見え方が変わります。</p>
</div></section>

<section class="band"><div class="wrap read">

<div class="note"><b>この年表の読み方</b>年代には研究者のあいだで見解が分かれるものがあります。特に稲作の伝来時期は、いまも決着していません。対立がある箇所は両方の説を併記しました。出典のないことは書いていません。</div>

<ul class="tl">

<li class="major">
<div class="era">紀元前10世紀 または 紀元前5世紀ごろ</div>
<h4>稲作が九州北部に伝わる — 年代は決着していない</h4>
<p>国立歴史民俗博物館は、AMS炭素14年代測定にもとづき「紀元前10世紀ごろに九州北部で水田稲作が始まった」とし、弥生時代を紀元前10世紀から紀元前3世紀までの約700年としています。約600年後には、水田稲作を受け入れる地域と受け入れない地域に大きく分かれたとも述べています。</p>
<p>一方この新説には異論があります。従来の定説はおよそ紀元前500年ごろで、歴博が2003年に発表した「定説より約500年古い」とする説に対し、考古学会や考古学者から異議が唱えられました。批判の論拠は、基礎データを示さない発表のしかたと、測定結果への<b>海洋リザーバー効果</b>の影響です。</p>
<p>公的機関のあいだでも年代観は揃っていません。吉野ヶ里歴史公園（佐賀県）は紀元前8世紀に北部九州で水稲耕作が始まったとし、弥生時代を紀元前5世紀から紀元後3世紀としています。</p>
<p class="src">出典：<a href="https://www.rekihaku.ac.jp/exhibitions/room1/" target="_blank" rel="noopener">国立歴史民俗博物館</a>／<a href="https://nihonkodaishi.net/special/maruchi/beginning_of_the_yayoi-period.html" target="_blank" rel="noopener">従来説と批判の整理</a>／<a href="https://www.yoshinogari.jp/introduction/remains/" target="_blank" rel="noopener">吉野ヶ里歴史公園</a></p>
</li>

<li>
<div class="era">縄文晩期〜弥生早期</div>
<h4>菜畑遺跡（佐賀県唐津市）— 日本最古級の水田</h4>
<p>縄文時代晩期から弥生時代中期にかけて、数期にわたる変遷が確認されています。最下層からは縄文時代晩期後半の土器が出土しました。水田は<b>土を盛った畦や矢板列によって区画</b>され、水路と井堰をともなっていました。木製・石製の農具が炭化米とともに見つかっています。</p>
<p>つまり最初期の水田稲作は、すでに「区画して水を張り、水の出入りを人が制御する」という現代とおなじ骨格を持っていました。</p>
<p class="src">出典：<a href="https://www.city.karatsu.lg.jp/uploaded/attachment/17396.pdf" target="_blank" rel="noopener">唐津市 菜畑遺跡</a></p>
</li>

<li>
<div class="era">弥生時代</div>
<h4>登呂遺跡と石包丁 — 穂を一本ずつ摘む</h4>
<p>登呂遺跡（静岡市）では8万平方メートルを超える水田跡が見つかっています。静岡市立登呂博物館は約2000年前の弥生時代後期としています。</p>
<p>当時の収穫具が<b>石包丁</b>です。半月形か三日月形の石に刃をつけ、手首に通す穴を二つ開けたもの。「弥生時代の稲は熟成時期がばらばら」だったため、熟れた穂だけを選んで刈る穂首刈りに使われました。品種が揃っていない稲を相手にする道具です。吉野ヶ里からは炭化米と竪杵が出ています。</p>
<p class="src">出典：<a href="https://www.shizuoka-toromuseum.jp/toro-site/about-torosite/" target="_blank" rel="noopener">静岡市立登呂博物館</a>／<a href="https://saga-museum.jp/museum/report/museum-diary/2020/10/003463.html" target="_blank" rel="noopener">佐賀県立博物館 石包丁</a></p>
</li>

<li>
<div class="era">7世紀後半〜平安時代</div>
<h4>条里制 — 田んぼが四角くなる</h4>
<p>1町（約109m）四方の区画を1坪とし、坪を横に6個並べて1里、縦に6個並べて1条とする土地区画制度です。7世紀後半に班田収授の法が始まり、奈良・平安時代に本格化しました。平安時代の水田遺構では一辺5〜20mの区画が確認されています。</p>
<p class="src">出典：<a href="https://gunmaibun.org/faq/faq_09" target="_blank" rel="noopener">群馬県埋蔵文化財調査事業団</a></p>
</li>

<li>
<div class="era">鎌倉〜室町時代</div>
<h4>二毛作が広がる</h4>
<p>鎌倉時代に米のあとに麦をつくる二毛作が畿内・西日本へ普及し、室町時代には東日本を含む全国へ広がりました。田んぼを一年に二度使う技術です。</p>
<p class="src">出典：<a href="https://842351c386.clvaw-cdnwnd.com/490aa9ffcf12cc31a1faf4c344d75607/200000308-a3ba6a3ba8/%E6%97%A5%E6%9C%AC%E5%8F%B2%E3%80%88%E4%B8%AD%E4%B8%96%E7%A4%BE%E4%BC%9A%E7%B5%8C%E6%B8%88%E5%8F%B2%E3%80%89%E3%83%86%E3%82%AD%E3%82%B9%E3%83%88%E7%B7%A8.pdf" target="_blank" rel="noopener">日本史（中世社会経済史）テキスト</a></p>
</li>

<li class="major">
<div class="era">江戸時代</div>
<h4>耕地が100年で倍近くに — そして『農業全書』</h4>
<p>豊臣秀吉のころ約150万町歩だった全国の耕地面積は、100年後の元禄のころには2倍近い約300万町歩に増えました。国立国会図書館のレファレンス（速水融編『日本経済史1』岩波書店 1997）では、1598年の太閤検地で田畑206万5000〜230万町、享保・延享期（1716-48）に約297万町、1873年の地租改正で323万4000町とされています。</p>
<p>元禄10年（1697年）には宮崎安貞の<b>『農業全書』</b>が京都で出版されました。序文は貝原益軒。150種以上の作物を収録し、著者が福岡西郊で40年暮らした実践にもとづいています。日本で最初の体系的な農書です。</p>
<p>この時代の除草は、すべて人の手でした。幕藩は優良品種の持ち出しを禁じており、品種は藩ごとに囲い込まれていました。</p>
<p class="src">出典：<a href="https://suido-ishizue.jp/daichi/part1/02/05.html" target="_blank" rel="noopener">水土の礎</a>／<a href="https://crd.ndl.go.jp/reference/entry/index.php?page=ref_view&amp;id=1000261399" target="_blank" rel="noopener">国立国会図書館 レファレンス協同データベース</a>／<a href="https://www.zck.or.jp/site/column-article/33073.html" target="_blank" rel="noopener">『農業全書』解説</a></p>
</li>

<li class="major">
<div class="era">明治期</div>
<h4>在来品種の黄金時代 — 神力・愛国・亀の尾・旭</h4>
<p>いまも自然栽培でよく使われる在来品種は、この時期に篤農家が田んぼで見つけ、選び抜いたものです。育種家ではなく、農家が主役でした。</p>
<div class="tbl-wrap"><table>
<caption>明治期に選抜された主な在来品種</caption>
<thead><tr><th>品種</th><th class="num">年</th><th>育成者・場所</th></tr></thead>
<tbody>
<tr><td class="name">神力</td><td class="num">1877年</td><td>兵庫県・丸尾重次郎</td></tr>
<tr><td class="name">愛国</td><td class="num">1882年</td><td>静岡県・高橋安兵衛が選出。1892年に宮城県で命名</td></tr>
<tr><td class="name">亀の尾</td><td class="num">1893年</td><td>山形県・阿部亀治</td></tr>
<tr><td class="name">旭</td><td class="num">1908年</td><td>京都府・山本新次郎</td></tr>
</tbody></table></div>
<p>大正10年（1921年）には人工交配による<b>陸羽132号</b>が生まれます。母は愛国由来の陸羽20号、父は亀の尾4号。昭和4年から27年まで23年間、東北地方で作付第1位を保ちました。農家の選抜から、試験場の交配へと主役が移った節目です。</p>
<p class="src">出典：<a href="https://www.komenet.jp/pdf/chousa-rep_R01-1.pdf" target="_blank" rel="noopener">米穀安定供給確保支援機構「日本の在来稲とその現状」2019年12月</a></p>
</li>

<li>
<div class="era">1946年〜</div>
<h4>農地改革</h4>
<p>昭和21年（1946年）10月21日に自作農創設特別措置法が公布され、翌年12月29日に施行されました。小作地が耕作者のものになり、戦後の日本の農村の骨格ができます。</p>
<p class="src">出典：<a href="https://www.archives.go.jp/ayumi/kobetsu/s21_1946_05.html" target="_blank" rel="noopener">国立公文書館</a></p>
</li>

<li class="major">
<div class="era">1959年</div>
<h4>除草剤PCPの登場 — 田の草取りが消えた年</h4>
<p>これは自然栽培をやる人にとって、いちばん重い節目かもしれません。除草剤PCPが導入されたのは昭和34年（1959年）。それ以前の田の草取りは<b>「労働10回、時間50時間を超える重労働」</b>でした。10aあたりの数字です。</p>
<p>PCPは<b>全面積188万ヘクタール、全稲作の60%で採用</b>されました。ほとんど一夜にして、日本の田んぼから草取りという仕事が消えたことになります。PCPは魚毒性の問題から1962年以降に使用が制限され、1980年代に廃止されました。</p>
<p>自然栽培で除草にかかる時間の重さは、この歴史を知ると腑に落ちます。<a href="index.html#josou">チェーン除草や田車</a>でやっているのは、1959年に手放した仕事を引き受け直すことです。ただし当時とちがい、いまは深水管理や機械除草という技術の蓄積があります。</p>
<p class="src">出典：<a href="https://www.jataff.or.jp/senjin3/8.html" target="_blank" rel="noopener">日本植物調節剤研究協会</a></p>
</li>

<li class="major">
<div class="era">1956年</div>
<h4>コシヒカリが生まれる</h4>
<p>父「農林1号」、母「農林22号」から1956年に誕生。いまもうるち米の作付第1位で<b>35.0%</b>を占めます（上位20品種で約8割）。日本の田んぼの3枚に1枚がコシヒカリという状態が、半世紀以上つづいています。</p>
<p class="src">出典：<a href="https://www.naro.go.jp/laboratory/tarc/rice_faq/variety/025108.html" target="_blank" rel="noopener">農研機構</a>／<a href="https://www.komenet.jp/pdf/chousa-rep_R01-1.pdf" target="_blank" rel="noopener">米穀機構</a></p>
</li>

<li>
<div class="era">1942年 → 1995年 → 2018年</div>
<h4>食糧管理法から減反の廃止まで</h4>
<p>食糧管理法は1942年に制定され、1995年に廃止されて主要食糧法（新食糧法）に移りました。生産調整、いわゆる減反は1971年に始まり、平成30年（2018年）から行政による生産数量目標の配分が廃止され、産地・生産者が中心となって需要に応じた生産を行う仕組みへ変わりました。</p>
<p class="src">出典：<a href="https://www.maff.go.jp/j/council/seisaku/kikaku/bukai/03/pdf/ref_data2-4.pdf" target="_blank" rel="noopener">農林水産省</a>／<a href="https://www.maff.go.jp/j/wpaper/w_maff/r1/r1_h/trend/part1/chap3/c3_4_00.html" target="_blank" rel="noopener">令和元年度 食料・農業・農村白書</a></p>
</li>

</ul>

<h2 class="rule">自然農法・有機農業の系譜</h2>

<p>農薬と化学肥料が普及していく、まさにその同じ時代に、それを使わない農のかたちを模索した人たちがいました。</p>

<ul class="tl">
<li>
<div class="era">1935年 / 1950年</div>
<h4>岡田茂吉 — 「無肥料栽培」から「自然農法」へ</h4>
<p>1935年に無農薬・無肥料の栽培を始め、昭和25年（1950年）に「無肥料栽培」から「自然農法」へと呼び名を改めました。1953年には自然農法普及会を設立しています。</p>
</li>
<li class="major">
<div class="era">1947年 / 1975年</div>
<h4>福岡正信 — 『わら一本の革命』</h4>
<p>1947年、<b>不耕起・無肥料・無農薬・無除草</b>の四大原則にもとづく農法を始めました。1975年9月に柏樹社から『自然農法 わら一本の革命』を刊行（1983年5月に春秋社から新版）。世界各国語に訳され、日本発の農法思想として最も広く読まれた一冊です。</p>
<p>この教科書の品種一覧にある<b>ハッピーヒル</b>は、福岡正信が育成した品種です。</p>
</li>
<li>
<div class="era">1971年</div>
<h4>日本有機農業研究会 結成</h4>
<p>一楽照雄が結成趣意書を起草しました。「有機農業」という言葉が日本で使われはじめた起点にあたります。</p>
</li>
<li>
<div class="era">2006年 / 2021年</div>
<h4>有機農業推進法、そしてみどりの食料システム戦略</h4>
<p>2006年12月、有機農業推進法が議員立法として制定されました。2021年5月には、みどりの食料システム戦略が策定されます。2050年に有機農業を耕地面積の25%（100万ha）へ、化学農薬を50%低減、化学肥料を30%低減という目標です。</p>
<p>ただし現状は<a href="genjou.html">耕地面積の0.8%</a>。目標との距離は30倍あります。</p>
</li>
</ul>

<p class="src">出典：<a href="https://ja.wikipedia.org/wiki/%E8%87%AA%E7%84%B6%E8%BE%B2%E6%B3%95" target="_blank" rel="noopener">自然農法</a>／<a href="https://ja.wikipedia.org/wiki/%E7%A6%8F%E5%B2%A1%E6%AD%A3%E4%BF%A1" target="_blank" rel="noopener">福岡正信</a>（この2項目のみ、公的資料に該当記述が見つからず二次情報を用いています）／<a href="https://www.1971joaa.org/%E6%9C%AC%E4%BC%9A%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6/" target="_blank" rel="noopener">日本有機農業研究会</a>／<a href="https://www.agri.kagoshima-u.ac.jp/wpo/wp-content/uploads/2022/06/yuuki-202206.pdf" target="_blank" rel="noopener">鹿児島大学 有機農業に関する資料</a></p>

<div class="warnbox"><b>調べきれなかったこと</b>川口由一・木村秋則の活動年、そして「自然栽培」という語がいつごろから使われるようになったかについては、公的・学術的な出典を見つけられませんでした。有機JAS制度の開始年も、確たる一次資料に到達できていません。分かりしだい追記します。</div>

<h2 class="rule">数字で見る、この百年</h2>

<p>技術の進歩がなにをもたらしたかは、二つの数字にはっきり出ています。</p>

'''

BODY_BTM = '''
<p>収量は明治16年の178kg/10aから令和2年の531kg/10aへ、およそ3倍になりました。同じ面積から3倍の米が穫れるようになったということです。いっぽう労働時間は、昭和55年の64.4時間/10aから平成27年の23.0時間へ、3分の1近くまで減りました。1959年以前は<b>草取りだけで50時間を超えていた</b>ことを思えば、減り方の大半は除草剤が担ったことになります。</p>

<div class="tip"><b>自然栽培をやるということ</b>この二つのグラフの、下向きの矢印を自分で押し戻すのが自然栽培です。労働時間は増え、収量はおそらく落ちます。それでも選ぶ理由があるとすれば、穫れる米の質か、田んぼという場所との関わり方か、その両方でしょう。数字の上では不利だという事実を、はじめに正面から見ておいたほうが長続きします。</p></div>

<p class="src">出典：<a href="https://agrin.jp/hp/kome/library/r03pdf/12.pdf" target="_blank" rel="noopener">山形県 農業関係資料（全国値）</a>／<a href="https://www.maff.go.jp/j/seisan/ryutu/zikamaki/z_genzyo/pdf/01.pdf" target="_blank" rel="noopener">農林水産省 労働時間</a>／<a href="https://www.jataff.or.jp/project/inasaku/koen/koen_h28_1.pdf" target="_blank" rel="noopener">日本植物調節剤研究協会 講演資料</a>。1950年代の労働時間は公的統計での具体値を確認できませんでした。</p>

<h2 class="rule">次に読む</h2>
{next}

</div></section>
'''


def build():
    c1 = chart.bars(
        [("明治16年\n1883", 178), ("令和2年\n2020", 531)],
        "kg", "10aあたりの収量", "全国値",
        '出典：<a href="https://agrin.jp/hp/kome/library/r03pdf/12.pdf" target="_blank" rel="noopener">山形県 農業関係資料</a>', h=210)
    c2 = chart.bars(
        [("昭和55年\n1980", 64.4), ("平成18年\n2006", 27.96), ("平成27年\n2015", 23.0)],
        "時間", "10aあたりの労働時間", "全国平均",
        '出典：<a href="https://www.maff.go.jp/j/seisan/ryutu/zikamaki/z_genzyo/pdf/01.pdf" target="_blank" rel="noopener">農林水産省</a>／<a href="https://www.jataff.or.jp/project/inasaku/koen/koen_h28_1.pdf" target="_blank" rel="noopener">日本植物調節剤研究協会</a>',
        dec=1, h=210)
    nxt = shell.nextnav([
        ("DATA", "日本の稲作の現状", "genjou.html"),
        ("VARIETY", "自然栽培に向く品種", "hinshu.html"),
        ("START", "教科書トップに戻る", "index.html"),
    ])
    body = BODY_TOP + c1 + c2 + BODY_BTM.replace("{next}", nxt)
    return shell.page("rekishi.html", "日本の稲作の歴史｜" + shell.SITE,
                      "稲作の伝来から条里制、江戸の新田開発、明治の在来品種、1959年の除草剤PCP導入、そして自然農法の系譜まで。出典つきの年表で、いまの田んぼがどう出来上がったかをたどります。",
                      body)
