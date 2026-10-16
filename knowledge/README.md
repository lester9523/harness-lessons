# 我们的 Agent 工作方法

这里是日常使用入口。内容经过重新组织，以“遇到什么问题、怎样处理、怎样确认有效”为主线，可以直接使用，不要求先读课程或重新打开原课。底部来源仅用于追溯和深入核实。

当前方法基于已整理至第 22 讲的课程知识与个人讨论，整理于 2026-10-16。它们是可用的方法说明，不表示我们已经逐项验证过效果。具体实验结果仍单独记录。

## 从一个实际问题开始

| 我现在遇到的问题 | 先用哪个方法 | 入口 |
| --- | --- | --- |
| 不知道该给多少要求，也不知道何时算完成 | 先写任务卡 | [任务与循环](01-task-and-loop.md#task-card) |
| 想知道要不要拆阶段、开多个 Agent | 按任务依赖与验收边界选择循环 | [选择工作规模](01-task-and-loop.md#choose-loop) |
| AI 理解了目标，却总不符合我的习惯 | 把冲突时的取舍写清楚 | [原则与规则](02-context-and-rules.md#principles) |
| 文档齐全，结果仍与现实不符 | 给知识加来源和更新条件 | [知识维护](02-context-and-rules.md#source-maintenance) |
| 规则越来越多，结果反而难以预测 | 合并、裁决和清理规则 | [规则治理](02-context-and-rules.md#rule-maintenance) |
| 资料越给越多，重点越来越模糊 | 先索引，再按需读取 | [上下文预算](02-context-and-rules.md#context-budget) |
| 不停强调要求，仍然要反复纠错 | 把要求转成检查 | [反馈优先](03-feedback-and-quality.md#feedback-first) |
| AI 说完成了，我却发现漏项 | 根据原始范围独立验收 | [完成证据](03-feedback-and-quality.md#completion-evidence) |
| 修了很多轮，始终收不了尾 | 给反馈分级，并定义停止条件 | [分级修正](03-feedback-and-quality.md#graded-feedback) |
| 该放手到什么程度 | 按动作影响选择人的介入点 | [人的介入](03-feedback-and-quality.md#human-judgment) |
| 长对话后期开始跳步骤 | 缩小子任务，建立恢复点 | [检查点](04-state-and-continuity.md#checkpoint) |
| 换会话又得重新解释 | 同步进度、证据和决策 | [交接记录](04-state-and-continuity.md#handoff) |
| 一次猜测被反复当成事实 | 分开临时数据和长期知识 | [状态分区](04-state-and-continuity.md#state-partition) |
| 有效提示词每次都得重写 | 先提炼稳定流程，再考虑 Skill | [知识固化](05-skills-and-examples.md#solidify) |
| Skill 触发不准或过程忽好忽坏 | 明确触发、自由度、检查与转向 | [技能设计](05-skills-and-examples.md#skill-design) |
| 输出不稳定，或总在沿用旧模式 | 给模板、示例和可检查的基线 | [示例与基线](05-skills-and-examples.md#anchors) |
| 昨天可用、换电脑后失败 | 对比运行条件，固定可控环境 | [环境复现](06-environment-and-improvement.md#environment) |

## 一次任务怎样用

1. 描述一个可以观察到的问题，选择上表的一项；不要一次套用所有方法。
2. 读对应文档，明确输入、操作和验收，再让 Agent 执行。
3. 检查结果。有效、无效和无法验证分别记录，不能仅凭感觉宣布改进成功。
4. 同一方法反复有效后，再决定是否写入稳定规则或 Skill。

完整路径见 [将方法用于当前任务](../prompts/apply.md)。想先理解整体，按下面顺序读。

## 六个主题

| 主题 | 能回答什么 | 最小产物 |
| --- | --- | --- |
| [任务与循环](01-task-and-loop.md) | 我到底要什么，任务该拆到什么程度 | 任务卡与阶段产物 |
| [上下文与规则](02-context-and-rules.md) | 给什么信息，按什么原则判断 | 资料入口与明确的取舍 |
| [反馈与验收](03-feedback-and-quality.md) | 怎么知道做对，做不对怎么办 | 验收证据与修正条件 |
| [状态与接续](04-state-and-continuity.md) | 怎样继续工作，哪些信息值得留下 | 可核实的交接记录 |
| [技能与范例](05-skills-and-examples.md) | 怎样复用方法、减少输出和过程歧义 | 一套可重复执行的方法 |
| [环境与持续改进](06-environment-and-improvement.md) | 怎样复现问题、验证改进并维护知识 | 环境记录与实践证据 |

## 从课程知识到自己的知识

- [KNOWLEDGE.md](../KNOWLEDGE.md) 保留按课程整理的概念、原始目录与出处。
- `knowledge/` 维护按问题组织、可以直接执行的方法。对具体主题，优先在对应方法文档维护，不再把操作步骤复制到多个地方。
- [个人用法](../practice/codex-playbook.md) 记录用户当前选择与讨论边界；实际结果进入实践记录。
- [来源清单](../sources/course-index.json) 继续记录读到什么以及核对日期。

新课带来方法变化时，既更新来源，也检查这里的操作方法是否需要修订。仅增加一条课程目录，不算完成知识消化。
