# GeoGuessing

## Functional description

TBD

## Data modell

TBD


## Flask Installation manual

I have looked into Flask and got it running. However, to make it work, you need to configure it yourself after checking it out from GitHub using this guide: [Flask VS Code Tutorial.](https://code.visualstudio.com/docs/python/tutorial-flask)

**Important:**

1. Create the Python project environment that sets up the `.venv` folder.
2. Activate the environment via PowerShell or Command (depending on Windows or Mac).
3. Install the two packages `flask` and `flask-restful`:
   ```bash
   python -m pip install flask
   python -m pip install flask-restful
   ```
4. Start the app with:
   ```bash
   python -m flask run
   ```
After that, it should be accessible in the browser via http://127.0.0.1:5000/.

Afterwards, the project in GitHub should look like this and be able to start as described in the guide:

- All HTML pages must be placed in the `/templates` subfolder.
- In `app.py`, there is a function that renders `index.html` when the page is called.
- Additionally, a test REST endpoint is defined in it, which is successfully called in `test.html`.
- I will define the correct endpoints for our project by the weekend.

---
