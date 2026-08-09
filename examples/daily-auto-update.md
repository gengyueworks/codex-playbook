# 案例：每天自动更新内容站

> 场景：一个内容型项目，要求每天自动更新，不用人盯着。
> 我用 GitHub Action + Codex 实现。已稳定运行一个月。

---

## 要解决的问题

我有个"每天认识一位科学家"的项目，每天要更新一篇人物介绍。人工做太累，我想要：

1. 每天自动更新内容
2. 自动提交到 GitHub
3. 不用人管

## 怎么做的

### 1. 让 Codex 写 GitHub Action workflow

在 `.github/workflows/daily.yml` 里定义定时任务：

```yaml
name: Daily Update
on:
  schedule:
    - cron: "0 1 * * *"   # 每天早上 1 点（UTC）
  workflow_dispatch:

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run update script
        run: python scripts/daily_update.py
      - name: Commit and push
        run: |
          git config user.name "gengyueworks"
          git config user.email "gengyueworks@users.noreply.github.com"
          git add .
          git commit -m "daily update $(date +%F)"
          git push
```

### 2. 更新脚本

让 Codex 写 `scripts/daily_update.py`：从内容池里选今天的内容，生成页面，更新索引。

### 3. 验证

- 在 GitHub Actions 页面看每天是否触发成功
- 刚开始几天每天抽查一次
- 稳定后彻底放手

## 关键经验

- **定时用 cron**，注意时区（GitHub Action 用 UTC）
- **workflow_dispatch** 加上，方便手动触发测试
- **第一次一定要盯几天**，确认真的在跑
- 内容池要提前准备（我是把 365 篇都备好了）

## 你的项目能怎么用

- 每日一诗/一句话/一个知识卡片
- 每日数据汇总（股票、天气、新闻）
- 每日生成一个随机内容页面

**只要内容源有规律，就能自动化。**
