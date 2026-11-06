# Chalkdust

Claude Code answers you can watch and interrupt. Your own Claude Code writes an animated, narrated video about your codebase, you watch it at a link, and you can raise your hand at any moment to get a video answer.

## Install

```bash
claude plugin marketplace add iankonradjohnson/chalkdust-plugin
claude plugin install chalkdust@chalkdust
```

Then ask Claude Code to explain something as a video, for example `/chalkdust:video explain how our login works`. The first time, a browser tab opens to connect your GitHub account, and new accounts get 10 narrated minutes free. More minutes are at https://getchalkdust.com/account.

You don't need ffmpeg, Playwright or an OpenAI account. The command needs `python3`, which comes with macOS and most Linux systems.

## What leaves your machine

The script and scene files your agent writes go to the Chalkdust service, and the narration text goes on to OpenAI for the voice. Scenes can quote your code, so don't publish anything your company doesn't allow to be sent out. Your codebase itself isn't uploaded. Voice questions are transcribed and not kept, and you can delete a video and everything about it at any time. Anyone with a video's link can watch it, and only you can ask questions in it.

## Terms and privacy

https://getchalkdust.com/terms and https://getchalkdust.com/privacy. Questions: hello@getchalkdust.com.

## License

Proprietary. See `LICENSE`.
