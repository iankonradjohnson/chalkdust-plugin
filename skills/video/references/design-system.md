# The design system

Read this first, before writing any scene. It lists everything a scene can use: every color, size, font and text class, every layout, every drawing, every piece a slide is made of with its options, every `K` helper and form, and the transitions. Diagrams are drawn with our own pieces: `Flow`, `Sequence` and `Machine`. `scene-authoring.md` says how to put them together.

It is generated from the code by `scripts/design_system.js`, so if something is here it exists, and if it isn't here it doesn't. Use what is here rather than drawing plain boxes: a folder is `Part('folder')` or `data-part="folder"`, not a rectangle.

## Colors

One set of names, in every theme and every place: `var(--name)` in CSS, `.c-name` for text, `K.light(el, { color: 'name' })`, and a piece's `color` option. Name a color, never write a hex value, so light and dark both work. Prefer the brand's accents (`blue`, `green`, `yellow`, `red`) and the screen's own `ink`, `muted`, `surface` and `line`; the drawing colors are for the rare hand-drawn shape.

| Name | Slate (dark) | Chalk (light) | Kind |
| --- | --- | --- | --- |
| `bg` | #121519 | #FFFFFF | screen |
| `bg-deep` | #0B0E12 | #F4F4F2 | screen |
| `surface` | #1D2128 | #F4F4F2 | screen |
| `surface-2` | #252A33 | #EBEBE7 | screen |
| `line` | #30363F | #E2E2DE | screen |
| `line-strong` | #454C57 | #CFCFC9 | screen |
| `ink` | #F6F4EE | #2A2A28 | screen |
| `ink-2` | #D9D6CE | #3F3F3C | screen |
| `muted` | #A8A6A0 | #6A6963 | screen |
| `faint` | #6F6D68 | #9A9892 | screen |
| `yellow` | #F5D76E | #E9BE3C | screen |
| `yellow-text` | #F5D76E | #8A6A00 | screen |
| `blue-hover` | #6FA3FF | #1A55CF | screen |
| `blue-ink` | #0B0E12 | #FFFFFF | screen |
| `blue-soft` | rgba(77, 141, 255, .14) | rgba(31, 100, 242, .10) | screen |
| `red-soft` | rgba(255, 90, 79, .14) | rgba(217, 58, 47, .10) | screen |
| `green-soft` | rgba(53, 208, 127, .14) | rgba(15, 154, 76, .10) | screen |
| `orange` | #e0a23a | #e0a23a | drawing |
| `orange-dark` | #c98f28 | #c98f28 | drawing |
| `gold` | #f5d76e | #f0c43c | drawing |
| `cream` | #f4ead2 | #dfcd9c | drawing |
| `chalk` | #f4f2ec | #e4e6ea | drawing |
| `steel` | #a9b4c0 | #97a2af | drawing |
| `slate-grey` | #6b7a8a | #6b7a8a | drawing |
| `slate` | #4b5d70 | #4b5d70 | drawing |
| `slate-dark` | #2c3a49 | #2c3a49 | drawing |
| `red` | #ff5a4f | #d93a2f | drawing |
| `red-light` | #ff8f87 | #e88780 | drawing |
| `blue-dark` | #3663b2 | #184dba | drawing |
| `blue` | #4d8dff | #1f64f2 | drawing |
| `blue-light` | #91b8ff | #84aaf8 | drawing |
| `green` | #35d07f | #0f9a4c | drawing |
| `green-dark` | #26965b | #0c7a3c | drawing |
| `green-light` | #86e3b2 | #80c9a0 | drawing |
| `wood` | #7a4a2a | #7a4a2a | drawing |
| `wood-dark` | #5a3620 | #5a3620 | drawing |
| `skin` | #f0c6a0 | #f0c6a0 | drawing |
| `amber` | #F5D76E | #E9BE3C | same as yellow |

A project is Slate (dark) unless a file called `theme` says `light` (Chalk) or `navy`, the old look, which changes the screen colors `bg`, `surface`, `line`, `ink`, `muted`, `blue`, `yellow`, `red`, `green`, `yellow-text` and adds `--bg-image` and `--panel`. `.c-yellow` and `.c-amber` use `yellow-text`, which stays readable on Chalk.

## Fonts and text

| Variable | Font |
| --- | --- |
| `--font` | "Instrument Sans", -apple-system, "Segoe UI", sans-serif |
| `--title` | Fraunces, Georgia, serif |
| `--code` | "JetBrains Mono", ui-monospace, Menlo, monospace |

