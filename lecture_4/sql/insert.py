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


def create_project(conn, project):
    sql = '''
        INSERT INTO projects(name,begin_date,end_date)
        VALUES(?,?,?)
    '''
    cur = conn.cursor()
    cur.execute(sql, project)
    return cur.lastrowid


def create_task(conn, task):
    sql = '''
        INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
        VALUES(?,?,?,?,?,?)
    '''
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid


def main():
    database = "./company.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        project = ('My new project', '2019-03-01', '2019-03-30')
        project_id = create_project(conn, project)

        # tasks
        task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2019-03-01', '2019-03-02')
        task_2 = ('Confirm with user about the top requirements', 2, 1, project_id, '2019-03-03', '2019-03-05')

        # create tasks
        create_task(conn, task_1)
        create_task(conn, task_2)


if __name__ == '__main__':
    main()
