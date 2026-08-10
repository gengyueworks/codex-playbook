# 环境配置：基础设置、Thread、Sandbox、AGENTS.md

> 消化自雨哥 Codex 实战课第 6 节（四个基础设置）与第 31 节（保姆级教程），叠加橙皮书环境配置内容。

---

## 首次上手需要关注的三个配置

打开 Codex 后，新手最先看到也最容易困惑的几个地方：

### 1. 权限控制（Sandbox）

| 配置 | 行为 | 适用场景 |
|---|---|---|
| 请求批准 | 任何越界操作都先问你再执行 | 新手默认 |
| 自动审批 | AI 自行判断哪些操作放行、哪些询问 | 已验证的低风险任务 |
| 完全访问 | 所有权限交给 AI，不再询问 | 高风险，仅限完全信任的系统级自动化 |

**建议**：从"请求批准"开始。等确认 AI 的行为模式可靠后，再根据任务类型调整。不要一上来开完全访问。

### 2. 模型选择

把模型理解成你请来干活的工人。日常任务用当前主力模型即可，遇到特别复杂的问题再切换到更强版本。模型越强，推理越深，消耗也越大——不是越强越好，是按需选择。

### 3. 推理深度

低、中、高、超高四档。深度越高，解决问题的能力和输出质量越好，但耗时和 Token 消耗也越大。日常任务用中等即可，复杂分析类任务上高或超高。

### 4. 额度管理

留意剩余额度。不要让一个长任务烧光当天的配额。

---

## Thread 管理

Thread 是 Codex 中的任务对话单元。设计原则：**一个 Thread 处理一个独立任务。**

| 实践 | 说明 |
|---|---|
| 任务隔离 | 不同任务（新功能 / 修 bug / 优化样式 / 文档）使用独立 Thread |
| 完成任务归档 | 完成后使用 Archive 清理当前任务列表 |
| 失败任务重开 | 不要在失败的 Thread 上继续，新开 Thread 重新描述需求 |
| 避免上下文膨胀 | 单一 Thread 的对话轮次控制在 20 轮以内 |

**原因**：混合多种任务会导致上下文混乱，降低输出质量，增加审查成本。

---

## 项目与对话的区别

Codex 里的"项目"可以理解为：把你的项目文件 + 聊天记录 + 上下文放在一起。下次使用时能关联上之前的聊天内容和项目内容。

普通对话模式则跟网页聊天一样——每次都是新的，不关联项目文件。

---

## AGENTS.md

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

**价值**：消除每次任务中对相同规则的重复描述，降低上下文消耗，确保行为一致性。相当于每次开工前给 AI 读一遍公司手册。
