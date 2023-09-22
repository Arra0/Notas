import streamlit as st

st.sidebar.title("calculadora")
n1 = st.number_input("Numero 1")
n2 = st.number_input("Numero 2")
n3={1,2,3,4}

   

opcion = st.sidebar.selectbox("opciones", ["Suma","Resta","Multiplicacion","Divicion"])

match opcion:
    case "Suma":
        st.write("Esta es la opcion suma...")
        if st.button("Sumar"):
            st.write(f"{n1}+{n2} = {n1+n2}")
    case "Resta":
        st.write("Esta es la opcion Resta...")
        if st.button("Resta"):
            st.write(f"{n1}-{n2} = {n1-n2}")
    case "Multiplicacion":
        st.write("Esta es la opcion Multiplicacion...")
        if st.button("Multiplicacion"):
            st.write(f"{n1}*{n2} = {n1-n2}")
    case "Divicion":
        st.write("Esta es la opcion divicion...")

