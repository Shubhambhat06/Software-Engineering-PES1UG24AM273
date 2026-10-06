Software Engineering Repo 

Shubham D Bhat 

PES1UG24AM273 

Section E

SE LAB 4 Vibe-coding session claude-ai chat - 
https://claude.ai/share/0006f7e8-9882-4fd0-b856-671e384993b7

topic for lab 4 - https://github.com/SETAPESU26/34_pacman
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
