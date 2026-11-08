# Scene authoring

A video is one file, `video.md`. Each slide is a `## heading`, a `js` block that says what can be on screen (the cast), and the narration under it, where each action sits on the word it happens on (the script). The cast has no timing in it. The script owns time.

**Read `design-system.md` first.** It lists every color, size, drawing, piece, option and form there is, generated from the code, so what it names exists. `presets.md` has a tested slide for every piece and form, cast and script together: start from the closest one and change its words, drawings and data.

## A slide

````md
## s02 How a request finds its data

```js
const browser = Labeled('Browser', Part('browser')), server = Labeled('Server', Part('server'))
const cache = Labeled('Cache', Part('cache')), db = Labeled('Database', Part('database'))
slide(Flow([[browser, server, 'GET /'], [server, cache], [server, db, { dashed: true }]]))
```

The [browser](browser) [asks](browser->server) the server. The server [tries the cache](server->cache) first, and only on a [miss](cache:red) does it [go to the database](server->db).

Then [the page comes back](db->server).
````

- **The cast** is plain code: `const` names for what the script will point at, and one `slide(...)`. Name what you'll talk about; leave the rest unnamed. A cast makes one slide; the next is under the next heading.
- **The script** is the narration, in plain short sentences, the way you'd explain it at a desk. A blank line starts a new beat, a separate voice line, so break at sentence ends. Spell symbols out ("request dot auth"), because the voice mangles `request.auth`.
- **Every slide fades in** from the one before; the cut lands on its first word.

## Links

`[spoken words](what)`. The words are what the voice says; what's in the parentheses is what happens as they're said. Several, separated by spaces, happen together: `[comes back](db->server server:green)`.

| Written | Does |
| --- | --- |
| `name` | First time: it comes on, and lights. After: it lights again. A light goes out when the next thing on the slide lights. |
| `name:red`, `name:green` | Lights it in that color: `red`, `green`, `blue`, `yellow` or `orange`. Use red for a miss or a failure. |
| `name:spot` | The spotlight: everything else dims while it's lit. Lift, which grows it a little, is the default. |
| `+name`, `-name` | Shows it without a light; hides it, and anything drawn inside it. |
| `*` | Brings on everything not on yet. |
| `a->b` | The line between two things. The first time it draws, and brings on what it leads to as it lands; after that, something travels along it. In a `Sequence`, each mention is the next message between those two. |
| `name.part` | Something inside a piece (below). |
| `name.swap` | A move the cast gave it (below). |

Link about one thing a sentence, and the first mention of each. Light the exact word as it's said: when a card, point or line holds the words the voice speaks, give that text its own `const` and link its key word (`[ten years](years.years)`), not the whole card. Never light a thing before the voice reaches it: a card linked on a sentence's first words lights early (Ian, 2026-11-08: "why are we not highlighting individual words?"). A thing the script never names follows the usual order: a flow builds along its arrows from what is named, timeline steps and stack layers follow each other, a message comes after the one before, and anything else comes on with the slide. The build says what was never named, so read that and decide.

A part the script names comes on at its own word, in whatever order the script says them: a Compare's right card before its left, a Stack's bottom layer before its top, the last bar before the first. It never waits for the parts listed before it. A card or layer comes on with the first thing said on it.

A slide is never blank for more than a second. When the first thing drawn would come on later than that, whatever the script names first comes on with the slide instead, and still lights on its word; everything else still comes on at its own word. So a slide opens on its first named thing, the way an album opens on its first picture. Still, link something in the first sentence: a thing that arrives on its word reads better than one that was waiting.

The build stops, before any voice, on a link to a name the cast doesn't have, a part a piece doesn't have, or a piece timing itself (`.on`, `.at`, `.light`, `.hide`, an `on:` inside it): each says which slide and line, and what there is instead.

## Parts: pointing inside a piece

