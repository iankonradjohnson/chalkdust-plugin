#!/usr/bin/env python3
"""A map of a repo, drawn from its real imports (Ian, 2026-11-07, picking the folders look for the repo map).

  python3 repo_map.py <repo> [--most 12]      prints a cast for video.md: a Flow, each folder an area

It reads the Python imports (import a.b, from a import b, from .b import c) and the JavaScript ones (import ... from
'./x', require('../y')), keeps only what points inside the repo, and keeps the most connected modules, so a big repo
gives a map that fits a slide. Each import is an arrow from the file importing to the file imported. The drawing is
Flow's, with its areas, so the map looks like every other diagram.
"""
import argparse, os, re, sys

SKIP = {".git", "node_modules", "venv", ".venv", "dist", "build", "__pycache__", ".claude", ".next", "coverage"}
CODE = (".py", ".js", ".mjs", ".ts", ".tsx", ".jsx")
PY_IMPORT = re.compile(r"^\s*import\s+([\w.]+(?:\s*,\s*[\w.]+)*)", re.M)
PY_FROM = re.compile(r"^[ \t]*from[ \t]+(\.*[\w.]*)[ \t]+import[ \t]+(?:\(([^)]*)\)|([\w \t,]+))", re.M)
JS_IMPORT = re.compile(r"""(?:import\s[^'"]*?from\s*|import\s*\(\s*|require\(\s*)['"](\.{1,2}/[^'"]+)['"]""")


TESTS = {"tests", "test", "__tests__", "spec"}


def files_of(root, tests=False):
    out = []
    for here, dirs, names in os.walk(root):
        dirs[:] = sorted(d for d in dirs if d not in SKIP and not d.startswith(".") and (tests or d not in TESTS))
        out += [os.path.relpath(os.path.join(here, n), root).replace(os.sep, "/") for n in sorted(names) if n.endswith(CODE)]
    return out


def python_modules(files):
    """{dotted name: file}: api/routes.py is api.routes, billing/__init__.py is billing."""
    mods = {}
    for f in files:
        if f.endswith(".py"):
            name = f[:-3].replace("/", ".")
            mods[name[: -len(".__init__")] if name.endswith(".__init__") else name] = f
    return mods


def python_imports(f, text, mods):
    package = os.path.dirname(f).replace("/", ".")
    found = []

    def first(*names):
        for n in names:
            if n in mods and mods[n] != f:
                return mods[n]

    # A bare name can be a sibling, when the script's own folder is on the path (import pictures, in scripts/).
    near = lambda n: [n, f"{package}.{n}"] if package else [n]
    for m in PY_IMPORT.finditer(text):
        for name in m.group(1).split(","):
            hit = first(*near(name.strip()))
            if hit:
                found.append(hit)
    for m in PY_FROM.finditer(text):
        source, names = m.group(1), [n.split(" as ")[0].strip() for n in (m.group(2) or m.group(3)).replace("\n", ",").split(",") if n.strip()]
        dots = len(source) - len(source.lstrip("."))
        if dots:
            base = package.split(".") if package else []
            base = base[: len(base) - (dots - 1)] if dots > 1 else base
            source = ".".join([*base, source[dots:]] if source[dots:] else base)
        for n in names:
            hit = first(*(near(f"{source}.{n}") if source else near(n)), *(near(source) if source else []))
            if hit:
                found.append(hit)
    return found


def js_imports(f, text, files):
    have, found = set(files), []
    for m in JS_IMPORT.finditer(text):
        base = os.path.normpath(os.path.join(os.path.dirname(f), m.group(1))).replace(os.sep, "/")
        for c in [base, *(base + e for e in CODE), *(f"{base}/index{e}" for e in CODE)]:
            if c in have and c != f:
                found.append(c)
                break
    return found


def read(root, most=12, tests=False):
    """{'files': [...], 'imports': [(importer, imported), ...]}, kept to the most connected modules. Tests are left out
    unless tests=True: a map of the code, not of what checks it."""
    files = files_of(root, tests)
    mods = python_modules(files)
    pairs = set()
    for f in files:
        try:
            text = open(os.path.join(root, f), encoding="utf-8", errors="ignore").read()
        except OSError:
            continue
        found = python_imports(f, text, mods) if f.endswith(".py") else js_imports(f, text, files)
        pairs.update((f, g) for g in found)
    degree = {}
    for a, b in pairs:
        degree[a] = degree.get(a, 0) + 1
        degree[b] = degree.get(b, 0) + 1
    kept = set(sorted(degree, key=lambda f: (-degree[f], f))[:most])
    imports = sorted((a, b) for a, b in pairs if a in kept and b in kept)
    return {"files": sorted({f for pair in imports for f in pair}), "imports": imports}


def var(path):
    return re.sub(r"\W+", "_", os.path.splitext(path)[0]).strip("_") or "file"


def cast(m):
    """The cast for video.md: a drawing per file, a Flow of the imports, and an area per folder."""
    lines = [f"const {var(f)} = Labeled('{os.path.basename(f)}', Part('code-file', {{ size: 's' }}))" for f in m["files"]]
    folders = {}
    for f in m["files"]:
        folders.setdefault((os.path.dirname(f) or ".") + "/", []).append(var(f))
    links = ", ".join(f"[{var(a)}, {var(b)}]" for a, b in m["imports"])
    areas = ", ".join(f"['{name}', {', '.join(vs)}]" for name, vs in folders.items())
    lines.append(f"slide(Flow([{links}], {{ areas: [{areas}] }}))")
    return "\n".join(lines)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="A Flow cast of a repo's imports, each folder an area.")
    ap.add_argument("repo")
    ap.add_argument("--most", type=int, default=12, help="how many of the most connected modules to keep")
    ap.add_argument("--tests", action="store_true", help="include test files")
    a = ap.parse_args()
    m = read(a.repo, a.most, a.tests)
    if not m["imports"]:
        sys.exit("No imports between the repo's own files were found.")
    print(cast(m))