| Class | For | CSS |
| --- | --- | --- |
| `.big` | one huge number or word | `font-size: 160px; font-weight: 800; line-height: 1.05;` |
| `.h1` | the slide's main words | `font-size: 84px; font-weight: 800; line-height: 1.1; letter-spacing: -.02em;` |
| `.h2` | a heading | `font-size: 62px; font-weight: 700; line-height: 1.15;` |
| `.h3` | a label under a drawing | `font-size: 46px; font-weight: 600; line-height: 1.2;` |
| `.caption` | a quiet line | `font-size: 32px; font-weight: 500; color: var(--muted);` |
| `.small` | small grey text | `font-size: 21px; color: var(--muted);` |
| `.mono` | code font | `font-family: var(--code);` |
| `.g-serif` | Fraunces, as titles use it | `font-family: var(--title); font-variation-settings: 'opsz' 96, 'SOFT' 100, 'WONK' 0;` |
| `.mark` | a word pointed at, in the accent (add `.c-green` or another for another color) | `color: var(--blue); font-weight: 700;` |

Text colors: `.c-<color>` for any color above, like `.c-blue`, `.c-red` or `.c-muted`.

## Sizes

A drawing (`data-part`) or icon (`data-icon`) takes one size class. `Part(name, { size })` takes the same names.

| Class | Width and height |
| --- | --- |
| `.s` | 170px |
| `.m` | 290px |
| `.l` | 430px |
| `.xl` | 620px |

## Layouts

Inside `.slide`, which fills the area under the title and centers what it holds. Too much in a layout shrinks to fit.

| Class | For | CSS |
| --- | --- | --- |
| `.slide` | the area under the title | `position: absolute; left: 100px; right: 100px; top: 190px; bottom: 130px; display: flex; flex-direction: column; gap: 36px; align-items: center; justify-content: center; text-align: center;` |
| `.across` | a row | `display: flex; gap: 48px; align-items: center; justify-content: center;` |
| `.far` | a row with room for arrows | `gap: 170px;` |
| `.down` | a column | `display: flex; flex-direction: column; gap: 28px; align-items: center; justify-content: center;` |
| `.grid` | equal columns, 3 by default | `display: grid; grid-template-columns: repeat(var(--n, 3), 1fr); gap: 32px; align-items: center; justify-items: center;` |
| `.n2` | 2 columns in a grid | `--n: 2;` |
| `.n4` | 4 columns | `--n: 4;` |
| `.n5` | 5 columns | `--n: 5;` |
| `.left` | left-aligned (with `.slide` or `.down`) | `align-items: flex-start; text-align: left; justify-content: flex-start;` |
| `.wide` | the full width | `width: 100%;` |
| `.fill` | the leftover room | `flex: 1; min-width: 0;` |
| `.layer` | a full-stage wrapper | `position: absolute; left: 0; top: 0; width: 1920px; height: 1080px;` |

## Building blocks

| Class | For | CSS |
| --- | --- | --- |
| `.card` | the card: a slate panel, no border, with an `<h3>` title in Fraunces. `.amber` lit, `.green` done, `.red` trouble, each a thin outline | `position: absolute; background: var(--surface); border: 0; border-radius: var(--r); padding: 24px 30px;` |
| `.tile` | the same card, in a layout | `background: var(--surface); border: 0; border-radius: var(--r); padding: 24px 36px;` |
| `.box` | the same card, placed by hand (`.amber`, `.green`, `.red`, `.ghost`, `.sketch`, `.left`, `.row`) | `position: absolute; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; background: var(--surface); border: 0; border-radius: var(--r); font-size: 28px; line-height: 1.3; padding: 12px 20px;` |
| `.panel` | the same card, as the forms use it | `position: absolute; background: var(--panel, var(--surface)); border: 0; border-radius: var(--r);` |
| `.note` | the one callout: a quiet panel labeled Note (`.red` says Watch out, `.blue`) | `position: absolute; font-size: 26px; padding: 14px 22px; border-radius: var(--r); background: var(--surface); border: 0; line-height: 1.3;` |
| `.label` | the label: a small quiet patch for a word or two. The only one | `display: inline-block; font-size: 20px; padding: 4px 12px; background: var(--surface-2); color: var(--ink-2); border: 0; border-radius: var(--r-sm); font-family: var(--font); font-weight: 600; max-width: 100%; text-wrap: balance;` |
| `.frame` | a dashed group with a `.lbl` | `position: absolute; border: 2px dashed var(--line); border-radius: var(--r-lg);` |
| `.window` | a browser window with a `.bar` and an `<img>` | `position: absolute; display: flex; flex-direction: column; background: var(--surface); border: 1px solid var(--line); border-radius: var(--r-lg); overflow: hidden;` |
| `.code` | a code block (`<pre><code>`), a darker panel; `.hl` lights a line in blue | `position: absolute; background: var(--bg-deep); border: 0; border-radius: var(--r-lg); text-align: left;` |
| `.bar` | a neutral chart bar, `style="--v:60%"`; `.hi` is the one being talked about, in blue | `height: 56px; width: var(--v, 50%); background: var(--line-strong); border-radius: 0 var(--r-sm) var(--r-sm) 0; align-self: flex-start;` |
| `.shot` | a screenshot `<img>` | `position: absolute; border-radius: var(--r-lg); border: 2px solid var(--line); background: var(--surface); object-fit: contain;` |

