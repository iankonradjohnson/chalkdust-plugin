# The design system

Read this first, before writing a video. It lists everything a slide can use: every color, text size, drawing, piece with its options and parts, move and form. `scene-authoring.md` says how to put them together, and `presets.md` has a tested slide for each piece.

It is generated from the code by `scripts/design_system.js`, so if something is here it exists, and if it isn't here it doesn't. Use what is here rather than words in boxes: a folder is `Part('folder')`.

## Colors

One set of names, everywhere: a piece's `color` option, and a link's light, like `[trouble](server:red)`. Name a color, never write a hex value, so light and dark both work. Prefer the brand's accents (`blue`, `green`, `yellow`, `red`) and the screen's own `ink`, `muted`, `surface` and `line`; the drawing colors are for the rare hand-drawn shape.

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
| `skin-tan` | #d9a273 | #d9a273 | drawing |
| `skin-brown` | #a8704a | #a8704a | drawing |
| `skin-deep` | #6e4630 | #6e4630 | drawing |
| `amber` | #F5D76E | #E9BE3C | same as yellow |

A project is Slate (dark) unless a file called `theme` says `light` (Chalk) or `navy`, the old look, which changes the screen colors `bg`, `surface`, `line`, `ink`, `muted`, `blue`, `yellow`, `red`, `green`, `yellow-text`.

## Fonts and text sizes

| Variable | Font |
| --- | --- |
| `--font` | "Instrument Sans", -apple-system, "Segoe UI", sans-serif |
| `--title` | Fraunces, Georgia, serif |
| `--code` | "JetBrains Mono", ui-monospace, Menlo, monospace |

`Text(words, { size })` takes one of these:

| Size | For | CSS |
| --- | --- | --- |
| `big` | one huge number or word | `font-size: 160px; font-weight: 800; line-height: 1.05;` |
| `h1` | the slide's main words | `font-size: 84px; font-weight: 800; line-height: 1.1; letter-spacing: -.02em;` |
| `h2` | a heading | `font-size: 62px; font-weight: 700; line-height: 1.15;` |
| `h3` | a label under a drawing | `font-size: 46px; font-weight: 600; line-height: 1.2;` |
| `caption` | a quiet line | `font-size: 32px; font-weight: 500; color: var(--muted);` |

## Drawings

349 drawings in the brand's style. Use one by name, `Part('name')`, at a size: `s`, `m`, `l`, `xl`. `Part('person').badge('check')` pins a small one to a corner for a variant. Draw a new one only when nothing here fits.

### Icons

For cards, labels, steps and diagrams: square, and placed with `Part(name)`.

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
- `map`: map navigation route directions location pin travel journey folded
- `puzzle`: puzzle jigsaw pieces fit solve integration plugin problem game
- `lighthouse`: lighthouse beacon coast guide signal shore light harbor
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

### Actors

People and animals, for scenes. A person is `Person({ pose })`; these stand on the bottom of their frame and are placed with `Actor(name, { at, height, from, flip })`, at their real size.

- `dog` (2 ft tall, 3 ft long): dog pet puppy animal walk
- `cat` (1 ft tall, 1.5 ft long): cat kitten pet animal
- `cow` (5 ft tall, 8 ft long): cow cattle farm animal dairy milk
- `horse` (6 ft tall, 8 ft long): horse animal farm ride stable
- `pigeon` (1 ft tall, 1.2 ft long): pigeon bird city street animal

### Props

Things, for scenes: vehicles, furniture, boxes, buildings. Drawn to scale, standing on the bottom of their frame, vehicles facing right, placed and moved with `Prop(name, { at, height, from, flip })`. Each says its real size, to size it beside a person.

