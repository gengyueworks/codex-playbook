# 案例：Obsidian 知识库免费同步

> 场景：知识库要跨设备同步，不想付费订阅 iCloud/坚果云。
> 方案：Git + Codex，免费、可控、还能版本管理。

---

## 背景

我的笔记在 Obsidian 里。多设备（Mac / 手机）要看，但同步工具要么贵要么慢。

## 方案

用 Git 做同步：

1. 把笔记库变成 Git 仓库
2. 推到 GitHub（私有仓库）
3. 每台设备 clone 或 pull
4. 改完 push

### 手机上怎么搞

- iOS：装 Working Copy（Git 客户端）
- 安卓：Termux + git

## Codex 在这里的作用

- 写同步脚本（一键 push/pull）
- 处理冲突
- 写 `.gitignore`（排除附件、缓存）

指令示例：

> 帮我在 Obsidian 笔记库里配好 git 同步：写一个 sync.sh，先 add 再 commit 再 push，忽略 .obsidian 缓存目录和附件文件夹。

## 好处

- **免费**（私有仓库不要钱）
- **版本历史**（改坏了能回滚）
- **不依赖某家公司**（GitHub 挂了还有本地）

## 注意

- 笔记含隐私的话用**私有仓库**
- 手机端编辑后记得 pull 再改，避免冲突
- 附件大的话用 Git LFS 或单独管理

---

*这就是"Git + Codex 打造 AI 知识库"的实践版。*
