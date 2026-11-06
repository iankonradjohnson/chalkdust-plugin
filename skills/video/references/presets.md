# Presets

A tested scene for every form and piece. Pick the one closest to what you're showing, copy its code into `scenes/<id>.html`, and change the words, drawings and data. Each one runs without a warning as it is.

A preset times things by words in its narration: `.on('server')` comes on when "server" is spoken, and each word is looked for after the one before. When you change the narration, keep those words, in that order, or change the code to match.

Generated from `brand/specimens` by `scripts/design_system.js`. The full list of pieces, forms and options is in `design-system.md`.

| Preset | Shows |
| --- | --- |
| `f-trace` | the form K.trace |
| `f-states` | the form K.states |
| `f-reshape` | the form K.reshape |
| `f-race` | the form K.race |
| `f-barrier` | the form K.barrier |
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
| `p-light` | light, badge, Form |
| `p-form` | Form, as a piece |

## `f-trace` · K.trace

Narration: "The browser asks the server which asks the database."

```html
<script>
scene(({ K }) => {
K.trace({ lang: 'js', hops: [
  { on: 'browser', label: 'Browser', icon: 'browser', carry: 'GET /', code: 'fetch(url)' },
  { on: 'server', label: 'Server', icon: 'server', carry: 'query', code: 'db.query(sql)' },
  { on: 'database', label: 'Database', icon: 'database', carry: 'rows', code: 'SELECT * FROM users' }] });
});
</script>
```

## `f-states` · K.states

Narration: "Idle then busy then done."

```html
<script>
scene(({ K }) => {
K.states({ states: [{ id: 'a', label: 'Idle', col: 0, row: 0 }, { id: 'b', label: 'Busy', col: 1, row: 0, color: 'yellow' }, { id: 'c', label: 'Done', col: 2, row: 0, color: 'green' }],
  start: { state: 'a', on: 'idle' }, steps: [{ from: 'a', to: 'b', on: 'busy', label: 'start' }, { from: 'b', to: 'c', on: 'done', label: 'finish' }] });
});
</script>
```

## `f-reshape` · K.reshape

Narration: "The row becomes the shape the browser wants with a new date and the old field dropped."

```html
<script>
scene(({ K }) => {
K.reshape({ via: 'map', from: { title: 'Row', fields: [{ name: 'id', value: 1 }, { name: 'name', value: 'Ann' }, { name: 'old' }] },
  to: { title: 'Response', fields: [{ name: 'id', from: 'id' }, { name: 'name', from: 'name' }, { name: 'date' }] },
  on: { from: 'row', to: 'shape', keep: 'browser', add: 'date', drop: 'dropped' } });
});
</script>
```

## `f-race` · K.race

Narration: "Two requests read then both write and one update is lost."

```html
<script>
scene(({ K }) => {
K.race({ lanes: ['Request A', 'Request B'], span: 10, fromOn: 'two', toOn: 'lost',
  events: [{ lane: 0, x: 2, label: 'read' }, { lane: 1, x: 3, label: 'read' }, { lane: 0, x: 6, label: 'write', kind: 'write' }, { lane: 1, x: 7, label: 'write', kind: 'bad' }],
  verdict: { text: 'one update lost', color: 'red', on: 'lost' } });
});
</script>
```

## `f-barrier` · K.barrier

Narration: "The app tries to delete files and read keys but the sandbox stops it and only the network passes."

```html
<script>
scene(({ K }) => {
K.barrier({ source: { label: 'App', icon: 'robot' }, wall: 'sandbox', rows: [
  { on: 'delete', attempt: 'delete', target: 'Disk', why: 'files' }, { on: 'keys', attempt: 'read', target: 'Keys', why: 'tokens' },
  { on: 'network', attempt: 'call', target: 'API', why: 'allowed', pass: true }] });
});
</script>
```

## `p-layout` · Row, Column, Grid, Part, Text, Labeled, Arrow

Narration: "The browser asks the server."

```html
<script>
slide(Column(Text('Layout pieces', { size: 'h2' }), Row(Labeled('Browser', Part('browser', { size: 'm' })), Arrow(), Labeled('Server', Part('server', { size: 'm' })).light('server')), Grid(4, Text('big', { size: 'caption' }), Text('h1', { size: 'caption' }), Text('h2', { size: 'caption' }), Text('h3', { size: 'caption' }))))
</script>
```

## `p-text` · Text sizes

Narration: "Five sizes of text."

```html
<script>
slide(Column(Text('Big', { size: 'big' }), Text('Heading one', { size: 'h1' }), Text('Heading two', { size: 'h2', color: 'blue' }), Text('Heading three', { size: 'h3' }), Text('A caption line', { size: 'caption' })))
</script>
```