- `wrench` (1 ft tall, 0.33 ft long): wrench spanner tool repair fix mechanic
- `house` (22 ft tall, 26 ft long): house home building residence property real estate family
- `store` (16 ft tall, 18 ft long): store shop retail storefront market business awning merchant
- `clipboard` (1.1 ft tall, 0.75 ft long): clipboard notes checklist doctor inspector form
- `airliner` (41 ft tall, 129 ft long): airliner airplane jet aircraft plane side flight airline travel boeing airbus
- `bus` (10.5 ft tall, 40 ft long): bus school bus transit commute vehicle public transport
- `office-tower` (75 ft tall, 33 ft long): office tower building skyscraper company corporate headquarters downtown work
- `park-tree` (22 ft tall, 18 ft long): park tree oak shade nature green leafy
- `lamp-post` (14 ft tall, 2 ft long): lamp post street light lamppost night sidewalk
- `bench` (2.8 ft tall, 6 ft long): bench park seat sit wait sidewalk
- `bush` (3 ft tall, 6 ft long): bush shrub hedge garden plant green
- `bicycle` (3.5 ft tall, 5.8 ft long): bicycle bike cycle ride commute pedal
- `traffic-cone` (2.3 ft tall, 1.2 ft long): traffic cone construction roadwork caution warning safety
- `school` (28 ft tall, 35 ft long): school building education class students teacher kids campus
- `warehouse` (28 ft tall, 42 ft long): warehouse storage depot logistics distribution building garage loading
- `suitcase` (2.2 ft tall, 1.5 ft long): suitcase luggage travel trip bag airport rolling
- `coffee-cup` (0.55 ft tall, 0.4 ft long): coffee cup takeaway drink cafe morning latte
- `box-stack` (3.4 ft tall, 4 ft long): boxes stack cardboard packages moving shipping inventory
- `bank-front` (30 ft tall, 38 ft long): bank building columns finance money vault savings loan
- `gas-station` (16 ft tall, 24 ft long): gas station fuel pump petrol filling station car
- `taxi` (4.8 ft tall, 15.5 ft long): taxi cab ride car city hail uber
- `delivery-van` (9 ft tall, 20 ft long): delivery van courier parcel shipping vehicle
- `forklift` (7 ft tall, 10 ft long): forklift warehouse lift pallet loading logistics
- `money-stack` (0.4 ft tall, 1.2 ft long): money cash bills stack dollars payment price
- `mailbox` (4 ft tall, 2 ft long): mailbox mail letters post box delivery
- `fire-hydrant` (2.6 ft tall, 1.6 ft long): fire hydrant street sidewalk water
- `sedan` (4.8 ft tall, 15.5 ft long): sedan car automobile drive commute vehicle road side
- `box-truck` (11.5 ft tall, 24 ft long): box truck delivery moving freight lorry vehicle side
- `desk` (2.5 ft tall, 5 ft long): desk office work table workstation furniture
- `office-chair` (3.2 ft tall, 2.4 ft long): office chair seat desk chair furniture sit
- `table` (2.5 ft tall, 6 ft long): table dining kitchen furniture
- `sofa` (2.8 ft tall, 7 ft long): sofa couch living room furniture lounge
- `fridge` (6 ft tall, 2.5 ft long): fridge refrigerator kitchen appliance food
- `potted-plant` (3.5 ft tall, 2 ft long): potted plant houseplant pot leaves office home
- `helicopter` (12 ft tall, 42 ft long): helicopter chopper aircraft rotor flight
- `fuel-truck` (11 ft tall, 30 ft long): fuel truck tanker gas oil delivery vehicle
- `control-tower` (110 ft tall, 40 ft long): control tower airport air traffic tower aviation
- `baggage-cart` (4 ft tall, 10 ft long): baggage cart luggage trolley airport bags
- `tug` (5 ft tall, 14 ft long): tug aircraft tug pushback tractor airport ground vehicle
- `stove` (3 ft tall, 2.5 ft long): stove oven cooker range kitchen cooking
- `shop-counter` (3.5 ft tall, 6 ft long): shop counter checkout till register cash store retail
- `school-desk` (2.5 ft tall, 2.5 ft long): school desk student pupil classroom table
- `hospital-bed` (3 ft tall, 7 ft long): hospital bed patient ward clinic sick
- `shopping-cart` (3.3 ft tall, 3 ft long): shopping cart trolley groceries supermarket store
- `motorcycle` (3.6 ft tall, 7 ft long): motorcycle motorbike bike ride vehicle
- `atm` (5.5 ft tall, 2.5 ft long): atm cash machine bank money withdraw
- `vending-machine` (6 ft tall, 3 ft long): vending machine snacks drinks
- `trash-can` (3 ft tall, 2 ft long): trash can bin garbage waste street
- `conveyor` (3 ft tall, 12 ft long): conveyor belt factory line warehouse production
- `traffic-light` (12 ft tall, 2 ft long): traffic light signal stop go intersection street
- `bus-stop` (8 ft tall, 10 ft long): bus stop shelter transit wait street
- `tv` (3.5 ft tall, 5 ft long): tv television screen stand living room watch
- `bed` (3.5 ft tall, 7 ft long): bed bedroom sleep rest night
- `dining-chair` (3 ft tall, 1.6 ft long): dining chair seat restaurant kitchen
- `excavator` (10 ft tall, 30 ft long): excavator digger construction machine building site
- `cement-mixer` (11 ft tall, 28 ft long): cement mixer concrete truck construction vehicle
- `dumpster` (5 ft tall, 12 ft long): dumpster skip bin waste construction trash
- `barrier` (3.5 ft tall, 6 ft long): barrier construction roadblock stripes road work
- `toolbox` (1 ft tall, 1.6 ft long): toolbox tools repair kit builder mechanic
- `frying-pan` (0.3 ft tall, 1.6 ft long): frying pan skillet cook chef kitchen
- `briefcase` (1.1 ft tall, 1.5 ft long): briefcase bag business work office case
- `laptop-side` (0.75 ft tall, 1 ft long): laptop side view open typing desk computer work
- `clipboard-back` (1.1 ft tall, 0.75 ft long): clipboard back held facing us chart doctor

### Backdrops

