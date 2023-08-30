# Setting up the Working Space 🛠

## 🎯 Objective

The main objective of this guide is to help you set up your Python development environment.

## 📘 Content Points

### ⬇️ Downloading and Installing Python

#### General Steps:

1. **Visit Python's Official Website**: Navigate to the [Python official website](https://www.python.org/downloads/).
---

> :warning: <span style="color:red">**Important Version Information**

<span style="color:yellow">I used Python version `3.11.3` in this training. I strongly and strongly urge you to pay attention to the version used in different trainings. Here, because of the use of public libraries with support and community, there is no need for this.</span>

---


#### Operating System Specific Guidelines

##### For Windows Users:

1. **Download the Installer**: Click on the "Download Python" button to download the executable installer.
2. **Run the Installer**: Locate the downloaded file and double-click to initiate the installation process.
3. **Customize Installation (Optional)**: You can choose to customize the installation, although the default settings are usually sufficient.
4. **Add to PATH**: Ensure the "Add Python to PATH" checkbox is selected for easier command-line access.
5. **Install**: Click the "Install Now" button.
6. **Check Installation**: Open a Command Prompt and type `python --version` to confirm that Python was installed correctly.

##### For Mac Users:

1. **Install Homebrew**: If not already installed, install Homebrew by running:  
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
2. **Install Python via Homebrew**:  
```bash
brew install python
```
3. **Check Installation**: Open a terminal and type `python3 --version`.

> **Note**: On Mac, Python 2.x might be pre-installed. Use `python3` to run Python 3.x.

##### For Linux Users:

1. **Debian/Ubuntu**:  
```bash
sudo apt update
sudo apt install python3
```
2. **Fedora**:  
```bash
sudo dnf install python3
```
3. **Check Installation**: Open a terminal and type `python3 --version`.

> **Note**: Most Linux distributions come with Python pre-installed. You may only need to update it.

#### Verifying Installation:

1. **Windows**: Open a Command Prompt and type `python --version`.
2. **Mac/Linux**: Open a Terminal and type `python3 --version`.

#### What's Next?

You've successfully installed Python! The next step is to pick an IDE and set up your coding environment.

---

### 🎯 Introduction to IDEs (like PyCharm, VSCode, etc.)

An Integrated Development Environment (IDE) is a software application that provides comprehensive facilities to computer programmers for software development. An IDE generally consists of a source code editor, build automation tools, and a debugger.

#### Popular IDEs for Python:

1. **VSCode**: 
    - Light-weight, highly extensible, and free.
    - Supports multiple languages beyond Python.
    - Great Git integration and terminal access.

2. **PyCharm**:
    - Feature-rich, specifically designed for Python.
    - Offers a free community version and a paid professional version.
    - Built-in tools for database, web development, and data science.

3. **Jupyter Notebook**:
    - its will automatically install after you run setup.py in next part
#### Choose What Suits You

In fact, the IDE completely depends on your taste and you can write your codes even in NotePad. The best IDE for you will depend on your specific needs, the complexity of your project, and your personal preferences.

---

---

## :book: Introduction to pip and Virtual Environments

Welcome to this essential guide on pip and virtual environments! Before we dive into the nitty-gritty of package management and isolated development spaces, let's talk about a magical script we've prepared just for you: `setup.py`. This script is your one-stop solution to setting up your Python development environment.

### :star2: The Magic of `setup.py`

#### Virtual Environment Made Easy

Running `setup.py` in your project directory will automatically create a virtual environment (`venv`) for you. A virtual environment is an isolated space where you can install Python packages without affecting the global Python environment on your system. This makes your project much more manageable and avoids package version conflicts.

#### Package Installation with pip

The `setup.py` script also takes care of installing all the required packages listed in a `RequeirMents.txt` file. This happens seamlessly using `pip`, the Python package installer. In case you're not familiar with pip, it's a tool that allows you to install and manage Python packages from the Python Package Index (PyPI) or from a local directory.

---

**Place for bash commands to run `setup.py`**

---

#### IDE Auto-Configuration

What's even more exciting is that, upon running this script, your Integrated Development Environment (IDE) should automatically detect and configure the virtual environment. This means you don't have to go through any cumbersome setup procedures in the IDE itself, whether you're using PyCharm, VSCode, or any other Python-compatible IDE.

### :warning: Important Note

Please make sure you have Python installed on your machine before executing `setup.py`. The virtual environment and package management are dependent on Python being properly set up.

---



### 🛠 Installing an IDE and Setting It Up

Installing an IDE enhances your programming experience by providing advanced features like debugging, code suggestions, and version control. This section focuses on installing PyCharm, one of the most popular IDEs for Python development.

#### Installing PyCharm

1. **Download Installer**:
    - Visit the [PyCharm download page](https://www.jetbrains.com/pycharm/download).
    - Choose between the Community (free) and Professional (paid) versions based on your needs.

2. **Run the Installer**: 
    - Locate the downloaded file and double-click to initiate the installation process.
  
3. **Installation Wizard**:
    - Follow the on-screen instructions. You'll be given options to create desktop shortcuts, add associations so Python files automatically open in PyCharm, and more.

4. **Finalize Installation**:
    - Once all settings are configured, click on the "Install" button.

5. **Launch PyCharm**:
    - After installation, run PyCharm either from the Start menu (Windows) or the Applications folder (Mac).

#### Setting Up PyCharm

1. **Initial Configuration**:
    - Upon first launch, PyCharm will ask you to configure your development environment settings. You can import settings or set up a fresh environment.

2. **Create a New Project**:
    - Go to `File > New Project` to create a new Python project.

3. **Select Python Interpreter**:
    - You can choose the interpreter we made earlier or create a new virtual environment directly from PyCharm.

4. **Explore IDE**:
    - Familiarize yourself with the IDE layout: the editor, project navigator, terminal, and other panes.

5. **Run a Test Script**:
    - Create a new Python file, write a simple program like `print("Hello, PyCharm!")`, and run it to make sure everything is set up correctly.

Congratulations! You've successfully installed and set up PyCharm for Python development.

---

## 📝 Assignment: Environment Setup

Congratulations on making it this far in the training! Your next challenge is to set up your own Python development environment. This hands-on assignment aims to provide you with practical experience in setting up a workspace tailored to your needs.

### Tasks

1. **Install Python**:
    - Navigate to the [official Python website](https://www.python.org/downloads/) to download and install the latest Python version.

2. **Choose and Install an IDE**:
    - Decide on an Integrated Development Environment (IDE) that suits you best. Some popular options are PyCharm, Visual Studio Code, and Jupyter Notebook. Download and install your chosen IDE.

3. **Create a Virtual Environment**:
    - Create a new directory for your Python project.
    - Navigate to this directory in the terminal.
    - Create a virtual environment (`venv`). More information can be found in the "Introduction to pip and Virtual Environments" section.

---

**Note**: If you have completed these tasks successfully, you will have a fully functional Python development environment tailored to your needs. This environment will allow you to write, test, and debug code more efficiently.

---

