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

## 7. 能力扩展：Skill、Plugin、MCP

### 三者关系

| 概念 | 职责 | 类比 | 使用门槛 |
|---|---|---|---|
| Plugin | 打包 Skill 和 MCP 为可安装单元 | 工具箱 | 普通用户可安装 |
| Skill | 定义同类任务的标准执行流程 | 说明书 | 普通用户可编写 |
| MCP | 连接外部工具或数据源 | 插座 | 偏开发者配置 |

### Skill 的构成

| 组件 | 说明 |
|---|---|
| Prompt | 该任务的触发提示词 |
| Workflow | 执行步骤 |
| Template | 输出格式模板 |
| Instructions | 持久化行为规则 |
| Resources | 参考资料 |
| Scripts | 自动化脚本 |

### 插件方向

| 类型 | 能力 |
|---|---|
| 浏览器操作 | Chrome, Computer Use |
| 代码协作 | GitHub |
| 前端设计 | Build Web Apps, Figma |
| 文档交付 | Documents, Presentations, Spreadsheets |
| 视频生成 | HyperFrames, Remotion |

详细说明见 [core-features.md](core-features.md)。

---