Cards and labels: use these, never a box or tag of your own. A scene that styles its own rounded box doesn't look like Chalkdust.

## Animation classes

For hand-timed scenes, with `data-b`, `data-f` and `data-o`. A `K` helper or a piece is usually the better way.

`.a-in`, `.a-pop`, `.a-fade`, `.a-dim`, `.a-out`, `.a-draw`, `.a-strike`, `.a-glow`, `.a-glowred`, `.a-press`, `.a-fly`, `.a-flystay`, `.a-cap`

Every other class the template styles: `.kicker`, `.title`, `.amber`, `.green`, `.red`, `.ghost`, `.sketch`, `.g-link-label`, `.dot`, `.hl`, `.lbltxt`, `.sline`, `.ov`, `.dots`, `.kit`, `.kit-label`, `.icon`, `.row`, `.g-part`, `.g-text`, `.g-arrow`, `.g-label`, `.hi`.

## Drawings

197 drawings in the brand's style. Use one by name: `<div data-part="name" class="l"></div>` or `Part('name')`. `Part('person').badge('check')` pins a small one to a corner for a variant. A Lucide name in `data-icon` draws our version when we have one. Draw a new one only when nothing here fits.

- `person`: person user human customer developer engineer viewer
- `robot`: robot agent ai claude model bot assistant
- `laptop`: laptop computer developer machine local notebook
- `phone`: phone mobile device smartphone app
- `server`: server rack backend datacenter host machine
- `database`: database storage data table records sql postgres cylinder
- `cloud`: cloud hosted internet service sky online
- `browser`: browser window webpage website screen app page
- `document`: document file page report paper text note
- `folder`: folder directory project files repo
- `envelope`: envelope email mail message letter send notification
- `book`: book reading library learn documentation history manual
- `lightbulb`: lightbulb idea insight thought think bright
- `shield`: shield security safe protect sandbox privacy
- `magnifier`: magnifier search zoom inspect find look
- `gear`: gear settings process engine mechanism machine
- `sun`: sun morning day bright sky weather
- `moon`: moon night sky dark
- `mountains`: mountains landscape scenery background hills nature range
- `waves`: waves sea ocean water tide background
- `tree`: tree nature forest plant growth
- `ship`: ship sailing boat sailor voyage sea
- `trophy`: trophy winner goal result success award
- `stopwatch`: stopwatch timer time speed fast measure clock
- `chart`: chart graph bars results data statistics growth
- `queue`: queue messages conveyor jobs backlog pipeline waiting async kafka
- `function`: function machine input output lambda transform compute serverless
- `chip`: chip cpu processor hardware silicon gpu compute microchip
- `load-balancer`: load balancer traffic distribute servers scaling routing proxy requests
- `cache`: cache fast memory redis speed storage lightning quick
- `terminal`: terminal shell console command line cli bash prompt
- `log-list`: log logs list clipboard checklist events audit errors status
- `package`: package box parcel dependency npm module library shipping release
- `key`: key secret credential api key access password unlock
- `token`: token coin access auth jwt credit session llm
- `layers`: layers stack levels architecture tiers overlap sheets
- `login`: login sign in form authentication password account user session
- `plug`: plug power connect electric plugin cable integration socket
- `git-branch`: git branch version control fork commit feature source
- `hard-drive`: hard drive disk storage hdd hardware data platter
- `flask`: flask experiment test lab science beaker chemistry trial
- `wifi`: wifi wireless router signal internet connection network
- `git-merge`: git merge pull request version control combine commit join
- `padlock`: padlock lock locked secure security private encrypted protected
- `code-file`: code file source script program developer html
- `unlocked`: unlocked open padlock unlock access insecure public decrypted
- `network`: network computers connected lan hub internet nodes topology
- `api`: api endpoint request response integration rest service interface
- `bug`: bug insect ladybug error defect debug issue glitch
- `braces`: braces curly brackets json code object syntax block
- `webhook`: webhook hook event callback notification message trigger
- `target`: target bullseye goal aim dart focus objective accuracy
- `sparkle`: sparkle magic new shine ai glitter special
- `microphone`: microphone mic voice record speak podcast audio narration
- `question`: question ask help unknown why faq speech bubble
- `download`: download save arrow down import get receive inbox
- `big-arrow`: big arrow right next direction forward point flow
- `scales`: scales balance justice compare weigh law fair tradeoff
- `bell`: bell notification alert ring reminder alarm
- `flag`: flag milestone goal mark country finish banner report
- `check`: check tick yes correct approved done success right pass
- `warning`: warning caution alert danger attention risk hazard triangle
- `refresh`: refresh reload loop cycle repeat update sync retry
- `raised-hand`: raised hand palm stop volunteer wave high five person
- `play`: play start video watch begin button run
- `picture`: picture image photo photograph frame painting landscape gallery
- `speaker`: speaker sound volume audio loud announce megaphone
- `star`: star favorite rating best quality award highlight
- `wrench`: wrench tool fix repair spanner maintenance settings
- `hammer`: hammer tool build construct fix nail
- `pencil`: pencil write draw edit sketch note
- `eye`: eye see look watch view vision visible observe
- `map-pin`: map pin location place marker address where geography
- `stop-sign`: stop sign halt forbidden blocked no entry road end
- `cross`: cross x no wrong rejected error fail cancel incorrect
- `upload`: upload send arrow up export publish share
- `pause`: pause wait hold break button stop
- `ear`: ear hear listen audio sound hearing
- `film`: film movie video strip cinema reel frames
- `megaphone`: megaphone announcement marketing loud bullhorn broadcast promote speaker shout
- `house`: house home building residence property real estate family
- `map`: map navigation route directions location pin travel journey folded
- `puzzle`: puzzle jigsaw pieces fit solve integration plugin problem game
- `lighthouse`: lighthouse beacon coast guide signal shore light harbor
- `store`: store shop retail storefront market business awning merchant
- `cart`: cart shopping trolley buy checkout ecommerce basket order groceries
- `magnet`: magnet attract attraction pull magnetic force retention horseshoe
- `teacher`: teacher instructor professor lesson classroom chalkboard school tutor education
- `battery`: battery power energy charge charging level electric
- `factory`: factory plant manufacturing industry production smokestack chimney pollution
- `team`: team group people colleagues staff crew coworkers employees together
- `fish`: fish ocean sea animal swimming aquarium goldfish marine
- `coins`: coins money cash payment price savings gold stack finance cost
- `gem`: gem diamond jewel crystal precious value premium treasure sapphire
- `graduation-cap`: graduation cap mortarboard degree diploma college university education graduate
- `anchor`: anchor boat nautical harbor port stability sea sailor dock
- `compass`: compass direction navigation guide north bearing explore orientation
- `credit-card`: credit card debit payment billing checkout bank pay plastic
- `gift`: gift present box reward birthday bonus surprise ribbon
- `speech-bubble`: speech bubble chat talk message conversation comment dialogue typing
- `rain-cloud`: rain cloud weather storm drops shower wet forecast
- `globe`: globe world earth planet international global map geography
- `rocket`: rocket launch startup space spaceship growth fast ship
- `flame`: flame fire hot burn heat trending campfire energy
- `developer`: developer programmer engineer coder coding software headphones laptop hacker
- `student`: student learner pupil backpack reading school study kid education
- `link`: link chain url hyperlink connect reference join
- `brain`: brain mind think thinking ai intelligence memory idea
- `zap`: zap lightning bolt fast speed power energy electric instant
- `hourglass`: hourglass time waiting wait timeout deadline sand slow
- `calendar`: calendar date day schedule month deadline event plan
- `camera`: camera photo picture screenshot capture snapshot record
- `heart`: heart love like favorite health care
- `thumbs-up`: thumbs up like approve yes good agree vote
- `thumbs-down`: thumbs down dislike reject no bad disagree
- `trash`: trash delete bin remove garbage discard waste
- `plane`: plane airplane flight travel ship deploy fly
- `archive`: archive box storage old backup store keep
- `wallet`: wallet money pay payment cash funds budget
- `container`: container docker shipping box image deploy
- `palette`: palette color colors paint design theme brand style
- `loop`: loop repeat cycle sync refresh again retry iterate
- `cookie`: cookie session browser tracking snack
- `dashboard`: dashboard metrics analytics overview monitor panel stats
- `captions`: captions subtitles transcript video text accessibility
- `dollar`: dollar money price cost revenue pay coin cash
- `diagram`: diagram flowchart tree hierarchy structure org chart architecture
- `door`: door entry exit enter leave room access
- `bridge`: bridge connect span cross gap link between
- `receipt`: receipt bill invoice purchase order total payment
- `tag`: tag label price category version release
- `ticket`: ticket pass admission event issue support
- `bank`: bank finance institution building money government court
- `atom`: atom science physics react molecule small
- `presentation`: presentation slides deck talk pitch chart board
- `radar`: radar scan detect monitor search find nearby
- `type`: type text font typography letters words write
- `shapes`: shapes geometry design elements triangle circle square
- `hash`: hash number tag channel id pound hashtag
- `gauge`: gauge speed meter performance level score measure
- `timeline`: timeline history sequence steps milestones progress events
- `clipboard`: clipboard copy paste checklist task form done list
- `headset`: headset support help call service audio listen
- `newspaper`: newspaper news article blog post press story
- `quote`: quote quotation said saying testimonial citation
- `undo`: undo back revert reverse rollback return
- `scissors`: scissors cut split trim divide snip
- `toggle`: toggle switch on off setting flag option enable
- `siren`: siren alarm alert emergency incident urgent outage
- `bird`: bird tweet fly nature animal light
- `keyboard`: keyboard type typing input keys shortcut
- `mouse`: mouse click pointer input device
- `monitor`: monitor screen desktop display computer
- `tablet`: tablet ipad device touch app
- `watch`: watch smartwatch wearable wrist time
- `printer`: printer print paper office output
- `router`: router wifi network modem internet home
- `satellite`: satellite orbit space signal broadcast gps
- `usb`: usb stick drive plug storage device
- `power`: power on off button start shutdown
- `memory`: memory ram chip hardware cache stick
- `floppy`: floppy save disk storage
- `plus`: plus add new more create badge
- `pdf-file`: pdf file document report export
- `image-file`: image file photo upload picture png
- `zip-file`: zip file archive compress bundle
- `variable`: variable value code x parameter
- `regex`: regex pattern match search expression
- `pull-request`: pull request pr review merge code branch
- `commit`: commit git change version save
- `issue`: issue bug ticket report github open
- `kanban`: kanban board tasks columns sprint project
- `form`: form input fields signup survey submit
- `slider`: slider settings adjust range control tune
- `cursor-click`: cursor click pointer select tap
- `window-tabs`: window tabs browser app page
- `dialog`: dialog modal popup confirm prompt
- `inbox`: inbox messages mail tray queue incoming
- `paper-plane`: paper plane send message submit deliver
- `video-call`: video call meeting zoom chat remote
- `music-note`: music note song audio sound
- `rss`: rss feed subscribe blog updates
- `alarm`: alarm clock wake reminder alert time
- `car`: car drive vehicle road travel
- `truck`: truck delivery shipping freight logistics
- `train`: train rail transit subway commute
- `office`: office building company business city
- `hospital`: hospital health medical care clinic
- `piggy-bank`: piggy bank savings money save budget
- `pie-chart`: pie chart share percent breakdown split
- `line-chart`: line chart graph trend growth metrics
- `trend-down`: trend down decline drop fall loss
- `funnel`: funnel filter conversion sales pipeline narrow
- `antenna`: antenna signal broadcast radio transmit
- `window`: window app desktop mac frame screen program
- `file-tree`: file tree folder directory structure project files
- `diff`: diff change compare added removed lines patch review

