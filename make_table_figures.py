"""Render every Markdown table in paper_draft.md as a figure (PNG at 2x + SVG with text as outlines).
Cells are taken verbatim from the Markdown source; **bold** markup is rendered as bold and the asterisks removed.
Style matches make_header_figure.py. Output: results/table_NN_<slug>.png/.svg"""
import os, re, json, textwrap, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

_fonts = [f"/home/box/.fonts/InterStatic-{w}.ttf" for w in ("Regular", "SemiBold", "Bold")]
if all(os.path.exists(f) for f in _fonts):
    for f in _fonts: fm.fontManager.addfont(f)
    plt.rcParams["font.family"] = "InterStatic"
plt.rcParams["svg.fonttype"] = "path"
INK, MUTED, BG, BAND, RULE, ACCENT = "#141414", "#6b6b6b", "#FBFAF7", "#F0EDE6", "#BDB8AE", "#0072B2"

# Titles/subtitles per table, in paper order. The paper has no per-table captions; both tables sit under
# "## What we found" and share the note that follows them, so titles describe each table and the note is reused.
META = [
    ("stance-by-asker", "Average judged stance by who is asking (all five models)",
     "Mean judged stance on −3…+3 for each question, by asker framing, with the devout − atheist gap and its 95% interval"),
    ("gap-by-model", "The devout − atheist gap, model by model",
     "Mean judged stance for devout-framed minus atheist-framed answers, per model and question"),
]
SOURCE = ("n = 900 answers (5 models × 4 questions × 3 wordings × 3 askers × 5 samples), scored blind by 3 judge models · "
          "Nov 14–15, 2026 · No human audit · github.com/michaelbaird/tribe-in-the-machine")

def find_tables(md):
    L = md.split("\n"); out = []; i = 0
    while i < len(L) - 1:
        if L[i].startswith("|") and L[i + 1].startswith("|") and set(L[i + 1].replace("|", "").strip()) <= set("-: "):
            j = i
            while j < len(L) and L[j].startswith("|"): j += 1
            rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in L[i:j]]
            out.append({"start": i, "end": j, "header": rows[0], "rows": rows[2:]})
            i = j
        else: i += 1
    return out, L

def note_after(L, end):
    for l in L[end:end + 16]:  # the shared note below both tables
        if l.startswith("#"): break
        if l.startswith("*Gap ="):
            t = l.strip().strip("*")
            return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)
    return None

def render(tab, idx, slug, title, sub, note):
    hdr, rows = tab["header"], tab["rows"]
    W = 14.56; fs, hfs = 16.5, 13.5
    fig = plt.figure(figsize=(W, 4), dpi=200, facecolor=BG)
    r = fig.canvas.get_renderer()
    def width_in(s, bold=False, size=fs):
        t = fig.text(0, 0, s, fontsize=size, fontweight="bold" if bold else "normal"); bb = t.get_window_extent(r); t.remove()
        return bb.width / fig.dpi
    cells = [[(re.sub(r"\*\*(.+?)\*\*", r"\1", c), "**" in c) for c in row] for row in rows]
    pad = 0.32
    colw = [max(width_in(c[k][0], c[k][1]) for c in cells) + pad for k in range(len(hdr))]
    avail = W - 0.9
    if sum(colw) > avail: raise SystemExit(f"table {idx} too wide ({sum(colw):.2f} in)")
    # spend spare width first on letting headers sit on one line, then share the rest equally
    def hparts(h):  # a header with a bracketed note goes on two lines: label / [note]
        return h.replace(" [", "\n[").split("\n")
    need = [max(0, max(width_in(x, True, hfs) for x in hparts(h)) + pad - colw[k]) for k, h in enumerate(hdr)]
    spare = avail - sum(colw)
    if sum(need) <= spare: colw = [c + n for c, n in zip(colw, need)]
    extra = (avail - sum(colw)) / len(colw); colw = [c + extra for c in colw]
    def wrap(h, maxw):  # greedy word wrap of a header against its final column width
        out, cur = [], ""
        for wd in h.split():
            t = (cur + " " + wd).strip()
            if cur and width_in(t, True, hfs) + pad > maxw: out.append(cur); cur = wd
            else: cur = t
        return out + [cur]
    hdr_lines = [sum((wrap(x, colw[k]) for x in hparts(h)), []) for k, h in enumerate(hdr)]
    rowh, hdrh = 0.62, 0.42 * max(len(x) for x in hdr_lines) + 0.25
    note_lines = textwrap.wrap(note, 150) if note else []
    H = 1.55 + hdrh + rowh * len(rows) + 0.3 * len(note_lines) + 0.75
    fig.set_size_inches(W, H)
    X0 = 0.45
    def fx(x): return x / W
    def fy(y): return 1 - y / H          # y measured in inches from top
    fig.text(fx(X0), fy(0.72), title, fontsize=26, fontweight="bold", color=INK)
    fig.text(fx(X0), fy(1.15), sub, fontsize=14, color=MUTED)
    y = 1.55
    ax = fig.add_axes([0, 0, 1, 1], facecolor="none"); ax.set_xlim(0, W); ax.set_ylim(H, 0); ax.axis("off")
    ax.plot([X0, X0 + avail], [y, y], color=INK, lw=1.6)
    x = X0
    for k, lines in enumerate(hdr_lines):
        ha = "left" if k == 0 else "right"
        tx = x + 0.14 if k == 0 else x + colw[k] - 0.14
        ax.text(tx, y + hdrh / 2, "\n".join(lines), fontsize=hfs, fontweight="bold", color=MUTED, ha=ha, va="center",
                linespacing=1.25)
        x += colw[k]
    y += hdrh
    ax.plot([X0, X0 + avail], [y, y], color=RULE, lw=1.0)
    for i, row in enumerate(cells):
        if i % 2 == 1: ax.add_patch(plt.Rectangle((X0, y), avail, rowh, color=BAND, lw=0, zorder=0))
        x = X0
        for k, (txt, bold) in enumerate(row):
            ha = "left" if k == 0 else "right"
            tx = x + 0.14 if k == 0 else x + colw[k] - 0.14
            ax.text(tx, y + rowh / 2, txt, fontsize=fs, fontweight="bold" if bold else "normal", color=INK, ha=ha, va="center")
            x += colw[k]
        y += rowh
    ax.plot([X0, X0 + avail], [y, y], color=INK, lw=1.6)
    y += 0.42
    for l in note_lines:
        ax.text(X0, y, l, fontsize=11.5, color=MUTED, va="center"); y += 0.3
    ax.text(X0, H - 0.3, SOURCE, fontsize=10.5, color=MUTED, va="center")
    base = f"results/table_{idx:02d}_{slug}"
    fig.savefig(base + ".png", dpi=200, facecolor=BG); fig.savefig(base + ".svg", facecolor=BG); plt.close(fig)
    return base

if __name__ == "__main__":
    md = open("paper_draft.md").read()
    tabs, L = find_tables(md)
    assert len(tabs) == len(META), f"found {len(tabs)} tables, META has {len(META)}"
    manifest = []
    for n, (tab, (slug, title, sub)) in enumerate(zip(tabs, META), 1):
        b = render(tab, n, slug, title, sub, note_after(L, tab["end"]))
        manifest.append({"file": b + ".png", "title": title, "header": tab["header"], "rows": tab["rows"]})
        print(b, "|", title)
    json.dump(manifest, open("results/table_figures_manifest.json", "w"), ensure_ascii=False, indent=1)
