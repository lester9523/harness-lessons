# Harness 课程个人知识库

用于持续整理《Agent 驾驭工程之美》的课程知识，把理解转化为日常工作方法，并在实践成熟后用于 AI 使用分享。

**完整课程知识从 [KNOWLEDGE.md](KNOWLEDGE.md) 进入。** 本仓库独立于任何聊天历史：换电脑、换会话后，读取仓库即可接续。

## 当前内容

- 课程：极客时间《Agent 驾驭工程之美》，徐昊。
- 来源快照核对时间：**2026-10-15**；知识库初始化时间：2026-10-16。
- 已整理：24 条课程内容，包括开篇词、直播文字整理及第 01—22 讲；快照中课程计划共 35 讲。
- 这代表已整理范围，不代表课程今天仍只更新到这里，也不代表个人已熟练掌握全部内容。
- 内容包括课程方法的重新表述、个人讨论结论和待验证实践。未收录课程全文、音视频或公司内部材料。

## 按目的阅读

| 现在要做什么 | 从这里开始 |
| --- | --- |
| 换电脑后恢复上下文 | [接续提示词](prompts/resume.md) → [当前学习状态](state/learning-state.md) |
| 查看全部课程与关键知识 | [完整知识文件](KNOWLEDGE.md) |
| 分清内外部 Harness 与内外层循环 | [个人理解与 Codex 用法](practice/codex-playbook.md) |
| 根据实际问题改进工作方式 | [坏味道排查入口](KNOWLEDGE.md#diagnostics) → [实践记录](practice/README.md) |
| 补充新课程或纠正旧认识 | [更新方法](UPDATING.md) → [更新提示词](prompts/update.md) |
| 将知识用于开发工作 | [应用提示词](prompts/apply.md) |
| 将已理解内容准备成分享 | [分享素材入口](sharing/README.md) |
| 查看知识来源和核实范围 | [来源说明](sources/README.md) · [课程清单](sources/course-index.json) |

## 在公司电脑接续

第一次拉取：

```zsh
git clone https://github.com/lester9523/harness-lessons.git
cd harness-lessons
```

已有本地仓库：先用 `git status` 检查未提交改动；工作区干净后运行 `git pull --ff-only`。

用 Codex 打开这个目录，粘贴：

```text
请按本仓库 AGENTS.md 工作。先读 README.md、state/learning-state.md 和 practice/codex-playbook.md，再按需读 KNOWLEDGE.md。告诉我知识覆盖范围、当前关注点、关键概念和未验证事项，引用仓库文件位置。今天先从我个人使用 Codex 出发继续探索，分清内外部 Harness 与内外层循环，用一个坏味道给出小规模可验证的改进。不要假设我已经掌握全部课程，也不要自动改我的其他项目或全局配置。
```

更完整的接续方式见 [prompts/resume.md](prompts/resume.md)。不要求安装专用插件或特定 Skill；普通文件即可承载知识。

## 如何持续积累

1. 新课先登记来源、标题、核实日期和实际可读范围。
2. 提炼关键方法，并与已有概念比较；按需要更新 `KNOWLEDGE.md`。
3. 个人推论与实际验证分别记录；实践只在有结果后标记“已验证”。
4. 更新学习状态和变更记录，检查链接后提交。

本仓库只提供知识与方法。将方法用于其他项目时，应明确目标项目和改动范围，再遵循那个项目的规则。

## 检查知识库

本地安装 Python 3 后运行：

```zsh
python3 scripts/check_knowledge.py
```

检查会核对课程记录、原文入口、笔记锚点和本地链接。它不能代替对知识准确性的人工核实。

## 来源与使用边界

课程版权属于原作者及平台。仓库保存自主整理的学习笔记和应用方法，重要概念附原课入口；它不替代原课程。工具操作存在版本差异，使用前根据官方文档核对。
