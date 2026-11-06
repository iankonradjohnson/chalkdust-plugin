#!/usr/bin/env python3
"""Fill in a preset: a slide from a preset's name and what goes in it, so a slide is a couple of lines to write.

  python3 show.py <project>                               writes scenes/<id>.html for every slide in shows.json
  python3 show.py <project> <slide id> '<show as JSON>'   writes one slide

A show is {"preset": "flow", "things": ["Browser", "Server", "Database"], "verbs": ["asks", "queries"]}. Each thing's drawing is found by its name,
and nothing is timed: the narration's marks bring each thing on and light it. Write the marked script first, then the
shows after, one per slide (Ian, 2026-11-06: "Yes, that way"). For anything a preset can't draw, write the slide by hand.
"""
import json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

js = json.dumps
# The drawings there are, by name, with their tags. The plugin's command sets this to the service's; here, it's read from
# this machine's shelves.
SHELF = None


def shelf():
    if SHELF is not None:
        return SHELF
    import parts
    return {n: p["tags"] for n, p in parts.shelves(True).items()}


def drawing(name):
    """The drawing for a thing's name: one called that, or else the best match by its tags. None if nothing fits."""
    have, slug = shelf(), name.strip().lower().replace(" ", "-")
    if slug in have:
        return slug
    wanted = set(re.findall(r"\w+", name.lower()))
    scored = sorted(((len(wanted & set(re.findall(r"\w+", (n + " " + t).lower()))), n) for n, t in have.items()), key=lambda x: (-x[0], x[1]))
    return scored[0][1] if scored and scored[0][0] else None


class Raw(str):
    """Code written as is, like a glyph, inside a preset's data."""


def jsx(x):
    """Data as code, with glyphs written as code rather than as strings."""
    if isinstance(x, Raw):
        return str(x)
    if isinstance(x, dict):
        return "{ " + ", ".join(f"{js(k)}: {jsx(v)}" for k, v in x.items()) + " }"
    if isinstance(x, (list, tuple)):
        return "[" + ", ".join(jsx(v) for v in x) + "]"
    return js(x)


def glyph_row(part, text, stacked=False):
    """A drawing and its words, side by side or one over the other: everything is a glyph (Ian, 2026-11-06). Big, so
    when the chart scales it to its slot, the two keep their proportions."""
    return Raw(f"{'Column' if stacked else 'Row'}(Part({js(part)}, {{ size: 's' }}), Text({js(text)}, {{ size: 'h2' }}))")


def with_drawings(items, key, whole=False, stacked=False):
    """Each item's words with a drawing found by its name, or the one it names with "part", as a glyph. whole: the
    item itself becomes the glyph (a stack layer); otherwise its words do (a point, a step, a bar's label)."""
    out = []
    for it in items:
        if isinstance(it, (list, tuple)):
            raise ValueError(f"each item should be a word or an object like {{{key!r}: ..., ...}}, and got {it!r}")
        it = {key: it} if isinstance(it, str) else dict(it)
        part = it.pop("part", None) or drawing(str(it.get(key, "")))
        if part and isinstance(it.get(key), str):
            row = glyph_row(part, it[key], stacked)
            out.append(row if whole and set(it) <= {key} else {**it, key: row})
        else:
            out.append(it[key] if whole and set(it) <= {key} else it)
    return out


def thing(t):
    """A thing to show: its caption, over its drawing if there is one. A thing can be "Name" or {"name", "part"}."""
    name = t if isinstance(t, str) else t.get("name", "")
    part = (None if isinstance(t, str) else t.get("part")) or drawing(name)
    # JSON quoting is valid JavaScript, so a name with an apostrophe or a quote stays one string.
    return f"Labeled({js(name)}, Part({js(part)}))" if part else f"Text({js(name)}, {{ size: 'h3' }})"


def things(show):
    return [thing(t) for t in show.get("things", [])]


def flow(show):
    t = things(show)
    names = [f"t{i}" for i in range(len(t))]
    # Each arrow can say its verb, like "asks": it lights when the narration marks it.
    verbs = list(show.get("verbs", [])) + [None] * len(names)
    links = ", ".join(f"[{a}, {b}{', ' + js(v) if v else ''}]" for (a, b), v in zip(zip(names, names[1:]), verbs))
    return "const " + ", ".join(f"{n} = {g}" for n, g in zip(names, t)) + f";\nslide(Flow([{links}]))"


def side(sd):
    """A compare side with a drawing over its title, and each point a drawing and its words, where there's a drawing."""
    sd = dict(sd)
    part = sd.pop("part", None) or drawing(str(sd.get("title", "")))
    if part and isinstance(sd.get("title"), str):
        # The title as a glyph: its drawing over its words, in the card's title font.
        sd["title"] = Raw(f"Column(Part({js(part)}, {{ size: 's' }}), Text({js(sd['title'])}, {{ size: 'h1' }}))")
    sd["points"] = [p["text"] if isinstance(p, dict) and isinstance(p.get("text"), Raw) else p for p in with_drawings(sd.get("points", []), "text")]
    return sd


def bars(items):
    for b in items:
        if not isinstance(b, dict) or "label" not in b or "value" not in b:
            raise ValueError(f"each bar is {{\"label\": ..., \"value\": ...}}, and got {b!r}")
    return with_drawings(items, "label")


PRESETS = {
    "flow": flow,
    "row": lambda s: f"slide(Row({', '.join(things(s))}))",
    "cycle": lambda s: f"slide(Cycle([{', '.join(things(s))}]))",
    "compare": lambda s: f"slide(Compare({jsx(side(s['left']))}, {jsx(side(s['right']))}))",
    "stack": lambda s: f"slide(Stack({jsx(with_drawings(s['layers'], 'label', whole=True))}{', { nest: true }' if s.get('nest') else ''}))",
    "timeline": lambda s: f"slide(Timeline({jsx(with_drawings(s['steps'], 'what', stacked=not s.get('down')))}{', { down: true }' if s.get('down') else ''}))",
    "bars": lambda s: f"slide(Bars({jsx(bars(s['bars']))}))",
    "code": lambda s: f"slide(Code({js(s['code'])}, {js({k: s[k] for k in ('lang', 'link', 'caption') if k in s})}))",
    "terminal": lambda s: f"slide(Terminal({js(s['lines'])}))",
    "stat": lambda s: f"slide(Stat({js(s['value'])}, {js(s.get('label', ''))}, {js({k: s[k] for k in ('suffix', 'prefix', 'color') if k in s})}))",
}


def script_for(show):
    """A slide's code for a show. An unknown preset says which there are."""
    name = show.get("preset")
    if name not in PRESETS:
        raise ValueError(f"there's no preset {name!r}. There are: {', '.join(PRESETS)}. For anything else, write the slide by hand.")
    return f"<script>\n{PRESETS[name](show)}\n</script>\n"


def write(project, slide, show):
    path = os.path.join(project, "scenes", f"{slide}.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(script_for(show))
    return path


def main(argv):
    if len(argv) == 2:
        shows = json.load(open(os.path.join(argv[1], "shows.json")))
        for slide, show in shows.items():
            print("wrote", write(argv[1], slide, show))
    elif len(argv) == 4:
        print("wrote", write(argv[1], argv[2], json.loads(argv[3])))
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    try:
        main(sys.argv)
    except ValueError as e:
        sys.exit(f"show: {e}")
