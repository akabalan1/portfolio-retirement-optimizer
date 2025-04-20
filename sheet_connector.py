import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

def get_settings():
    return {
        'starting_value': 1000000,
        'spend': 50000,
        'mu': 0.07,
        'sigma': 0.12
    }

def write_results(results):
    pass  # Implement Google Sheets write here