For scenes: they stretch behind everything as `Layer(name)`. A set, `Scene('forest')`, stacks its far, mid and near sheets for parallax. A named setting drifts left as the slide plays, up to 480 px at the front of the stage and less further back, so stand front props right of center and they stay in view. Settings, a street, an office or a park, are places for a story, and a ground sheet (street-ground, park-ground, country-road) is a foreground to put in front of any of them. Each says its horizon and perFoot, for Scene({ horizon, perFoot }), and the areas, bands down the stage, to stand actors and props in: `street` (horizon 0.5, perFoot 45: sidewalk 0.76 to 0.88, road 0.89 to 1); `office-interior` (horizon 0.45, perFoot 125: floor 0.77 to 1); `park` (horizon 0.5, perFoot 55: grass 0.76 to 1); `city-skyline` (horizon 0.6, perFoot 20: street 0.89 to 1); `desert-dunes` (horizon 0.5, perFoot 40: sand 0.88 to 1); `forest` (horizon 0.55, perFoot 14: ground 0.89 to 1); `farm-fields` (horizon 0.45, perFoot 55: field 0.78 to 1); `night-sky` (horizon 0.6, perFoot 40: hill 0.88 to 1); `ocean-horizon` (horizon 0.5, perFoot 60: beach 0.88 to 1); `street-ground` (horizon 0.45, perFoot 66: far sidewalk 0.7 to 0.75, road 0.76 to 0.85, near sidewalk 0.86 to 1); `park-ground` (horizon 0.45, perFoot 60: grass 0.61 to 1, path 0.8 to 0.96); `country-road` (horizon 0.45, perFoot 55: far field 0.61 to 0.72, road 0.73 to 0.85, near field 0.86 to 1); `city-street` (horizon 0.45, perFoot 66: far sidewalk 0.7 to 0.75, road 0.76 to 0.85, near sidewalk 0.86 to 1); `countryside` (horizon 0.45, perFoot 55: far field 0.61 to 0.72, road 0.73 to 0.85, near field 0.86 to 1); `airport` (horizon 0.45, perFoot 20: apron 0.61 to 0.67, taxiway 0.68 to 0.77, ramp 0.78 to 1); `kitchen` (horizon 0.45, perFoot 125: floor 0.77 to 1); `shop` (horizon 0.45, perFoot 125: floor 0.77 to 1); `classroom` (horizon 0.45, perFoot 125: floor 0.77 to 1); `hospital-room` (horizon 0.45, perFoot 125: floor 0.77 to 1); `warehouse-interior` (horizon 0.45, perFoot 60: floor 0.77 to 1, aisle 0.8 to 0.96); `living-room` (horizon 0.45, perFoot 100: floor 0.77 to 1); `restaurant` (horizon 0.45, perFoot 100: floor 0.77 to 1); `suburb` (horizon 0.45, perFoot 66: far sidewalk 0.7 to 0.75, road 0.76 to 0.85, near sidewalk 0.86 to 1); `construction-site` (horizon 0.45, perFoot 50: site 0.7 to 1).

