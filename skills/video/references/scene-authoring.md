# Scene authoring

**Read `design-system.md` first.** It lists every color, size, font, layout, drawing, piece, `K` helper, form, transition and diagram type there is, generated from the code, so what it names exists. This guide says how to put them together. `presets.md` has a tested scene for every form and piece: start from the closest one.

How to write `scenes.json` and `scenes/<id>.html`. The hosted service supplies the page template, the styles for every class named here, and GSAP and `scene-kit`, so scenes use them without loading anything. `examples/demo/` is a short worked example.

## Start here: the fast way

Name what you want and let the system color it. Every picture should be big and full, and show the actual thing being said: real code rather than made-up code, real numbers, and several things working together. A small cluster in the middle reads as thin, and the check warns about it. Too much in a layout shrinks to fit, so it can't overlap or run off the stage. Layouts are a quick start, not a limit, so place things by hand whenever that makes a better picture, and then look at a picture of that slide, because nothing protects it.

```html
<div class="slide">
  <div class="across far wide">
    <div class="down"><div id="b" data-part="browser" class="l"></div><div class="h3">Browser</div></div>
    <div class="down"><div id="d" data-part="database" class="l"></div><div class="h3">Database</div></div>
  </div>
  <div id="t" class="big c-red">0</div>
</div>
<script>
scene(({ K }) => K.say(`
  browser   #b
  database  #d in; arrow #b #d; light #d red
  twenty    count #t 20 suffix=s; #t fade
  index     morph #t color=var(--green) +0.4
`));
</script>
```

**Show how things connect first.** Choose the move by what the voice is saying:

