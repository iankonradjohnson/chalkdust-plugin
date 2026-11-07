# Presets

A tested slide for every form and piece. Pick the one closest to what you're showing, copy it into your `video.md`, and change the words, drawings and data. Each one builds without a warning as it is.

The cast says what's on screen and has no timing in it. The script says when: `[words](name)` brings a thing on, or lights it, as the words are said. Point inside a piece with a path (`steps.launch`, `code.2`, `trace.server`) and at a line between two things with `a->b`. A link to something the cast doesn't have fails the build, with the slide and the line.

Generated from `brand/specimens/video.md` by `scripts/design_system.js`. The full list of pieces, forms and options is in `design-system.md`.

| Preset | Shows |
| --- | --- |
| `f-trace` | Form: trace |
| `f-reshape` | Form: reshape |
| `f-race` | Form: race |
| `f-barrier` | Form: barrier |
| `p-layout` | Row, Column, Grid, Part, Text, Labeled, Arrow |
| `p-text` | Text sizes |
| `p-flow` | Flow and Connect |
| `p-machine` | Machine and State |
| `p-sequence` | Sequence |
| `p-data` | Dots, Bars, Stat |
| `p-table` | Table |
| `p-code` | Code |
| `p-diff` | Diff |
| `p-files` | Files |
| `p-terminal` | Terminal |
| `p-window` | Window |
| `p-scene` | Scene and Layer |
| `p-light` | light, badge |
| `p-form` | Form, as a piece |
| `p-image` | Image, and links |
| `p-line` | Line |
| `p-timeline` | Timeline |
| `p-tree` | Tree |
| `p-stack` | Stack |
| `p-compare` | Compare |
| `p-cycle` | Cycle |

## f-trace Form: trace

```js
const trace = Form('trace', { lang: 'js', hops: [
  { label: 'Browser', icon: 'browser', carry: 'GET /', code: 'fetch(url)' },
  { label: 'Server', icon: 'server', carry: 'query', code: 'db.query(sql)' },
  { label: 'Database', icon: 'database', carry: 'rows', code: 'SELECT * FROM users' }] })
slide(trace)
```

The [browser](trace.browser) asks the [server](trace.server), which asks the [database](trace.database).

## f-reshape Form: reshape

```js
const shape = Form('reshape', { via: 'map',
  from: { title: 'Row', fields: [{ name: 'id', value: 1 }, { name: 'name', value: 'Ann' }, { name: 'old' }] },
  to: { title: 'Response', fields: [{ name: 'id', from: 'id' }, { name: 'name', from: 'name' }, { name: 'date' }] } })
slide(shape)
```

The [row](shape.from) becomes the [shape](shape.to) the [browser](shape.keep) wants, with a new [date](shape.add) and the old field [dropped](shape.drop).

## f-race Form: race

```js
const race = Form('race', { lanes: ['Request A', 'Request B'], span: 10,
  events: [{ lane: 0, x: 2, label: 'read' }, { lane: 1, x: 3, label: 'read' }, { lane: 0, x: 6, label: 'write', kind: 'write' }, { lane: 1, x: 7, label: 'write', kind: 'bad' }],
  verdict: { text: 'one update lost', color: 'red' } })
slide(race)
```

[Two](race.start) requests read, then both write, and one update [is lost](race.end race.verdict).

## f-barrier Form: barrier

```js
const barrier = Form('barrier', { source: { label: 'App', icon: 'robot' }, wall: 'sandbox', rows: [
  { attempt: 'delete', target: 'Disk', why: 'files' }, { attempt: 'read', target: 'Keys', why: 'tokens' },
  { attempt: 'call', target: 'API', why: 'allowed', pass: true }] })
slide(barrier)
```

The app tries to [delete files](barrier.disk) and [read keys](barrier.keys), but the sandbox stops it, and only the [network](barrier.api) passes.

## p-layout Row, Column, Grid, Part, Text, Labeled, Arrow

```js
const title = Text('Layout pieces', { size: 'h2' })
const browser = Labeled('Browser', Part('browser', { size: 'm' })), server = Labeled('Server', Part('server', { size: 'm' }))
const sizes = Grid(4, Text('big', { size: 'caption' }), Text('h1', { size: 'caption' }), Text('h2', { size: 'caption' }), Text('h3', { size: 'caption' }))
slide(Column(title, Row(browser, Arrow(), server), sizes))
```