- `mountains`: mountains landscape scenery background hills nature range
- `waves`: waves sea ocean water tide background
- `city-skyline`: city skyline buildings downtown skyscrapers urban night lights background backdrop landscape
- `desert-dunes`: desert dunes sand hot sun dry cactus sahara background backdrop landscape
- `forest`: forest woods trees pine nature wilderness background backdrop landscape
- `farm-fields`: farm fields crops barn wheat countryside rural agriculture background backdrop landscape
- `night-sky`: night sky stars moon dark evening background backdrop landscape
- `ocean-horizon`: ocean horizon sea sunset sailboat water beach background backdrop landscape
- `city-skyline-far`: city skyline buildings far distant back sky parallax layer sheet backdrop scene
- `city-skyline-mid`: city skyline buildings middle mid parallax layer sheet backdrop scene
- `city-skyline-near`: city skyline buildings near front foreground parallax layer sheet backdrop scene
- `desert-dunes-far`: desert dunes sand far distant back sky parallax layer sheet backdrop scene
- `desert-dunes-mid`: desert dunes sand middle mid parallax layer sheet backdrop scene
- `desert-dunes-near`: desert dunes sand near front foreground parallax layer sheet backdrop scene
- `forest-far`: forest pine trees far distant back sky parallax layer sheet backdrop scene
- `forest-mid`: forest pine trees middle mid parallax layer sheet backdrop scene
- `forest-near`: forest pine trees near front foreground parallax layer sheet backdrop scene
- `farm-fields-far`: farm fields barn far distant back sky parallax layer sheet backdrop scene
- `farm-fields-mid`: farm fields barn middle mid parallax layer sheet backdrop scene
- `farm-fields-near`: farm fields barn near front foreground parallax layer sheet backdrop scene
- `night-sky-far`: night sky stars hills far distant back sky parallax layer sheet backdrop scene
- `night-sky-mid`: night sky stars hills middle mid parallax layer sheet backdrop scene
- `night-sky-near`: night sky stars hills near front foreground parallax layer sheet backdrop scene
- `ocean-horizon-far`: ocean sea horizon far distant back sky parallax layer sheet backdrop scene
- `ocean-horizon-mid`: ocean sea horizon middle mid parallax layer sheet backdrop scene
- `ocean-horizon-near`: ocean sea horizon near front foreground parallax layer sheet backdrop scene
- `street`: street shops storefronts sidewalk road town main street downtown background backdrop landscape setting
- `street-far`: street shops storefronts sidewalk road town main street downtown far distant back sky parallax layer sheet backdrop scene
- `street-mid`: street shops storefronts sidewalk road town main street downtown middle mid parallax layer sheet backdrop scene
- `street-near`: street shops storefronts sidewalk road town main street downtown near front foreground ground parallax layer sheet backdrop scene
- `office-interior`: office interior room workplace desk bookshelf whiteboard indoors background backdrop landscape setting
- `office-interior-far`: office interior room workplace desk bookshelf whiteboard indoors far distant back sky parallax layer sheet backdrop scene
- `office-interior-mid`: office interior room workplace desk bookshelf whiteboard indoors middle mid parallax layer sheet backdrop scene
- `office-interior-near`: office interior room workplace desk bookshelf whiteboard indoors near front foreground ground parallax layer sheet backdrop scene
- `park`: park grass trees path fence outdoors city park background backdrop landscape setting
- `park-far`: park grass trees path fence outdoors city park far distant back sky parallax layer sheet backdrop scene
- `park-mid`: park grass trees path fence outdoors city park middle mid parallax layer sheet backdrop scene
- `park-near`: park grass trees path fence outdoors city park near front foreground ground parallax layer sheet backdrop scene
- `street-ground`: street ground sidewalk road curb foreground floor stand backdrop scene layer
- `park-ground`: park ground grass path lawn foreground stand backdrop scene layer
- `country-road`: country road dirt road field fence rural foreground stand backdrop scene layer
- `city-street`: city street daytime buildings shops downtown town sidewalk road background backdrop landscape setting
- `city-street-far`: city street daytime buildings shops downtown town sidewalk road far distant back sky skyline parallax layer sheet backdrop scene
- `city-street-mid`: city street daytime buildings shops downtown town sidewalk road middle mid buildings parallax layer sheet backdrop scene
- `city-street-near`: city street daytime buildings shops downtown town sidewalk road near front foreground ground street parallax layer sheet backdrop scene
- `countryside`: countryside country rural farm hills trees road fields background backdrop landscape setting
- `countryside-far`: countryside country rural farm hills trees road fields far distant back sky hills parallax layer sheet backdrop scene
- `countryside-mid`: countryside country rural farm hills trees road fields middle mid trees parallax layer sheet backdrop scene
- `countryside-near`: countryside country rural farm hills trees road fields near front foreground ground road parallax layer sheet backdrop scene
- `airport`: airport terminal apron taxiway runway tarmac gate aviation flight background backdrop landscape setting
- `airport-far`: airport terminal apron taxiway runway tarmac gate aviation flight far distant back sky parallax layer sheet backdrop scene
- `airport-mid`: airport terminal apron taxiway runway tarmac gate aviation flight middle mid wall building parallax layer sheet backdrop scene
- `airport-near`: airport terminal apron taxiway runway tarmac gate aviation flight near front foreground ground floor parallax layer sheet backdrop scene
- `kitchen`: kitchen cupboards counter cabinets home cooking indoors room background backdrop landscape setting
- `kitchen-far`: kitchen cupboards counter cabinets home cooking indoors room far distant back sky parallax layer sheet backdrop scene
- `kitchen-mid`: kitchen cupboards counter cabinets home cooking indoors room middle mid wall building parallax layer sheet backdrop scene
- `kitchen-near`: kitchen cupboards counter cabinets home cooking indoors room near front foreground ground floor parallax layer sheet backdrop scene
- `shop`: shop store interior shelves goods retail checkout indoors room background backdrop landscape setting
- `shop-far`: shop store interior shelves goods retail checkout indoors room far distant back sky window view parallax layer sheet backdrop scene
- `shop-mid`: shop store interior shelves goods retail checkout indoors room middle mid wall parallax layer sheet backdrop scene
- `shop-near`: shop store interior shelves goods retail checkout indoors room near front foreground floor ground parallax layer sheet backdrop scene
- `classroom`: classroom school chalkboard lesson teacher students indoors room background backdrop landscape setting
- `classroom-far`: classroom school chalkboard lesson teacher students indoors room far distant back sky window view parallax layer sheet backdrop scene
- `classroom-mid`: classroom school chalkboard lesson teacher students indoors room middle mid wall parallax layer sheet backdrop scene
- `classroom-near`: classroom school chalkboard lesson teacher students indoors room near front foreground floor ground parallax layer sheet backdrop scene
- `hospital-room`: hospital room ward clinic doctor patient monitor indoors background backdrop landscape setting
- `hospital-room-far`: hospital room ward clinic doctor patient monitor indoors far distant back sky window view parallax layer sheet backdrop scene
- `hospital-room-mid`: hospital room ward clinic doctor patient monitor indoors middle mid wall parallax layer sheet backdrop scene
- `hospital-room-near`: hospital room ward clinic doctor patient monitor indoors near front foreground floor ground parallax layer sheet backdrop scene
- `warehouse-interior`: warehouse interior racks pallets storage shelving logistics inventory indoors background backdrop landscape setting
- `warehouse-interior-far`: warehouse interior racks pallets storage shelving logistics inventory indoors far distant back sky window parallax layer sheet backdrop scene
- `warehouse-interior-mid`: warehouse interior racks pallets storage shelving logistics inventory indoors middle mid wall racks parallax layer sheet backdrop scene
- `warehouse-interior-near`: warehouse interior racks pallets storage shelving logistics inventory indoors near front foreground floor ground parallax layer sheet backdrop scene
- `countryside-fence`: countryside country fence rail posts front parallax layer sheet backdrop scene
- `living-room`: living room lounge home house sofa indoors room background backdrop landscape setting
- `living-room-far`: living room lounge home house sofa indoors room far distant back sky window view parallax layer sheet backdrop scene
- `living-room-mid`: living room lounge home house sofa indoors room middle mid wall parallax layer sheet backdrop scene
- `living-room-near`: living room lounge home house sofa indoors room near front foreground floor ground parallax layer sheet backdrop scene
- `restaurant`: restaurant cafe diner dining menu eat indoors room background backdrop landscape setting
- `restaurant-far`: restaurant cafe diner dining menu eat indoors room far distant back sky window view parallax layer sheet backdrop scene
- `restaurant-mid`: restaurant cafe diner dining menu eat indoors room middle mid wall parallax layer sheet backdrop scene
- `restaurant-near`: restaurant cafe diner dining menu eat indoors room near front foreground floor ground parallax layer sheet backdrop scene
- `suburb`: suburb suburban houses homes neighborhood residential street lawns background backdrop landscape setting
- `suburb-far`: suburb suburban houses homes neighborhood residential street lawns far distant back sky parallax layer sheet backdrop scene
- `suburb-mid`: suburb suburban houses homes neighborhood residential street lawns middle mid parallax layer sheet backdrop scene
- `suburb-near`: suburb suburban houses homes neighborhood residential street lawns near front foreground ground parallax layer sheet backdrop scene
- `construction-site`: construction site building crane steel frame dirt fence work background backdrop landscape setting
- `construction-site-far`: construction site building crane steel frame dirt fence work far distant back sky parallax layer sheet backdrop scene
- `construction-site-mid`: construction site building crane steel frame dirt fence work middle mid parallax layer sheet backdrop scene
- `construction-site-near`: construction site building crane steel frame dirt fence work near front foreground ground parallax layer sheet backdrop scene


