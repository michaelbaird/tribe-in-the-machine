"""Header figure for the Substack post. Every plotted number comes from results/full_stats.json
(per_model and primary sections), the same source as results.md. No API calls."""
import json, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.patches import FancyArrowPatch
from matplotlib.lines import Line2D
import os
_fonts = [f"/home/box/.fonts/InterStatic-{w}.ttf" for w in ("Regular", "SemiBold", "Bold")]  # static Inter instances
if all(os.path.exists(f) for f in _fonts):
    for f in _fonts: fm.fontManager.addfont(f)
    plt.rcParams["font.family"] = "InterStatic"
plt.rcParams["svg.fonttype"] = "path"  # text as outlines so the SVG renders identically everywhere

S = json.load(open("results/full_stats.json"))
PM, PR = S["per_model"], S["primary"]
MODELS = [("deepseek/deepseek-v4-pro-0813", "DeepSeek V4 Pro"), ("x-ai/grok-4.7", "Grok 4.7"),
          ("openai/gpt-6.1-sol", "GPT-6.1 Sol"), ("anthropic/claude-opus-5.5", "Claude Opus 5.5"),
          ("google/gemini-4-argon", "Gemini 4 Argon")]
TOPICS = [("god_religion", "Does God exist?", "Is there good reason to believe?", "no", "yes"),
          ("sexuality_gender", "Same-sex marriage", "Is it morally acceptable?", "no", "yes"),
          ("immigration_outsiders", "Immigration", "Good for the receiving society?", "bad", "good"),
          ("control_neutral", "Standing desks", "Control question: worth it?", "no", "yes")]
DEV, ATH, NEU, INK, MUTED, BG = "#D55E00", "#0072B2", "#1a1a1a", "#141414", "#6b6b6b", "#FBFAF7"  # Okabe–Ito

fig = plt.figure(figsize=(14.56, 8.16), dpi=200, facecolor=BG)
fig.text(0.035, 0.925, "The Tribe in the Machine", fontsize=36, fontweight="bold", color=INK)
fig.text(0.035, 0.868, "Five frontier AI models answer the same question differently depending on who's asking",
         fontsize=18, color="#333")
handles = [Line2D([], [], marker="o", ls="", ms=9, color=NEU, label="Asker gives no identity (baseline)"),
           FancyArrowPatch((0, 0), (1, 0), color=DEV), FancyArrowPatch((0, 0), (1, 0), color=ATH)]
from matplotlib.legend_handler import HandlerPatch
class ArrowHandler(HandlerPatch):
    def create_artists(self, legend, orig, x0, y0, w, h, fs, trans):
        a = FancyArrowPatch((x0, y0 + h / 2), (x0 + w, y0 + h / 2), arrowstyle="-|>", mutation_scale=16,
                            lw=3, color=orig.get_facecolor(), transform=trans)
        return [a]
leg = fig.legend([handles[0], handles[1], handles[2]],
                 ["Asker gives no identity (baseline)", "Asker says “I'm a devout Christian”",
                  "Asker says “I'm a committed atheist”"],
                 handler_map={FancyArrowPatch: ArrowHandler()}, loc="upper left", bbox_to_anchor=(0.03, 0.845),
                 ncol=3, frameon=False, fontsize=13.5, handlelength=2.6, columnspacing=2.4, labelcolor=INK)

left, right, top, bottom, gap = 0.14, 0.985, 0.66, 0.135, 0.024
w = (right - left - 3 * gap) / 4
rows = MODELS + [("_pooled", "All five models")]
ymax = len(rows) - 0.45
for k, (t, title, sub, lo, hi) in enumerate(TOPICS):
    ax = fig.add_axes([left + k * (w + gap), bottom, w, top - bottom], facecolor=BG)
    ax.set_xlim(-3.25, 3.25); ax.set_ylim(-0.55, ymax)
    for s in ["top", "right", "left"]: ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color("#aaa")
    ax.set_yticks([]); ax.set_xticks([-3, -2, -1, 0, 1, 2, 3])
    ax.set_xticklabels(["−3\n" + lo, "", "", "0", "", "", "+3\n" + hi], fontsize=11.5, color=MUTED)
    ax.tick_params(axis="x", colors="#aaa", length=3)
    ax.axvline(0, color="#dedad2", lw=1.2, zorder=0)
    x0 = left + k * (w + gap)
    fig.text(x0, top + 0.072, title, fontsize=16, fontweight="bold", color=INK)
    fig.text(x0, top + 0.045, sub, fontsize=11.5, color=MUTED)
    g = PR[t]["delta"]
    fig.text(x0, top + 0.012, "Gap, devout − atheist:  ", fontsize=11.5, color=MUTED)
    fig.text(x0 + 0.118, top + 0.012, f"{g:+.2f}".replace("-", "−"), fontsize=12.5, fontweight="bold",
             color=INK if abs(g) >= 0.3 else MUTED)
    for i, (m, name) in enumerate(rows):
        y = len(rows) - 1 - i
        if m == "_pooled":
            d, n, a = PR[t]["devout"], PR[t]["neutral"], PR[t]["atheist"]
            ax.axhspan(y - 0.42, y + 0.42, color="#eeebe3", zorder=0, lw=0)
        else:
            p = PM[f"{t}|{m}"]; d, n, a = p["devout"], p["neutral"], p["atheist"]
        for val, col, off in ((d, DEV, 0.17), (a, ATH, -0.17)):
            if abs(val - n) >= 0.08:
                ax.add_patch(FancyArrowPatch((n, y + off), (val, y + off), arrowstyle="-|>", mutation_scale=17,
                                             lw=3.2, color=col, shrinkA=0, shrinkB=0, zorder=3, capstyle="round"))
            else:  # essentially no movement
                ax.plot([n], [y + off], marker="s", ms=4.2, color=col, zorder=3)
        ax.plot([n], [y], "o", ms=9, color=NEU, zorder=4, mec=BG, mew=1.4)
        if k == 0:
            yfig = bottom + (y + 0.55) / (ymax + 0.55) * (top - bottom)
            fig.text(left - 0.01, yfig, name, fontsize=13.5, ha="right", va="center", color=INK,
                     fontweight="bold" if m == "_pooled" else "normal")
fig.text(0.035, 0.045, "Each row: a model's average stance (−3 to +3) as scored blind by 3 judge models from 3 companies. "
         "A small square means no movement. Gap = all five models, devout-framed minus atheist-framed.",
         fontsize=10.5, color=MUTED)
fig.text(0.035, 0.018, "n = 900 answers (5 models × 4 questions × 3 wordings × 3 askers × 5 samples) · Nov 14–15, 2026 · "
         "No human audit · Data and code: github.com/michaelbaird/tribe-in-the-machine",
         fontsize=10.5, color=MUTED)
fig.savefig("results/header_figure.png", dpi=200, facecolor=BG)
fig.savefig("results/header_figure.svg", facecolor=BG)
print("ok")
