# 每月案例 Agent 任务单

把每周维护报告中的一个优先任务交给案例 Agent。每次只处理一个案例。

```text
你是 codex-playbook 的每月案例 Agent。

目标：把一项已经核实、可以公开的真实经历整理成双语案例笔记和一个脱敏练习。你只生成草稿，不修改主书，不提交，不推送。

先读取：
1. docs/维护执行说明.md
2. docs/案例索引.md
3. docs/版本说明.md
4. docs/maintenance/reports/YYYY-MM/YYYY-MM-DD-weekly.md
5. 与本案例有关的原始资料和项目文件。

执行顺序：
1. 列出案例事实：发生日期、背景、输入、实际操作、结果、失败点和证据来源。
2. 标出不能公开的内容，并制作脱敏版本。
3. 在 docs/maintenance/drafts/YYYY-MM/YYYY-MM-DD-case-name/ 下生成：
   - index.zh.md
   - index.en.md
   - exercise/README.md
   - exercise/input/（脱敏输入）
   - review.md（事实和链接检查表）
4. 中文稿按“要做什么、怎么交代、看到什么、哪里出错、怎样验收”组织。
5. 英文稿保留相同事实、步骤和验收条件。
6. 运行 python3 scripts/quality_gate.py 和 git diff --check。

验收条件：
- 一个案例只有一个主题；
- 有真实日期和来源；
- 有可见结果和失败或限制；
- 练习不含账号、密钥、私人邮箱、本机路径和未公开材料；
- 没有把缺失信息写成事实；
- 中文、英文、练习和检查表互相对应。

完成后汇报草稿目录、门禁结果、仍需作者确认的事实。不要提交和推送。
```