[Layout pieces](title): the [browser](browser) [asks](browser->server) the [server](server:green), in rows, columns and [a grid](sizes).

## p-text Text sizes

```js
const big = Text('Big', { size: 'big' }), h1 = Text('Heading one', { size: 'h1' }), h2 = Text('Heading two', { size: 'h2', color: 'blue' })
const h3 = Text('Heading three', { size: 'h3' }), caption = Text('A caption line', { size: 'caption' })
slide(Column(big, h1, h2, h3, caption))
```

Text comes [big](big), as [heading one](h1), [two](h2) and [three](h3), and as a [caption](caption).

## p-flow Flow and Connect

```js
const b = Part('browser', { size: 's' }), s = Part('server', { size: 's' }), c = Part('cache', { size: 's' }), d = Part('database', { size: 's' })
slide(Flow([[b, s, 'GET /'], [s, c], [s, d, { dashed: true }]]), Connect(b, d, { travel: 'query' }))
```

The [browser](b) [calls](b->s) the server, which [reads the cache](s->c) and the [database](s->d). A query can also go [straight](b->d) [there](b->d).

## p-machine Machine and State

```js
const idle = State('Idle'), busy = State('Busy', { color: 'yellow' }), done = State('Done', { color: 'green' })
slide(Machine([[idle, busy, 'start'], [busy, done, 'finish'], [busy, idle, 'cancel']], { start: idle }))
```

[Idle](idle), then [busy](busy), then [done](done).

## p-sequence Sequence

```js
const a = Part('browser', { size: 's' }), b = Part('server', { size: 's' }), c = Part('database', { size: 's' })
slide(Sequence([a, b, c], [[a, b, 'GET /'], { note: 'checks the cache', on: b },
  { loop: 'each page', messages: [[b, c, 'query'], [c, b, 'rows', { reply: true }]] },
  { alt: [['found', [[b, a, '200 OK', { reply: true }]]], ['missing', [[b, a, '404', { reply: true }]]]] }]))
```

The [browser](a) [asks](a->b) the server, which checks its cache, then [queries](b->c) the database for each page. The [rows come back](c->b), and the [page goes out](b->a), or [a not found](b->a).

## p-data Dots, Bars, Stat

```js
const dots = Dots(120, { groups: [{ count: 80, label: 'the same', color: 'red' }, { count: 10, label: 'new', color: 'green' }] })
const bars = Bars([{ label: 'Before', value: 12, text: '12s' }, { label: 'After', value: 4, text: '4s', color: 'green' }])
const stat = Stat(3, 'times faster', { suffix: '×', color: 'green' })
slide(Row(dots, Column(bars, stat)))
```

[Most prompts](dots) were [the same](dots.the-same), only a few were [new](dots.new), and it [got](bars) [faster](bars.after), [three times](stat) over.

## p-table Table

```js
const people = Table(['Name', 'Joined', 'Plan'], [['Ann', 2019, 'Pilot'], { cells: ['Bob', 2021, 'Pilot'], color: 'green' }, ['Cy', 2023, 'Free']])
slide(people)
```

Of our [users](people), [Bob](people.2:green) joined later.

## p-code Code

```js
const code = Code('def handle(req):\n    row = db.get(req.id)\n    return render(row)', { lang: 'python', caption: 'app.py' })
slide(code)
```

The [handler](code) [reads the row](code.2), and [renders](code.3.render) it.

## p-diff Diff

```js
const diff = Diff('def get(id):\n    return db[id]', 'def get(id):\n    if id not in db:\n        return None\n    return db[id]', { lang: 'python' })
slide(diff)
```

The [fix](diff) [adds a check](diff.change).

## p-files Files

```js
const files = Files(['src/app.py', 'src/db/models.py', 'tests/test_models.py', 'README.md'], { added: ['tests/test_models.py'] })
slide(files)
```

In the [project](files), the [models file](files.models) changes, and the [test](files.test-models:green) is added.

## p-terminal Terminal

```js
const term = Terminal([{ cmd: 'npm test' }, { out: '12 passing', color: 'green' }, { cmd: 'git push' }, { out: 'main -> main' }], { title: 'zsh' })
slide(term)
```

[Run the tests](term.1), then [push](term.3).

## p-window Window

```js
const win = Window(Part('gear'), { title: 'Settings' })
slide(win)
```