## Pieces

A slide is a tree of pieces: `slide(Row(Labeled('Browser', Part('browser')), Arrow(), Labeled('Server', Part('server'))))`. `slide.cut(word, ...)` starts a new slide when the word is spoken. Each piece is listed with its arguments, what it is, and the options its code reads.

### `Row(...kids)`

Pieces side by side, centered: Row(Part('browser'), Arrow(), Part('server')).

Options: `enter`.

### `Column(...kids)`

Pieces one above another, centered.

Options: `enter`.

### `Grid(count, ...kids)`

Pieces in equal columns, count across: Grid(3, a, b, c, d, e, f).

Options: `enter`.

### `Part(name, options)`

One of the brand's drawings.

Options: `size`, `enter`. `size` is one of `s`, `m`, `l`, `xl`.

### `Text(words, options)`

Words on the slide, at one of the text sizes: Text('Ship it', { size: 'h1', color: 'green' }).

Options: `size`, `color`, `enter`. `size` is one of `big`, `h1`, `h2`, `h3`, `caption`. `color` is any color name.

### `Labeled(words, inner, options)`

A decorator: a caption that belongs to another glyph, so it's centered on it by construction.

Options: `enter`.

### `Arrow(options)`

Connects the glyph before it to the glyph after it, from edge to edge. thin, bold or heavy; dashed; filled, open or no head; both ways.

