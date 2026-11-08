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
| `p-math` | Equation, Cells, Matrix |
| `p-plots` | Scatter, Histogram, Heatmap |
| `p-structure` | Calls, Schema |
| `p-motion` | Stream, sort, countTo |
| `p-reveal` | The big reveal |
| `p-before-after` | Before and after |
| `p-predict` | Pause and predict |
| `p-countdown` | Countdown |
| `p-photo` | A real photo, large |
| `p-myth` | The wrong idea first |
| `p-quote` | A quote |
| `p-steps-icons` | Steps, each with its drawing |
| `p-compare-icons` | Compare, each point with its drawing |
| `p-stack-icons` | Layers, each with its drawing |
| `p-bars-icons` | Bars, each label with its drawing |
| `p-checklist` | A checklist |
| `p-stat-row` | Numbers, each with its drawing |
| `p-callout` | A callout |
| `p-definition` | A definition |
| `p-qa` | A question and its answer |
| `p-cutout` | Cutout |

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

## p-math Equation, Cells, Matrix

```js
const area = Equation(['A', '=', 'π', 'r²']), list = Cells([7, 3, 9, 4]), grid = Matrix([[1, 2], [3, 4]])
slide(Column(area, Row(list, grid)))
```

The [area](area.a) is [pi](area.3) times [r squared](area.r). A list keeps [nine](list.2) at [index two](list.2), and a matrix has [rows](grid.row-0) and [columns](grid.col-1).

## p-plots Scatter, Histogram, Heatmap

```js
const sc = Scatter([[1, 2], [2, 3], [3, 3], { x: 4, y: 9, label: 'outlier' }, [5, 5]], { trend: true })
const spread = Histogram([1, 2, 2, 3, 3, 3, 4, 4, 5], { bins: 5 })
const week = Heatmap([[2, 8], [9, 3]], { rows: ['Mon', 'Tue'], cols: ['AM', 'PM'] })
slide(Row(sc, Column(spread, week)))
```

The points [rise](sc.trend), but for [one outlier](sc.outlier). The values [bunch in the middle](spread.2), and [Tuesday](week.tue) is busy [in the morning](week.am).

## p-structure Calls, Schema

```js
const calls = Calls([{ name: 'main()', ms: 420 }, [{ name: 'load()', ms: 310 }, { name: 'read()', ms: 40 }, { name: 'parse()', ms: 260 }], { name: 'render()', ms: 90 }])
const db = Schema([{ name: 'users', fields: [{ name: 'id', type: 'int' }, 'email'] }, { name: 'orders', fields: ['id', 'user_id', 'total'] }], { keys: [['orders.user_id', 'users.id']] })
slide(Column(calls, db))
```

The [main](calls.main) call spends its time in [load](calls.load), mostly in [parse](calls.parse). An [order](db.orders) points at its user through [user id](db.orders.user-id).

## p-motion Stream, sort, countTo

```js
const app = Labeled('App', Part('phone', { size: 'm' })), api = Labeled('API', Part('server', { size: 'm' }))
const list = Cells([7, 3, 9, 4]).sort(), users = Stat(12, 'users').countTo(40)
slide(Column(Flow([[app, api, { label: 'events', stream: true }]]), Row(list, users)))
```

The [app](app) [keeps sending](app->api) events. The list [sorts itself](list.sort), and the [users](users) [climb to forty](users.countTo).

## p-reveal The big reveal

```js
const setup = Text('How many tests run on every push?', { size: 'h2' }), answer = Stat(1744, 'tests, in two seconds', { color: 'blue' })
slide(Column(setup, answer))
```

[How many tests](setup) run on [every push](setup.every)? [Seventeen hundred forty four](answer), in [two seconds](answer).

## p-before-after Before and after

```js
const before = Part('stopwatch', { size: 'l' }), was = Text('12 seconds', { size: 'h2' })
const after = Part('rocket', { size: 'l' }), now = Text('4 seconds', { size: 'h2', color: 'green' })
slide(Row(Column(before, was), Arrow(), Column(after, now)))
```

[Before](before), the build took [twelve seconds](was). [After](after) the cache, [four](now).

## p-predict Pause and predict

```js
const think = Part('question', { size: 'm' }), pause = Text('Pause and guess', { size: 'h3', color: 'blue' })
const ask = Text('Two requests at once?', { size: 'h2' }).swap('Both read the old value')
slide(Column(Row(think, pause), ask))
```

[Pause](think) and [guess](pause.guess): what happens when [two requests arrive at once](ask)? [Both read the old value](ask.swap).

## p-countdown Countdown

```js
const slow = Text('Slow queries'), nocache = Text('No cache'), loop = Text('Calls in a loop', { color: 'red' })
const ranks = Timeline([{ when: '3', what: Row(Part('database', { size: 's' }), slow) }, { when: '2', what: Row(Part('cloud', { size: 's' }), nocache) }, { when: '1', what: Row(Part('bug', { size: 's' }), loop), color: 'red' }], { down: true })
slide(ranks)
```

The [three biggest costs](ranks). Number three: [slow queries](slow). Two: [no cache](nocache). And number one: [calls in a loop](loop).

