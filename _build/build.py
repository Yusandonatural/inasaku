# -*- coding: utf-8 -*-
import io, os, sys, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODS = ["p_genjou", "p_rekishi", "p_nouki", "p_hinshu", "p_sagyou"]
FILES = {"p_genjou":"genjou.html","p_rekishi":"rekishi.html","p_nouki":"nouki.html",
         "p_hinshu":"hinshu.html","p_sagyou":"sagyou.html"}
for m in MODS:
    if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), m+".py")):
        print("  skip", m); continue
    mod = importlib.import_module(m)
    html = mod.build()
    p = os.path.join(OUT, FILES[m])
    io.open(p, "w", encoding="utf-8").write(html)
    print("  %-14s %7d 文字" % (FILES[m], len(html)))
