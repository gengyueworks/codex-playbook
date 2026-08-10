<p align="center">
  <img src="https://img.shields.io/badge/Codex-Playbook-10a37f?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/10-章节-0366B5?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/非程序员-指南-2ea44f?style=for-the-badge"/>
</p>

# Codex Playbook

*A practical guide to using Codex, written for people who don't write code — by someone who doesn't either.*

[中文说明](README.zh-CN.md)

---

Codex is usually described as a coding tool. That framing scares off a lot of capable people. This book takes the opposite view: if you can describe what you want in plain language, you can already use Codex to build and run real things. No programming background required.

## Who this is for

This guide is written for non-technical users — people with strong ideas and zero code. It comes from someone in exactly that position: a writer by training (formerly in travel storytelling, now covering AI tools), with no computer-science background and no hand-written production code to their name.

What makes it more than opinion is the system behind it. This is not a demo built for the book. It is a setup that has run in production, every day:

- **41 repositories** on GitHub, all holding original writing and content
- a single **rule file (AGENTS.md) of roughly 859 lines** that keeps every project consistent
- **5 scheduled tasks** that publish and update content on their own
- **40+ reusable skills** that compress repeated work into one-line commands

All of it was built *with* Codex, not coded by hand. That is the point of this book: a non-programmer can operate at this scale.

## The one idea

> **Codex = describe the outcome in plain language, and it does the building.**

You are the editor; it is the team. You decide what matters, it handles the mechanics. The skill isn't in coding — it's in saying clearly what you want, and setting guardrails so it doesn't wander.

## If you don't know where to start

Codex isn't thrown off by a messy brief — what it struggles with is a vague one-line ask followed by "just build it." Most people who find AI hard (any AI, not just Codex) aren't held back by a weak tool or fancy prompting. They've just never handed it a real, specific, messy problem in full.

So the first step isn't learning to write prompts. It's saying it out loud:

1. Open the voice recorder on your phone, as if no one's listening. Talk about what you want to do, what's stuck, what you've been meaning to start.
2. Don't organize your language. Don't aim for logic. Don't try to sound smart. Just talk — at least ten minutes.
3. Send the recording to your computer and transcribe it with any tool you like (Feishu Miaoji, MacWhisper, Notta, iFlytek, or similar).
4. Back in Codex, paste the transcript and add one line: "Don't jump to a solution. Ask me questions first — help me find what actually matters here, and keep asking until I say go."
5. Hand over the wheel.

This is exactly what Codex is good at: you drop in a messy idea, it asks back before it builds, which gets around the "afraid to ask the wrong thing, so I don't ask at all" block. Curiosity and follow-up questions beat memorized prompt templates. The rest of this book is about turning what you said into something real.

## What's inside

Ten chapters, each a self-contained how-to. Read in order, or jump to what you need.

| # | English | 中文 | One line |
|---|---------|------|----------|
| 01 | [What Codex Can Do For You](playbook/01-Codex能帮你干什么.md) | Codex 能帮你干什么 | The five kinds of work it takes off your plate |
| 02 | [Getting Started](playbook/02-怎么开始用.md) | 怎么开始用 | Install the desktop app, switch to Codex, open a folder |
| 03 | [Telling It What You Want](playbook/03-怎么把话说清楚.md) | 怎么把话说清楚 | State the outcome, the scope, and the lines not to cross |
| 04 | [Keeping It From Editing The Wrong Things](playbook/04-让它别乱改东西.md) | 让它别乱改东西 | Boundaries so it only touches what you pointed at |
| 05 | [Making It Remember Your Rules](playbook/05-让它记住你的规矩.md) | 让它记住你的规矩 | A rule file it reads before every task |
| 06 | [Turning Routines Into Skills](playbook/06-把常用操作变成Skill.md) | 把常用操作变成 Skill | Save a repeated workflow as a reusable command |
| 07 | [Letting Projects Run Themselves](playbook/07-让项目自己跑起来.md) | 让项目自己跑起来 | Scheduled tasks that run without you |
| 08 | [Gathering and Organizing Material](playbook/08-抓资料整理资料.md) | 抓资料整理资料 | Pull scattered notes into one clean file |
| 09 | [Common Pitfalls](playbook/09-常见的坑.md) | 常见的坑 | Six mistakes that waste an afternoon |
| 10 | [Templates That Work](playbook/10-验过的模板.md) | 验过的模板 | Copy-ready rule file and repo README |

## How to read this

New to Codex? Start at 01. Already tried it once? Jump to 03 (how to phrase requests) and 05 (the rule file) — those two change everything. Chapters 09 and 10 are the ones to read before you trust it with anything real.

## License

Released under the MIT License. See [LICENSE](LICENSE).
