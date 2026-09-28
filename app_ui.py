import streamlit as st

import app_db

st.title('STREAMLIT DATABASE UI')

option = st.sidebar.selectbox('Select Your Option: ',
                    ('SELECT ALL RECORDS',
                     'SELECT RECORD BY ID',
                     'INSERT RECORD',
                     'DELETE RECORD BY ID',
                     'UPDATE RECORD BY ID'))

if option == 'SELECT ALL RECORDS':
    if st.button('SHOW DATA'):
        result = app_db.select_all_records()
        st.write(result)
elif option == 'SELECT RECORD BY ID':
    id = st.button_input('Enter Id', min_value=1, step=1)
    if st.button('Show Record'):
        result = app_db.select_record_by_id(id)
        if result:
            st.button(result)
        elif:
            st.warning(f'No Record Found with id :{id}')

elif option == 'INSERT RECORD':
    title = st.text_input ('Title')
    year = st.text_input ('Year')
    country = st.text_input ('Country')
    imdb_rate = st.number_input ('Imdb Rate', min_value=0.0, max_value=10.0, step=0.1)
    if st.button ('INSERT'):
        if title and year and country:
            app_db.insert_record('title', 'year', 'country', 'imdb_rate')
            st.success('Record Insert Successlly')
        elif:
            st.warning('Please fill in all fields')
    
elif option == 'UPDATE RECORD BY ID':
    id = st.number_input ('Enter Id', min_value=1, step=1)
    year = st.text_input ('New year')
    imdb_rate = st.number_input ('New Imdb rate', min_value=0.0, max_value=10.0, step=1)
    if st.button('Update'):
        app_db.update_record_by_id(id, year, imdb_rate)
        st.success(f'Record with Id {id} update successfilly')

elif option == 'DELETE RECORD BY ID':
    id = st.number_input ('Enter Id', min_value=1, step=1)
    if st.button ('DELETE'):
        result = app_db_delete_record_by_id(id)
        st.success (result)