Options: `color`, `enter`. `weight` is one of `thin`, `bold`, `heavy`, `head` one of `filled`, `open`, `none`, and `dashed` and `both` are true or false.

### `State(name, options)`

One state in a Machine: its name in a pill.

### `Machine(transitions, options)`

A state machine: Machine([[idle, busy, 'start'], [busy, idle, 'cancel']], { start: idle, steps: [{ to: busy, on: 'busy' }] }). The states are laid out and the transitions drawn as Flow does it. The current state wears a ring in its own color, from when the start state appears, and the ring moves to each step's state on its word, or as that state appears.

Options: `start`, `steps`, `color`, `direction`.

### `Sequence(actors, messages, options)`

Who sends what to whom, in order: Sequence([browser, server], [[browser, server, 'GET /'], [server, browser, '200', { reply: true }]]). Actors stand across the top with lifelines down. Each message is an arrow on its own row, with its words above it; a reply is dashed, and a message to itself loops back. Each comes in on its word, or after the last.

### `Connect(from, to, options)`

An arrow between any two glyphs, even ones far apart. It leaves from an edge, and goes around what's between them.

Options: `on`, `color`, `label`, `travel`, `fromSide`, `toSide`.

### `Flow(links, options)`

A diagram of our own glyphs: Flow([[browser, server, 'GET /'], [server, db]], { direction: 'down' }). Each link is [from, to], with a label or arrow options third. Nodes go in columns, and each link is drawn as a Connect.

