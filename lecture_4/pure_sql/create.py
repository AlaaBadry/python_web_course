import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def create_table(conn, create_table_sql):
    try:
        cur = conn.cursor()
        cur.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = "./company.db"

    sql_create_projects_table = """
        CREATE TABLE IF NOT EXISTS projects (
            id integer PRIMARY KEY,
            name text NOT NULL,
            begin_date text,
            end_date text
        );
         """

    sql_create_tasks_table = """
        CREATE TABLE IF NOT EXISTS tasks (
            id integer PRIMARY KEY,
            name text NOT NULL,
            priority integer,
            status_id integer NOT NULL,
            project_id integer NOT NULL,
            begin_date text NOT NULL,
            end_date text NOT NULL,
            FOREIGN KEY (project_id) REFERENCES projects (id)
        );
        """

    conn = create_connection(database)
    if conn:
        create_table(conn, sql_create_projects_table)
        create_table(conn, sql_create_tasks_table)
        conn.close()
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
