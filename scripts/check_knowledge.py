#!/usr/bin/env python3
"""检查知识库的课程记录、笔记入口和本地链接；仅使用 Python 标准库。"""

import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
ERRORS = []


def require(condition, message):
    if not condition:
        ERRORS.append(message)


def read(path):
    return path.read_text(encoding="utf-8")


def anchors(path):
    return set(re.findall(r'<a\s+id="([^"]+)"\s*>', read(path)))


def main():
    required = [
        "README.md", "AGENTS.md", "KNOWLEDGE.md", "UPDATING.md",
        "CHANGELOG.md", "sources/course-index.json", "sources/README.md",
        "state/learning-state.md", "practice/codex-playbook.md",
        "prompts/resume.md", "prompts/update.md", "prompts/apply.md",
        "templates/lesson.md", "templates/experiment.md", "sharing/README.md",
    ]
    for name in required:
        path = ROOT / name
        require(path.is_file(), f"缺少必要文件：{name}")
        if path.is_file():
            require(bool(read(path).strip()), f"文件为空：{name}")

    try:
        index = json.loads(read(ROOT / "sources/course-index.json"))
    except (OSError, ValueError) as exc:
        ERRORS.append(f"来源清单无法读取：{exc}")
        return finish()

    entries = index.get("entries", [])
    require(bool(entries), "来源清单没有课程记录")
    require(index.get("lesson_count") == len(entries), "lesson_count 与课程记录数不一致")
    for field in ["snapshot_checked_at", "updated_at"]:
        try:
            date.fromisoformat(index[field])
        except (KeyError, ValueError, TypeError):
            ERRORS.append(f"无效日期字段：{field}")

    for field in ["key", "url"]:
        duplicates = [key for key, count in Counter(e.get(field) for e in entries).items() if count > 1]
        require(not duplicates, f"重复课程 {field}：{duplicates}")

    numbers = sorted(e["number"] for e in entries if isinstance(e.get("number"), int))
    require(numbers == list(range(1, index.get("last_numbered_lesson", 0) + 1)),
            "编号课程缺失、重复，或 last_numbered_lesson 不一致")

    for entry in entries:
        key = entry.get("key", "未知记录")
        for field in ["key", "title", "url", "source_checked_at", "access", "status",
                      "note_file", "note_anchor", "method", "summary"]:
            require(bool(entry.get(field)), f"{key} 缺少 {field}")
        try:
            date.fromisoformat(entry["source_checked_at"])
        except (KeyError, ValueError, TypeError):
            ERRORS.append(f"{key} 来源日期无效")
        url = urlsplit(entry.get("url", ""))
        require(url.scheme == "https" and url.netloc == "time.geekbang.org"
                and re.fullmatch(r"/column/article/\d+", url.path) is not None,
                f"{key} 原课链接格式异常")
        require(entry.get("access") in {"full_text", "excerpt", "summary", "catalog", "user_notes"},
                f"{key} 可读范围取值不明确")
        require(entry.get("status") in {"summarized", "partial", "pending"},
                f"{key} 整理状态取值不明确")
        path = (ROOT / entry.get("note_file", "")).resolve()
        if not path.is_relative_to(ROOT) or not path.is_file():
            ERRORS.append(f"{key} 笔记文件缺失或不在仓库内")
            continue
        content = read(path)
        require(entry.get("note_anchor") in anchors(path), f"{key} 缺少笔记锚点")
        require(entry.get("title", "") in content, f"{key} 笔记未包含原课标题")
        require(entry.get("url", "") in content, f"{key} 笔记未包含来源链接")

    md_files = sorted(ROOT.rglob("*.md"))
    links_checked = 0
    for path in md_files:
        if ".git" in path.parts:
            continue
        raw = read(path)
        without_code = re.sub(r"```[\s\S]*?```", "", raw)
        require(not re.search(r"^<{7} |^={7}$|^>{7} ", raw, flags=re.M),
                f"{path.relative_to(ROOT)} 留有冲突标记")
        require(not any(prefix in raw for prefix in ["/Users/", "/private/tmp/", "C:\\Users\\"]),
                f"{path.relative_to(ROOT)} 包含机器绝对路径，不便跨电脑接续")
        for target in re.findall(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)", without_code):
            target = target.strip().strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            destination = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            require(destination.is_relative_to(ROOT), f"链接越出仓库：{path.name} → {target}")
            require(destination.is_file(), f"本地链接不存在：{path.relative_to(ROOT)} → {target}")
            if parsed.fragment and destination.is_file():
                require(unquote(parsed.fragment) in anchors(destination),
                        f"本地锚点不存在：{path.relative_to(ROOT)} → {target}")
            links_checked += 1

    if not ERRORS:
        print(f"通过：{len(entries)} 条课程记录，{len(md_files)} 个 Markdown 文件，{links_checked} 个本地链接。")
        print("本检查仅验证结构与入口；内容准确性、来源更新及实践有效性需要另行核实。")
    return finish()


def finish():
    for message in ERRORS:
        print(f"错误：{message}", file=sys.stderr)
    return 1 if ERRORS else 0


if __name__ == "__main__":
    raise SystemExit(main())
