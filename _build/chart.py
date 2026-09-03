# -*- coding: utf-8 -*-
"""単一系列のかんたんなSVGグラフ。値はすべて直接ラベルし、下に表も置く前提。"""


def _fmt(v, dec=0):
    s = ("%%.%df" % dec) % v
    a, _, b = s.partition(".")
    a = "{:,}".format(int(a))
    return a + ("." + b if b else "")


def bars(rows, unit, caption, sub, source, dec=0, h=250, highlight=None):
    """rows: [(label, value)] 上端を4px丸めた棒。ベースラインに接地。"""
    W, PADL, PADR, PADT, PADB = 720, 8, 8, 30, 40
    n = len(rows)
    vmax = max(r[1] for r in rows) * 1.18
    plotw = W - PADL - PADR
    ploth = h - PADT - PADB
    slot = plotw / n
    bw = min(slot * 0.52, 76)
    R = 4
    marks, labels, vals = [], [], []
    for i, (lab, v) in enumerate(rows):
        cx = PADL + slot * (i + 0.5)
        bh = max(R + 0.5, ploth * (v / vmax))
        x, y = cx - bw / 2, PADT + ploth - bh
        cls = "c-bar"
        op = ' opacity=".42"' if (highlight is not None and i not in highlight) else ""
        d = ("M%.1f %.1f V%.1f a%d %d 0 0 1 %d -%d H%.1f a%d %d 0 0 1 %d %d V%.1f Z"
             % (x, PADT + ploth, y + R, R, R, R, R, x + bw - R, R, R, R, R, PADT + ploth))
        marks.append('<path class="%s" d="%s"%s><title>%s: %s%s</title></path>'
                     % (cls, d, op, lab, _fmt(v, dec), unit))
        vals.append('<text class="c-val" x="%.1f" y="%.1f" text-anchor="middle">%s</text>'
                    % (cx, y - 7, _fmt(v, dec)))
        parts = lab.split("\n")
        tsp = "".join('<tspan x="%.1f" dy="%s">%s</tspan>' % (cx, "0" if k == 0 else "1.35em", p)
                      for k, p in enumerate(parts))
        labels.append('<text class="c-axis" y="%.1f" text-anchor="middle">%s</text>'
                      % (h - PADB + 18, tsp))
    base = '<line class="c-grid" x1="%d" y1="%.1f" x2="%d" y2="%.1f"/>' % (PADL, PADT + ploth, W - PADR, PADT + ploth)
    svg = ('<svg viewBox="0 0 %d %d" role="img" aria-label="%s">%s%s%s%s</svg>'
           % (W, h, caption, base, "".join(marks), "".join(vals), "".join(labels)))
    return _fig(caption, sub, unit, svg, source)


def line(points, unit, caption, sub, source, dec=0, h=250, label_every=1):
    """points: [(label, value)] 折れ線＋面。"""
    W, PADL, PADR, PADT, PADB = 720, 26, 26, 34, 40
    vs = [p[1] for p in points]
    vmax, vmin = max(vs) * 1.14, 0
    plotw, ploth = W - PADL - PADR, h - PADT - PADB
    n = len(points)
    xs = [PADL + (plotw * i / (n - 1)) for i in range(n)]
    ys = [PADT + ploth - ploth * ((v - vmin) / (vmax - vmin)) for v in vs]
    pl = " ".join("%.1f,%.1f" % (x, y) for x, y in zip(xs, ys))
    area = "M%.1f,%.1f L%s L%.1f,%.1f Z" % (xs[0], PADT + ploth, pl.replace(",", " ").replace(" ", " ") if False else pl, xs[-1], PADT + ploth)
    area = "M%.1f %.1f " % (xs[0], PADT + ploth) + " ".join("L%.1f %.1f" % (x, y) for x, y in zip(xs, ys)) + " L%.1f %.1f Z" % (xs[-1], PADT + ploth)
    g = []
    for k in range(3):
        gy = PADT + ploth * k / 2.0
        g.append('<line class="c-grid" x1="%d" y1="%.1f" x2="%d" y2="%.1f"/>' % (PADL - 6, gy, W - PADR + 6, gy))
    dots, vals, labs = [], [], []
    for i, ((lab, v), x, y) in enumerate(zip(points, xs, ys)):
        dots.append('<circle class="c-dot" cx="%.1f" cy="%.1f" r="4.5"><title>%s: %s%s</title></circle>' % (x, y, lab, _fmt(v, dec), unit))
        if i % label_every == 0 or i == n - 1:
            anc = "start" if i == 0 else ("end" if i == n - 1 else "middle")
            dx = 4 if i == 0 else (-4 if i == n - 1 else 0)
            vals.append('<text class="c-val" x="%.1f" y="%.1f" text-anchor="%s">%s</text>' % (x + dx, y - 12, anc, _fmt(v, dec)))
            labs.append('<text class="c-axis" x="%.1f" y="%.1f" text-anchor="%s">%s</text>' % (x + dx, h - PADB + 20, anc, lab))
    svg = ('<svg viewBox="0 0 %d %d" role="img" aria-label="%s">%s<path class="c-area" d="%s"/>'
           '<polyline class="c-line" points="%s"/>%s%s%s</svg>'
           % (W, h, caption, "".join(g), area, pl, "".join(dots), "".join(vals), "".join(labs)))
    return _fig(caption, sub, unit, svg, source)


def _fig(caption, sub, unit, svg, source):
    return ('<figure class="chart"><figcaption>%s</figcaption>'
            '<div class="csub">単位：%s%s</div>%s<div class="c-src">%s</div></figure>'
            % (caption, unit, ("／" + sub if sub else ""), svg, source))