| Piece | Parts | Example |
| --- | --- | --- |
| `Code` | its lines by number, and a word on one | `[reads the row](code.2)`, `[db](code.2.db)` |
| `Text` | each of its words, lowercase | `[make it fast](quote.fast)` |
| `Diff` | the moment it changes, and its lines | `[the fix](diff.change)` |
| `Table` | its rows by number | `[Bob](people.2)` |
| `Files` | its files by name, without the extension | `[the models](files.models)` |
| `Terminal` | its lines by number; the lines after a command follow it | `[run the tests](term.1)` |
| `Timeline` | its steps by what they say | `[launch](steps.launch)` |
| `Stack` | its layers by name | `[the server](layers.server)` |
| `Bars` | its bars by label: the one named turns blue | `[faster](bars.after)` |
| `Compare` | its sides by title, and each side's points by number; a point can be a glyph, or `{ text: glyph, good }` to keep its mark | `[REST](sides.rest)`, `[one request](sides.graphql.1)` |
| `Line` | its marks by label | `[launch](line.launch)` |
| `Dots` | its groups by label | `[new](dots.new)` |
| `Part` with a badge | its badge by drawing name | `[approved](person.check)` |
| `Machine` | its states are names: naming one moves the ring there | `[busy](busy)` |
| `Form` | its moments (below) | `[the server](trace.server)` |

