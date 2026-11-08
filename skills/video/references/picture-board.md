# The picture board

The picture board is how to tell a story or a history: how Disney began, how Disneyland began, the rise of a company, a person's life. It comes in three shapes: the board (people big, pictures building around them), the album (one picture at a time) and the filmstrip (pictures along a line of dates). Each slide is a real photo of the place, with big real people standing in front of it. Every person, place, thing and number the narration names pops in on its word as a real picture.

This is the style Ian liked best ("this is like one of the best ones that we've done"). Every rule below is one he gave while watching, so follow all of them.

For diagrams, code and how-things-work, use the usual slides in `presets.md`. For a scene that has to be physically believable, with people standing in a place at the right size and moving through it, see `Actor` and `Scene({ photo, horizon, perFoot })` in `design-system.md`.

## The rules

- **Every person, place, thing and number the narration names gets a picture, on its word.** Ian: "Every single thing that you're naming should have a thing so I can see it."
  - A person is their photo.
  - A work is its poster, title card or still.
  - An amount or idea is a photo of a real object: $40 is an old wallet and a 1923 dollar bill, bankrupt is a nickel.
  - If no picture can be found, rephrase the line so it doesn't name the thing.
- **Lots of pictures, more than feels needed, and cut out.** About a picture every 1.5 seconds, 6 to 8 per slide, building up. Cut out every person and every object (`Actor('cut:...')` for people, `Prop('cut:...')` for things: a car, a gavel, a stack of money). Frame only flat things and places: documents, posters, logos, screenshots, buildings. Ian: "I like the cutouts a lot. So if you can have more cutouts, that would be better." A cutout takes about 1.4 s on this machine, and the same photo is cut once in any video, kept in the shared library. Ian, after the first Disneyland board: the bench he sat on, his two daughters, Lillian, "all these other things you could have easily filled up with more images". List everything the script names, including the small things, and fetch them all.
- **People big.** A person stands in front, a cutout 800–1000 px tall, cut off by the bottom of the frame, a little in from the corner: `at: [0.24, 1.1]`.
- **Photos only, no icons.** Our flat drawings and photos must not mix ("they should not mix"), and a photo scene refuses them.
- **No title, no kicker.** A slide with a scene shows no title or kicker. The build hides them.
- **Four layouts, taking turns** (Ian, 2026-11-08: "different presets, because if it's just the same preset, then that could be annoying"; he took all four as modes, A and B first). Leave people's `at` out and the board stands them by its layout:
  - `sides` (A): two people at both sides, in from the corners, pictures between and above.
  - `beside` (B): one person to one side, every picture beside them.
  - `middle` (C): one person in the middle, pictures on both flanks.
  - `hero` (D): no people, one big picture (the first named) and the rest beside it.
  With no `board`, the build rotates each board through the layouts its people fit (one person: beside, middle, beside on the other side; none: the hero swaps sides), so boards in a row never repeat. Name one with `Scene({ photo, drift: 0, board: 'middle' }, ...)` when the slide needs it. A person given an `at` keeps it.
- **Words go on slabs, in the scene.** When a board needs words, put them in it (Ian, 2026-11-08, picked from options A and C):
  - A title: `Scene({ photo }, walt, Text('The Happiest Place'))`. Our serif at h1, on a flat slab of the slide's color a line at a time, at the top of the room beside the people; the board lays its pictures out below it. One short line, two at most.
  - A name tag: `Actor('cut:Walt Disney 1950s', { at, height, tag: ['Walt Disney', 'founder, 1923'] })`, or just `tag: 'Walt Disney'`. A slab with a yellow edge, low across the cutout. It comes on just after the cutout, or on its word: `[Walt](walt.tag)`. Tag the people the narration names, so the viewer knows who's who.
  - No shadows or glows: the slab is what makes words read on a photo.
- **Charts of cutouts, bare on the photo.** When the story needs a diagram (this led to that, this much versus that much), use our own pieces with cutouts where the drawings go, beside the scene: `slide(Scene({ photo, drift: 0 }), Flow([[Labeled('Handheld security', palm), Labeled('eBay sellers', boxes)]]))`, with `const palm = Cutout('cut:Palm Pilot 1999')`. Ian, 2026-11-08: "I like A the best. This is probably the most versatile."
  - A cutout or `Image` stands where a `Part` goes in Flow, Bars, Timeline, Compare, Stack, Cycle and Grid, sized as a drawing is.
  - On the photo, arrows are bold and in ink, and words off a card sit on slabs, by themselves. Compare and Stack keep their cards.
  - Never a drawing: a `Part` anywhere on a slide with a photo scene is refused.
- **Hover.** The camera holds still (`drift: 0`) and each picture hovers gently on its own beat, which is the default for a picture board. `float: 'drift'` slides them instead, and `float: 'none'` keeps them still.
- **Animate the people on their words.** A cutout can't move its limbs, so it moves whole:
  - `.bounce()` hops
  - `.shake()` wobbles, for bad news
  - `.pop()` swells, for the punchline
  - `.turn()` faces the other way, toward someone it's talking about

  Link each one, like `[it was bankrupt](walt.shake)`.
