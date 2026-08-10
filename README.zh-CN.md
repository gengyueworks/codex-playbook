<p align="center">
  <img src="https://img.shields.io/badge/Codex-Playbook-10a37f?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/11-章节-0366B5?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/3-案例-2ea44f?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/ZH/EN-8b949e?style=for-the-badge"/>
</p>

# Codex Playbook

> **Codex 被严重低估了。** 大多数人的用法止步于：打开项目→扔需求→改代码→收工。这当然能干活——但就像买了一台工作站只用来开浏览器。它有意思的地方在于，你可以让它陪着一个项目从无到有、一点点成型、不断改善。它是一个虚拟世界里的长期工程搭档，你们一起在实际世界共创了新的发明。你挥洒灵感，它为你搭建城堡的骨架、添加细节。它值得不断被探索，就像你开拓了世界上一块新的地图。

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

## 内容速览

| 章节 | 核心 |
|---|---|
| [开始](playbook/01-getting-started.md) | 安装、登录、第一个命令 |
| [执行模型](playbook/02-execution-model.md) | Codex 和对话工具的本质差异 |
| [AI First](playbook/03-ai-first.md) | 五步习惯 + 三个实战案例 |
| [需求表述](playbook/04-task-specification.md) | 指令公式、LLM 认知模型、迭代法 |
| [六步工作流](playbook/05-standard-workflow.md) | 从需求到交付的完整管控 |
| [模板库](playbook/workflow.md) | 8 个可直接复制的 prompt 模板 |
| [环境配置](playbook/06-environment.md) | 四个基础设置、Thread、Sandbox |
| [Skill 系统](playbook/07-capabilities.md) | 创建、优化、串联 Skill |
| [实战工作流](playbook/08-real-world-workflows.md) | 五步骨架、harness 心法 |
| [进阶用法](playbook/10-advanced.md) | 10 个超越代码补全的用法 |
| [故障排查](playbook/09-troubleshooting.md) | 方案切换的判断框架 |
| [核心功能](playbook/core-features.md) | Thread / Sandbox / Plugin / Skill / MCP |

---

## 仓库结构

```
codex-playbook/
├── README.md              ← English
├── README.zh-CN.md        ← 中文
├── playbook/
│   ├── 01-getting-started.md
│   ├── 02-execution-model.md
│   ├── 03-ai-first.md
│   ├── 04-task-specification.md
│   ├── 05-standard-workflow.md
│   ├── 06-environment.md
│   ├── 07-capabilities.md
│   ├── 08-real-world-workflows.md
│   ├── 09-troubleshooting.md
│   ├── 10-advanced.md
│   ├── 11-case-index.md
│   ├── core-features.md
│   └── workflow.md
├── examples/
└── resources/
```

---

## 3 分钟上手

```
1. 装 Codex（App / CLI）
2. 终端进入项目目录: codex
3. 说人话
```

剩下的都是习惯问题。

---

## 🙌 一起完善

有 Codex 实战经验？欢迎 PR——尤其如果你也是非程序员。

- 提 PR 补充你的工作流
- 开 Issue 告诉我踩过的坑
- Star 一下，让我知道有人需要它

**License**: MIT

---

*一个写作者，找到了新的打字机。Made by a writer who found a new typewriter.*