When a slot holds a drawing as well as words (`what: Row(Part('rocket'), Text('propose one'))`, a bar's `label: Row(...)`), the slot has no name to point at, so point at it by number: `steps.2`, `bars.1`. Better, give its text a `const` and point at its words. A Flow `areas` box can't be pointed at; to say "it's a marketplace", put a `Text` heading under the Flow and link that. A `const` can't use a name the browser already has (`name`, `top`, `self`…): the build says so. And when every node of a Flow is inside one area, the area becomes a single column, so leave something outside it or drop the box.

A name made of several words is written with dashes: `steps.timing-fails`, `sides.graphql`. A number points at one in order: `steps.2`. A glyph inside a chart's slot can have its own `const` name and be linked like any other.

## Moves: what a cast says can happen

| Move | Script |
| --- | --- |
| `Text('v1').swap('v2')`: the old text lifts away, the new settles in | `[now](label.swap)` |
| `Text('a = 1 + 2').rewrite('a = 3')`: shared words travel to their new places | `[becomes](sum.rewrite)` |
| `x.morph({ color: 'green', scale: 1.1 })` | `[it's fixed](x.morph)` |
| `chip.moveTo(other)` | `[moves over](chip.moveTo)` |

A second move of the same kind is named with its number: `label.swap-2`. A move the script never says doesn't happen, and the build says so. `Text(...).typed()` and `.wordByWord()` are how text arrives, when it's named.

## Choosing the picture

Every picture should be big and full, and show the actual thing being said: real code rather than made-up code, real numbers, several things working together. A small cluster in the middle reads as thin, and the check warns about it.

| The voice says | Show it with |
| --- | --- |
| One thing leads to, calls or sends to another | `Flow`, or `Row(a, Arrow(), b)`, or `Connect(a, b, { travel: 'query' })` for something moving along it |
| Who sends what to whom, in order | `Sequence` |
| Something in one state at a time, and what moves it | `Machine` with `State`s |
| How parts are structured | `Tree` for what branches, `Stack` for layers (`nest: true` for what runs inside what) |
| Steps in time, or a loop | `Timeline` (`down: true` for a card each), `Cycle` |
| This versus that | `Compare`: good points green, bad ones red |
| One thing becoming another | `rewrite`, `swap`, `Form('reshape')`, `moveTo` |
| Amounts | `Bars`, `Stat`, `Dots`, `Line` for change over time (`trend: true` when the trend is the point) |
| How code behaves | `Code`, lit line by line; `Diff` for a change; `Form('trace')` for a request moving through it |
| Look at this exact thing | a link with `:spot`, at most once or twice a slide |
| A story told on a real photo | a picture board, `Scene({ photo, drift: 0 }, ...)` (`picture-board.md`): a title on a slab is `Text` inside the scene, a cutout says who it is with `tag`, and a diagram beside the scene takes `Cutout`s where its drawings go |

- **Everything is a glyph, so put icons inside your diagrams.** Any slot in a chart takes any glyph as well as words: a Stack layer, a Timeline step's `what`, a bar's `label`, a Compare point or title. Reach for an icon in a slot whenever one fits: `Stack([Row(db, Text('Database'))])` with `const db = Part('database')` reads at a glance where a box of words doesn't (Ian, 2026-11-07: "I don't think that is used enough"). The chart sizes it for you: words in a slot take the chart's own text size, and a drawing is sized to them, so don't pick sizes there. Name the icon with its own `const` and link it, `[the database](db)`, so it grows as it's said; the chart comes on with the first thing in it the script names.
- **Drawings** are ours: `chalkdust parts <words>`, then `Part('name')`, sizes `s`, `m`, `l`, `xl`. `Labeled('Server', Part('server'))` puts a caption under one. `Part('person').badge('check')` pins a small one to a corner for a variant. Use drawings as much as you can: a slide of pictures reads faster than a slide of words. Never an emoji.
- **Layouts:** `Row`, `Column` and `Grid(n, ...)`. Too much in a layout shrinks to fit, so it can't overlap or run off the stage.
- **Text:** `Text('words', { size: 'h1', color: 'green' })`, sizes `big`, `h1`, `h2`, `h3`, `caption`. At most about 15 words on screen; the narration does the explaining.
- **Long code wraps** by itself, so paste real lines; keep a block under about 12 lines rather than shrinking it.

## Forms for explaining code

Five ready-made ways to explain how code behaves, as one piece: `Form(kind, data)`. Each fills the stage. Their moments are parts, named from the data:

| The explanation is about | Form | Its moments |
| --- | --- | --- |
| Something moving through a system and changing on the way | `Form('trace', { hops: [{ label, icon, carry, job, code }] })` | each hop by its label: `trace.server` |
| Something in one state at a time, and what moves it | `Machine([[idle, busy, 'start']], { start: idle })` | each state as it's named: `busy` |
| One data shape becoming another | `Form('reshape', { via, from, to })` | `from`, `to`, `keep`, `add`, `rename`, `drop` |
| Two things at once, where the order decides | `Form('race', { lanes, span, events, verdict })` | `start`, `end`, `verdict` |
| Attempts stopped at a wall, like security checks | `Form('barrier', { source, wall, rows })` | each row by its target: `barrier.disk` |

A moment the script doesn't name comes a little after the one before. `presets.md` has each one, cast and script.

## The diagrams engineers already know

UML and the other standard diagrams are modes of the pieces above, not pieces of their own, so they look and move like everything else (Ian, 2026-11-07: "make sure we are consolidating and using the existing graph systems we already have"):

| The diagram | Write it as | Preset |
| --- | --- | --- |
| Class diagram | `Schema` with `methods` and a `color` per class, and keys between whole classes in words: `['CardPayment', 'Payment', 'is a']` | `p-classes` |
| Class diagram, strict UML | the same `Schema` with `uml: true`: visibility marks, a «stereotype», a hollow triangle for `is a` | `p-uml-classes` |
| Activity diagram | `Flow(..., { direction: 'down' })` of `State`s, with `State('Declined?', { shape: 'decision' })` and `shape: 'start'` / `'end'` | `p-activity` |
| Activity in swimlanes, who does each step | the same `Flow`, with `lanes: [['Customer', pays, receipt], ['Billing', charge]]`, every step in one lane | `p-swimlanes` |
| State diagram | `Machine` | `p-machine` |
| Sequence diagram | `Sequence` | `p-sequence` |
| Commit graph, for a pull request | `Timeline(..., { down: true })` whose steps name their `branch`, and `merge: 'retry'` | `p-commits` |
| Component diagram | `Flow` of `Labeled` drawings, each link labeled with the call: `[web, billing, 'pay()']` | `p-components` |
| Deployment diagram | `Flow` with `areas` for the cloud and each machine | `p-areas` |
| Use case diagram | `Flow` from `Labeled` people, `Part('person')`, to `State` steps, inside an `areas` box for the system | `p-usecase` |
| Map of a repo | `chalkdust map <repo>` writes the cast from the real imports, each folder an area | `p-areas` |
| Database schema | `Schema` | `p-structure` |

## Links to code

**Always link code to its source when there is one** (Ian, 2026-11-08: "provide a GitHub URL for wherever we have that available for the code. That is important"). When the code comes from a repository on GitHub, give `Code` and `Diff` the file's link, at the commit or branch you read it from, and the line if you can: `Code(src, { lang: 'py', link: 'https://github.com/owner/repo/blob/main/app/orders.py#L40' })`. The block shows the file's name and opens it when clicked, and clicking it in the player pauses the video. Prefer this to naming the file in the narration. Only `https://` links work.

