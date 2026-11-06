# ACP — Friday Morning

192-201 Advanced Computer Programming with Generative AI

| Folder | Week | What it is |
|---|---|---|
| `library_web/` | Week 10 | Library web app: Flask + SQLite + Bootstrap (MVC) |
| `library_mobile/` | Week 11 | Library phone app: Flet, using the **same** `models.py` |

Both projects are finished: all steps in the Week 10 guide (Steps 0–16) and all milestones in the Week 11 guide (Milestones 1–7) are done.

---

## Week 10 — `library_web` (Flask)

| File | Layer | Job |
|---|---|---|
| `setup_db.py` | — | Makes the database (run once) |
| `models.py` | Model | The `Book` class: `all`, `load`, `save`, `update`, `delete`, `validate`, `search`, `to_dict` |
| `app.py` | Controller | The routes (list, detail, add, edit, delete, search, JSON API) |
| `templates/*.html` | View | The pages (`base.html` with Bootstrap and flash messages) |

### Run it in VS Code

1. **File → Open Folder…** and choose `library_web`.
2. **Terminal → New Terminal**, then:

| | Windows | macOS |
|---|---|---|
| Make the box | `python -m venv .venv` | `python3 -m venv .venv` |
| Turn it on | `.venv\Scripts\activate` | `source .venv/bin/activate` |
| Install | `pip install -r requirements.txt` | `pip install -r requirements.txt` |
| Make the DB | `python setup_db.py` | `python3 setup_db.py` |
| Run | `flask --app app run --debug` | `flask --app app run --debug` |

3. Open <http://127.0.0.1:5000/books>.

You can also use the **Run and Debug** panel (Ctrl+Shift+D): choose *Make the database*, then *Run Flask app*.

JSON API (in a second terminal; on Windows PowerShell type `curl.exe`):

```
curl http://127.0.0.1:5000/api/books
curl -i -X DELETE http://127.0.0.1:5000/api/books/3
```

---

## Week 11 — `library_mobile` (Flet)

| File | Layer | Job |
|---|---|---|
| `setup_db.py` | — | Copied from Week 10 |
| `models.py` | Model | Shared with Week 10; both copies stay identical |
| `main.py` | View + Controller | The phone screen and the event functions (no SQL) |

Both `models.py` copies open the `library.db` beside the model file. This keeps the mobile app pointed at its project database even when Flet runs it from a separate working directory.

### Run it in VS Code

1. **File → Open Folder…** and choose `library_mobile`.
2. **Terminal → New Terminal**, then:

| | Windows | macOS |
|---|---|---|
| Make the box | `python -m venv .venv` | `python3 -m venv .venv` |
| Turn it on | `.venv\Scripts\activate` | `source .venv/bin/activate` |
| Install | `pip install -r requirements.txt` | `pip install -r requirements.txt` |
| Check | `pip show flet` (Version 1.x) | `pip show flet` (Version 1.x) |
| Make the DB | `python setup_db.py` | `python3 setup_db.py` |
| Run (desktop) | `flet run main.py` | `flet run main.py` |
| Run (phone) | `flet run --android main.py` | `flet run --ios main.py` |

For the phone: install the free **Flet** app, put the phone and laptop on the same Wi-Fi (or the phone hotspot), and scan the QR code shown in the terminal.

### Proof: the Model did not change

| Windows (PowerShell) | macOS |
|---|---|
| `fc.exe models.py ..\library_web\models.py` | `diff models.py ../library_web/models.py` |
| `FC: no differences encountered` | no output |

And `main.py` contains no `sqlite3`: all SQL stays in `models.py`.

---

`library.db` and `.venv` are not in Git (see `.gitignore`). Run `setup_db.py` after you clone, or any time you want to start again with 3 books.
