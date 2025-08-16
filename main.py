# app.py
import subprocess
import sys
from database.db import criar_tabela

def run_app():
    subprocess.run([sys.executable, "-m", "streamlit", "run", "pages/main_page.py"])

if __name__ == "__main__":
    criar_tabela()
    run_app()
