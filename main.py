import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout='wide')
st.title("Interactive Visualization of Indian Census and Infrastructure Data")
components.html("""
    <script>
        const observer = new MutationObserver((mutations) => {
            for (const mutation of mutations) {
                const sidebar = document.querySelector('[data-testid="stSidebar"]');
                if (sidebar && sidebar.style.transform.includes('-100%')) {
                    document.querySelector('[data-testid="collapsedControl"]').click();
                }
            }
        });
        observer.observe(document.body, { childList: true, subtree: true });
    </script>
""", height=0)

df=pd.read_csv('india.csv')
states=list(df['State'].unique())
states.insert(0,'Overall India')

st.sidebar.title("India Data Visualisation")
selected_state=st.sidebar.selectbox('Select a state',states)
primary=st.sidebar.selectbox('Select primary parameter',sorted(df.columns[5:]))
secondary=st.sidebar.selectbox('Select secondary parameter',sorted(df.columns[5:]))

plot=st.sidebar.button('Plot Graph')
if plot:
    if selected_state=='Overall India':
        fig=px.scatter_mapbox(df,lat='Latitude',lon='Longitude',zoom=3,mapbox_style='carto-positron',size=primary,color=secondary,size_max=30,width=1200,height=700,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
    else:
        state_df=df[df['State']==selected_state]
        fig=px.scatter_mapbox(state_df,lat='Latitude',lon='Longitude',zoom=6,mapbox_style='carto-positron',size=primary,color=secondary,size_max=20,width=1200,height=700,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
    st.text("Size represents primary parameter")
    st.text("Color represents secondary parameter")