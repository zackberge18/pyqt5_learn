import sqlite3
conn = sqlite3.connect("cook.db")
c = conn.cursor()
c.execute("""CREATE TABLE cook(
            cook_name text,
            dish_name text,
            dish_info text
            )""")
conn.commit()
conn.close()