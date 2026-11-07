---
name: video
description: Make an animated, narrated explainer video of anything in this codebase, played at a link with diagrams that build in step with a voice, where the viewer can raise a hand at any moment and you answer with another video. Use whenever the user asks for a video, a "video version" of an explanation, an animated walkthrough of code or a spec or PR, or wants to "watch" an explanation instead of reading it. Also use when the user says they left comments on a video, or wants to answer questions asked in one. Not for status updates, which are better read.
---

# Chalkdust

You turn an explanation into a short animated video. Each diagram builds step by step while a voice explains it, and captions run along the bottom. You write the scenes here, because you know this codebase. The `chalkdust` command sends them to the hosted service, which narrates them and plays them at a link. When the viewer asks a question, it wakes you, and you answer with another video.

Match the explanation to what the user already knows, and prefer concrete code and diagrams, with few words. If `~/.claude/chalkdust-preferences.md` exists, read it first: it holds this user's own preferences, and they win over the defaults here. What the user tells you for this video wins over both.

**Keep slides light on text. This matters more than anything else on the screen.** The narration carries the explaining. The screen shows a picture of the idea: shapes, arrows, things moving, one short label each.
- At most about **15 words on screen per scene**, not counting code. Labels are 1–5 words. No full-sentence notes, and no file paths or line numbers on screen.
- **Show, don't list.** If a scene is a list of boxes with sentences in them, redesign it as a diagram.
- One idea per scene. Captions already show the narration, so never repeat it as on-screen text.
- **Prefer real code with animated line highlights** for anything about how code behaves. Keep blocks under about 12 lines.
- **Make things look like what they are.** Use our drawings, not emoji, large enough to read. Send the same piece somewhere with `moveTo` rather than popping in a copy, and land every change on the word that says it, with a link. The scene guide has all of these.

## Before the first publish

**Check the user is logged in.** If a command says "Not logged in", run `chalkdust login` yourself, in the background. It opens their browser on a page showing a short code, and prints the same code. Tell them the code, and ask them to check it matches, sign in with GitHub, and press Connect. The command finishes by itself once they do, and the key never appears in the conversation. New accounts get 10 free narrated minutes.

Never ask for a key in chat, and never run `chalkdust login <key>` with a key you were given: it would stay in the conversation.

**Tell the user what leaves this machine,** once, before their first publish in a project, and get a yes: "The script and scene files I write go to the Chalkdust service, and the narration text goes on to OpenAI for the voice. Anyone with the video's link can watch it." If they've already told you publishing is fine, still say this once, then go ahead. Follow any rule their company has about sending code out.

**Never put secrets in a scene.** Before each publish, check the script and scene files for keys, tokens, passwords, customer data and internal URLs, even if they appear in the code you're explaining. Trim them out.

## Making a video

1. **Outline first, then write one slide at a time.** Write `outline.md` before anything else: one line per slide, its id and heading and a few words on what it covers. Write slide one yourself, its cast, its script and its links together, and stream it (step 4), so the user is watching within a minute. Then link the rest in order, one slide at a time: add the next slide's cast, words and links to `video.md`, and stream it. Write each while the one before it plays, and keep every slide yourself, since you already have the context. One scene per idea, usually 25–60 seconds each, with the length set by the concept or by what the user asks for. Narration runs at about 2.4 words per second, so a one-minute video is about 145 words. Lead with the user's actual question, use real code from the repo, and finish with a recap.
2. **Keep them watching.** A video people leave is a video nobody learned from (Ian, 2026-11-07: a viewer found a video "felt linear"). Build every video to these rules; the build warns when one is broken, and never refuses a slide for it.
   - **Prove the title in the first ten seconds.** Slide one shows the payoff, its picture on screen, with a link on its first words: the engines lighting up, not a list of steps.
   - **Open a loop, and pay it off.** Early on, promise something the end delivers ("by the end, you'll see why engine two starts first"), and make sure the last slides deliver it.
   - **Put the wrong idea first.** Where people usually believe something wrong, say it, then correct it: it teaches more than a clear explanation alone (Derek Muller's research for Veritasium).
   - **Change the form on every slide.** No two slides in a row are the same kind of picture: follow a diagram with code, a big number, a comparison, a chart or a photo. Name each slide's form in the outline. The presets have a form for each: `p-reveal` (a question, then the big number), `p-before-after`, `p-predict` (pause and guess, then the answer swaps in), `p-countdown`, `p-photo` (a real image, full width), `p-myth` (the wrong idea, then what's true) and `p-quote`, besides the charts, code and diagrams.
   - **Something moves every second.** At about two and a half words a second, that is something every two or three words: a word lighting, a part coming on, a line drawing, a number counting. Moves that play for a while, a count-up, a stream of dots, a line drawing in, count while they play. Link more words, let pieces build in part by part, and never link the same thing twice in a row (Ian, 2026-11-07: "it should be every one second").
