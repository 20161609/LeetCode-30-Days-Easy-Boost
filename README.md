# LeetCode 30 Days — Easy Boost (with Backtracking)

A confidence-building 30-day plan focused on **easy wins** across multiple algorithms, with a dedicated **Backtracking** block. Designed to keep momentum high while rounding out fundamentals.

## 🏁 Progress Tracking
- Start Date: 2025-10-25
- End Date: -
- Current Progress: 11 / 30 problems solved ✅

## 🎯 Goals
- Finish **30 problems** in ~4–5 weeks (≈ 6–7 per week)
- Keep **~85% Easy**, **~15% Medium** (backtracking core)
- Write clean **English** notes (short + to the point)
- Commit daily for steady portfolio signals

## 🗂 Structure
```
leetcode-30days-easy-boost/
├── README.md
├── roadmap.md
└── weeks/
    ├── week01-arrays-two-pointers/
    ├── week02-linkedlist-prefix-hash/
    ├── week03-binarysearch-strings/
    ├── week04-backtracking-focus/
    ├── week05-trees-bits-dp-greedy/
    └── week06-graphs-wrapup/
```

## 📅 Weekly Track (lightweight)
- **Week 01:** Arrays & Two Pointers (Days 1–3), Linked List (4–6)
- **Week 02:** Prefix Sum / Hash / Kadane refresher (7–10), Strings (11–12)
- **Week 03:** Two Pointers polish (13–14), Binary Search (15), buffer day if needed
- **Week 04:** **Backtracking Week** (Days 16–20)
- **Week 05:** Trees (21–24), Bits/DP-lite/Greedy (25–28)
- **Week 06:** Graph basics (29–30), short review & mock

## ✅ Daily Routine (≤60–75 min)
1. 5–10m: Read problem + spot the **category**.
2. 30–45m: Implement, test small cases.
3. 10–15m: Write **notes.md** (idea + complexity + 1 gotcha).
4. Push with commit: `feat: dayNN - <slug> (topic)`.

## 📝 Notes Template (copy into `notes.md`)
```
# Notes
## Idea
- Key pattern(s): <Two Pointers / Backtracking / BFS ...>
- Core steps in 2–4 bullets.

## Complexity
- Time: O(...)
- Space: O(...)

## Gotcha
- 1~2 failure cases or pitfalls.
```

## 🧩 Backtracking Tips
- Use a shared `path` list; **append → recurse → pop**.
- Control branching with early exits (pruning) when possible.
- Prefer parameters `(idx, path)` or `(remain, start)` patterns.



├── README.md
├── .gitignore
├── 설명서
├── main.py

├── text/
    └── easy.txt
    └── medium.txt
    └── hard.txt
    └── .txt