## p-photo A real photo, large

```js
const photo = Image('assets/player.jpg', { size: 'xl', ratio: 6 / 7 }), caption = Text('the real thing', { size: 'caption' })
slide(Column(photo, caption))
```

[Here it is](photo), [the real thing](caption).

## p-myth The wrong idea first

```js
const servers = Text('more servers, more speed'), limit = Text('the database is the limit')
const myth = Compare({ title: 'Myth', points: [Row(Part('server', { size: 's' }), servers)] }, { title: 'Actually', points: [Row(Part('database', { size: 's' }), limit)] })
slide(myth)
```

[Most people think](myth.myth) [more servers mean more speed](servers). [Actually](myth.actually), [the database is the limit](limit).

## p-quote A quote

```js
const quote = Text('"Make it work, then make it fast."', { size: 'h1' }), who = Labeled('Kent Beck', Part('person', { size: 's' }))
slide(Column(quote, who))
```

[Make it work](quote.work), then [make it fast](quote.fast). That's [Kent Beck](who).

## p-steps-icons Steps, each with its drawing

```js
const power = Text('Power up'), apu = Text('Start the APU'), align = Text('Align the IRS')
const steps = Timeline([{ when: '1', what: Row(Part('battery', { size: 's' }), power) }, { when: '2', what: Row(Part('gear', { size: 's' }), apu) }, { when: '3', what: Row(Part('compass', { size: 's' }), align) }], { down: true })
slide(steps)
```

[Power up](power) first, then [start the APU](apu), then [align the IRS](align).

## p-compare-icons Compare, each point with its drawing

```js
const fast = Text('fast reads'), more = Text('more to run'), simple = Text('one place'), slow = Text('slow reads')
const sides = Compare({ title: 'Cache', points: [Row(Part('zap', { size: 's' }), fast), Row(Part('warning', { size: 's' }), more)] }, { title: 'No cache', points: [Row(Part('check', { size: 's' }), simple), Row(Part('alarm', { size: 's' }), slow)] })
slide(sides)
```

[A cache](sides.cache) gives [fast reads](fast), but [more to run](more). [No cache](sides.no-cache) is [one place](simple), with [slow reads](slow).

## p-stack-icons Layers, each with its drawing

```js
const browser = Text('Browser'), server = Text('Server'), db = Text('Database')
const layers = Stack([Row(Part('phone', { size: 's' }), browser), Row(Part('server', { size: 's' }), server), Row(Part('database', { size: 's' }), db)])
slide(layers)
```

[The browser](browser) talks to [the server](server), which reads [the database](db).

## p-bars-icons Bars, each label with its drawing

```js
const py = Text('Python'), js = Text('JavaScript')
const tests = Bars([{ label: Row(Part('bug', { size: 's' }), py), value: 808 }, { label: Row(Part('gear', { size: 's' }), js), value: 699 }])
slide(tests)
```

[Python](py) runs eight hundred eight tests, and [JavaScript](js) six hundred ninety nine.

## p-checklist A checklist

```js
const doors = Row(Part('check', { size: 's' }), Text('Doors closed', { size: 'h3' })), beacon = Row(Part('check', { size: 's' }), Text('Beacon on', { size: 'h3' }))
const brakes = Row(Part('check', { size: 's' }), Text('Brakes set', { size: 'h3' }))
slide(Column(doors, beacon, brakes, { align: 'start' }))
```

[Doors closed](doors). [Beacon on](beacon). [Brakes set](brakes).

## p-stat-row Numbers, each with its drawing

```js
const users = Stat(1200, 'users'), uptime = Stat(99.9, 'uptime', { suffix: '%' }), reply = Stat(40, 'ms to reply', { color: 'green' })
slide(Grid(3, Part('person', { size: 's' }), Part('server', { size: 's' }), Part('zap', { size: 's' }), users, uptime, reply))
```

[Twelve hundred users](users), [ninety nine point nine percent up](uptime), and [forty milliseconds](reply) to reply.

## p-callout A callout

```js
const tip = Row(Part('lightbulb', { size: 'm' }), Text('Start engine 2 first', { size: 'h2' }))
slide(tip)
```

[A tip](tip): start engine two first.

## p-definition A definition

```js
const term = Text('Idempotent', { size: 'h1' }), means = Text('same result, however many times', { size: 'h3' })
slide(Column(Row(Part('key', { size: 'm' }), term), means))
```

[Idempotent](term) means [the same result, however many times](means) you run it.

## p-qa A question and its answer

```js
const q = Row(Part('question', { size: 's' }), Text('Why engine 2 first?', { size: 'h3' })), a = Row(Part('check', { size: 's' }), Text('Its pump runs the brakes', { size: 'h3' }))
slide(Column(q, a))
```

[Why engine two first](q)? [Its pump runs the brakes](a).

## p-cutout Cutout

```js
const engine = Cutout('assets/engine-cutout.png', { size: 'l', ratio: 3 / 2, tilt: -3 }), label = Text('a jet engine, cut from a photo', { size: 'h3' })
slide(Column(engine, label))
```

[A cutout](engine): [one thing from a photo](label), on nothing, placed like a drawing.
