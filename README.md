# Software Engineering Lab Portfolio

**Name:** Shubham D Bhat  
**SRN:** PES1UG24AM273  
**Section:** E  
**Campus:** PES University, Ring Road Campus, Bengaluru

---

## Lab 2–3 — PDF Submissions

The deliverables and documentation for **Labs 1, 2, and 3** have been uploaded as PDF files.

- **Lab 2:** PDF submission uploaded.
- **Lab 3:** PDF submission uploaded.

The following sections document Labs 4, 5, 6, and 7, including their source repositories, implementations, deliverables, and testing results.

---

## Lab 4 — Vibe Coding: Pac-Man Repair Lab

**Original Repository:** https://github.com/SETAPESU26/34_pacman  
**LLM Used:** Claude (Anthropic)  
**Claude Chat History:** https://claude.ai/share/0006f7e8-9882-4fd0-b856-671e384993b7

The objective of this lab was to use AI-assisted coding to identify and repair issues in a Pac-Man game while validating the changes through regression testing.

**Note:** The work was maintained in a forked/cloned copy. No pull request was raised to the original repository.

### Deliverables

| Requirement | File |
|---|---|
| Before and after videos | `videos/before.mp4`, `videos/after.mp4` |
| Updated game code | `code/game.py` |
| Chat history | `Chat_History_Lab4_Pacman.pdf` |
| Regression tests | `tests/test_game.py` |
| Video recording utility | `tools/record.py` |

### Changes Implemented

| Task | Description |
|---|---|
| Power-pellet bug | Corrected the pellet character comparison from `"O"` to `"o"`, enabling frightened mode and ghost reversal. |
| Ghost colours | Implemented `ghost_color(name, mode)` to provide distinct frightened-mode colours for each ghost while preserving normal and ending behaviour. |
| Bonus fruit | Implemented `on_pellet_eaten(score, pellets_left)` to trigger bonus cherries at 100 and 40 pellets remaining, with blinking, timed disappearance, and HUD effects. |
| Bonus life | Implemented `bonus_life_threshold()` to return `1000`, awarding an extra life for every 1,000 points. |

### Testing and Execution

Install Pygame and run the game:

```bash
pip install pygame
python game.py
```

Run the regression tests:

```bash
python Lab-4/tests/test_game.py
```

The test suite contains 24 regression tests.

### Video Demonstration

The before-and-after videos are scripted, headless captures of the game rendered frame by frame. Both clips use the same autopilot and random seed to make the comparison consistent.

To regenerate the videos:

```bash
python Lab-4/tools/record.py --game <original_game.py> --out before.mp4 --title "BEFORE" --speed 1.5 --seed 6
python Lab-4/tools/record.py --game game.py --out after.mp4 --title "AFTER" --speed 1.5 --seed 6
```

---

## Lab 5 — Static Code Analysis

**Original Repository:** https://github.com/SETAPESU26/L5_34_online_exam  
**My Fork:** https://github.com/Shubhambhat06/L5_34_online_exam

This lab focused on identifying and fixing security vulnerabilities, code-quality problems, and style violations using Pylint, Bandit, and Flake8.

**File analysed:** `online_exam.py`  
**Tools used:** Pylint 4.1.3, Bandit 1.9.4, and Flake8 7.4.1.

**Note:** The work and commits are available in my fork. No pull request was raised to the original repository.

### Deliverables

| Requirement | File or Location |
|---|---|
| Three tool-specific commits | Fork's Git history |
| Before-analysis reports | `Lab-5/reports/before/` |
| After-analysis reports | `Lab-5/reports/after/` |
| Updated Python source | `Lab-5/online_exam.py` |
| Lab report | `Lab-5/Lab5_Report.pdf` |
| Issue documentation | `Lab-5/issues.md` |
| Reflection | `Lab-5/reflection.md` |

The reports directory contains the Pylint, Bandit, and Flake8 reports before and after the fixes.

### Results

| Tool | Before | After |
|---|---|---|
| Pylint | 5.65/10; 20 messages | **10.00/10** |
| Bandit | 4 issues: 2 High, 2 Low | **0 issues** |
| Flake8 | 4 issues | **0 issues** |

### Changes Implemented

**1. Bandit — Security fixes**

- Replaced shell-based SSH command construction with `subprocess.run` using an argument list and host validation.
- Replaced MD5 with SHA-256.
- Moved the hard-coded password to an environment variable.
- Replaced `random.choice` with `secrets.choice`.
- Documented justified suppressions for informational subprocess findings.

**2. Pylint — Code quality and correctness**

- Improved naming conventions and added docstrings.
- Used `enumerate` where appropriate.
- Fixed control-flow and mutable-default-argument issues.
- Fixed `topper()` crashing on empty results.
- Prevented `main()` from running automatically when the module is imported.

**3. Flake8 — Style corrections**

- Fixed blank-line and spacing violations.
- Corrected comment formatting and continuation indentation.
- Resolved line-length violations.

The program's output was kept consistent before and after the changes, apart from the randomly selected bonus question.

### Verification

Install the tools:

```bash
pip install pylint bandit flake8
```

Run the program and analysis tools:

```bash
python Lab-5/online_exam.py
python -m pylint Lab-5/online_exam.py
python -m bandit -r Lab-5/online_exam.py
python -m flake8 Lab-5/online_exam.py
```

---

## Lab 6 — Tennis Scoring: Code Coverage

**Original Repository:** https://github.com/SETAPESU26/L6_L7_34_tennis_scoring  
**My Fork:** https://github.com/Shubhambhat06/L6_L7_34_tennis_scoring

