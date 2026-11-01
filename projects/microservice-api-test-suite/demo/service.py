"""Tiny stand-in for a backend microservice (stdlib only) so the demo runs anywhere.

Stores data in SQLite (the original suite used PostgreSQL) and serves two read endpoints.
Set `drift = True` to simulate an unannounced API change that breaks the contract.
"""
import json
import re
import sqlite3
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class Db:
    def __init__(self):
        self._conn = sqlite3.connect(":memory:", check_same_thread=False)
        self._lock = threading.Lock()
        self._conn.executescript(
            """
            CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL UNIQUE);
            CREATE TABLE orders(id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL REFERENCES users(id),
                                total_cents INTEGER NOT NULL, status TEXT NOT NULL);
            """
        )

    def execute(self, sql, args=()):
        with self._lock:
            cur = self._conn.execute(sql, args)
            self._conn.commit()
            return cur.lastrowid

    def query(self, sql, args=()):
        with self._lock:
            return self._conn.execute(sql, args).fetchall()


class Service:
    def __init__(self, db: Db):
        self.db = db
        self.drift = False
        self._httpd = None

    @property
    def base_url(self) -> str:
        return f"http://127.0.0.1:{self._httpd.server_address[1]}"

    def start(self):
        svc = self

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *args):  # keep test output quiet
                pass

            def _send(self, code, body):
                data = json.dumps(body).encode()
                self.send_response(code)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)

            def do_GET(self):
                if m := re.fullmatch(r"/users/(\d+)", self.path):
                    rows = svc.db.query("SELECT id, name, email FROM users WHERE id = ?", (int(m[1]),))
                    if not rows:
                        return self._send(404, {"error": "not_found"})
                    uid, name, email = rows[0]
                    return self._send(200, {"id": uid, "name": name, "email": email})
                if m := re.fullmatch(r"/users/(\d+)/orders", self.path):
                    rows = svc.db.query(
                        "SELECT id, total_cents, status FROM orders WHERE user_id = ? ORDER BY id", (int(m[1]),)
                    )
                    key = "total" if svc.drift else "total_cents"  # drift: field silently renamed
                    return self._send(200, {"orders": [{"id": i, key: t, "status": s} for i, t, s in rows]})
                self._send(404, {"error": "not_found"})

        self._httpd = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        threading.Thread(target=self._httpd.serve_forever, daemon=True).start()

    def stop(self):
        self._httpd.shutdown()
        self._httpd.server_close()
