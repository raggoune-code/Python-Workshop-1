# Workshop 1: Introduction to Python & Git Basics

Welcome to the first session of the Python Workshop Series! 
In this session, we will focus on mastering the "Fork-Clone-Branch-PR" workflow using Git and GitHub, as well as verifying our Python environment setup.

## Prerequisites
Before you begin, ensure you have:
- A GitHub account.
- Git installed on your computer.
- Python 3.x installed.

## The Task
Your goal is to add your name to the list of contributors in this repository by following these steps:

### Step 1: Fork the Repository
1. Click the **Fork** button at the top right of this repository's page to create a copy in your own GitHub account.

### Step 2: Clone Your Fork
1. Open your terminal or command prompt.
2. Clone your forked repository to your local machine:
   ```bash
   git clone https://github.com/YOUR-USERNAME/workshop-01-git-basics.git
   ```
3. Navigate into the cloned directory:
   ```bash
   cd workshop-01-git-basics
   ```

### Step 3: Create a New Branch
1. Create and switch to a new branch named `feat/add-<your-name>` (replace `<your-name>` with your actual name):
   ```bash
   git checkout -b feat/add-firstname-lastname
   ```

### Step 4: Verify Your Python Environment
1. Run the included `hello_world.py` script to ensure your Python environment is working correctly:
   ```bash
   python hello_world.py
   ```
   *If you are using macOS/Linux, you might need to use `python3 hello_world.py`.*

### Step 5: Complete the Exercise
1. Open the `contributors.txt` file in your favorite text editor.
2. Add your Name and GitHub Handle to the table (or list).
3. Save the file.

### Step 6: Commit and Push Your Changes
1. Stage your changes:
   ```bash
   git add contributors.txt
   ```
2. Commit your changes with a descriptive message:
   ```bash
   git commit -m "Add <Your Name> to contributors list"
   ```
3. Push your branch to your forked repository on GitHub:
   ```bash
   git push origin feat/add-firstname-lastname
   ```

### Step 7: Open a Pull Request (PR)
1. Go back to your forked repository on GitHub in your web browser.
2. You should see a prompt to **Compare & pull request**. Click it.
3. Ensure the base repository is the original repository and the base branch is `main`.
4. Add a title and description, then click **Create pull request**.

Congratulations! You've successfully completed the Fork-Clone-Branch-PR workflow!
