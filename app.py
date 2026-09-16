from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

DATABASE = "database/phishguard.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender TEXT,
        subject TEXT,
        result TEXT,
        score INTEGER,
        created_at TEXT
    )
""")

    conn.commit()
    conn.close()


@app.route("/")
def dashboard():

    conn = get_db()

    reports = conn.execute("""
        SELECT *
        FROM reports
        ORDER BY id DESC
    """).fetchall()

    reports = [dict(r) for r in reports]

    total_reports = len(reports)

    phishing_count = sum(
        1 for r in reports
        if r["result"] == "Phishing"
    )

    safe_count = sum(
        1 for r in reports
        if r["result"] == "Safe"
    )

    conn.close()

    return render_template(
        "dashboard.html",
        total_reports=total_reports,
        phishing_count=phishing_count,
        safe_count=safe_count,
        reports=reports
    )

@app.route("/analyze", methods=["GET", "POST"])
def analyze():

    result = None
    score = 0

    if request.method == "POST":

        sender = request.form.get("sender", "")
        subject = request.form.get("subject", "")
        content = request.form.get("content", "")

        text = f"{sender} {subject} {content}".lower()

        phishing_words = [
            "urgent", "verify", "password", "login",
            "bank", "click here", "account suspended",
            "update account", "winner", "prize"
        ]

        score = sum(
            1 for word in phishing_words
            if word in text
        )

        result = "Phishing" if score >= 2 else "Safe"

        conn = get_db()

        conn.execute("""
            INSERT INTO reports
            (sender, subject, result, score, created_at)
            VALUES (?, ?, ?, ?, ?)
        """, (
            sender,
            subject,
            result,
            score,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))

        conn.commit()
        conn.close()

    return render_template(
        "analyze.html",
        result=result,
        score=score
    )
@app.route("/reports")
def reports():

    conn = get_db()

    reports = conn.execute("""
        SELECT *
        FROM reports
        ORDER BY id DESC
    """).fetchall()

    reports = [dict(r) for r in reports]

    conn.close()

    return render_template(
        "reports.html",
        reports=reports
    )


@app.route("/settings")
def settings():

    conn = get_db()

    rows = conn.execute(
        "SELECT * FROM analysts ORDER BY id DESC"
    ).fetchall()

    analysts = [dict(row) for row in rows]

    total = len(analysts)
    active = sum(
        1 for a in analysts
        if a["status"] == "Active"
    )

    conn.close()

    return render_template(
        "settings.html",
        analysts=analysts,
        total=total,
        active=active
    )



@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)