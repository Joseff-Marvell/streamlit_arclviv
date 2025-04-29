import streamlit as st
import pandas as pd
from do_query import do_query

def type_list(engine, num_type):
    sql_query = "select * from arcobj where objType_id = " + str(num_type)
    results = do_query(engine, sql_query)
    df = pd.DataFrame(results)
    df_lim = df.iloc[:, :2]     # Обмежимо таблицю df першими двома стовпчиками
    res = st.dataframe(df_lim, selection_mode="single-row", on_select="rerun")
    # res = st.dataframe(df, selection_mode="single-row", on_select="rerun")

    rowlist = res["selection"]["rows"]
    if len(rowlist) > 0:
        selrow = rowlist[0]
        id = df["id"][selrow]

        return id
    else:
        return False


