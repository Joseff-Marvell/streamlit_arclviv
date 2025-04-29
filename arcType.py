import streamlit as st
from sqlalchemy import create_engine
import pandas as pd
from do_query import do_query


def arc_type():
    engine = create_engine('sqlite:///lvivarc.db')
    sql_query = "select * from arctype"
    results = do_query(engine, sql_query)
    df = pd.DataFrame(results)
    # st.dataframe(df)
    res = st.dataframe(df, selection_mode="single-row", on_select="rerun")

    rowlist = res["selection"]["rows"]
    if len(rowlist) > 0:
        selrow = rowlist[0]
        id = df["id"][selrow]
        Назва = df["typeName"][selrow]

        # st.header(Назва)
        # Змінимо колір підзаголовка
        st.markdown(
            f"""
            <h2 style='color: blue;'>{Назва}</h2>
            """,
            unsafe_allow_html=True,
        )

        ret_list = [engine, id]
        return ret_list
    else:
        return False
