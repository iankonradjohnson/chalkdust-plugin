# What's new

## s01 Real images, clickable links

```js
const shot = Image('assets/player.jpg', { size: 'l', ratio: 6 / 7 })
const site = Text('Open getchalkdust.com', { size: 'h2', color: 'blue', link: 'https://getchalkdust.com/' })
slide(Row(shot, site))
```

Slides can show real [images](shot). This is the player itself, in a screenshot.

And because nothing is rendered to a video file, [links](site) on the stage really work. Click this one, and Chalkdust's site opens in a new tab, while the video pauses.

## s02 A question, as a sequence

```js
const player = Labeled('Player', Part('browser', { size: 's' }))
const watcher = Labeled('Watcher', Part('eye', { size: 's' }))
const agent = Labeled('Agent', Part('robot', { size: 's' }))
slide(Sequence([player, watcher, agent], [
  [player, watcher, 'question saved'],
  [watcher, agent, 'wake up'],
  [agent, player, 'answer ready', { reply: true }],
]))
```

Pictures build along with the narration. Here are the three parts involved in answering a question: the [player](player), the [watcher](watcher) and the [agent](agent).

You ask a question in the player, and it's [saved to the server](player->watcher).

The watcher picks it up, and [wakes the agent](watcher->agent).

The agent builds an answer, and the [player plays it](agent->player).

## s03 How a project fits together

```js
const project = Labeled('Project', Part('folder', { size: 's' }))
const scene = Labeled('Scene', Part('film', { size: 's' }))
const beat = Labeled('Beat', Part('microphone', { size: 's' }))
const comment = Labeled('Comment', Part('question', { size: 's' }))
slide(Flow([
  [project, scene, 'has'],
  [scene, beat, 'has'],
  [project, comment, 'has'],
  [comment, project, { label: 'answer', dashed: true }],
]))
```

Structure works too. A [project](project) has [scenes](scene), and each scene has [beats](beat).

A project also has [comments](comment), and a comment can have its own answer, which is another whole project. That's why answers can [branch](comment->project).

## s04 The loop

```js
const watch = Labeled('Watch', Part('eye', { size: 'm' }))
const raise = Labeled('Raise your hand', Part('raised-hand', { size: 'm' }))
const answer = Labeled('Agent answers', Part('robot', { size: 'm' }))
slide(Flow([[watch, raise], [raise, answer], [answer, watch, { dashed: true }]]))
```

And here's the whole loop, in a few of our drawings.

You [watch](watch), and [raise your hand](raise). The [agent answers](answer). If the answer raises another question, the loop goes around [again](answer->watch).