## Pieces

A slide is a tree of pieces, in the cast of a `## heading` in video.md: `const browser = Labeled('Browser', Part('browser')), server = Part('server'); slide(Row(browser, Arrow(), server))`. The cast says what is on screen and nothing about when; the script under it says when, by linking words to names: `The [browser](browser) [asks](browser->server) the [server](server).` See presets.md. Each piece is listed with its arguments, what it is, the options its code reads, and the parts a script can point at in it.

### `Row(...kids)`

Pieces side by side, centered: Row(Part('browser'), Arrow(), Part('server')).

Options: `enter`.

### `Column(...kids)`

Pieces one above another, centered, or lined up on the left with a last { align: 'start' }. Rows of a drawing and its words line up as a list on their own; { align: 'center' } centers each instead.

Options: `align`, `enter`.

### `Grid(count, ...kids)`

Pieces in equal columns, count across: Grid(3, a, b, c, d, e, f).

Options: `enter`.

### `Part(name, options)`

One of the brand's drawings.

Options: `size`, `enter`. `size` is one of `s`, `m`, `l`, `xl`.

### `Text(words, options)`

Words on the slide, at one of the text sizes: Text('Ship it', { size: 'h1', color: 'green' }). The script lights one word by changing its color: [ship](title.ship:green).

Options: `size`, `color`, `link`, `enter`. `size` is one of `big`, `h1`, `h2`, `h3`, `caption`. `color` is any color name.

### `Labeled(words, inner, options)`

A decorator: a caption that belongs to another glyph, so it's centered on it by construction.

Options: `enter`.

### `Image(src, options)`

A real image from assets/, like a screenshot: Image('assets/player.jpg', { size, ratio, link }).

Options: `size`, `link`, `ratio`, `alt`, `enter`.

### `Cutout(src, options)`

One thing cut from a photo, on a transparent background, placed like a drawing: Cutout('assets/thing-cutout.png', { size, ratio, tilt }), or found by name, Cutout('cut:stack of dollar bills'). It stands where a drawing goes in any piece, as tall as a Part of its size (a wide one two drawings wide), and in a chart's slot sized to its words as a drawing is. On a slide with a photo scene, a chart of cutouts sits bare on the photo: its arrows bold and in ink, its words on slabs.

Options: `tilt`, `size`, `link`, `ratio`, `alt`, `enter`.

### `Arrow(options)`

Connects the glyph before it to the glyph after it, from edge to edge. thin, bold or heavy; dashed; filled, open or no head; both ways.

Options: `color`, `weight`, `enter`. `weight` is one of `thin`, `bold`, `heavy`, `head` one of `filled`, `open`, `none`, and `dashed` and `both` are true or false.

### `State(name, options)`

One step in a Machine or a Flow: State('Idle'). shape: 'decision' is a diamond, and 'start' and 'end' the dots of an activity diagram.

Options: `shape`.

### `Machine(transitions, options)`

A state machine: Machine([[idle, busy, 'start'], [busy, idle, 'cancel']], { start: idle }). The states are laid out and the transitions drawn as Flow does it. The current state wears a ring in its own color, from when the start state appears, and the ring moves to each state as the script names it: [busy](busy).

Options: `start`, `color`, `direction`, `areas`, `lanes`.

### `Sequence(actors, messages, options)`

Who sends what to whom, in order: Sequence([browser, server], [[browser, server, 'GET /'], [server, browser, '200', { reply: true }]]). Actors stand across the top with lifelines down. Each message is an arrow on its own row, with its words above it; a reply is dashed, and a message to itself loops back. Each comes in when the script names it, [asks](browser->server), the next between the same two the next time it's named, or else after the last. Boxes go around messages: { loop: 'each page', messages: [...] }, { opt: 'logged in', messages: [...] }, and alternatives, { alt: [['found', [...]], ['missing', [...]]] }, each drawn on with its first message. { note: 'words', on: actor } is a note on that actor's line, in a row of its own.

### `Connect(from, to, options)`

An arrow between any two glyphs, even ones far apart. It leaves from an edge, and goes around what's between them. stream: true sends a run of dots along it once it draws, for something that keeps flowing; stream: 3 sends three.

Options: `color`, `weight`, `label`, `travel`, `stream`, `fromSide`, `toSide`.

### `Flow(links, options)`

A diagram of our own glyphs: Flow([[browser, server, 'GET /'], [server, db]], { direction: 'down' }). Each link is [from, to], with a label or arrow options third. Nodes go in columns, and each link is drawn as a Connect. areas draws a labeled box around some nodes, for a folder, a machine or a system's boundary: { areas: [['api/', routes, auth]] }. lanes puts every step in a swimlane, who does it, across, and down in arrow order: { lanes: [['Customer', pays], ['Bank', approve]] }.