## `p-flow` · Flow and Connect

Narration: "The browser calls the server which reads the cache and the database."

```html
<script>
const b = Part('browser', { size: 's' }), s = Part('server', { size: 's' }), c = Part('cache', { size: 's' }), d = Part('database', { size: 's' });
slide(Flow([[b, s, 'GET /'], [s, c], [s, d, { dashed: true }]]), Connect(b, d, { on: 'database', travel: 'query' }))
</script>
```

## `p-machine` · Machine and State

Narration: "Idle then busy then done."

```html
<script>
const idle = State('Idle'), busy = State('Busy', { color: 'yellow' }), done = State('Done', { color: 'green' });
slide(Machine([[idle, busy, 'start'], [busy, done, 'finish'], [busy, idle, 'cancel']], { start: idle, steps: [{ to: busy, on: 'busy' }, { to: done, on: 'done' }] }))
</script>
```

## `p-sequence` · Sequence

Narration: "The browser asks the server which queries the database."

```html
<script>
const a = Part('browser', { size: 's' }), b = Part('server', { size: 's' }), c = Part('database', { size: 's' });
slide(Sequence([a, b, c], [[a, b, 'GET /'], [b, c, 'query'], [c, b, 'rows', { reply: true }], [b, a, '200 OK', { reply: true }]]))
</script>
```

## `p-data` · Dots, Bars, Stat

Narration: "Most prompts were the same and only a few were new and it got faster."

```html
<script>
slide(Row(Dots(120, { groups: [{ count: 80, label: 'the same', color: 'red', on: 'same' }, { count: 10, label: 'new', color: 'green', on: 'new' }] }), Column(Bars([{ label: 'Before', value: 12, text: '12s', on: 'got' }, { label: 'After', value: 4, text: '4s', color: 'green', on: 'faster' }]), Stat(3, 'times faster', { suffix: '×', color: 'green' }))))
</script>
```

## `p-table` · Table

Narration: "Bob joined later."

```html
<script>
slide(Table(['Name', 'Joined', 'Plan'], [['Ann', 2019, 'Pilot'], { cells: ['Bob', 2021, 'Pilot'], on: 'Bob', color: 'green' }, ['Cy', 2023, 'Free']]))
</script>
```

## `p-code` · Code

Narration: "The handler reads the row."

```html
<script>
slide(Code('def handle(req):\n    row = db.get(req.id)\n    return render(row)', { lang: 'python', caption: 'app.py', highlight: [{ line: 2, on: 'reads' }] }))
</script>
```

## `p-diff` · Diff

Narration: "The fix adds a check."

```html
<script>
slide(Diff('def get(id):\n    return db[id]', 'def get(id):\n    if id not in db:\n        return None\n    return db[id]', { lang: 'python', change: 'check' }))
</script>
```

## `p-files` · Files

Narration: "The models file changes and the test is added."

```html
<script>
slide(Files(['src/app.py', 'src/db/models.py', 'tests/test_models.py', 'README.md'], { highlight: [{ path: 'src/db/models.py', on: 'models' }], added: ['tests/test_models.py'] }))
</script>
```

## `p-terminal` · Terminal

Narration: "Run the tests then push."

```html
<script>
slide(Terminal([{ cmd: 'npm test', on: 'run' }, { out: '12 passing', color: 'green' }, { cmd: 'git push', on: 'push' }, { out: 'main -> main' }], { title: 'zsh' }))
</script>
```

## `p-window` · Window

Narration: "The settings window."

```html
<script>
slide(Window(Part('gear'), { title: 'Settings' }))
</script>
```

## `p-scene` · Scene and Layer

Narration: "Over the hills."

```html
<script>
slide(Scene(Layer('mountains', { depth: 0.2 }), Layer('tree', { depth: 1 })), Text('Over the hills', { size: 'h1' }))
</script>
```

## `p-light` · light, badge, Form

Narration: "The person checks in and the server is in trouble."

```html
<script>
slide(Row(Labeled('lift', Part('person', { size: 'm' }).badge('check', { on: 'checks' }).light('in')), Labeled('spot', Part('server', { size: 'm' }).badge('warning').light('trouble', { color: 'red', style: 'spot' }))))
</script>
```

## `p-form` · Form, as a piece

Narration: "The app tries to delete files but only the network passes."

```html
<script>
slide(Form('barrier', { source: { label: 'App', icon: 'robot' }, wall: 'sandbox', rows: [{ on: 'delete', attempt: 'delete', target: 'Disk', why: 'files' }, { on: 'network', attempt: 'call', target: 'API', why: 'allowed', pass: true }] }))
</script>
```
