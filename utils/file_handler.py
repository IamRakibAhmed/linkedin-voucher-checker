import pandas as pd
from config import URLS_FILE

def load_urls():
    """Load URLs from the Excel file."""
    return pd.read_excel(URLS_FILE)['URLs']

def update_urls_file(remaining_urls):
    """Update the Excel file to keep only remaining URLs."""
    df = pd.DataFrame(remaining_urls, columns=["URLs"])
    df.to_excel(URLS_FILE, index=False)
