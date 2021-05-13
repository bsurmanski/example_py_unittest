import sqlite3

def post_count(con, author_id):
    cur = con.cursor()
    out = cur.execute("SELECT COUNT(*) FROM posts WHERE author_id = ?", (author_id,))
    return out.fetchone()[0]
