import subprocess

def run_stramlit():
    subprocess.run(["streamlit", "run", "streamlit.py"])

if __name__ == "__main__":
    run_stramlit()