Options: `direction`, `areas`, `lanes`.

### `Tree(spec, options)`

A tree, growing down from its root: Tree([root, child, [child, grandchild]], { direction }).

Options: `direction`, `areas`, `lanes`.

### `Cycle(steps, options)`

A loop of steps around a ring, the last leading back to the first: Cycle([plan, build, ship]).

Options: `fromSide`, `toSide`, `direction`, `areas`, `lanes`.

### `Form(kind, data)`

One of the explaining forms, as a glyph. It fills the stage, and its slide's cut hides it like anything else.

### `Scene(...args)`

Scenery for a story slide: layers, back to front, that drift at different speeds behind everything else. photo: 'assets/hangar.jpg' puts a real photo behind them, covering the stage, muted toward the slide's color (mute, 0 to 1, 0.55 unless said), so cutouts and drawings in front of it read. The way the explainers studied set a real place (Ian, 2026-11-07: "a photograph as the background ... slightly muted, and then put the cutouts"). A backdrop's name, Scene('forest'), stacks its far, mid and near sheets for parallax; Layers and Actors after it stand in front. A photo scene takes words too, Scene({ photo }, walt, Text('The Happiest Place')): a title, our serif at h1 unless sized, on a flat slab of the slide's color a line at a time, at the top of the room beside the people, with the board's pictures laid out below it.

Options: `photo`, `size`, `horizon`, `perFoot`, `feet`, `layers`, `float`, `drift`, `mute`, `album`, `ratio`, `at`, `height`, `timeline`, `x`, `board`, `y`, `dur`, `label`.

### `Album(...pics)`

Pictures one at a time, each filling the frame on its word over the last: Album(Prop('assets/a.jpg', { ratio }), ...).

Options: `photo`, `size`, `horizon`, `perFoot`, `feet`, `layers`, `float`, `drift`, `mute`, `album`, `ratio`, `at`, `height`, `timeline`, `x`, `board`, `y`, `dur`, `label`.

### `Filmstrip(...pics)`

Pictures in a row along a line, each labelled, the camera gliding to each on its word: Filmstrip(Prop('assets/a.jpg', { ratio, label: '1922' }), ...).

Options: `photo`, `size`, `horizon`, `perFoot`, `feet`, `layers`, `float`, `drift`, `mute`, `album`, `ratio`, `at`, `height`, `timeline`, `x`, `board`, `y`, `dur`, `label`.

### `Actor(src, options)`

A cutout standing in a scene, that drives in and moves about in it: Actor('assets/tug-cutout.png', { at: [0.3, 0.85], height: 300, from: 'left' }). tag: ['Larry Page', 'Stanford PhD student, 1998'] pins a name tag low across it, a slab with a yellow edge, the name over a quieter line (or just tag: 'Larry Page'); it comes on just after the cutout, or on its word, [Larry](larry.tag).

Options: `ratio`, `from`, `at`, `feet`, `height`, `flip`, `alt`.

### `Prop(src, options)`

An object in a scene, a truck or a box, placed and moved as an actor is: Prop('assets/tug-cutout.png', { at: [0.3, 0.85], height: 300, from: 'left' }).

Options: `at`, `along`, `flip`, `from`, `ratio`, `feet`, `height`, `alt`.

### `Layer(part, options)`

One sheet of scenery. depth 0 stays still, and 1 moves the whole way. A landscape stretches across the stage; an object keeps its shape, standing at the bottom, at x (0 to 1 across the stage). stretch: true or false says otherwise.

### `Person(options)`

Chalkdust's character, an actor in a drawn scene placed like any Actor: Person({ at: [0.3, 0.9], height: 420, from: 'left' }).goTo([0.7, 0.9]).turn().wave().point(), said as [walks over](sam.goTo). goTo walks it there in step, or runs with goTo(spot, { pace: 'run' }); more moves: nod, shake, shrug, think, explain, clap, jump, cheer, sitDown (sitDown({ on: bench }) sits on it), standUp; holding: 'coffee-cup', 'suitcase', 'clipboard', 'toolbox', 'wrench', 'frying-pan' or 'briefcase' starts it holding one, pickUp(prop) walks over and carries it, putDown() sets it down; outfit: 'doctor' | 'pilot' | 'builder' | 'chef' | 'suit' dresses it, look: 'kid' is a child, hair: 'steel' greys it; hairdo: 'long' | 'ponytail' | 'bun' | 'curly' | 'bob' | 'afro' styles the hair, skirt: a palette colour puts on a skirt, legs bare under it, dress: a palette colour a dress; glasses: true | 'bold', beard: 'full' | 'moustache'; look: 'woman' a woman's figure, look: 'elder' an older person, cane: true a cane in hand; skin: 'skin' | 'skin-tan' | 'skin-brown' | 'skin-deep'; feel('happy' | 'sad' | 'worried' | 'surprised' | 'neutral') changes its face on a word named for the mood, talk({ style: 'open' | 'soft' | 'nod' }) talks calmly, face: starts it in a mood; turnTo(other) turns side on toward another actor, wherever it stands then; turn() turns it to face us, turn({ to: 'side' }) back; view: 'front' starts facing us; pose holds it still (standing, walking, waving, pointing, carrying, sitting). Looks: classic (the one), mascot, slim, sturdy, shelf, tee; shirt, pants, hair, skin and shoes take palette names.; at a desk: sitDown({ on: seat }) sits the way the seat is drawn (side on in a chair, facing us on a bench; facing: 'side' or 'front' says which), type({ dur }) types, glance() looks at the screen, leanBack() leans back in the chair

