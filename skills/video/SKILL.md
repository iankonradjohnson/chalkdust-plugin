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
- **Make things look like what they are.** Use real icons, not emoji, large enough to read, with panels and browser frames. Pick entrances by meaning, send the same element somewhere with `K.move` rather than popping in a copy, and land animations on the spoken word with `at.word`. The scene guide has all of these.

## Before the first publish

**Check the user is logged in.** If a command says "Not logged in", run `chalkdust login` yourself, in the background. It opens their browser on a page showing a short code, and prints the same code. Tell them the code, and ask them to check it matches, sign in with GitHub, and press Connect. The command finishes by itself once they do, and the key never appears in the conversation. New accounts get 10 free narrated minutes.

Never ask for a key in chat, and never run `chalkdust login <key>` with a key you were given: it would stay in the conversation.

**Tell the user what leaves this machine,** once, before their first publish in a project, and get a yes: "The script and scene files I write go to the Chalkdust service, and the narration text goes on to OpenAI for the voice. Anyone with the video's link can watch it." If they've already told you publishing is fine, still say this once, then go ahead. Follow any rule their company has about sending code out.

**Never put secrets in a scene.** Before each publish, check the script and scene files for keys, tokens, passwords, customer data and internal URLs, even if they appear in the code you're explaining. Trim them out.

## Making a video

1. **Plan scenes.** One scene per idea, usually 25–60 seconds each, with the length set by the concept or by what the user asks for. Narration runs at about 2.4 words per second, so a one-minute video is about 145 words. Lead with the user's actual question, use real code from the repo, and finish with a recap.
2. **Write the project** in a folder outside the repo, such as `~/chalkdust/<slug>/`, unless the user names another: `scenes.json`, `scenes/<id>.html` and, if needed, `assets/`. Read `${CLAUDE_PLUGIN_ROOT}/skills/video/references/design-system.md` first: every color, size, layout, drawing, piece, `K` helper, form and transition there is, so use what it names rather than plain boxes. Then start each slide from the closest preset in `${CLAUDE_PLUGIN_ROOT}/skills/video/references/presets.md`: a tested scene for every form and piece, to copy and change. Then read `${CLAUDE_PLUGIN_ROOT}/skills/video/references/scene-authoring.md`. It has the timing rules, building blocks, layout grid, diagrams, images and links. `${CLAUDE_PLUGIN_ROOT}/skills/video/examples/demo/` is a short complete project to copy from. Write narration in plain, short sentences, and land each animation on the sentence that describes it. Mark what to show: put backticks around a word in the narration, like "and `Flow` builds along its arrows", and what it names on screen (a name in the code, or a caption) lights as it's said. The voice and captions get the plain words. When you show code from a repository you can reach on GitHub, give `Code` its `link` to the file (`https://github.com/owner/repo/blob/<branch>/<path>#L<line>`): the block shows the file's name and opens it, so prefer that to naming the file in the narration.
   **The fast way: the marked script first, then fill in presets.**
   - Write `scenes.json` first, every slide's title and narration, with the things to show marked in backticks (about one a sentence, and the first mention of each thing). This needs the most thought, so write it yourself.
   - Then fill in each slide. For most, a preset is enough: `chalkdust show ~/chalkdust/<slug> <slide id> '{"preset": "flow", "things": ["Browser", "Server", "Database"]}'` writes `scenes/<id>.html`, with each thing's drawing found by its name. Presets: `flow` (`things`, and `verbs` for the words on its arrows), `row`, `cycle` (`things`), `compare` (`left`, `right`), `stack` (`layers`, `nest`), `timeline` (`steps`, `down`), `bars`, `code` (`code`, `lang`, `link`), `terminal` (`lines`) and `stat`. Or put every slide's show in `shows.json` as `{ "<slide id>": { "preset": ... } }` and run `chalkdust show ~/chalkdust/<slug>`.
   - Slides are independent once the script is written, so hand them to Sonnet subagents in parallel, one per slide, each with that slide's marked narration and the list of presets. Nothing in a preset is timed: the marks do that.
   - For anything a preset can't draw, like a custom drawing, write that slide by hand.

3. **Publish:**
   ```bash
   chalkdust publish ~/chalkdust/<slug>
   ```
   This uploads the scenes, waits for the narration and build, and prints any warnings, the stills and two links. Publishing the same folder again updates the same video and links. It saves `.chalkdust.json`, which holds the private owner link, and `.chalkdust/` in the folder. If the folder is inside a repo, add both to `.gitignore`.
4. **Check the stills.** Read every sheet it lists. They show each scene near its end, fully built, so also think through the order things appear. If it says no stills because a scene didn't load, fix that scene, because it's blank in the player too. If it says the problem is on the service, tell the user you couldn't check the visuals. Look for text wrapping in pills, arrows crossing boxes or labels, notes overlapping, and content running into the caption zone. Count the words on screen. Fix them and publish again. Work presented as finished that still has flaws loses trust, so look properly. If a warning says the spoken text differs from the script, read it: small differences are fine, but a line where the voice says something else isn't. Reword that line and publish again.
5. **Start the watcher, then give the user the link:**
   ```bash
   chalkdust watch ~/chalkdust/<slug>       # background task
   ```
   Start it before handing over the link, unless the user says not to. A question asked while it isn't running waits unanswered, and the player shows "Claude isn't listening". Give the user their own link, which lets them ask questions, and the watch-only link for sharing. Their own link is private to them.

