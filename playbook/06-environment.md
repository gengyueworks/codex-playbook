# Codex Playbook · Full Edition

> 一本面向非程序员的 Codex 实战手册。基于真实项目的使用经验，整理为系统化的方法论、可复用的工作流、以及可验证的案例。
> Suggested companion chapters: [Core Features](core-features.md), [Standard Workflow](workflow.md), [Case Studies](../../examples/)

---

## 目录

1. [手册定位](#1-手册定位)
2. [Codex 的执行模型](#2-codex-的执行模型)
3. [AI First 工作习惯](#3-ai-first-工作习惯)
4. [任务驱动：需求表述规范](#4-任务驱动需求表述规范)
5. [标准工作流：需求到交付的六步管控](#5-标准工作流需求到交付的六步管控)
6. [环境配置：Thread、Sandbox、AGENTS.md](#6-环境配置threadsandboxagentsmd)
7. [能力扩展：Skill、Plugin、MCP](#7-能力扩展skillpluginmcp)
8. [实战工作流](#8-实战工作流)
9. [故障排查与方案切换](#9-故障排查与方案切换)
10. [进阶用法：超越代码补全](#10-进阶用法超越代码补全)
11. [案例索引](#11-案例索引)

---

## 6. 环境配置：Thread、Sandbox、AGENTS.md

### Thread 管理

Thread 是 Codex 中的任务对话单元。设计原则：**一个 Thread 处理一个独立任务。**

| 实践 | 说明 |
|---|---|
| 任务隔离 | 不同任务（新功能/修 bug/优化样式/文档）使用独立 Thread |
| 完成任务归档 | 完成后使用 Archive 清理当前任务列表 |
| 失败任务重开 | 不要在失败的 Thread 上继续，新开 Thread 重新描述需求 |
| 避免上下文膨胀 | 单一 Thread 的对话轮次控制在 20 轮以内 |

**原因**：混合多种任务会导致上下文混乱，降低输出质量，增加审查成本。

### Sandbox 配置

Sandbox 是 Codex 的安全边界。选择原则：

| 配置 | 适用场景 | 风险等级 |
|---|---|---|
| 请求批准 | 日常开发、新手使用 | 低 |
| 自动审批 | 信任已验证的低风险操作 | 中 |
| 完全访问 | 需要系统级操作的自动化任务 | 高 |

**建议**：从"请求批准"开始使用。在确认 Codex 的行为模式可靠后，可根据任务类型调整。

### AGENTS.md

项目根目录下的 `AGENTS.md` 文件用于定义 Codex 的行为规则。Codex 在每次执行任务前自动读取。

**配置示例：**

```markdown
# Project Rules

## Language
- Copy: Chinese
- README: bilingual (zh/en)
- Commit messages: English

## Style
- No AI-generated filler language
- No corporate jargon (赋能, 抓手, 闭环)

## Code
- Never comment out errors to bypass checks
- Verify changes after implementation

## Boundaries
- Do not modify: auth logic, API endpoints, database schema
```

**价值**：消除每次任务中对相同规则的重复描述，降低上下文消耗，确保行为一致性。

---