import sqlite3


def create_database():

    conn = sqlite3.connect("database/candidates.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS candidates(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,

        ats_score REAL,

        rating TEXT
    )
    """)

    conn.commit()

    conn.close()


def insert_candidate(name, score, rating):

    conn = sqlite3.connect("database/candidates.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO candidates(
            name,
            ats_score,
            rating
        )
        VALUES(?,?,?)
        """,
        (
            name,
            score,
            rating
        )
    )

    conn.commit()

    conn.close()

def get_all_candidates():

    conn = sqlite3.connect("database/candidates.db")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            name,
            ats_score,
            rating
        FROM candidates
        ORDER BY ats_score DESC
    """)

    candidates = cursor.fetchall()

    conn.close()

    return candidates

def search_candidate(name):

    conn = sqlite3.connect("database/candidates.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            name,
            ats_score,
            rating
        FROM candidates
        WHERE name LIKE ?
        ORDER BY ats_score DESC
        """,
        ('%' + name + '%',)
    )

    candidates = cursor.fetchall()

    conn.close()

    return candidates
def filter_candidates(rating):

    conn = sqlite3.connect("database/candidates.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            name,
            ats_score,
            rating
        FROM candidates
        WHERE rating = ?
        ORDER BY ats_score DESC
        """,
        (rating,)
    )

    candidates = cursor.fetchall()

    conn.close()

    return candidates
def get_dashboard_stats():

    conn = sqlite3.connect("database/candidates.db")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            COUNT(*),
            AVG(ats_score),
            MAX(ats_score),
            MIN(ats_score)
        FROM candidates
    """)

    stats = cursor.fetchone()

    conn.close()

    return stats

def delete_candidate(name):

    conn = sqlite3.connect("database/candidates.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM candidates
        WHERE name = ?
        """,
        (name,)
    )

    conn.commit()

    conn.close()