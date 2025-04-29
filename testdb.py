from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///lvivarc.db")
with engine.connect() as conn:
    sql_query = "select * from arctype"
    result = conn.execute(text(sql_query)).fetchall()
    print(result)