This lab focused on measuring test coverage for the tennis-scoring module using line coverage and branch coverage techniques.

### Deliverables

| Requirement | File |
|---|---|
| Line coverage tests | `lab6/LAB_6_CodeCoverageTest_tennis_scoring.py` |
| Branch coverage tests | `lab6/LAB6_BranchCoverageTest_tennis_scoring.py` |
| Line coverage screenshot | `lab6/LAB_6code_coverage_screenshot.png` |
| Branch coverage screenshot | `lab6/LAB_6branch_coverage_screenshot.png` |
| Source module | `lab6/tennis_scoring.py` |

### Test Coverage Results

| Coverage Type | Result |
|---|---:|
| Line (Code) Coverage | **97%** |
| Branch Coverage | **100%** |

### Test Cases Covered

- Normal tennis scoring and game-winning conditions.
- Deuce and advantage scenarios.
- Invalid negative-point inputs.
- Set-winning conditions, including two-game leads and tiebreak scores.
- Match status, including wins, deciding stages, and matches in progress.
- Boundary conditions and both outcomes of decision branches.

### How to Run

Run the commands from the `lab6` directory.

**Line coverage:**

```bash
coverage run --source=. -m pytest LAB_6_CodeCoverageTest_tennis_scoring.py
coverage report -m
```

**Branch coverage:**

```bash
coverage run --branch --source=. -m pytest LAB6_BranchCoverageTest_tennis_scoring.py
coverage report -m
```

### Screenshots

**Line Coverage Results**

![Line Coverage Results](lab6/LAB_6code_coverage_screenshot.png)

**Branch Coverage Results**

![Branch Coverage Results](lab6/LAB_6branch_coverage_screenshot.png)

### Conclusion

The tests exercise the main tennis-scoring logic, including boundary conditions and decision branches. The reported results are **97% line coverage** and **100% branch coverage**.

---

## Lab 7 — Tennis Scoring: Fuzz Testing

**Original Repository:** https://github.com/SETAPESU26/L6_L7_34_tennis_scoring  
**My Fork:** https://github.com/Shubhambhat06/L6_L7_34_tennis_scoring  
**Tools used:** Python, Hypothesis, pytest

This lab focused on fuzz testing (property-based testing) the tennis-scoring module with Hypothesis to find input-validation bugs, then hardening the code so that no input can make a function crash.

**Files under test:** `parse_score`, `game_lead` and `set_spread` in `tennis_scoring.py`.

**Note:** The handout refers to `processor.py` / `test_processor.py`; in this repository the equivalent files are `tennis_scoring.py` / `test_tennis_scoring.py`. The work is in my fork. No pull request was raised to the original repository.

### Deliverables

| Requirement | File |
|---|---|
| PDF with screenshots of every step | `lab7/Lab7_Fuzzing_Report.pdf` |
| Fixed application script | `lab7/tennis_scoring.py` |
| Updated Hypothesis tests | `lab7/test_tennis_scoring.py` |
| Lab README | `lab7/README.md` |

### Results

| Code Version | Test Result |
|---|---|
| Original (buggy) code | **10 failed, 4 passed** |
| Fixed code | **14 passed** (also passes with 5,000 generated examples per test) |

### Bugs Found by Fuzzing

| Function | Minimal failing input | Exception |
|---|---|---|
| `parse_score` | `None`, `''`, `'-'` | `AttributeError`, `ValueError` |
| `game_lead` | `None`, `''`, `'-'`, `'50-30'` | `AttributeError`, `ValueError`, `KeyError` |
| `set_spread` | `None`, `''` (also `'1,,3'`, `'6,4,'`) | `AttributeError`, `ValueError` |
| All three | `0`, `b''` (non-string types) | `AttributeError`, `TypeError` |

The original `int()` conversion also silently accepted invalid scores such as `'1_0'` (read as 10), `'+3'` and non-ASCII digits.

### Changes Implemented

- **Type check:** non-string input returns `None` instead of raising.
- **Separator check:** `parse_score` and `game_lead` require exactly one `-`.
- **Strict number parsing:** only ASCII digits are accepted before calling `int()`.
- **Tennis-point whitelist:** `game_lead` accepts only `0`, `15`, `30` and `40`.
- **Whole-CSV validation:** `set_spread` validates every element before using `max()` and `min()`.
- **Input length cap:** inputs over 1,000 characters are rejected.
- **Friendlier `main()`:** prints a clear message for invalid input and handles `EOFError` / `KeyboardInterrupt`.

### Test Suite

The suite contains 14 tests: the 3 required no-crash tests, plus correctness, output-shape, malformed-type and regression tests.

### How to Run

Run the commands from the `lab7` directory.

```bash
pip install hypothesis pytest
python tennis_scoring.py
pytest test_tennis_scoring.py
```

### Conclusion

Fuzzing exposed crashes in all three functions that ordinary inputs never trigger. After adding validation, every generated input is either processed correctly or rejected with `None`, and all 14 tests pass.

---

## Overall Summary

| Lab | Topic | Main Tools / Technologies |
|---|---|---|
| Labs 1–3 | PDF submissions | PDF documentation |
| Lab 4 | Vibe Coding and Pac-Man Repair | Claude, Python, Pygame, regression testing |
| Lab 5 | Static Code Analysis | Pylint, Bandit, Flake8 |
| Lab 6 | Code Coverage | Python, pytest, Coverage.py |
| Lab 7 | Fuzz Testing | Python, pytest, Hypothesis |

This portfolio documents the progression from the initial PDF-based lab submissions to practical software engineering work involving AI-assisted development, security and code-quality analysis, systematic testing, and fuzz testing.