Options: `direction`.

### `Tree(spec, options)`

A tree, growing down from its root: Tree([root, child, [child, grandchild]], { direction }).

Options: `direction`.

### `Cycle(steps, options)`

A loop of steps around a ring, the last leading back to the first: Cycle([plan, build, ship]).

Options: `fromSide`, `toSide`, `direction`.

### `Form(kind, data)`

One of the explaining forms, as a glyph. It fills the stage, and its slide's cut hides it like anything else.

### `Scene(...args)`

Scenery for a story slide: layers, back to front, that drift at different speeds behind everything else.

Options: `x`, `y`, `dur`.

### `Layer(part, options)`

One sheet of scenery. depth 0 stays still, and 1 moves the whole way. A landscape stretches across the stage; an object keeps its shape, standing at the bottom, at x (0 to 1 across the stage). stretch: true or false says otherwise.

### `Dots(total, options)`

A field of total dots, some colored in groups as they're talked about: Dots(230, { groups: [{ count: 140, label, color, on }] }).

Options: `groups`, `length`, `enter`.

### `Bars(items, options)`

A bar chart, each bar growing to its value: Bars([{ label, value, text, color, on }], { color }).

Options: `color`, `enter`.

### `Stat(value, label, options)`

A big number that counts up to its value when it comes on, with what it counts under it.

Options: `color`, `enter`, `prefix`, `suffix`, `dec`.

### `Line(points, options)`

A line over time, neutral with one moment marked in blue, or all blue with trend: Line([3, 5, 4, 8], { mark: { at: 2, label } }).

Options: `trend`, `color`, `mark`, `enter`.

### `Timeline(steps, options)`

Steps in time, across or down: Timeline([{ when, what, color, on }], { down }).

Options: `down`, `follow`, `enter`.

### `Stack(layers, options)`

Layers of a system, stacked or nested: Stack(['Browser', 'Server', 'Database'], { nest }).

Options: `nest`, `enter`.

### `Compare(left, right, options)`

This versus that, side by side: Compare({ title, points }, { title, points }).

Options: `enter`.

### `Table(columns, rows, options)`

A table: Table(['Name', 'Joined'], [['Ann', 2019], { cells: ['Bob', 2021], on: 'Bob', color: 'green' }]). A row given as { cells, on, color } lights on its word.

Options: `enter`.

### `Code(source, options)`

Real code, highlighted, with lines that light as they're talked about: Code(source, { lang, caption, link, highlight: [{ line, on, color }] }).

Options: `lang`, `link`, `caption`, `highlight`, `enter`.

### `Diff(before, after, options)`

The change between two versions of some code: Diff(before, after, { lang, change: 'word' }). It's drawn as Code is. Lines that stay are shown once; a line taken out is signed with a minus and a line put in with a plus. On the change word, or just after it appears, the old lines go red and fade, and the new ones come in, marked green.

Options: `change`, `lang`, `link`, `caption`, `highlight`, `enter`.

### `Files(paths, options)`

A project's files as a tree: Files(['src/app.py', 'src/db/models.py', 'README.md'], { highlight: [{ path, on }], added: [paths], removed: [paths] }). Folders come from the paths. A highlighted file lights on its word, and files added or removed are marked with a green plus or a red minus. It sizes itself as Code does.

