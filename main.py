# app.py
import subprocess
import sys

def run_app():
    subprocess.run([sys.executable, "-m", "streamlit", "run", "pages/main_dashboard.py"])

if __name__ == "__main__":
    run_app()
