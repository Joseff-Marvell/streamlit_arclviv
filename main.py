import streamlit as st
from arcType import arc_type
from typeList import type_list
from arcObj import arc_obj

st.set_page_config(layout="wide")
# st.title("Архітектура міста Львова")

# Змінимо колір заголовка
st.markdown(
    """
    <h1 style='color: blue;'>Архітектура міста Львова</h1>
    """,
    unsafe_allow_html=True,
)

# url = st.secrets.connection.url
# st.write(url)

ret = arc_type()
if not type(ret) is bool:
    engine = ret[0]
    num_type = ret[1]

    numObj = type_list(engine, num_type)
    if not type(numObj) is bool:
        arc_obj(engine, numObj)