3. **Write the video** in a folder outside the repo, such as `~/chalkdust/<slug>/`, unless the user names another: one file, `video.md`, and `assets/` for any images. Each slide is a `## heading`, a `js` block that says what can be on screen with no timing in it (the cast), and the narration under it, where each action sits on the word it happens on (the script):

   ````md
   # How login works

   ## s01 Signing in

   ```js
   const user = Part('browser'), app = Part('server'), db = Part('database')
   slide(Sequence([user, app, db], [[user, app, 'sign in'], [app, db, 'lookup']]))
   ```

   The [user](user) [signs in](user->app), and the [server](app) [checks the database](app->db db:red).
   ````

   A link names what happens on its words: `name` brings it on, then lights it; `name:red` or `name:spot` lights it in a color or with the spotlight; `-name` hides it; `pointer: on` under the `# title` adds a dot that glides to each thing a beat before it lights; `a->b` draws the line between two things, and sends something along it the next time; `name.part` points inside a piece, like `code.2`, `steps.launch` or `trace.server`; `name.swap` runs a move the cast gave it. Write about one thing to show a sentence, and link it. Link only what that sentence is about: a light is where the viewer's attention goes, so never light an unrelated thing to keep a slide moving. If a sentence names nothing on screen, put something on screen that shows it (an icon, a word in a diagram, a step) and link that, or say less. Read `${CLAUDE_PLUGIN_ROOT}/skills/video/references/presets.md`: a tested slide for every piece and form, cast and script, to copy and change. `${CLAUDE_PLUGIN_ROOT}/skills/video/references/design-system.md` lists every color, drawing, piece and option, with the parts each piece has, and `${CLAUDE_PLUGIN_ROOT}/skills/video/references/scene-authoring.md` has the rest of the grammar and how to choose a picture. `${CLAUDE_PLUGIN_ROOT}/skills/video/examples/demo/video.md` is a short complete video to copy from. Use drawings (`chalkdust parts <words>`) rather than words wherever you can. When you show code from a repository you can reach on GitHub, give `Code` its `link` to the file (`https://github.com/owner/repo/blob/<branch>/<path>#L<line>`): the block shows the file's name and opens it, so prefer that to naming the file in the narration.

4. **Stream it, so the user watches while you write.** Once the first slide is written, run:
   ```bash
   chalkdust stream ~/chalkdust/<slug>
   ```
   The first run makes the video and prints its two links. Start the watcher (step 6) and give the user their link now: the player starts at the first beat, while you write the rest. Then write the next slide, or the next paragraph of this one, and run the same command again. Only what's new is voiced, and it plays within seconds. It prints `live:` and what the checks found on the newest slide. A warning is for the slides still to come: write the next ones better, and don't go back to change a slide the user has already watched. A beat once played can't change, so say only what you've checked. Finish with `chalkdust stream ~/chalkdust/<slug> --done`, which checks the whole video.

   When nobody's waiting, you can build it whole instead:
   ```bash
   chalkdust publish ~/chalkdust/<slug>
   ```
   This uploads `video.md`, waits for the narration and build, and prints any warnings, the stills and two links. Publishing the same folder again updates the same video and links. It saves `.chalkdust.json`, which holds the private owner link, and `.chalkdust/` in the folder. If the folder is inside a repo, add both to `.gitignore`.
5. **Check the stills and the warnings.** A link to something the cast doesn't have, or a slide that was never named, comes back as a warning: fix it in `video.md`. A file that can't be read at all is refused with its slide and line. Read every sheet it lists. They show each scene near its end, fully built, so also think through the order things appear. If it says no stills because a scene didn't load, fix that scene, because it's blank in the player too. If it says the problem is on the service, tell the user you couldn't check the visuals. Look for text wrapping in pills, arrows crossing boxes or labels, notes overlapping, and content running into the caption zone. Count the words on screen. Fix them and publish again. Work presented as finished that still has flaws loses trust, so look properly. If a warning says the spoken text differs from the script, read it: small differences are fine, but a line where the voice says something else isn't. Reword that line and publish again.
6. **Start the watcher, then give the user the link:**
   ```bash
   chalkdust watch ~/chalkdust/<slug>       # background task
   ```
   Start it before handing over the link, unless the user says not to. A question asked while it isn't running waits unanswered, and the player shows "Claude isn't listening". Give the user their own link, which lets them ask questions, and the watch-only link for sharing. Their own link is private to them.

In the player: **Space** plays and pauses, **R** asks a question out loud, **T** types one, **G** marks "got it", **L** marks "lost here", **C** turns captions on or off, and links in a scene are clickable. Tell the user these in a line or two.