Options: `look`, `view`, `pose`, `holding`, `face`, `outfit`, `hairdo`, `skirt`, `glasses`, `beard`, `dress`, `cane`, `shirt`, `pants`, `at`, `feet`, `flip`, `from`, `ratio`, `height`, `alt`.

### `Dog(options)`

A dog, rigged: Dog({ at, feet, from }).goTo([x, y]).wag().follow(sam). It trots with planted feet and wags its tail.

Options: `ratio`, `from`, `at`, `feet`, `height`, `flip`, `alt`.

### `Cat(options)`

A cat, rigged: Cat({ at, feet, from }).goTo([x, y]).sit().standUp().flick().follow(sam). It stalks, low and smooth, with planted feet; sit() sits it upright, and its next goTo gets it up.

Options: `ratio`, `from`, `at`, `feet`, `height`, `flip`, `alt`.

### `Cow(options)`

A cow, rigged: Cow({ at, feet, from }).goTo([x, y]).graze().moo().follow(sam). It plods, slow and heavy-headed, with planted feet; graze() puts its head down to the grass and nibbles.

Options: `ratio`, `from`, `at`, `feet`, `height`, `flip`, `alt`.

### `Crowd(options)`

People walking past in a scene, so it feels alive: Crowd({ count: 10, seed: 1, clear: [0.86, 0.95], pace: 'walk' | 'run' | 'mixed' }), in a Scene like any actor. In a named setting they walk only where its walk bands say (its sidewalks, never the road); band: [from, to] says otherwise, and is needed in a hand-built Scene. Each walks on at one edge and off the other, in step, at its own depth and size, dressed from the seed; they set off with the slide, or on its word, [people bustle past](crowd). clear keeps a lane empty for the main actors.

Options: `at`.

### `Dots(total, options)`

A field of total dots, some colored in groups as they're talked about: Dots(230, { groups: [{ count: 140, label, color, on }] }).

Options: `groups`, `length`, `enter`.

### `Bars(items, options)`

A bar chart, each bar growing to its value: Bars([{ label, value, text, color, on }], { color }).

Options: `color`, `enter`.

### `Stat(value, label, options)`

A big number that counts up to its value when it comes on, with what it counts under it. .countTo(40) counts on from there to 40 on its word, [rises to forty](st.countTo).

Options: `color`, `dec`, `enter`, `prefix`, `suffix`.

### `Line(points, options)`

A line over time, neutral with one moment marked in blue, or all blue with trend: Line([3, 5, 4, 8], { mark: { at: 2, label } }).

Options: `trend`, `color`, `mark`, `enter`.

### `Timeline(steps, options)`

Steps in time, across or down: Timeline([{ when, what, color, on }], { down }). A commit graph too: give each step its branch, and a merge, { what, branch: 'retry' }, { what, branch: 'main', merge: 'retry' }.

Options: `down`, `follow`, `enter`.

### `Stack(layers, options)`

Layers of a system, stacked or nested: Stack(['Browser', 'Server', 'Database'], { nest }).

Options: `nest`, `enter`.

### `Compare(left, right, options)`

This versus that, side by side: Compare({ title, points }, { title, points }).

Options: `enter`.

### `Equation(terms, options)`

An equation, a term at a time: Equation(['A', '=', 'π', 'r²']), each term lit as it's said, [pi](eq.3).

Options: `enter`.

### `Cells(values, options)`

Values in boxes with their indexes, the way code holds them: Cells([7, 3, 9, 4]), a cell by index, [first](arr.0). .sort() sorts it on its word, [sorts itself](arr.sort).

Options: `index`, `enter`.

### `Matrix(rows, options)`

Rows of values: Matrix([[1, 2], [3, 4]]), lit by row, m.row-1, column, m.col-0, or cell, m.0-1.

Options: `index`, `enter`.

### `Scatter(points, options)`

Points on two axes, a labeled one in blue, with its fitted line if trend: Scatter([[1, 2], { x, y, label }], { trend }).

Options: `trend`, `enter`.

### `Histogram(values, options)`

How values spread, counted into bins: Histogram([1, 2, 2, 3], { bins }), a bin by number, [the middle](h.2).

Options: `bins`, `color`, `enter`.

### `Heatmap(rows, options)`

A grid shaded by value: Heatmap([[0, 5], [10, 2]], { rows, cols }), lit by a row or column label, [Tuesday](hm.tue).

Options: `rows`, `cols`, `values`, `enter`.

### `Calls(spec, options)`

Who calls whom, indented by depth, with a bar for each call's time: Calls(['main()', ['load()', 'read()'], { name, ms }]).

Options: `enter`.

### `Schema(tables, options)`

Tables with their fields and the keys between them: Schema([{ name, fields }], { keys: [['orders.user_id', 'users.id']] }). A class diagram too: give a table methods and a color, and key whole classes in words, ['CardPayment', 'Payment', 'is a']. uml: true draws it as strict UML.

Options: `uml`, `keys`, `enter`.

### `Table(columns, rows, options)`

A table: Table(['Name', 'Joined'], [['Ann', 2019], { cells: ['Bob', 2021], color: 'green' }]). The script names a row by number: [Bob](table.2).

Options: `enter`.

### `Code(source, options)`

Real code, highlighted: Code(source, { lang, file, caption, link }). file names it in a bar across the top; caption describes it underneath. The script lights a line, [reads](code.2), or a word on it, [db](code.2.db).

