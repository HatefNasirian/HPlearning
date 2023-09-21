import os
import subprocess
import sys
from threading import Thread


def create_venv():
    # Create virtual environment named 'venv'
    subprocess.run([sys.executable, '-m', 'venv', 'venv'])


def install_requirements():
    # Install packages from the Requirements file into the virtual environment
    if sys.platform == 'win32':
        pip_path = os.path.join('venv', 'Scripts', 'pip')
        python_path = os.path.join('venv', 'Scripts', 'python')
    else:
        pip_path = os.path.join('venv', 'bin', 'pip')
        python_path = os.path.join('venv', 'bin', 'python')

    subprocess.run([pip_path, 'install', '-r', 'requirements.txt'])
    # Installing ipykernel
    subprocess.run([pip_path, 'install', 'ipykernel'])

    # Adding virtual environment to Jupyter Notebook
    kernel_name = "HPlearning"
    subprocess.run([python_path, '-m', 'ipykernel', 'install', '--user', '--name', kernel_name])
    subprocess.run([pip_path, 'install', 'jupyter'])


def launch_jupyter():
    # Run Jupyter Notebook and capture its output
    if sys.platform == 'win32':
        jupyter_path = os.path.join('venv', 'Scripts', 'jupyter-notebook')
    else:
        jupyter_path = os.path.join('venv', 'bin', 'jupyter-notebook')

    process = subprocess.Popen([jupyter_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    while True:
        output = process.stdout.readline()
        print(output.strip())
        if "http://" in output or "https://" in output:
            break

    process.terminate()


def main():
    print("Setting up your Python environment...")

    print("Creating virtual environment...")
    create_venv()

    print("Installing required packages...")
    install_requirements()

    print("Setup complete!")

    print("Launching Jupyter Notebook...")
    Thread(target=launch_jupyter).start()


if __name__ == '__main__':
    main()