## Answering questions while the user watches

Questions should be answered in the moment, like raising a hand in class. **Every answer is a branch, not a footnote:** a full video with one scene or many, as deep as the question needs, at any nesting level. How long and how deep is your call, per question.

`chalkdust watch` runs as a **background task**. It blocks until there are comments to handle, claims all of them, prints each one's context as a JSON object, and exits. Its exit is what wakes you. If comments are already waiting, it returns right away. The context has the question, the caption on screen, the narration around it, `scene_source` (the scene they were watching), `asked_inside` (the questions above it, if it was asked inside an answer) and `answer_folder`. `time` is when it was asked: in the main video, or inside the answer clip if `in_answer` is set. `ask` is true for every comment except "got it", so decide for yourself whether it's really a question.

When it wakes you:

1. **Restart the watcher first,** in the background, so a second question isn't missed. Then **hand each question to its own background agent**, one per question, as soon as it's claimed, so the user never waits on one answer for another, or on whatever you're doing. Give the agent the question, its `answer_folder`, the facts it needs already checked, and these steps. It writes only in that folder. If the question asks for a change to the code, the agent's answer says what's changing, and you make the change yourself. Check each answer when its agent reports. Always read what it printed. A question it claimed that nobody answered comes back under `REMINDER:` once three minutes pass with nothing written for it, every time the watcher starts, until you answer it (`chalkdust stream ... --done` or `release`), or note it with `chalkdust note` if it needs no answer.
2. Read the context. Check the code if the answer depends on facts.
3. **Stream the answer,** so the viewer starts hearing it after its first sentence instead of waiting for the whole clip. The answer is a `video.md` in `answer_folder`, written as `# Answer` and slides like `## a01 <a title that makes sense on its own>`. Write the first slide, with one paragraph of script, and publish it:
   ```bash
   chalkdust stream ~/chalkdust/<slug> <question id>
   ```
   The service narrates and builds what's new, and the player starts the answer about a second after the first beat lands. The command prints `live:` and what the checks found on the newest slide. Then add the next beat, a paragraph under the same slide or a new `## a02` slide, and run the same command again: only the new beat is narrated. A nested answer gets its own `answer_folder`, so use the path you're given.
   - To grow the graphic, add to the slide's cast and link the new piece in the new paragraph.
   - The first sentence answers the question and makes sense by itself, as in "Because the wait doubles, so a fixed amount stops mattering." Don't re-explain the whole scene. If the question comes back a second time, go deeper and slower, not shorter.
   - A beat once played can't change or go, so say only what you've checked, and only add after it. A cast can be corrected and sent again, which adds no beat. If a beat fails to build, the viewer sees no change: fix it and run the command again. If the command can't reach the service, run it again: what already went out isn't added twice.
   - While someone's waiting, don't stop for pictures. Fix what the checks flag and keep going. If the player catches up with you, it waits and tells the viewer.
4. Finish with `chalkdust stream ~/chalkdust/<slug> <question id> --done`, which checks the whole answer.

When nobody's waiting, or an answer needs a full plan first, you can build it whole instead: write the whole `video.md` in `answer_folder`, run `chalkdust answer ~/chalkdust/<slug> <question id>`, read the stills it lists, then run `chalkdust release ~/chalkdust/<slug> <question id>`. That takes a couple of minutes before the viewer sees anything.

If a comment isn't a question, such as a statement or "got it, never mind", leave one line instead of a video:

```bash
chalkdust note ~/chalkdust/<slug> <question id> "Glad it clicked. Nothing more needed here."
```

Keep it to what they said: confirm what they worked out, or point them to the moment that covers it.

The watcher stops by itself about 30 minutes after nobody has the video open, and says so. Don't restart it then, unless the user comes back to that video.

## Reading comments later

Run `chalkdust comments ~/chalkdust/<slug>` when the user says they've left comments, without asking them what they said. It shows everything, including answers already given. To answer the ones still waiting, run `chalkdust watch`: it claims them and gives you each `answer_folder`, which you need for answering. Answer them as branches, not in a separate video, unless the user asks for one.

## Editing

Edit `video.md` and publish again. Changing narration shifts the timeline, so older comments point at old timestamps, though they keep their scene and caption text.

## Deleting

If the user wants a video gone, confirm first, because it can't be undone, then run `chalkdust delete ~/chalkdust/<slug> --yes`. It removes the video, narration, comments and answers from the service, and the links stop working. Voice questions aren't kept after they're transcribed.

## Problems

- **402:** their narrated minutes have run out. Tell the user, and give them the link in the message, where they can get more.
- **429:** too many requests. Wait a little and try again.
- **Connection errors:** `chalkdust watch` retries by itself. For other commands, say the service may be down, and try once more.
- **Build failed:** read the error. It usually names the scene or file.