Options: `added`, `removed`, `highlight`, `enter`.

### `Terminal(entries, options)`

A terminal: Terminal([{ cmd: 'npm test', on: 'run' }, { out: '12 passing', color: 'green' }], { title: 'zsh' }), or plain text where lines starting with $ are commands. Each command types out at the prompt on its word, or after the entry before, and the lines it prints come in once it's typed. Copying copies just the commands.

Options: `title`, `color`, `enter`.

### `Window(inner, options)`

A window around any glyph: Window(Part('browser'), { title: 'App' }). It's the brand's one window frame, a title bar with red, yellow and green dots, so a browser, an app and a terminal on a slide all match. What it holds sits in its pane and comes in with it.

Options: `title`, `enter`.

### What every piece can do

Each returns the piece, so they chain: `Part('server').on('server').light('busy', 'red')`. A word is one the narration speaks. `enter` in a piece's options picks its entrance, as `K.show`'s `kind` does.

- `.on(word)`: Come on screen when this word is spoken.
- `.at(time)`: Come on screen at this many seconds into the slide.
- `.light(word, how = 'yellow')`: Light up when this word is spoken: light('busy'), or light('busy', { style: 'spot' }). It goes out when the next thing on the slide lights, or on its own word with { until: 'word' }; { keep: true } keeps it on. lift (the default) grows it a little inside an outline in its color; spot dims everything else.
- `.badge(name, options = {})`: Pins a small drawing to a corner, so one drawing covers its variants: a person with a check, a shield with a padlock. It pops in just after the drawing, or when its own word is spoken: badge('check', { on: 'approved' }).
- `.unlight(word)`: Stop glowing when this word is spoken.
- `.morph(word, styles, options = {})`: Change how it looks when this word is spoken: morph('fixed', { color: 'green', scale: 1.1 }).
- `.hide(word)`: Go away when this word is spoken, with any arrows inside.
- `.moveTo(word, other, options = {})`: Travel to where another glyph is when this word is spoken. Arrows don't follow it.
- `.zoom(word, options = {})`: Move the camera in until this fills the stage, when the word is spoken. zoom('look', { pad, max, dur }).
- `.zoomOut(word, options = {})`: Take the camera back out to the whole stage when this word is spoken, and bring back what the zoom put away.
- `.swap(word, text)`: The old text lifts away and the new one settles in, when this word is spoken.
- `.rewrite(word, text)`: Becomes new text when this word is spoken, and the words both share travel to their new places.
- `.typed(options = {})`: Arrive letter by letter. typed({ dur }) sets how long the typing takes.
- `.wordByWord(options = {})`: Arrive a word at a time. wordByWord({ each }) sets the seconds between words.

`.light` styles: `lift`, `spot`.

## K helpers

In `scene(({ K, at }) => { ... })`, or by name in `K.say`. `at(beat, fraction)` is a time in a beat, and `at.word('word')` is when a word is spoken.

Every helper takes `at`, the time it happens. The options listed are the ones `K.say` passes as `name=value`.

