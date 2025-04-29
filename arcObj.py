import streamlit as st
from do_query import do_query


def arc_obj(engine, numObj):
    sql_query = "select * from arcobj where id = " + str(numObj)
    results = do_query(engine, sql_query)
    row = results[0]

    objName = row[1]
    # st.subheader(objName)

    # Змінимо колір заголовка
    st.markdown(
        f"""
        <h3 style='color: blue;'>{objName}</h3>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)
    with col1:
        image = row[4]
        st.image("media/" + image, objName)
        curAddr = row[3]
        st.write("Сучасна адреса: " + curAddr)

    with col2:
        descr = row[2]
        st.write(descr)