| The voice says | Show it with |
| --- | --- |
| One thing leads to, calls or sends to another | `arrow #a #b`, or `K.travel` for something moving along it |
| Steps in a system, or code running | `K.trace`, `K.states` or `K.barrier` (see [Forms](#forms-for-explaining-code)) |
| How parts are structured | `Flow`, `Sequence` or `Machine` ([Diagrams](#diagrams-our-own-pieces)), `Tree` for what branches, `Stack` for layers (`nest: true` for what runs inside what) |
| Steps in time, or a loop | `Timeline` (`down: true` for a card each), `Cycle` for steps that come back round |
| This versus that | `Compare`, two cards side by side with good points green and bad ones red |
| One thing becoming another | `rewrite`, `swap`, `K.reshape` or `move` |
| Amounts and comparisons | `Bars` and `Stat`, `Line` for change over time (`trend: true` when the trend is the point), `count` |
| Look at this exact thing | `light` or `mark`, as the last resort, and at most one or two per slide. In code, light the one word: `highlight: [{ word: 'retries', on: 'retries' }]` |

- **Things come on as they're said.** A piece, a caption, a Compare point, a Timeline step, a Stack layer or a bar with no `.on` of its own comes on when the narration first says its own words, and a Flow, Tree or Cycle builds along its arrows to it. So name things in the narration in the order you want them to appear, and give `.on('word')` only when the word that should bring it on isn't one of its own. Don't put `.at(0.1)` on everything: the build warns when a label is on screen long before it's said.
- **Mark what to show in the narration.** Put backticks around a word in a beat's narration, and what it names on screen follows it: the first mark brings it on, and every later mark lights it again. "The `browser` asks, and `Flow` builds along its arrows" brings on the Browser and lights `Flow` in the code; "back to `Sonnet`" lights the caption Sonnet writes. It works for every piece: drawings, captions, text, code, Compare points, Stack layers, Timeline steps and bars. The voice and the captions get the plain words. Mark the first mention of each thing, and every name you point at after, about one a sentence. Keep `.on('word')` for verbs a mark can't say: swap, travel, count. The build warns when you name something on screen and nothing about it moves, and when a marked word isn't in what the voice said.
- **Every light ends.** A light goes out when the next thing on the slide lights, so only what's being talked about is lit. Give it its own end with `.light('word', { until: 'other' })`, or `unlight` in `K.say`; say `keep` (`{ keep: true }`, or `light #a keep`) only when it should stay on. Code highlights end the same way.
- **Long code wraps** by itself, so paste real lines; keep a block short rather than shrinking it.

- **Layouts:** `.slide` fills the area under the title and centers its contents. Inside it use `.across` (add `.far` when an arrow goes between things), `.down`, and `.grid` (`.n2`, `.n4` or `.n5` for the number of columns, 3 by default). `.left` left-aligns, `.wide` takes the full width, and `.fill` takes the leftover room.
- **Text:** `.big`, `.h1`, `.h2`, `.h3`, `.caption`. Color it with `.c-<name>` for any color in `design-system.md`, like `.c-blue`, `.c-yellow`, `.c-red`, `.c-green` or `.c-muted`.
- **Drawings:** use our own, with `data-part` and `chalkdust parts <words>`. They take `.s`, `.m`, `.l` or `.xl`. Don't use stock line icons. `data-icon` still works, and it draws our version of that thing when we have one. `.tile` is a card. `.bar` with `style="--v:60%"` is a chart bar.
- **Colors:** in hand-written CSS, use `var(--ink)`, `var(--muted)`, `var(--surface)`, `var(--line)` or `var(--<name>)` for any color in `design-system.md` (`var(--amber)` is yellow), so light and dark both work. Only flat colors.
- **`K.say`:** one line per moment. A line starts with a word from the narration, and each line looks for its word after the previous one, so repeats just work and digits or near misses still match. It can also start with `+1.5` (seconds after the last line) or `@2` or `@2.5` (beat 2, or halfway through it). The first thing on a line is always its time, so to run a move half a second later, write `+0.5 arrow #a #b`. A line that starts with a selector is the one exception. After that, moves separated by `;`: any `K` helper by name, then selectors, `"text"`, numbers, `name=value`, a `+0.3` nudge, and bare words such as `red`, `in`, `fade`, `box` or `left`. A selector alone means show, and a selector matching several elements goes through them in turn. `spot` takes `until=word`. Selectors can't contain spaces, so give the element a class.
- **Cuts:** a new slide is a cut. So is `cut #two` between sibling `.slide` or `.layer` blocks in one scene, which also clears lines drawn so far, ends any spot and resets the camera. Later blocks stay hidden until cut to.
- Arrows and marks measure where things are when the scene loads, so don't change the text of something next to them, except with `K.count`, which holds its width.

Everything below still works when a scene needs something special, including exact positions. A project is dark by default, and a file called `theme` containing `light` or `navy` changes that.

## Contents

- [scenes.json](#scenesjson)
- [Transitions between scenes](#transitions-between-scenes)
- [Timing: data-b, data-f, data-o, data-d](#timing)
- [Animation classes](#animation-classes)
- [Building blocks](#building-blocks)
- [Arrows and moving things](#arrows-and-moving-things)
- [Code with line highlights](#code-with-line-highlights)
- [Layout rules](#layout-rules)
- [GSAP scenes with scene-kit](#gsap-scenes-with-scene-kit)
- [Icons and richer shapes](#icons-and-richer-shapes)
- [Forms for explaining code](#forms-for-explaining-code)
- [Diagrams: our own pieces](#diagrams-our-own-pieces)
- [Images](#images)
- [Links](#links)
- [Patterns that worked](#patterns-that-worked)

## scenes.json

```json
[
  {"id": "s01", "kicker": "1 · What a route is", "title": "A route is one backend HTTP endpoint", "beats": [
    {"say": "A route is one backend HTTP endpoint. Here it's GET internal users, by id.",
     "cap": "A route is one backend HTTP endpoint. Here it's GET /internal/users/:id."},
    {"say": "Each module folder has the same files."}
  ]}
]
```

- A **beat** is one or two sentences of narration and the animations that go with it. Each beat is a separate TTS call, so start each one at a sentence boundary.
- `say` is what the voice reads. Spell symbols out ("request dot auth", "colon goal id"), because TTS mangles `request.auth` and `/api/goals/:goalId`.
- `cap` (optional) is the caption when it should differ from `say`, for example to show the real identifier. The caption is split into sentences, and each one is timed by its share of the beat's characters.
- An empty `title` hides the header. The title scene (`s00`) does this and draws its own large title.
- Scene ids sort in order. Use `s00`, `s01`, and so on.

## Transitions between scenes

Every scene after the first crossfades in, so slides don't change abruptly. You don't need to do anything. To change that, add `transition` to the scene in `scenes.json`. It describes how this scene comes in:

```json
{"id": "s02", "kicker": "2 · The fix", "title": "Retry with backoff", "transition": "fade", "beats": [...]}
```

| `transition` | Effect | Use for |
| --- | --- | --- |
| `cut` | Hard cut | A deliberate jolt, like a sudden change of subject |
| `fade` | Crossfade. The default. | Almost everything |
| `slide` | The new scene pushes the old one off to the left | Moving on to the next step in a sequence |
| `slide-up` | The new scene pushes the old one off the top | Going deeper into the same thing |

`transition_dur` (optional) sets the length in seconds, from 0.1 to 1. The default is 0.6, or 0.4 for a streamed slide, whose pauses are shorter.

- A transition is centred on the boundary between the scenes and plays in the silence already there, so **it never moves the narration, the timeline or existing comments**. Adding or changing one needs no new narration, and a rebuild takes seconds.
- During the overlap, both scenes run on the audio clock. The outgoing one holds its final picture, and the incoming one holds its first until the boundary. Its first beat starts after the transition ends, so nothing is missed.
- So the first frame of the incoming scene shows during the transition. Anything with no entrance animation is already visible as it arrives.
- The first scene has nothing to come in from, so giving it a transition fails the build, as does an unknown name or a length outside the range. An answer clip's first scene follows the same rule, and transitions work between the scenes inside a clip.
- Stills show each scene on its own, so they don't show transitions. Check them in the player.

## Timing

Every animated element names the beat it belongs to. `template.html` turns these attributes into an `animation-delay`:

| Attribute | Meaning |
| --- | --- |
| `data-b="2"` | Starts when beat 2's narration starts (0-indexed, within this scene) |
| `data-f="0.5"` | Plus this fraction of the beat's spoken length. Use it to land on a word partway through the beat. |
| `data-o="0.3"` | Plus this many seconds |
| `data-d="1.4"` | Overrides the animation's duration, in seconds |

To sync with a specific word, estimate its position by character count. "It drops four columns: email verified, image, created at, and updated at" puts the four strike-throughs at about f = 0.3, 0.48, 0.66, and 0.84.

An element with no `data-b` is visible from the first frame.

Beats are numbered from 0, and using one past the last, in `data-b` or `at()`, stops the scene from loading. The build refuses it, so if you remove a beat, renumber what used it.

## Animation classes

All of them use `fill: both`, so an element is in its "from" state before its delay and stays in its "to" state after.

| Class | Effect | Use for |
| --- | --- | --- |
| `a-in` | Fade in and rise 18px | Boxes, cards, notes, code |
| `a-pop` | Scale in with a small overshoot | Key boxes, labels, results |
| `a-fade` | Plain fade in | Labels, frames, highlight bars |
| `a-out` | Fade to 0 | Removing a note (wrap it in `.layer`) |
| `a-dim` | Fade to 0.28 | De-emphasizing the inputs once they're merged |
| `a-draw` | Draws an SVG path. Needs `pathLength="1"`. | Arrows |
| `a-strike` | Red line grows across | Dropped fields (`.sline` inside a `position:relative` span) |
| `a-glow` / `a-glowred` | Yellow or red ring pulse that settles | Pointing at a field, or flagging a problem |
| `a-press` | Button press | Click moments |
| `a-fly` | Moves along `offset-path`, fading in and out | Packets, events, labels traveling |
| `a-flystay` | Moves along `offset-path` and stays at the end | Something that arrives and remains |
| `a-cap` | Captions (internal) | — |

You need a wrapper to give one element two animations, for example "appear at beat 0, then dim at beat 2". The outer element gets one class and the inner element the other. `.layer` is a full-screen, absolutely positioned wrapper. Children keep page coordinates, so `<div class="layer a-dim" data-b="1">…pills…</div>` dims a group.

Dashed paths (`class="dash a-draw"`) fade in rather than draw, because the dash pattern and the draw trick both use `stroke-dasharray`.

Don't use infinite animations. The renderer copies static frames forward and only re-renders frames where some animation is active. An infinite animation forces every frame to render and also never settles.

## Building blocks

The canvas is 1920×1080. Everything is absolutely positioned with inline `left`, `top`, `width`, and `height`.

- `.box`: a centered card. Variants are `.amber` (schemas, marks), `.green` (correct/ok), `.red` (problems), `.sketch` (dashed, "proposed"), `.ghost`, and `.left` (left-aligned). Put a `<small>` inside for a subtitle.
- `.card` with `<h3>` and `.row` children: a vertical list of fields, such as a table's columns or a response's fields. Rows are 46px.
- `.frame` with `<span class="lbl">`: a dashed group outline with a label, such as a folder or a transaction.
- `.label`: the one label, a small quiet patch for a word or two: a route, a status, a tag. There's no pill, badge or chip.
- `.note`, `.note.red`, `.note.blue`: callouts.
- A `.label` can travel along a path with `a-fly` ("title", "item event").
- `.dot`: a glowing dot that travels along a path.
- `.lbltxt`: small grey label text.
- `.mark`: yellow bold text, for a translatable mark or a highlighted value.

## Arrows and moving things

One `<svg class="ov">` per scene covers the canvas in page coordinates:

```html
<svg class="ov">
  <path class="a-draw" data-b="1" data-f="0.35" pathLength="1" d="M760 420 L818 420"/>
  <path class="amber dash a-draw" data-b="2" pathLength="1" d="M720 608 L720 484"/>
</svg>
<div class="dots">
  <div class="dot a-fly" data-b="1" data-f="0.85" data-d="1.8" style="offset-path:path('M412 420 L1600 420')"></div>
  <div class="label a-fly" data-b="4" data-f="0.6" data-d="1.3" style="offset-path:path('M1660 715 L1660 850')">title</div>
</div>
```

Path colors are `amber`, `red`, and `green`, with blue as the default. Reuse the same `d` for an arrow and for the dot that travels on it. Start and end arrows 2px outside the box edges.

## Code with line highlights

```html
<div class="code a-in" data-b="0" style="left:100px;top:245px;width:1190px">
  <div class="hl a-fade" data-b="2" style="top:224px"></div>
  <div class="hl red a-fade" data-b="3" style="top:384px;height:120px"></div>
<pre><code class="language-typescript">…HTML-escaped code…</code></pre>
</div>
```

A line is 40px tall, and the `pre` has 24px of top padding. A bar for line *n* (0-indexed, counting every line in the block, including blank ones) is at `top: 24 + 40n`, and spanning *k* lines means `height: 40k`. A line fits about 72 characters in 1190px, and in this hand-placed block a longer one doesn't wrap, so break it yourself (the `Code` piece wraps by itself). Trim real code with `…` rather than shrink the font. Don't put the file name or line numbers on screen: say them in the narration, or in chat.

## Layout rules

- **The header** is the kicker at y≈56 and the title at y≈92–160. Content starts at y 200–240.
- **The caption zone** is y > 950. Keep content above about 940. A two-line caption reaches up to about y 946.
- **The right edge** is 1880. Leave 40px or more of margin.
- **Positioning**: classed building blocks are absolutely positioned already. A plain `div` isn't, so give it `position:absolute`.
- **Text widths**: monospace at 26px is about 15.6px per character. A label's width must fit its text plus its padding, or it wraps, and it needs a height of at least 60px. This was the most common layout bug.
- **Arrows** must not pass through boxes or labels. Route returns below a row of boxes, in the gap between the boxes and their labels.
- Put one idea on screen at a time. Build it up across beats, and don't show the finished diagram on the first frame.

## GSAP scenes with scene-kit

For arrows with heads, data moving along them, text that changes in place, a spotlight or a camera move, write the scene with `scene-kit` instead of CSS classes. A scene registers one function, and the template hands it the toolkit `K`, the narration's timing `at`, and a schedule `tl`. The schedule takes GSAP's `tl.to`, `tl.fromTo` and `tl.set`, with the same options, but it records the moves as data instead of animating: `scripts/vendor/render.js` draws each moment from it, and the player and renderer drive it through `window.__seek(t)`, so it scrubs exactly like the CSS animations. Pages don't load GSAP itself, so a scene can't call it directly. Both kinds can sit in the same scene.

Give elements an `id` and plain inline positions, with no `a-*` class and no `data-b`. Then time everything with `at(beat, fraction, seconds)`:

```html
<div id="br" class="box" style="left:100px;top:440px;width:300px;height:140px">Browser</div>
<div id="is" class="box" style="left:1260px;top:660px;width:440px;height:130px">interactions-service</div>
<script>
scene(({ at, K }) => {
  K.show('#br', { at: at(0, 0.05) });                          // pop in (kind: 'in' | 'fade')
  K.show('#is', { at: at(2, 0.45) });
  const a = K.arrow('#br', '#is', { at: at(2, 0.5), color: 'red', fromSide: 'bottom', toSide: 'left', flow: 2 });
  K.travel('request', a, { at: at(2, 0.7) });                  // a label rides the arrow
  K.morph('#is', { borderColor: '#e5534b', backgroundColor: '#3a1616' }, { at: at(3, 0.3) });
  K.spot(['#br', '#is'], { at: at(3, 0.15) });                 // dim everything else
});
</script>
```

| Helper | Does |
| --- | --- |
| `K.arrow(from, to, o)` | Curved arrow between two elements, drawn on, with a head that lands at the end. Without sides, perfect-arrows picks the edges. Use `fromSide` and `toSide` (`'right'`, `'bottom@0.3'`) to stop two arrows sharing an edge, and `curve` (0.25 to 0.5) for how much it bends. `color`: blue, green, amber, red, yellow. `flow: n` runs dots along it n times. `dashed: true`. Returns the path. |
| `K.path(d, o)` | The same for a hand-written SVG path. Pass `head: {x, y, angle}` (radians) for an arrowhead. |
| `K.travel(textOrSelector, path, o)` | A label, or an existing element, moves along a path. `stay: true` keeps it at the end. |
| `K.swap(sel, text, o)` | The text lifts away and the new text settles in, in the same spot. Use it for English → Spanish. Optional `color`. |
| `K.type(sel, text, o)` | Types text letter by letter. |
| `K.show / K.hide(sel, o)` | Enter or leave. `hide` also takes an arrow, and removes its head too. Pick the `kind` by what the entrance means: `slide` came from elsewhere (`from`: left, right, top, bottom), `grow` comes out of the thing above it. `pop`, `in` and `fade` are neutral, so don't use one for everything. |
| `K.morph(sel, vars, o)` | Tween any CSS: border color, background, size. |
| `K.spot(keep[], o)` | Dim everything else and ring the kept elements. `until` restores them. |
| `K.cam(selOrRect, o)` | Zoom so the target fills the stage. `reset: true` zooms back out. |
| `K.stagger(sel, o)` | A list enters one item after another (`each` seconds apart). |
| `K.move(sel, to, o)` | The same element travels to another element's center, or to `{x, y}`, so nobody has to be told it's the same thing. `style: {...}` changes other CSS on the way. Arrows don't follow, so draw them after the move. |
| `K.icon(sel, o)` | Draws an icon on, line by line. See [Icons and richer shapes](#icons-and-richer-shapes). |
| `K.light(sel, o)` | Lights something up to show it's active. By default it lifts: it rises with a soft shadow, and its color goes on its border and any icon inside. `color`: blue, green, amber, red, yellow. `style`: `glow`, `ring`, `card` or `spot` for another look. |
| `K.drift(sel, o)` | A slow constant move, so a held picture isn't dead still. No selector moves the whole stage. `scale`, `x`, `y`, `dur`. Don't combine the whole-stage form with `K.cam`. |
| `K.parallax({sel: depth}, o)` | Layers slide at different speeds, which reads as depth. Depth 0 stays still, 1 moves the full `x` or `y`. Make layers wider than the stage. |
| `K.mark(sel, o)` | Draws on something already on screen. `kind`: underline or box. `color`. It measures text when the scene loads, so don't use it on a `K.count` number. |
| `K.cut(sel, o)` | A hard cut to another `.slide` or `.layer` beside this one. |
| `K.unlight(sel, o)` | Turns off `K.light`. |
| `K.words(sel, o)` | Text arrives word by word. `spoken: true` lands each word as the narration says it, so the text must match the narration; use `beat` to limit it to one beat. |
| `K.count(sel, to, o)` | A number counts up. `from`, `dur`, `format: (n) => ...`. |
| `K.wipe(sel, o)` | Reveals by sweeping across. `from`: left, right, top, bottom. |
| `K.rewrite(sel, text, o)` | Text becomes new text, and the words they share travel to their new places. Good for a line of code or an equation changing. |

**Time things to the word.** `at.word('Altair')` is the moment that word is spoken, measured from a transcription of the audio, so prefer it to guessing a fraction. It takes `{ beat, nth, o }`: limit it to one beat, pick a later occurrence, or shift by some seconds. `K.swap` changes the text about 0.24 s after it starts, so use `o: -0.24` to land the new word on the spoken one. A word that isn't in the transcript warns at build time. Only scenes that use `at.word` pay for transcription: the first build of each line takes longer and costs a little, so in answer clips use it where the sync matters, and `at(beat, fraction)` elsewhere.

The build warns when a slide stays still for more than about six seconds. Fix it with a move or a cut that shows what the voice is saying, not with decoration.

The usual layout rules still apply. Arrows must not cross boxes or labels. Pick sides so arrows leaving the same box use different edges. Never write a literal script end tag inside a scene script.

## Icons and richer shapes

Make things look like what they are, using our own drawings (see the next section), and never an emoji. `data-icon="name"` draws our version of that thing, and a name we have no drawing for falls back to a stock line icon with a warning, so prefer `data-part`. Size them with `width` and `height`, or `.s`, `.m`, `.l` or `.xl`.

- `.panel` is a card with depth. `.window` is a browser frame for a screenshot. `.box.row` puts a drawing and its label side by side.
- Make the important things large. A diagram should fill the stage, not sit small in the middle of it.
- An image has to explain something, or leave it out. Real screenshots are the best kind, and you can point at the part that matters with `K.path` or `K.mark`.

## Parts: drawings that already exist

Look before you draw: `chalkdust parts lighthouse ship`. Use what it finds with `<div data-part="name" class="l"></div>`, and move it like any other element. A part keeps its shape inside its box, so add `data-stretch` for a background layer that has to fill it. The library covers most things. Draw something new, as an inline SVG, only if the answer really needs it, because drawing takes time.

## Forms for explaining code

Five helpers for how code behaves. **Reach for one first when a scene explains code.** You pass data and times, and the form does the layout and animation, so it takes far less writing than placing boxes by hand. `K.reshape` fills the stage. `K.trace` fills the upper two thirds. Each `K.race` takes about 340px from its `top`, so call it twice or put a code block under it. Anything that isn't one of the five below, build by hand. A form's elements behave like any others, so you can add `K` calls around it. Use real code in `code`, and keep labels to a few words.

| The explanation is about | Use |
| --- | --- |
| Something moving through a system and changing on the way | `K.trace` |
| Something that's in one state at a time, and what moves it | `K.states` |
| One data shape becoming another | `K.reshape` |
| Timing: two things at once, where the order decides the outcome | `K.race` |
| Separate attempts stopped at a wall, like security checks | `K.barrier` |

**Timing by word:** give a step `on: 'word'` instead of `at`, and it lands on that spoken word. Steps in a list look for their word after the one before, so a repeated word just works. `beat` limits the search and `o` adds seconds. `K.reshape` takes `on: { keep: 'word', add: 'word' }`, and `K.race` takes `fromOn` and `toOn`. Words must match the narration as spoken, and the build warns when one doesn't. You can also give `at`, a time in seconds from `at(beat, fraction)`. Icons are any Lucide name, written as `icon: 'name'`.

```html
<script>
scene(({ at, K }) => {
  K.trace({
    lang: 'python',
    hops: [
      { at: at(0, 0.2), label: 'Browser', icon: 'globe', carry: 'cookie', job: 'sends', code: "fetch('/me')", file: 'app.js' },
      { at: at(1, 0.1), label: 'API', icon: 'server', carry: 'user id', job: 'checks', code: 'user = session.get(cookie)', file: 'auth.py' },
      { at: at(2, 0.1), label: 'Database', icon: 'database', carry: 'row', job: 'reads', color: 'green' },
    ],
  });
});
</script>
```

`hops` holds 3–6 items. `carry` is the moving label's text at that hop, and it changes in place. `job` and `code` are optional.

```js
K.states({
  lang: 'python', code: 'if not paid:\n    return "open"\nreturn "closed"',   // optional: real code beside the diagram
  states: [{ id: 'open', label: 'open', col: 0, row: 0 }, { id: 'closed', label: 'closed', col: 1, row: 0, color: 'green' }],
  start: { state: 'open', at: at(0, 0.3), line: 1 },                             // line: 0-indexed line of code to highlight
  steps: [{ from: 'open', to: 'closed', label: 'pay', at: at(1, 0.2), line: 2 }],
});
```

`col` and `row` place the states on a grid. A state appears when it's first reached, and only the current one stays lit. `fromSide` and `toSide` on a step keep two arrows apart.

```js
K.reshape({
  via: 'toResponse()',
  from: { title: 'database row', fields: [{ name: 'id' }, { name: 'email' }, { name: 'created_at' }] },
  to: { title: 'API response', fields: [{ name: 'id', from: 'id' }, { name: 'createdAt', from: 'created_at' }, { name: 'href' }] },
  at: { from: at(0), to: at(0, 0.5), keep: at(1), rename: at(1, 0.5), drop: at(2), add: at(3) },
});
```

A target field's `from` names its source field. Same name: it flies across. Different name: it flies across and turns amber. No `from`: it's new, and turns green. A source field nothing uses gets struck out. Each field can have a `value`. Fit up to 8 rows, and give `at` the times for the kinds you use.

```js
K.race({
  top: 262, lanes: ['Comment A', 'Comment B'], span: 10, from: at(1), to: at(1, 0.9),
  shared: { label: 'file', values: [{ x: 0, text: '[ ]' }, { x: 7, text: '[B]  A is lost', bad: true }] },
  events: [{ lane: 0, x: 1, label: 'read [ ]' }, { lane: 1, x: 7, label: 'write [B]', kind: 'bad' }],
  holds: [{ lane: 1, x1: 1.5, x2: 4.5, label: 'waits' }],
  verdict: { text: 'no lock', color: 'red', at: at(0, 0.8) },
});
```

A playhead sweeps from time `from` to time `to`, and each event appears as it passes, so `x` runs from 0 to `span`. `kind` is `read`, `write`, `bad` or `good`. `shared` is optional, and shows the value both sides are fighting over. To compare a broken run with a fixed one, call it twice with `top: 262` and `top: 630`.

```js
K.barrier({
  source: { label: 'Scene', icon: 'file-code' }, wall: 'sandbox + policy',
  rows: [
    { on: 'cookie', attempt: 'document.cookie', target: 'session cookie', why: 'HttpOnly' },
    { on: 'fetch', attempt: 'fetch(api)', target: 'the API', why: "connect-src 'none'" },
    { on: 'pause', attempt: 'postMessage(pause)', target: 'the player', why: 'allowed list', pass: true },
  ],
});
```

Each row is one attempt, stopped at the wall unless it has `pass: true`. Fit up to 5 rows.

## Diagrams: our own pieces

For anything with real structure, draw it with our pieces, not boxes placed by hand. They lay themselves out, use our drawings, and build up in step with the narration. `examples/demo/`, next to this guide's folder, has working examples.

- **Something flows from one thing to the next:** `Flow([[a, b, 'label'], [b, c]])`. Each node comes on as the arrow reaching it draws.
- **Who sends what to whom, in order:** `Sequence([a, b, c], [[a, b, 'GET /', { on: 'asks' }], [b, a, '200', { reply: true }]])`.
- **States and what moves between them:** `Machine([[idle, busy, 'start']], { start: idle, steps: [{ to: busy, on: 'busy' }] })`.

```html
<script>
const player = Labeled('Player', Part('browser', { size: 's' })).on('player');
const agent = Labeled('Agent', Part('robot', { size: 's' })).on('agent');
slide(Sequence([player, agent], [[player, agent, 'question saved', { on: 'saved' }], [agent, player, 'answer ready', { reply: true, on: 'plays' }]]));
</script>
```

## Images

Put images in `<project>/assets/` and reference them as `src="assets/name.png"`. The build inlines them, so the page stays self-contained. Use them only when the image carries the idea, such as a real screenshot or a real chart. Decorative images tend to hurt learning.

```html
<img id="shot" class="shot" src="assets/player.jpg" style="left:120px;top:210px;width:600px;height:700px">
```

Treat a screenshot as published: check it for local paths, names and anything private before using it.

## Links

Any `<a href>` on the stage is clickable in the live player. It opens in a new tab and pauses the video. Clicking anywhere else plays or pauses. A link that hasn't appeared yet doesn't respond. Give it a class to style it as a building block: `<a class="box green" href="…" style="…">`.

**Link code to its file.** When the code comes from a repository you can reach on GitHub (it has a GitHub remote, or `gh` works), give `Code` and `Diff` the file's link, at the commit or branch you read it from, and the line if you can: `Code(src, { lang: 'py', link: 'https://github.com/owner/repo/blob/main/app/orders.py#L40' })`. The block shows the file's name and opens it when clicked, so the viewer can go to the real code. Prefer this to naming the file in the narration. Only `https://` links work.

## Patterns that worked

- **Request flow**: a request label, then boxes for each layer, then a dot traveling across, then a green return path to a response label, then a short label under each box naming its job.
- **Shape transform**: a source card of fields, then a mapper box, then a result card. Dropped fields get a strike, renamed fields get a red glow on both sides with a "≠" note.
- **Many-to-one**: concrete items on the left, arrows converging on one template label, then the inputs dim.
- **Counter**: stack number divs at the same spot with a solid background, each `a-fade` with `data-d="0.12"` at a later `data-f`.
- **Branching decision**: a question box, then a "yes" branch in amber and a "not yet" branch in red with `a-glowred` at the end of the beat.
- **Checklist finale**: one `.box.left` per item, 96px apart, timed to "One… Two… Three…" in the narration.