- **Real pixels.** A cutout is the photo's own pixels under a mask from a background-removal model running on this machine: ISNet, run with onnxruntime, about 2 seconds a person, and it never refuses a face. `cutout.py` uses it whenever `~/.chalkdust/models/isnet-general-use.onnx` and onnxruntime are installed. Run builds with the project's Python (`.venv/bin/python scripts/video.py`), which has the runtime; the system Python doesn't. It is the only way a cutout is made: without the model, `cutout.py` fails and says how to install it, and the build shows that name's plain photo instead.
- **Never make up history.** Say only what you can source, and choose words you can stand behind.

## The album

The album is the other way to tell a story with the same pictures: one picture at a time, each filling the frame on its word, over the one before ("like an album ... looking at each image, like one after another. So like, boom, boom, boom"). Each one pushes in slowly while it's up, and the first is up from the slide's start.

```js
const walt = Prop('assets/walt-disney-portrait.jpg', { ratio: 667 / 902 }), park = Prop('assets/merry.jpg', { ratio: 3648 / 2736 })
slide(Album(walt, park))
```

```
In the late 1930s, [Walt Disney](walt) took his daughters to [Griffith Park](park).
```

The pictures need no `at` or height: the album fits each to the frame. Link every picture to its words, in order, about every 1.5 seconds. Use the board when people should stay on screen while things build up around them, and the album for a fast run of pictures.

## The filmstrip

The third way: pictures in a row along a line, each with its year or label underneath, and the camera glides to each one on its word. Use it for a story told in dates.

```js
const kc = Prop('find:Laugh-O-Grams Walt Disney', { label: '1922' }), willie = Prop('find:Steamboat Willie 1928', { label: '1928' })
slide(Filmstrip(kc, willie))
```

```
In 1922, his first studio, [Laugh-O-Gram](kc), went bankrupt. Then, in 1928, [Steamboat Willie](willie).
```

The first picture is up from the start; the next ones show at the edges, waiting.

## Name the pictures; the build finds them

The fastest way is to skip file names entirely: name each picture in the cast, and the build finds them all at once before it voices anything.
- `Prop('find:<name>')` is that picture.
- `Actor('cut:<name>')` is the person in it, cut out. `Prop('cut:<name>')` is an object, cut out.
- `Scene({ photo: 'find:<name>' })` is a backdrop.

Every picture is fetched and checked by a vision model, every cutout is made, all at the same time. `video.md` is then rewritten with the files and their ratios, so leave `ratio` out. A name with no picture stops the build and says which, so try other words or rephrase the line.

In the Disney filmstrip test, two slides with 7 pictures, all named this way, took **10.8 seconds** from `video.md` to a built video.

### Names that get found the first time

A name with no checked picture stops the whole build, and each retry is a full search round, so a few bad names cost minutes (Ian, 2026-11-08: "why did images take so long to find?"). Name things that exist as pictures:
- **A specific, famous thing**: a person ("Tim O’Reilly"), a building ("Capitol Records Building"), a product ("Palm Pilot handheld 1999"), a company by its legal name ("Stripe, Inc."). These come back first try.
- **Not a staged scene** ("small startup team working at laptops", "eBay seller packages 1999"): stock-photo scenes rarely pass the check. Name a real event or place instead ("Y Combinator Demo Day").
- **A year only where the look changed**: "PayPal logo 2000" works, "Stripe logo 2011" didn't. If the era doesn't matter for the line, leave the year out.
- **Write an apostrophe as ’**, not ', inside a name: a straight quote ends the string (`Actor('cut:Tim O’Reilly')`).

### Where the pictures come from

For each name, in this order, about eight candidates in all:
1. **Wikipedia's lead image**: the curated photo or logo of a person, company, product or place. No key needed.
2. **Google Images**, when `SERPAPI_KEY` (real Google results, the best) or `BRAVE_API_KEY` is set in the environment. This finds news photos, old logos, screenshots of old web pages and real artifacts, which free archives don't have. A video about a company, a look or an era is commentary, so its real, copyrighted pictures are fine to show. The user sets the key in their own shell profile, never in chat.
3. **Wikimedia Commons**, the free pictures.

Files are 1280 pixels wide, so a full-height cutout stays crisp. Only real pictures (JPEG, PNG, GIF, WebP) are shown to the checker; a candidate that won't download or isn't a picture is skipped.

### Name each picture for its moment