The [settings window](win).

## p-scene Scene and Layer

```js
const hills = Scene(Layer('mountains', { depth: 0.2 }), Layer('tree', { depth: 1 })), title = Text('Over the hills', { size: 'h1' })
slide(hills, title)
```

[Over](hills) the [hills](title).

## p-light light, badge

```js
const person = Part('person', { size: 'm' }).badge('check'), server = Part('server', { size: 'm' }).badge('warning')
slide(Row(Labeled('Person', person), Labeled('Server', server)))
```

The [person](person) [checks](person.check) [in](person:green), and the [server](server) is [in trouble](server:red).

## p-form Form, as a piece

```js
const sandbox = Form('barrier', { source: { label: 'App', icon: 'robot' }, wall: 'sandbox', rows: [
  { attempt: 'delete', target: 'Disk', why: 'files' }, { attempt: 'call', target: 'API', why: 'allowed', pass: true }] })
slide(sandbox)
```

The app tries to [delete files](sandbox.disk), but only the [network](sandbox.api) passes.

## p-image Image, and links

```js
const shot = Image('assets/player.jpg', { size: 'l', ratio: 6 / 7 })
const site = Text('Open getchalkdust.com', { size: 'h2', color: 'blue', link: 'https://getchalkdust.com/' })
slide(Row(shot, site))
```

A [screenshot](shot) of the player, and a [link](site) a viewer can click.

## p-line Line

```js
const launch = Line([3, 4, 3.5, 5, 6.5, 9], { mark: { at: 4, label: 'launch' } })
const trend = Line([{ value: 300 }, { value: 420 }, { value: 380 }, { value: 640 }, { value: 900 }, { value: 1200, text: '1,200' }], { trend: true })
slide(Row(launch, trend))
```

A [line](launch) over time, neutral, with the [launch](launch.launch) marked in blue. Or [all blue](trend), when the trend is the point.

## p-timeline Timeline

```js
const steps = [{ when: 'Mar', what: 'idea' }, { when: 'Jun', what: 'beta' }, { when: 'Sep', what: 'launch', color: 'blue' }, { when: 'Dec', what: 'next' }]
const across = Timeline(steps), down = Timeline(steps, { down: true })
slide(Row(across, down))
```

Steps in time, [across](across), with the [launch](across.launch) in blue. Or [down](down), with a card for each step.

## p-tree Tree

```js
const app = Labeled('App', Part('phone', { size: 'm' })), web = Labeled('Web', Part('browser', { size: 'm' }))
const api = Labeled('API', Part('server', { size: 'm' })), db = Labeled('Database', Part('database', { size: 'm' })), jobs = Labeled('Jobs', Part('gear', { size: 'm' }))
slide(Tree([app, web, [api, db, jobs]]))
```

A tree grows down from the [app](app), to the [web](web) and the [API](api), and from the API to the [database](db) and the [jobs](jobs).

## p-stack Stack

```js
const layers = Stack(['Browser', { label: 'Server', color: 'blue' }, 'Database'])
const nested = Stack(['Machine', 'Container', { label: 'App', color: 'blue' }], { nest: true })
slide(Row(layers, nested))
```

Layers of a system, from the [browser](layers.browser) down to the [server](layers.server) and the [database](layers.database). Or [nested](nested), each one [inside the last](nested.app).

## p-compare Compare

```js
const sides = Compare(
  { title: 'REST', points: [{ text: 'simple to start', good: true }, { text: 'many round trips', good: false }, 'cached by URL'] },
  { title: 'GraphQL', points: [{ text: 'one request', good: true }, { text: 'a schema to keep', good: false }, 'typed'] })
slide(sides)
```

[REST](sides.rest) versus [GraphQL](sides.graphql), side by side: GraphQL takes [one request](sides.graphql.1), but has [a schema to keep](sides.graphql.2).

## p-cycle Cycle

```js
const plan = Labeled('Plan', Part('compass', { size: 'm' })), build = Labeled('Build', Part('hammer', { size: 'm' }))
const ship = Labeled('Ship', Part('rocket', { size: 'm' })), learn = Labeled('Learn', Part('book', { size: 'm' }))
slide(Cycle([plan, build, ship, learn]))
```

A loop: [plan](plan), [build](build), [ship](ship), [learn](learn), and [back to plan](learn->plan).
