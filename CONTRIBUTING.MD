# CONTRIBUTING.md

## How to contribute to the project

```bash

# Step 1: Create a Python virtual environment using `venv`
python3 -m venv venv && cd venv

# Step 2: Activate the virtual environment
# On Unix or macOS:
source bin/activate

# Step 3: Clone the repository
git clone https://github.com/lobocode/dlsub.git

# Step 4: Change to the cloned directory
cd dlsub

# Step 5: Install the required packages
pip install -r requirements.txt
```

## How to run the project example

```bash
python main.py --download 4Z59UtES2Gs -o output.txt -f -l pt

```

We appreciate your interest in contributing to our project! To help maintain the project's quality, please follow these guidelines when submitting your changes:

1. **Create a `develop` branch**: Please create a new branch called `develop` based on the current `main` branch. This will be the branch where you'll make your changes and submit your pull request.
2. **Use Pylint**: Run Pylint on your code to ensure it follows PEP 8 standards. You can install Pylint using `pip install pylint`, and then run it on your Python files with `pylint file_name.py`. Address any issues Pylint raises before submitting your pull request. Or install pylint in your vscode (or editor of choice).
3. **Write clean and readable code**: Make sure your code is well-organized, properly commented, and easy to understand. This will make it easier for others to review your changes and maintain the project in the future.
4. **Test your code**: Before submitting your pull request, thoroughly test your changes to ensure they work as intended and do not introduce new bugs. This will help maintain the project's stability and save time during the review process.
Once you have followed these guidelines, create a pull request from your `develop` branch to the project's `main` branch. We will review your changes and provide feedback. Thank you for your contribution!
