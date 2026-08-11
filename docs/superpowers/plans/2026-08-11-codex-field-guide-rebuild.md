# 非程序员使用 Codex 的经验手册改版实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 把现有的 Codex 入门手册重建为一套面向非程序员、可以跟着完成真实任务的双语经验教材。

**Architecture:** 以“第一次让 Codex 完成一件小事”为起点，用一个内容整理项目贯穿任务拆解、计划、执行、验证、规则、Skill 和自动化。正文负责学习路径，examples 负责过程样本，templates 负责可复用资产，docs 负责来源、版本和维护说明。

**Tech Stack:** GitHub Markdown、Codex App／CLI 当前公开能力、Git、GitHub Actions、Agent Skills 文件结构。

---

## 改版原则

- 经验手册的定位优先于产品百科，所有功能说明标注适用入口和校验日期。
- 每章必须给出前置条件、动作、可见结果、失败排查和验收标准。
- 用“资料整理与发布”作为贯穿案例，覆盖非程序员最容易复用的工作。
- 把 Codex Automations、GitHub Actions、Skills、Plugins、MCP 分开讲清楚。
- 中文正文和英文正文保持章节一一对应，英文文件放入独立目录。
- 所有模板都提供适用条件、风险边界和验证方式。

## 目标文件结构

- `README.zh-CN.md`
- `README.md`
- `playbook/zh/`
- `playbook/en/`
- `examples/`
- `templates/`
- `docs/`

## 教材主线

1. 认识 Codex 的工作方式与适用边界。
2. 在练习文件夹里完成第一次可验证任务。
3. 把模糊想法整理成任务说明。
4. 学会看计划、改动、测试和验收结果。
5. 用权限、Git 和目录边界控制风险。
6. 用 AGENTS.md 固化项目规则。
7. 用 Skill 固化重复工作。
8. 区分插件、MCP 和外部工具连接。
9. 设计可监控的自动化流程。
10. 完成三个真实工作流案例并建立自己的工作系统。

## 交付门槛

- 中文主教材章节齐全，所有章节具备实操、结果、排查和验收部分。
- 英文目录与中文目录一一对应，链接直接指向英文正文。
- 模板文件可以单独打开使用，且不包含私人路径、密钥或账号信息。
- README 中的产品能力说明带版本或校验日期。
- 所有内部链接存在，Markdown 表格结构有效，敏感表述完成检索。
- 最终本地改动通过 `git diff --check`、链接检查和目录清点。
