import MySQLdb

def connection():
    conn = MySQLdb.connect(host=config('HOST', default = ''),
                           user = config('ROOT', default = ''),
                           passwd = config('DB_PASSWORD', default = ''),
                           db =config('DATABASE', default = ''))
    c = conn.cursor()

    return c, conn
	