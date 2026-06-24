import sqlite3

DB_NAME = "qos.db"


class MetricsRepository:

    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)

        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS metrics(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            service TEXT,

            status_code INTEGER,

            success INTEGER,

            latency REAL,

            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP

        )
        """)

        self.conn.commit()


    def save(self, observation):

        self.conn.execute(
        """
        INSERT INTO metrics(
        service,
        status_code,
        success,
        latency
        )

        VALUES(?,?,?,?)

        """,

        (

            observation.service_name,

            observation.status_code,

            int(observation.is_up),

            observation.latency_ms

        )
        )

        self.conn.commit()


    def get_all(self, service):

        cursor = self.conn.execute(

        """

        SELECT success, latency

        FROM metrics

        WHERE service=?

        """,

        (service,)

        )

        return cursor.fetchall()