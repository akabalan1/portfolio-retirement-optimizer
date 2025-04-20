
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st

@st.cache_resource
def connect_sheet():
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(
        st.secrets["gcp_service_account"], scope)
    client = gspread.authorize(credentials)
    sheet = client.open_by_url(st.secrets["private_gsheets_url"])
    return sheet

def read_settings():
    sheet = connect_sheet()
    settings_ws = sheet.worksheet("Settings")
    data = settings_ws.get_all_values()
    return {row[0]: row[1] for row in data if len(row) > 1}

def write_results(table):
    sheet = connect_sheet()
    ws = sheet.worksheet("Simulation")
    ws.clear()
    ws.append_row(["Year", "p5", "p10", "p25", "p50", "p75", "p90"])
    for row in table:
        ws.append_row(row)