In the player: **Space** plays and pauses, **R** asks a question out loud, **T** types one, **G** marks "got it", **L** marks "lost here", **C** turns captions on or off, and links in a scene are clickable. Tell the user these in a line or two.

## Answering questions while the user watches

Questions should be answered in the moment, like raising a hand in class. **Every answer is a branch, not a footnote:** a full video with one scene or many, as deep as the question needs, at any nesting level. How long and how deep is your call, per question.

`chalkdust watch` runs as a **background task**. It blocks until there are comments to handle, claims all of them, prints each one's context as a JSON object, and exits. Its exit is what wakes you. If comments are already waiting, it returns right away. The context has the question, the caption on screen, the narration around it, `scene_source` (the scene they were watching), `asked_inside` (the questions above it, if it was asked inside an answer) and `answer_folder`. `time` is when it was asked: in the main video, or inside the answer clip if `in_answer` is set. `ask` is true for every comment except "got it", so decide for yourself whether it's really a question.

When it wakes you:

1. **Restart the watcher first,** in the background, so a second question isn't missed. Always read what it printed. A question it claimed that nobody answered comes back under `REMINDER:` once three minutes pass with nothing written for it, every time the watcher starts, until you answer it (`chalkdust stream ... --done` or `release`), or note it with `chalkdust note` if it needs no answer.
2. Read the context. Check the code if the answer depends on facts.
3. **Stream the answer,** so the viewer starts hearing it after its first sentence instead of waiting for the whole clip. For each beat, in one Bash call, write the slide in `answer_folder` and publish it:
   ```bash
   cat > <answer_folder>/scenes/a01.html <<'SCENE'
   <script>slide(...)</script>
   SCENE
   chalkdust stream ~/chalkdust/<slug> <question id> a01 "Slide title" "One or two sentences of narration."
   ```
   The service narrates and builds that beat, and the player starts the answer about a second after the first one lands. The command prints `live:` and what the checks found on that slide. Slide ids like `a01` only need to be unique within that answer, and a nested answer gets its own `answer_folder`, so use the path you're given. Give each slide a title that makes sense on its own.
   - To grow the graphic, use the same slide id, and write the whole slide again with the new piece added. Use a new id for a new idea. Write slides with the layouts in the authoring guide, and point at what you're talking about.
   - The first sentence answers the question and makes sense by itself, as in "Because the wait doubles, so a fixed amount stops mattering." Don't re-explain the whole scene. If the question comes back a second time, go deeper and slower, not shorter.
   - Published beats can't be taken back, so say only what you've checked. If a beat fails to build, the viewer sees no change: fix it and run the command again. If the command can't reach the service, run the same command again, because a beat that already went out isn't added twice.
   - While someone's waiting, don't stop for pictures. Fix what the checks flag by writing the slide again and running `chalkdust stream ~/chalkdust/<slug> <question id> --fix a01`, which adds no beat. If the player catches up with you, it waits and tells the viewer.
4. Finish with `chalkdust stream ~/chalkdust/<slug> <question id> --done`. It checks the whole answer and takes stills of any slide placed by hand, which the beats name as they go. Read those, and fix any slide that needs it with `--fix`.

When nobody's waiting, or an answer needs a full plan first, you can build it whole instead: write `scenes.json` and `scenes/<id>.html` in `answer_folder`, run `chalkdust answer ~/chalkdust/<slug> <question id>`, read the stills it lists, then run `chalkdust release ~/chalkdust/<slug> <question id>`. Use the kicker `Answer · <time> · "<short quote of the question>"`. That takes a couple of minutes before the viewer sees anything.

If a comment isn't a question, such as a statement or "got it, never mind", leave one line instead of a video:

```bash
chalkdust note ~/chalkdust/<slug> <question id> "Glad it clicked. Nothing more needed here."
```

Keep it to what they said: confirm what they worked out, or point them to the moment that covers it.

The watcher stops by itself about 30 minutes after nobody has the video open, and says so. Don't restart it then, unless the user comes back to that video.

## Reading comments later

Run `chalkdust comments ~/chalkdust/<slug>` when the user says they've left comments, without asking them what they said. It shows everything, including answers already given. To answer the ones still waiting, run `chalkdust watch`: it claims them and gives you each `answer_folder`, which you need for answering. Answer them as branches, not in a separate video, unless the user asks for one.

## Editing

Edit the files and publish again. Changing narration shifts the timeline, so older comments point at old timestamps, though they keep their scene and caption text.

## Deleting

If the user wants a video gone, confirm first, because it can't be undone, then run `chalkdust delete ~/chalkdust/<slug> --yes`. It removes the video, narration, comments and answers from the service, and the links stop working. Voice questions aren't kept after they're transcribed.

## Problems

- **402:** their narrated minutes have run out. Tell the user, and give them the link in the message, where they can get more.
- **429:** too many requests. Wait a little and try again.
- **Connection errors:** `chalkdust watch` retries by itself. For other commands, say the service may be down, and try once more.
- **Build failed:** read the error. It usually names the scene or file.
