import numpy as np
import streamlit as st
import pandas as pd

from os import devnull, sep
import xlrd
import warnings
import re
import gspread
# configuration
st.set_option('deprecation.showfileUploaderEncoding', False)



# title of the app
st.title("PROCESOS DE DATOS GPON")

# Add a sidebar
st.sidebar.subheader("Primero cargar Trouble Tickets")

# Setup file upload
uploaded_file = st.sidebar.file_uploader(
                        label="Upload your CSV or Excel file. (200MB max)",
                         type=['csv', 'xlsx', 'XLS'])

global df
if uploaded_file is not None:
    print(uploaded_file)
    print("hello")

    try:
        df = pd.read_excel(uploaded_file, engine="openpyxl", skiprows=3)
        df.to_csv('AVERIAS/DT_AVERIAS_Trouble.csv',index=False)

        datos = {
            'CONTRATA_TOA__c': ['ANALISIS DE RUIDO PEX','ANOVO','CABECERA','COBRA','COMFICA','CUARENTENA COE','DOMINION','ENERGIA','EZENTIS','FIBRA','GAC-VOIP','INGENIERIA HFC',
                    'LARI','LITEYCA','TRABAJOS PROGRAMADOS','TRANSMISIONES','TRATAMIENTO INTERMITENCIA','TRIAJE HFC','TRATAMIENTO CALL PIN TV-M1'],
            'codctr' : ['485','333','60','15','363','429','335','211','19','209','353','435','245','470','365','210','483','474','434']
        }
        df = pd.DataFrame(datos)
        #print(df)
        datos2 = {
            'Categorization Tier 3': ['Control Remoto'],
            'codmotv' : ['I129']
        }
        df2 = pd.DataFrame(datos2)
        #print(df2)
        Trouble = pd.read_csv('AVERIAS/DT_AVERIAS_Trouble.csv', sep=',', low_memory=False)
        Trouble=Trouble[['Incident Number','CREATION_DATE_CRM__c','Tipo de incidencia padre','CONTRATA_TOA__c','Categorization Tier 3','CUSTOMER_NAME_CRM__c',
        'OBSERVATIONS_CRM__c','STREETTYPE_CRM__c','STREETNAME_CRM__c','STREETNUMBER_CRM__c','SUBUNITTYPE_CRM__c','DEPARTMENT_CRM','DISTRICT_CRM__c',
        'Network Technology__c','LEX_NIL__c','BORNE_NIL__c','TROBA_ TYPE_NIL__c','TAP_STREET_NIL__c','PLANE_OLT_PORT','NODE_HFC_OLT_HOSTNAME',
        'currentVozTelephone_OMS__c','currentVozProduct_OMS__c','currentVozServiceTechnology_OMS__c','currentBafAccessid_OMS__c','CFS_SERVICE_TECHNOLOGY_NIL__c'
        ]]
        #<<------------------------->>
        #comvertir año 1070-01-01 con  FECHA REAL
        Trouble['CREATION_DATE_CRM__c'] = pd.to_datetime(Trouble['CREATION_DATE_CRM__c'], errors='coerce', unit='d', origin='1899-12-30')
        Trouble['CREATION_DATE_CRM__c'] = pd.to_datetime(Trouble.CREATION_DATE_CRM__c, errors = 'coerce').dt.strftime("%Y/%m/%d  %H:%M:%S")
        #concatenated_df=pd.concat([Trouble,cms],ignore_index=True)
        union1 = pd.merge(left=Trouble,right=df, how='left', left_on='CONTRATA_TOA__c', right_on='CONTRATA_TOA__c')
        union2 = pd.merge(left=union1,right=df2, how='left', left_on='Categorization Tier 3', right_on='Categorization Tier 3')
        Trouble2=union2[['Incident Number','CREATION_DATE_CRM__c','Tipo de incidencia padre','codctr','CONTRATA_TOA__c','codmotv','Categorization Tier 3','CUSTOMER_NAME_CRM__c',
        'OBSERVATIONS_CRM__c','STREETTYPE_CRM__c','STREETNAME_CRM__c','STREETNUMBER_CRM__c','SUBUNITTYPE_CRM__c','DEPARTMENT_CRM','DISTRICT_CRM__c',
        'Network Technology__c','LEX_NIL__c','BORNE_NIL__c','TROBA_ TYPE_NIL__c','TAP_STREET_NIL__c','PLANE_OLT_PORT','NODE_HFC_OLT_HOSTNAME',
        'currentVozTelephone_OMS__c','currentVozProduct_OMS__c','currentVozServiceTechnology_OMS__c','currentBafAccessid_OMS__c','CFS_SERVICE_TECHNOLOGY_NIL__c'
        ]]
        Trouble2["CFS_SERVICE_TECHNOLOGY_NIL__c"] = Trouble2["CFS_SERVICE_TECHNOLOGY_NIL__c"].replace({'VOIP':'VOZ','GPON':'DATOS','CATV':'TV','DOCSIS':''}, regex=True)
        Trouble2 = Trouble2.rename(columns={'CFS_SERVICE_TECHNOLOGY_NIL__c':'BORRAR',})
        Trouble2.columns = ['codreq','fec_regist','codedo','codctr','desnomctr','codmotv','desmotv','nomcli','desobsordtrab','destipvia','desnomvia','numvia','destipurb','codofcadm',
        'desdtt','tiptecnologia','codtap','codbor','codtrtrn','desurb','nroplano','codnod','numtelefvoip','codpromo','tiplinea','codcli','BORRAR']
        Trouble2['AVERIAS']='Trouble'

        #Trouble2.to_csv('AVERIAS/DT_AVERIAS_Trouble.csv',index=False)

        st.write("SER CARGO CON EXITO Trouble Tickets")
        #st.write(df)
    
    except Exception as e:
        print(e)