import sqlite3

def main():
  conn = sqlite3.connect("SANDVIK.tooldb")
  cur = conn.cursor()
  cur.execute('SELECT name from sqlite_master where type= "table"')

  rows = cur.fetchall()
  for row in rows:  print(row)
  cur.execute("SELECT * from TlCoolant")
  tools = cur.fetchall()
  for tool in tools:  print(tool)

  # for row in rows:
  #     search_str = f"SELECT * from {row[0]}"
  #     this = cur.execute(search_str)
  #     for some in this:
  #       print(some)



# print({True:'yes', 1:'no', 1.0:'maybe'})
# names = "John", "Rex", "Anna"
# print(type(names))

main()