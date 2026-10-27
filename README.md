Software Engineering Repo

Shubham D Bhat

PES1UG24AM273

Section E

SE LAB 4 Vibe-coding session claude-ai chat -
https://claude.ai/share/0006f7e8-9882-4fd0-b856-671e384993b7

topic for lab 4 - https://github.com/SETAPESU26/34_pacman

SE LAB 5 Static Code Analysis - Pylint, Bandit, Flake8

topic for lab 5 - https://github.com/SETAPESU26/L5_34_online_exam

my fork (work + commits) - https://github.com/Shubhambhat06/L5_34_online_exam

---

# Lab 4 - VibeCoding: Pac-Man Repair Lab

Repo: `SETAPESU26/34_pacman` (forked/cloned; **no PR raised to the main repo**).
LLM used: Claude (Anthropic).

## Deliverables

| Required | File |
|---|---|
| a. Videos (before and after) | `videos/before.mp4`, `videos/after.mp4` (10 s each) |
| b. Updated code | `code/game.py` (identical to `game.py` at the repo root) |
| c. Chat history (doc/pdf) | `Chat_History_Lab4_Pacman.pdf` |

Extras: `tests/test_game.py` (24 regression tests), `tools/record.py` (headless video recorder).

## What was done (one commit per task)

| Task | Change |
|---|---|
| 1. Fix power-pellet bug | `eat()` compared against `"O"`; the maze uses `"o"`. One-character fix. Frightened mode now triggers and ghosts reverse. |
| 2. `ghost_color(name, mode)` | Distinct frightened tint per ghost (Blinky violet, Pinky periwinkle, Inky teal, Clyde lime). Returns `None` for normal/eaten. `draw()` keeps the white "ending" flash. |
| 3. `on_pellet_eaten(score, pellets_left)` | Bonus cherry (+100) spawns at 100 and 40 pellets left, blinks, vanishes after 9 s. Gold HUD flash on fruit pickup and on the final pellet. Uses an event queue because the function has no access to `Game`. |
| 4. `bonus_life_threshold()` | Returns `1000` - an extra life every 1000 points. (README's `10000` is unreachable: the maze holds only 1460 pellet points.) |

## Run

```bash
pip install pygame
python game.py            # arrow keys to move, R to reset
python Lab-4/tests/test_game.py   # 24 tests, all pass
```

## About the videos

The videos are **scripted autoplay captures of the real `game.py`** (rendered headlessly frame-by-frame by
`tools/record.py`), not a manual screen recording. The same autopilot and random seed are used for both clips, at
1.5x game speed so that every feature fits in 10 seconds. A caption strip under the game shows the live
`frightened` state, speed and game time. To record a hand-played clip instead, run `python game.py` and use any
screen recorder.

Regenerate:

```bash
python Lab-4/tools/record.py --game <original_game.py> --out before.mp4 --title "BEFORE" --speed 1.5 --seed 6
python Lab-4/tools/record.py --game game.py            --out after.mp4  --title "AFTER"  --speed 1.5 --seed 6
```

---

# Lab 5 - Static Code Analysis (Pylint, Bandit, Flake8)

Repo: `SETAPESU26/L5_34_online_exam` (forked to `Shubhambhat06/L5_34_online_exam`; work pushed to the fork, **no PR raised to the main repo**).
File analysed: `online_exam.py` (online exam marker). Tools: Pylint 4.1.3, Bandit 1.9.4, Flake8 7.4.1 (Python 3.12).

## Deliverables

| Required | File |
|---|---|
| 1. Three commits (one per tool) | `fix(bandit)`, `fix(pylint)`, `style(flake8)` in the fork's history |
| 2. Reports (before and after) | `Lab-5/reports/before/` and `Lab-5/reports/after/` (`pylint_report.txt`, `bandit_report.txt`, `flake8_report.txt`) |
| 3. Updated Python source | `Lab-5/online_exam.py` |
| 4. Report | `Lab-5/Lab5_Report.pdf` (issue table, results, verification, reflection) |

Extras: `Lab-5/issues.md` (issue table), `Lab-5/reflection.md` (reflection answers), plus a fourth `docs` commit adding them.

## Results

| Tool | Before | After |
|---|---|---|
| Pylint | 5.65/10 (20 messages) | **10.00/10** |
| Bandit | 4 issues (2 High, 2 Low) | **0 issues** |
| Flake8 | 4 issues | **0 issues** |

Program output is identical before and after (apart from the random bonus question). The `after/flake8_report.txt` file is empty on purpose: Flake8 prints nothing when there are no issues.

## What was done (one commit per tool)

| Commit | Change |
|---|---|
| 1. Bandit | `os.system("ssh " + host)` (command injection, High) replaced by `subprocess.run` with an argument list, no shell and a validated host name. MD5 (High) replaced by SHA-256. Hard-coded password moved to an environment variable. `random.choice` replaced by `secrets.choice`. Two informational subprocess notes (B404, B603) suppressed with justified `# nosec`. |
| 2. Pylint | snake_case names, docstrings, `enumerate`, removed `elif` after `return`, fixed the mutable default argument `penalties={}`. Also fixed two bugs no tool reports: `topper()` crashed on empty results, and `main()` ran on import. |
| 3. Flake8 | Blank lines (E302), operator and comment spacing (E225, E261), long lines (E501), continuation indent (E128). |

## Run

```bash
pip install pylint bandit flake8
python Lab-5/online_exam.py
python -m pylint Lab-5/online_exam.py          # 10.00/10
python -m bandit -r Lab-5/online_exam.py       # No issues identified
python -m flake8 Lab-5/online_exam.py          # no output
```