The checker sees all the candidates side by side and keeps the best one that shows the name: sharp, well lit, the subject large and whole, not a collage or a watermarked thumbnail. It is also told **the line the picture is linked on**, and its **label** if it has one (a filmstrip's year), and keeps only a picture from that moment: never a modern logo, product or photo for an earlier event. (Ian, on the Google video: a modern Google Ads logo on the year 2000 "makes no sense for that year".)

So name pictures the way you'd search for them, with the year or version in the name:
- `find:Google AdWords logo 2000`, not `find:Google AdWords logo`
- `cut:Larry Page 1998`, not `cut:Larry Page young portrait`
- `find:Google homepage 1998`, `find:Sun Microsystems logo 1990s`

Give every filmstrip picture its year as its `label`, and say the year in its line.

A whole video can say the look it's about under its title, `<!-- look: 1990s hand-drawn coffeehouse -->`, and every picture is checked against it too. A slide can say its own, or `<!-- look: none -->` for pictures judged by name and moment alone, like portraits.

### Look before you build

After the pictures are found, look at every one once on a contact sheet. The mistakes the checker still makes:
- **A different person with a related name.** "Sergey Brin young portrait" once came back as Anne Wojcicki. Name people plainly, with a year.
- **An unrelated Wikipedia article's lead image** for a name that isn't an article title (a robot for "Google first server Lego storage", a US 101 sign for a garage's street address). Google Images fixes most of these; otherwise rename it.
- **Today's version of something old**: a current logo, product or building. Put the year in the name.
- **Two people in one photo.** A cutout keeps everyone in it, so `cut:Larry Page 1998` came back as Larry and Sergey together. Name a photo of one person, or crop the cutout at the gap between them.

To try again, put the name back in the cast (`find:` or `cut:` in place of the `assets/...` file and its `ratio`) and run the build again; the other pictures stay as they are.

## Making one, fast

1. **Outline and script.** Write the narration first, then list every person, place, thing and number it names. That list is what to find.
2. **Find every picture at once**, checked: name them in the cast as above, or run `python3 $S/pictures.py <project> --check "<name>" "<name>" ...`.
   - It searches every name at once, in the sources above, and downloads 1280-pixel files rather than originals.
   - A vision model then looks at each name's candidates and keeps the best one from the right moment, or none.
   - Licenses and credits go into `credits.json`, and everything is kept in a shared library, so nothing downloads twice.
   - In the Disneyland test, 28 names took 8.8 s, where finding pictures by hand took 4 min 40 s.
   - For a name that comes back with none, try other words in a second run, try `photos.py find` for Openverse and the museums, or rephrase the line.
   - Look at `pictures-sheet.jpg` once before writing.
3. **Cut out every person and object at once**, in parallel: `python3 $S/cutout.py <photo> "<what>"`. Each takes about 2 s with ISNet.
4. **Write `video.md`.** One `##` slide per beat of the story, each a photo scene:

   ```js
   const walt = Actor('assets/walt-cutout.png', { ratio: 354 / 978, at: [0.24, 1.1], height: 1000 }).bounce().shake()
   const logo = Prop('assets/laughograms.jpg', { ratio: 250 / 188, at: [0.62, 0.45], height: 300 })
   const red = Prop('assets/lrrh.jpg', { ratio: 771 / 503, at: [0.84, 0.62], height: 300 })
   slide(Scene({ photo: 'assets/kansas-city.jpg', mute: 0.6, drift: 0 }, walt, logo, red))
   ```

   ```
   In 1922, [Walt Disney](walt) [opened](walt.bounce) a studio called [Laugh-O-Gram](logo). It made cartoons like
   [Little Red Riding Hood](red). A year later, [it was bankrupt](walt.shake).
   ```

   - `ratio` is the file's width over its height.
   - `at` is where its bottom sits, across and down the stage.
   - People stand at the sides, moved in from the corners, about `[0.24, 1.1]` and `[0.77, 1.1]` (Ian, 2026-11-08: "too in the corner. It should be a little bit in because that way there's some room for the captions"). The board ends its pictures and name tags above the caption strip, at y 920. Give pictures no `at` or height: the board lays them out in the room between the people and in the band above their heads, splitting them so the smallest picture is as big as it can be, and nothing covers anything (Ian: "make sure that we don't have things in front of each other", and "a lot of the images were too small"). Keep people within the stage: a person's `at` is their middle, so a wide cutout at `0.17` runs off the left edge; `[0.24, 1.1]` and `[0.77, 1.1]` at about 760–820 tall leave the most room.
   - A picture the script only moves, like `[pledged](cash.pop)`, comes on at that move. Better still, name it first.
   - Each backdrop is a real place from the story, muted at 0.55–0.75. Don't use the same photo as both a backdrop and a picture on that slide.
5. **Build and look.** Run `python3 $S/video.py <project>` (about 30 s), then `node $S/stills.mjs <project> "" 0.96`. Read the contact sheet, fix what's wrong, and serve it with `--no-open`.

## How long it takes

Measured on the dense Disneyland board (21 pictures, 5 slides), November 7, 2026:

| Step | Time |
|---|---|
| Pictures, 28 names checked by a vision model | 8.8 s, then 3.5 s for a second try at the misses |
| Cutouts, all at once | about 30 s, the slowest single cutout |
| Write and build | 19 s |

Cutouts set the floor. Reuse the shared library's cutouts of the same people (Walt, Roy) instead of cutting them again.
