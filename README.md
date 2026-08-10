<p align="center">
  <img src="https://img.shields.io/badge/Codex-Playbook-10a37f?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/11-章节-0366B5?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/3-案例-2ea44f?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/ZH/EN-8b949e?style=for-the-badge"/>
</p>

# Codex Playbook

> **Codex 被严重低估了。**
>
> 大多数人的用法止步于：打开项目→扔需求→改代码→收工。这当然能干活——但就像买了一台工作站只用来开浏览器。它有意思的事，你可以让它陪伴着你的项目从建立、从无到有，到一点点成型，不断改善。
>
> 它是一个虚拟世界里的长期工程搭档，你们一起在实际世界共创了新的发明。你挥洒灵感，它为你搭建城堡的骨架，添加细节，它值得不断被探索，就像你开拓了世界的新的地图。
>
> *Codex is severely underestimated. Most usage stops at: open a project, drop a task, change code, done. It works — but that's a workstation used to browse the web. What makes it interesting is letting it walk with a project from nothing to something, from birth to shape, through every iteration. It's a long-term partner in a virtual world, co-creating real inventions with you. You bring the vision; it builds the castle's framework and fills in the details. It deserves to be explored endlessly — like charting a new territory on the map.*

*English · [中文](README.zh-CN.md)*

---

## What is this? / 这是什么？

Of course Codex's users include programmers. But I believe it also welcomes people like me: **great taste, endless ideas, and no coding background.** This book is my first-hand account of using Codex as a non-programmer — what works, what doesn't, and the traps I fell into.

*Codex 的用户当然包括程序员。但我想它也一定欢迎像我这样的人：有很棒的审美、有无数的灵感，只是还不会写代码。这本手册记录我一个非程序员真实用 Codex 的过程——什么好用、什么不好用、踩过的坑。*

**My story:** Long-time GitHub user, but I stayed stuck for years — ideas stalled because I couldn't code. AI coding agents changed that. I've used ChatGPT since launch, followed OpenAI closely, and admired Sam Altman's writing since his YC days. After half a year deep in the AI agents world, I finally pushed my work online: 100+ repositories, all original writing and content. This book is how.

---

## The One-Line Formula / 一句话核心

> **Codex = LLM + 你的上下文 + 工具。** 你会说人话，它就会干活。
> You are the boss. It is the employee. Say what you want — it builds.

---

## Content Overview / 内容速览

| 章节 | 核心 |
|---|---|
| [开始](playbook/en/01-getting-started.md) | 安装、登录、第一个命令 |
| [执行模型](playbook/en/02-execution-model.md) | Codex 和对话工具的本质差异 |
| [AI First](playbook/en/03-ai-first.md) | 五步习惯 + 真实案例 |
| [需求表述](playbook/en/04-task-specification.md) | 指令公式、边界约束、表述对比 |
| [六步工作流](playbook/en/workflow.md) | 从需求到交付的完整管控 |
| [模板库](playbook/en/workflow.md#task-template-library) | 8 个可直接复制的 prompt 模板 |
| [环境配置](playbook/en/05-environment.md) | Thread、Sandbox、AGENTS.md |
| [能力扩展](playbook/en/core-features.md) | Skill、Plugin、MCP 三者关系 |
| [实战工作流](playbook/en/06-workflows.md) | 写作转仓库、内容自动化、批量处理 |
| [进阶用法](playbook/en/07-advanced.md) | 10 个超越代码补全的用法 |
| [故障排查](playbook/en/08-troubleshooting.md) | 方案切换的判断框架 |

---

## Repository Structure / 仓库结构

```
codex-playbook/
├── README.md              ← English
├── README.zh-CN.md        ← 中文
├── playbook/              ← 手册正文 (Chinese)
│   ├── 01-getting-started.md
│   ├── 02-execution-model.md
│   ├── 03-ai-first.md
│   ├── 04-task-specification.md
│   ├── 05-environment.md
│   ├── 06-workflows.md
│   ├── 07-advanced.md
│   ├── 08-troubleshooting.md
│   ├── core-features.md
│   └── workflow.md
├── playbook/en/           ← English
│   ├── 01-getting-started.md
│   ├── ... (same structure)
│   ├── core-features.md
│   └── workflow.md
├── examples/              ← 实战案例
└── resources/             ← 资源导航
```

---

## Quick Start / 3 分钟上手

```
1. 装 Codex（App / CLI）
2. 终端进入项目目录: codex
3. 说人话
```

Done. Everything else is habit.

---

## 🙌 Contribute / 一起完善

Have Codex field experience? PRs welcome — especially if you're also a non-programmer.

- 提 PR 补充你的工作流
- 开 Issue 告诉我踩过的坑
- Star 一下，让我知道有人需要它

**License**: MIT

---

*Made by a writer who found a new typewriter. 一个写作者，找到了新的打字机。*
