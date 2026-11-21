# Study Modules

Interactive, self-contained study modules. Each runs in the browser with no installation.

| Module | What you practise | Open |
| --- | --- | --- |
| **Git from Zero** | Simulated terminal with a live view of the working directory, staging area, commits and remote. Covers `config`, `init`, `status`, `add`, `commit`, `log`, `diff`, `restore`, `revert`, `.gitignore`, branches, merging, conflicts, `clone`, `push`, `pull`. | `docs/git-basics.html` |
| **Exam Prep: Quantum Many-Body Physics 2** | Exam review for PHYS-E0432 (exam 09.12.2026). Chapters from the course schedule only. 96 questions: easy closed-book questions, and hard open-book exercises (from the book's exercises), each with a worked solution. Progress is saved in the browser. | `docs/exam-prep.html` |
| **SQL from Zero** | Real SQLite database (sql.js) of a small bookshop. Covers `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`, `DISTINCT`, aggregates, `GROUP BY`/`HAVING`, `JOIN`/`LEFT JOIN`, `INSERT`/`UPDATE`/`DELETE`, `CREATE`/`ALTER`/`DROP TABLE`. | `docs/sql-basics.html` |

Each module has 9 lessons: explanation, runnable examples, a short quiz and typed practice that is checked automatically. Git lessons have "Type the command" drills plus a practice terminal; SQL lessons have exercises you write in an editor (the solution unlocks only after your first attempt). Lessons are grouped into three levels and unlock one after another. Exercises are tagged Warm-up, Core or Challenge; challenges combine earlier lessons and give less help (hint after the first try, solution after the third). Both modules end with a final project and include a cheat sheet. Progress is saved in the browser (localStorage).

## Exam prep module

`exam-prep.html` is the source template. Chapter content lives in `exam-data/chapter_NN.json` and is merged in by `scripts/build_exam.py` (run by `build.sh`). Questions are multiple-choice (checked immediately) or free-response (solution revealed after an attempt, then self-marked). The module uses KaTeX from jsDelivr, so it needs an internet connection.

Content is drawn only from the course book, and only from the chapters and sections in the course schedule. Items marked "Unverified" were not checked against the printed book.

## Running

Open `docs/index.html` in a browser, or enable GitHub Pages on the `docs/` folder (Settings → Pages → Branch: `main`, folder: `/docs`).

The SQL module loads sql.js from the jsDelivr CDN, so it needs an internet connection. The Git module works offline (fonts aside).

## Files

- `git-basics.html`, `sql-basics.html`: page sources (body fragments, as published as Claude artifacts).
- `build.sh`: wraps the sources into full HTML documents in `docs/`.
- `docs/`: standalone pages ready to open or serve.

After editing a source file, run `./build.sh` to refresh `docs/`.