Options: `lang`, `link`, `caption`, `file`, `numbers`, `enter`.

### `Diff(before, after, options)`

The change between two versions of some code: Diff(before, after, { lang }). It's drawn as Code is. Lines that stay are shown once; a line taken out is signed with a minus and a line put in with a plus. When the script says, [the fix](diff.change), or just after it appears, the old lines go red and fade, and the new ones come in green.

Options: `lang`, `link`, `caption`, `file`, `numbers`, `enter`.

### `Files(paths, options)`

A project's files as a tree: Files(['src/app.py', 'src/db/models.py', 'README.md'], { added: [paths], removed: [paths] }). Folders come from the paths. A file lights when the script names it, [models](files.models), and files added or removed are marked with a green plus or a red minus. It sizes itself as Code does.

Options: `added`, `removed`, `enter`.

### `Terminal(entries, options)`

A terminal: Terminal([{ cmd: 'npm test' }, { out: '12 passing', color: 'green' }], { title: 'zsh' }), or plain text where lines starting with $ are commands. Each command types out at the prompt when the script names it, by number, [run the tests](term.1), or after the entry before, and the lines it prints come in once it's typed. Named again, a line fills its row; a word on it lights in its link's color, [push](term.3.push:green). Copying copies just the commands.

Options: `title`, `color`, `enter`.

### `Window(inner, options)`

A window around any glyph: Window(Part('browser'), { title: 'App' }). It's the brand's one window frame, a title bar with red, yellow and green dots, so a browser, an app and a terminal on a slide all match. What it holds sits in its pane and comes in with it.

Options: `title`, `enter`.

### What the script does with a piece

Naming a piece in a link brings it on the first time and lights it after that, until the next thing lights: `[the server](server)`. A color or a light goes after a colon: `[trouble](server:red)`, `[look](server:spot)`. `[gone](-server)` hides it, `[here](+server)` shows it without a light, and `[all of it](*)` brings on everything not on yet. `a->b` is the line between two things: it draws, and a second mention sends something along it. A path points inside a piece: `steps.launch`, `code.2`, `code.2.token`, `trace.server`. Any word lights the same way, by its color until the next light: the piece, its part, then the word, `[605](bars.javascript-605-tests.605:green)`, `[pro](table.2.pro)`, and in plain text the piece then the word, `[fast](title.fast)`. Light words as they are said: the more that moves with the voice, the better.

Colors: `red`, `green`, `blue`, `yellow`, `orange`. Lights: `lift`, `spot`, `grow`, `push`, `frame`, `drift`, lift by default.

### Moves a cast can give a piece

Each returns the piece, so they chain: `Text('v1').swap('v2')`. A move is named by its kind, a second of the same kind by its number (`swap-2`), and the script says when: `[ships](label.swap)`. `enter` in a piece's options picks its entrance.

- `.wordPart(path)`: A word in a part: the part, then the word, [605](time.javascript-605-tests.605) (Ian, 2026-11-07: "all words should have the ability to light up on their own"). The longest part that fits comes first. null if no part fits.
- `.partNode(key)`: (no description in the code)
- `.badge(name, options = {})`: Pins a small drawing to a corner, so one drawing covers its variants: a person with a check, a shield with a padlock. It pops in just after the drawing, or when the script names it: [approved](person.check).
- `.showAt(stage, time)`: Comes back after a hide: what [here](+name) does once it's gone.
- `.morph(styles, options = {})`: Change how it looks: morph({ color: 'green', scale: 1.1 }). The script says when: [fixed](box.morph).
- `.moveTo(other, options = {})`: Travel to where another glyph is: moveTo(other). The script says when: [moves over](chip.moveTo).
- `.swap(text)`: The old text lifts away and the new one settles in: swap('v2'). The script says when: [ships](label.swap).
- `.rewrite(text)`: Becomes new text, and the words both share travel to their new places: rewrite('new'). [now](label.rewrite).
- `.typed(options = {})`: Arrive letter by letter. typed({ dur }) sets how long the typing takes.
- `.wordByWord(options = {})`: Arrive a word at a time. wordByWord({ each }) sets the seconds between words.

## Forms

Ready-made ways to explain code, as one piece: `Form(kind, data)`. Each fills the stage. Its moments are parts the script names, like `trace.server`; see scene-authoring.md.

- `Form('trace', data)`: Something moves through a system and changes as it goes. Form('trace', { lang, hops: [{ label, icon, carry, job, code, file }] }), each hop a moment: trace.server
- `Form('reshape', data)`: One data shape becomes another. Each target field names the source field it came from. Form('reshape', { via, from: { title, fields: [{ name, value }] }, to: { title, fields: [{ name, value, from }] } }), with the moments from, to, keep, rename, add and drop
- `Form('race', data)`: Things happen at the same time, and the order decides the outcome. Call it twice to compare two runs. Form('race', { top, lanes: ['A', 'B'], span: 10, shared: { label, values: [{ x, text, bad }] }, events: [{ lane, x, label, kind: 'read' | 'write' | 'bad' | 'good' }], holds: [{ lane, x1, x2 }], verdict: { text, color } }), with the moments start, end and verdict
- `Form('barrier', data)`: Separate attempts stopped at a wall, each protecting something. A row with pass: true gets through. Form('barrier', { source: { label, icon }, wall: 'sandbox', rows: [{ attempt, target, why, pass }] }), each row a moment named by its target: barrier.disk
