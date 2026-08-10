<p align="center">
  <img src="https://img.shields.io/badge/Codex-Playbook-10a37f?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/4-手册章节-0366B5?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/3-实战案例-2ea44f?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/2-语言-8b949e?style=for-the-badge"/>
</p>

# Codex Playbook

> **Codex 被严重低估了。** 大多数人的用法止步于：打开项目→扔需求→改代码→收工。这当然能干活——但就像买了一台工作站只用来开浏览器。这个东西的真正价值，是作为一个长期工程搭档，而不只是一把快一点的扳手。

*[English](README.md) · 中文*

---

## 这是什么

Codex 的用户当然包括程序员。但我想它也一定欢迎像我这样的人：**有很棒的审美、有无数的灵感，只是还不会写代码。**

我不是程序员，我是写作者。旅行、音乐、AI、科学——我用 Codex 干这些：

- 把我的文章仓库化、自动化
- 让 GitHub Action 每天替我更新内容
- 一键把想法变成可发布的项目
- 一个人维护 100+ 个仓库

这本手册就是我的一手经验。**每个方法都经过真实使用验证，不是抄来的。**

**我的故事：** 注册 GitHub 很多年，但一直困在一个心结里——不会写代码，想法总卡在"动手"这一步。AI coding agent 改变了一切。GPT 问世我就在用，一直关注 OpenAI，从 Sam Altman 在 YC 时期就开始读他的博客。沉浸了半年 agents 世界之后，我终于把积累的东西一个个传上线：100+ 个仓库，全是原创写作和内容。这本手册记录的就是这条路。

---

## 一句话核心

> **Codex = LLM + 你的上下文 + 工具。** 你会说人话，它就会干活。
> 你是老板，它是员工。说清楚你要什么，剩下的交给它。

---

## 📚 内容速览

| # | 章节 | 一句话核心 | 阅读 |
|---|---|---|---|
| 1 | 🚀 开始 | 装好、登录、说第一句话 | [full](playbook/full.md) |
| 2 | 💬 说人话 | 指令公式：角色+任务+上下文+验收 | [full](playbook/full.md#第三章) |
| 3 | 📐 AGENTS.md | 让 Codex 记住你的规矩 | [full](playbook/full.md#第四章) |
| 4 | 🧩 核心功能 | Thread / 沙盒 / 插件 / Skill / MCP | [core-features](playbook/core-features.md) |
| 5 | 🔄 工作流 | 从需求到交付的六步法 | [workflow](playbook/workflow.md) |
| 6 | 🧰 模板库 | 8 个可直接复制的任务模板 | [workflow](playbook/workflow.md#任务模板库) |
| 7 | ⚠️ 常见坑 | 五个血泪教训 | [full](playbook/full.md#第七章) |

### 难度分级

| 难度 | 内容 | 在哪 |
|---|---|---|
| 🟢 入门 | 3 分钟跑起来 | [mini](playbook/mini.md) |
| 🔵 进阶 | 一页掌握核心 | [mini](playbook/mini.md) |
| 🟣 实战 | 完整手册 + 真实案例 | [full](playbook/full.md) + [examples](examples/) |
| 🔴 背下来 | 就记住这几条 | [nano](playbook/nano.md) |

---

## 📂 仓库结构

```
codex-playbook/
├── README.md              ← 你在这（中文）
├── README.zh-CN.md        ← 中文版
├── playbook/              ← 手册正文
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

## ⚡ 3 分钟上手

```
1. 装 Codex（App / CLI）
2. 终端进入项目目录: codex
3. 说人话："把这个 README 改得更吸引人"
```

完事。就这么简单。**剩下的都是习惯问题。**

---

## 🙌 一起完善

有 Codex 实战经验？欢迎 PR——尤其如果你也是非程序员。

- 提 PR 补充你的工作流
- 开 Issue 告诉我踩过的坑
- Star 一下，让我知道有人需要它

**License**: MIT

---

*一个写作者，找到了新的打字机。Made by a writer who found a new typewriter.*
