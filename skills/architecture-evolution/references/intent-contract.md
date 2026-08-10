# Architecture Intent Contract

只在 `Status: Architecture intent ready` 时读取。本文件只定义最终输出形状。

标题、字段和正文跟随用户主要语言；`Status` token、代码符号、文件名和稳定协议名称可保留原文。

```markdown
# Architecture Intent

Status: Architecture intent ready

## Problem
- Problem:
- Why architectural:

## Background
- Why now:
- Decisive evidence:

## Direction
- Intent: <优先表达为完成后必须长期成立的 architecture boundary / invariant，而不是具体实现>
- Desired end state: <说明哪些边界、ownership、dependency 或 semantics 应稳定，以及边界内哪些实现仍可自主变化>
- Stable acceptance rule: <直接说明 Direction + Boundary + Replacement / exit 何时成立；不指定 test/lint/evidence provider>
- Possible shapes: <可选；只在确有少量基本形态值得后续设计比较时简要列出>

## Boundary
- In scope:
- Out of scope:
- Must preserve:
- Replacement / exit:
```

只保留足以支撑 intent 的 evidence；不输出 taxonomy、Brooks、Challenge 或 reasoning trace。

到 architecture direction / basic shape 为止；具体 module/class/API、responsibility placement、调用流、迁移、任务拆分、lint/test 或 verification 属于后续设计或实现。