- `K.arrow(from, to, o = {})`: An arrow from one element to another: curved, drawn on, with an arrowhead that lands at the end. Options: `color`, `fromSide`, `toSide`, `curve`, `bow`, `flip`, `dashed`, `flow`, `padStart`, `padEnd`, `straights`, `dur`.
- `K.path(d, o = {})`: Any path, drawn on. head: {x, y, angle} (radians) or false. dashed: true for a dashed line.
- `K.flow(p, o = {})`: Dots that run along a drawn path a few times, to show direction.
- `K.travel(what, p, o = {})`: A chip (or any element) that travels along a path. stay: true keeps it at the end. Options: `dur`, `stay`.
- `K.swap(what, text, o = {})`: Replace an element's text in place: the old text lifts away, the new one settles in. Options: `color`.
- `K.type(what, text, o = {})`: Type text into an element, letter by letter. Options: `dur`.
- `K.show(what, o = {})`: Show an element. kind: pop (default), in, fade, or an entrance that means something: slide (came from elsewhere; from: 'left' | 'right' | 'top' | 'bottom', distance), grow (a part coming out of the thing above it). Options: `kind`, `from`, `distance`, `dur`, `each`.
- `K.icon(what, o = {})`: Draw an icon on, line by line. The element has data-icon="name", which the build fills in. Options: `dur`, `kind`, `each`.
- `K.move(what, to, o = {})`: The same element travels, so nobody has to be told it's the same thing. to: an element (centers line up) or {x, y} in page coordinates for the element's center. Other CSS can change on the way, with style: {...}. Arrows don't follow, so draw them after the move. Options: `x`, `y`, `dur`.
- `K.light(what, o = {})`: Light something up to show it's active: a glow, a border, and any icon inside. Options: `color`, `dur`, `each`, `style`.
- `K.hide(what, o = {})`: Hide an element. Options: `dur`, `each`.
- `K.spot(keep, o = {})`: Dim everything except the given elements, from `at` until `until` (or the end of the scene). Options: `until`.
- `K.cam(target, o = {})`: Move the camera so `target` (an element, or {x, y, w, h}) fills the stage. reset: true goes back. Options: `reset`, `pad`, `max`, `dur`.
- `K.morph(what, vars, o = {})`: Change an element's look: a box turning green when it's fixed, say.
- `K.stagger(what, o = {})`: Stagger a list of elements in, one after another. Options: `each`.
- `K.boxOf(el)`: Where an element is on the stage, ignoring any transform.
- `K.unlight(what, o = {})`: Turn off K.light. Options: `dur`, `each`, `style`.
- `K.cut(what, o = {})`: A hard cut inside a slide: show this .slide or .layer, hide the others beside it, and clear any lines drawn so far.
- `K.say(text, o = {})`: A list of moves, one line per moment. Each line starts with a word from the narration, and the next line looks for its word after that one, so repeated words just work: K.say(` browser   #b server    #s in; arrow #b #s green slow      mark #s red +0.3; count #t 4.2 suffix=s dec=1 +1.5      cut #second `); A line can start with +seconds (after the last line) or @beat, or @beat.fraction, instead of a word. A move is any K helper's name, then selectors, "text", numbers, name=value options, a +seconds nudge, and bare words like red, in, fade, box or left. A selector alone means show, and one matching several elements staggers them.
- `K.drift(what, o = {})`: A slow, constant move, so a held picture doesn't sit dead still. Defaults to the whole stage. Options: `scale`, `x`, `y`, `dur`, `origin`.
- `K.parallax(layers, o = {})`: Layers slide at different speeds, which reads as depth. layers: {'#sky': 0.1, '#hills': 0.4, '#front': 1}.
- `K.mark(what, o = {})`: Draw attention to something already on screen by drawing on it. kind: underline (default) or box. Options: `kind`, `color`, `pad`, `dur`, `width`, `each`.
- `K.words(what, o = {})`: Text arrives one word at a time. spoken: true lands each word on the moment the narration says it. Options: `spoken`, `beat`, `each`.
- `K.count(what, to, o = {})`: A number counts up to its value. format turns the number into text, like (n) => `$${n}`. Options: `from`, `dur`, `prefix`, `suffix`, `dec`.
- `K.wipe(what, o = {})`: Reveal something by sweeping across it. from: left (default), right, top, bottom. Options: `from`, `dur`, `each`.
- `K.rewrite(what, text, o = {})`: Text becomes new text, and the words they share travel to their new places, so you can see what changed. Works on a sentence, an equation or a line of code. Options: `dur`.

## Forms

Ready-made ways to explain code. Each fills the stage, so a scene usually needs only one. As a piece: `Form('trace', data)`.

- `K.trace(o)`: Something moves through a system and changes as it goes. K.trace({ lang, hops: [{ at, label, icon, carry, job, code, file }] })
- `K.states(o)`: Something moves between states. The current state stays lit. K.states({ lang, code, states: [{ id, label, col, row, color }], start: { state, at, line }, steps: [{ from, to, label, at, line, fromSide, toSide }] })
- `K.reshape(o)`: One data shape becomes another. Each target field names the source field it came from. K.reshape({ via, from: { title, fields: [{ name, value }] }, to: { title, fields: [{ name, value, from }] }, at: { from, to, keep, rename, add, drop } })
- `K.race(o)`: Things happen at the same time, and the order decides the outcome. Call it twice to compare two runs. K.race({ top, lanes: ['A', 'B'], span: 10, from, to, shared: { label, values: [{ x, text, bad }] }, events: [{ lane, x, label, kind: 'read' | 'write' | 'bad' | 'good' }], holds: [{ lane, x1, x2 }], verdict: { text, color, at } })
- `K.barrier(o)`: Separate attempts stopped at a wall, each protecting something. A row with pass: true gets through. K.barrier({ source: { label, icon }, wall: 'sandbox', rows: [{ on, attempt, target, why, pass }] })

## Transitions

How a scene comes in, as `"transition"` in `scenes.json`. Every scene after the first fades in unless it says otherwise.

`cut`, `fade`, `slide`, `slide-up`
