# Study Modules: Git and SQL from Zero

Two interactive, self-contained courses for complete beginners. Each runs in the browser with no installation.

| Module | What you practise | Open |
| --- | --- | --- |
| **Git from Zero** | Simulated terminal with a live view of the working directory, staging area, commits and remote. Covers `config`, `init`, `status`, `add`, `commit`, `log`, `diff`, `restore`, `revert`, `.gitignore`, branches, merging, conflicts, `clone`, `push`, `pull`. | `docs/git-basics.html` |
| **SQL from Zero** | Real SQLite database (sql.js) of a small bookshop. Covers `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`, `DISTINCT`, aggregates, `GROUP BY`/`HAVING`, `JOIN`/`LEFT JOIN`, `INSERT`/`UPDATE`/`DELETE`, `CREATE`/`ALTER`/`DROP TABLE`. | `docs/sql-basics.html` |

Each module has 9 lessons: explanation, runnable examples, a short quiz and typed practice that is checked automatically. Git lessons have "Type the command" drills plus a practice terminal; SQL lessons have exercises you write in an editor (the solution unlocks only after your first attempt). Lessons are grouped into three levels and unlock one after another. Exercises are tagged Warm-up, Core or Challenge; challenges combine earlier lessons and give less help (hint after the first try, solution after the third). Both modules end with a final project and include a cheat sheet. Progress is saved in the browser (localStorage).

## Running

Open `docs/index.html` in a browser, or enable GitHub Pages on the `docs/` folder (Settings → Pages → Branch: `main`, folder: `/docs`).

The SQL module loads sql.js from the jsDelivr CDN, so it needs an internet connection. The Git module works offline (fonts aside).

## Files

- `git-basics.html`, `sql-basics.html`: page sources (body fragments, as published as Claude artifacts).
- `build.sh`: wraps the sources into full HTML documents in `docs/`.
- `docs/`: standalone pages ready to open or serve.

After editing a source file, run `./build.sh` to refresh `docs/`.
