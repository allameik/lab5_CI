import subprocess

def test_run_application():
    try:
        result = subprocess.run(['python', 'app.py'], capture_output=True, check=True)
        print("Application ran successfully.")
        print("Output:")
        print(result.stdout.decode('utf-8'))

    except subprocess.CalledProcessError as e:
        print("Error running the application:")
        print(e)

if __name__ == "__main__":
    test_run_application()