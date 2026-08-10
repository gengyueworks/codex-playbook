<p align="center">
  <img src="https://img.shields.io/badge/Codex-Playbook-10a37f?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/4-手册章节-0366B5?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/3-实战案例-2ea44f?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/2-语言-8b949e?style=for-the-badge"/>
</p>

# Codex Playbook

> **用了一段时间 Codex 之后，我最大的感受是：很多人其实低估了它。**
> 现在很多人的用法基本是：打开项目文件夹 → 输入需求 → 等它改代码。这个当然已经很强了。但是如果只是这样用，感觉有点像买了一台高性能电脑，只拿来看网页。
> **Codex 真正有意思的地方，是把它当成一个"长期合作的开发助手"，而不是一个高级代码补全工具。**
>
> *After using Codex for a while, I've realized most people underestimate it. The typical usage is: open a project → describe a task → let it change code. That's already powerful. But using it only that way is like buying a high-performance PC just to browse the web. The interesting part of Codex is treating it as a long-term development partner, not a fancy autocomplete.*

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

## 📚 Content Overview / 内容速览

| # | 章节 | 一句话核心 | 阅读 |
|---|---|---|---|
| 1 | 🚀 开始 | 装好、登录、说第一句话 | [full](playbook/en/full.md) |
| 2 | 💬 说人话 | 指令公式：角色+任务+上下文+验收 | [full](playbook/en/full.md#chapter-3-the-secret-to-speaking-plainly) |
| 3 | 📐 AGENTS.md | 让 Codex 记住你的规矩 | [full](playbook/en/full.md#chapter-4-agentsmd) |
| 4 | 🧩 核心功能 | Thread / 沙盒 / 插件 / Skill / MCP | [core-features](playbook/en/core-features.md) |
| 5 | 🔄 工作流 | 从需求到交付的六步法 | [workflow](playbook/en/workflow.md) |
| 6 | 🧰 模板库 | 8 个可直接复制的任务模板 | [workflow](playbook/en/workflow.md#task-template-library) |
| 7 | ⚠️ 常见坑 | 五个血泪教训 | [full](playbook/en/full.md#chapter-7-common-traps) |

### Difficulty / 难度分级

| 难度 | 内容 | 在哪 |
|---|---|---|
| 🟢 入门 | 3 分钟跑起来 | [mini](playbook/en/mini.md) |
| 🔵 进阶 | 一页掌握核心 | [mini](playbook/en/mini.md) |
| 🟣 实战 | 完整手册 + 真实案例 | [full](playbook/en/full.md) + [examples](examples/) |
| 🔴 背下来 | 就记住这几条 | [nano](playbook/en/nano.md) |

---

## 📂 Repository Structure / 仓库结构

```
codex-playbook/
├── README.md              ← you are here (English)
├── README.zh-CN.md        ← 中文版
├── playbook/              ← 手册正文 (Chinese)
│   ├── full.md            ← 完整版
│   ├── workflow.md        ← 六步法 + 任务模板库
│   ├── mini.md            ← 一页版
│   └── nano.md            ← 背下来版
├── playbook/en/           ← The manual (English)
│   ├── full.md
│   ├── workflow.md
│   ├── mini.md
│   └── nano.md
├── examples/              ← 实战案例
│   ├── daily-auto-update.md
│   ├── repo-from-essay.md
│   └── obsidian-sync.md
└── resources/             ← 资源导航
    ├── zhihu.md           ← 知乎教程精选
    └── links.md           ← 外部链接
```

---

## ⚡ Quick Start / 3 分钟上手

```
1. 装 Codex（App / CLI）
2. 终端进入项目目录: codex
3. 说人话："把这个 README 改得更吸引人"
```

Done. That's it. **Everything else is habit.**

---

## 🙌 Contribute / 一起完善

Have Codex field experience? PRs welcome — especially if you're also a non-programmer.

- 提 PR 补充你的工作流
- 开 Issue 告诉我踩过的坑
- Star 一下，让我知道有人需要它

**License**: MIT

---

*Made by a writer who found a new typewriter. 一个写作者，找到了新的打字机。*
