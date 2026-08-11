# 非程序员使用 Codex 的经验手册

English · [A Practical Field Guide to Using Codex Without Writing Code](README.md)

> Codex 被严重低估了。它可以陪着一个项目从最初的想法，一直走到真正公开、持续生长的作品。

这是一本写给写作者、研究者、内容创作者和其他不会写代码的人的 Codex 实战手册。

作者是中文内容创作者，注册 GitHub 多年，却一直觉得“我不会代码，所以做不出来”。开始使用 Codex 之后，文章、人物故事、音乐、科学内容、自动更新、资料整理和项目规则，逐步从脑子里的想法变成了公开仓库。

作者把自己称作 coder 世界里的吟游诗人：别人交付功能，我把故事、知识和想法做成开源作品。这本手册记录的，正是一个非程序员怎样把这种工作做起来。

## 这本手册教什么

Codex 真正好用，依赖五个习惯：

1. 说清楚你想留下什么结果。
2. 把需要的材料放到它能读取的地方。
3. 说清楚哪些能改，哪些必须保持原样。
4. 看证据，不只听“已经完成”。
5. 把好用的方法留下来，下一次继续用。

全书使用作者的真实案例：Codex for OSS 申请、GitHub 主页数据从 84 更新到 102、681 条收藏筛出 22 条、每天认识一位科学家项目、35 个视频转录、AGENTS.md 项目规则，以及 100 多个仓库的维护经验。

## 从这里开始

先读[第一章：为什么写这本手册](playbook/zh/01-%E4%B8%BA%E4%BB%80%E4%B9%88%E5%86%99%E8%BF%99%E6%9C%AC%E6%89%8B%E5%86%8C.md)，然后完成[第一个完整任务练习](examples/01-first-task/)。

## 内容目录

| # | 章节 | 你会完成什么 |
|---|---|---|
| 01 | [为什么写这本手册](playbook/zh/01-%E4%B8%BA%E4%BB%80%E4%B9%88%E5%86%99%E8%BF%99%E6%9C%AC%E6%89%8B%E5%86%8C.md) | 从一个真实创作者的故事进入 Codex |
| 02 | [第一次让 Codex 把一件事做完](playbook/zh/02-%E7%AC%AC%E4%B8%80%E6%AC%A1%E8%AE%A9-Codex-%E6%8A%8A%E4%B8%80%E4%BB%B6%E4%BA%8B%E5%81%9A%E5%AE%8C.md) | 读文件夹、生成结果、检查原始材料 |
| 03 | [怎么把话说清楚](playbook/zh/03-%E6%80%8E%E4%B9%88%E6%8A%8A%E8%AF%9D%E8%AF%B4%E6%B8%85%E6%A5%9A.md) | 把模糊草稿推进成可核对的申请文案 |
| 04 | [先开对的文件夹，再动手](playbook/zh/04-%E5%85%88%E5%BC%80%E5%AF%B9%E7%9A%84%E6%96%87%E4%BB%B6%E5%A4%B9%E5%86%8D%E5%8A%A8%E6%89%8B.md) | 限定改动并检查 diff |
| 05 | [让它记住你的规矩](playbook/zh/05-%E8%AE%A9%E5%AE%83%E8%AE%B0%E4%BD%8F%E4%BD%A0%E7%9A%84%E8%A7%84%E7%9F%A9.md) | 把项目习惯写进 AGENTS.md |
| 06 | [把常用操作变成 Skill](playbook/zh/06-%E6%8A%8A%E5%B8%B8%E7%94%A8%E6%93%8D%E4%BD%9C%E5%8F%98%E6%88%90-Skill.md) | 把重复流程保存成 Skill |
| 07 | [让项目自己跑起来](playbook/zh/07-%E8%AE%A9%E9%A1%B9%E7%9B%AE%E8%87%AA%E5%B7%B1%E8%B7%91%E8%B5%B7%E6%9D%A5.md) | 建立可观察的 GitHub Actions 工作流 |
| 08 | [抓资料，整理资料](playbook/zh/08-%E6%8A%93%E8%B5%84%E6%96%99%E6%95%B4%E7%90%86%E8%B5%84%E6%96%99.md) | 保存、筛选并核验一大批资料 |
| 09 | [遇到问题，先这样查](playbook/zh/09-%E9%81%87%E5%88%B0%E9%97%AE%E9%A2%98%E5%85%88%E8%BF%99%E6%A0%B7%E6%9F%A5.md) | 找到出错的步骤，再决定怎么修 |
| 10 | [我的工具箱](playbook/zh/10-%E6%88%91%E7%9A%84%E5%B7%A5%E5%85%B7%E7%AE%B1.md) | 保存以后会反复使用的交代和检查 |

## 模板和练习

- [任务交代模板](templates/zh/01-%E4%BB%BB%E5%8A%A1%E4%BA%A4%E4%BB%A3%E6%A8%A1%E6%9D%BF.md)
- [项目规则模板](templates/zh/02-AGENTS.md-%E9%A1%B9%E7%9B%AE%E8%A7%84%E5%88%99%E6%A8%A1%E6%9D%BF.md)
- [Skill 模板](templates/zh/03-SKILL%E6%A8%A1%E6%9D%BF.md)
- [自动化检查清单](templates/zh/04-%E8%87%AA%E5%8A%A8%E5%8C%96%E6%A3%80%E6%9F%A5%E6%B8%85%E5%8D%95.md)
- [README 模板](templates/zh/05-README%E6%A8%A1%E6%9D%BF.md)
- [申请文案练习](examples/02-application-copy/)
- [资料筛选练习](examples/03-source-collection/)
- [日更自动化练习](examples/04-daily-workflow/)
- [教材质量门禁](docs/%E8%B4%A8%E9%87%8F%E9%97%A8%E7%A6%81.md)

## 来源与版本

中文章节是本手册的主要经验叙事，英文章节与中文一一对应，方便公开仓库读者阅读。详见[来源与写作说明](docs/%E6%9D%A5%E6%BA%90%E4%B8%8E%E5%86%99%E4%BD%9C%E8%AF%B4%E6%98%8E.md)、[案例索引](docs/%E6%A1%88%E4%BE%8B%E7%B4%A2%E5%BC%95.md)和[版本说明](docs/%E7%89%88%E6%9C%AC%E8%AF%B4%E6%98%8E.md)。

Codex、桌面应用、自动化和 GitHub 的界面会持续变化。涉及当前产品细节时，请同时查看[Codex 官方文档](https://developers.openai.com/codex/)和[OpenAI 帮助中心](https://help.openai.com/)。

## 长期维护

查看[教程路线图](docs/%E8%B7%AF%E7%BA%BF%E5%9B%BE.md)、[维护执行说明](docs/%E7%BB%B4%E6%8A%A4%E6%89%A7%E8%A1%8C%E8%AF%B4%E6%98%8E.md)和[每周维护 Agent 任务单](docs/maintenance/weekly-agent-prompt.zh-CN.md)。想报告问题或贡献内容，请看[贡献指南](CONTRIBUTING.zh-CN.md)。

## 许可证

MIT，见[LICENSE](LICENSE)。
