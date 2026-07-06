Hi, I'm Clayton

I'm a Python developer / data analyst  interested in automation, APIs, and clean data pipelines. This repo collects projects I've built to learn, experiment, and solve real problems.

📫 Reach me: claytonjroy@icloud.com 


🔧 Skills & Tools


Languages: Python, SQL
ML/AI: PyTorch, Hugging Face Transformers, CodeBERT, LSTM architectures
Data & Analysis: Pandas, NumPy, Matplotlib, regression/growth modeling
Security: Cryptography (Fernet/symmetric encryption), password hashing (hashlib)
UI/Tooling: ipywidgets, Jupyter/Colab




📂 Featured Projects

Agentic AI Model — SQL Query Optimizer (IN PROGRESS)

What it does: A neural network–based agent that learns to spot inefficient SQL queries and rewrite them into optimized versions with an explanation of the fix.
Tech used: PyTorch, Hugging Face Transformers, CodeBERT tokenizer, custom bidirectional LSTM query encoder, synthetic training data generation with sqlparse.
Highlights: Combines a custom training-data generator (inefficient/optimized query pairs with rationale) with a from-scratch encoder architecture.

Data Center Growth Projections for Large-Scale Solar Array Planning

What it does: A data analysis project that cleans and analyzes global data center data, then projects future growth (using U.S. Dept. of Energy growth-rate estimates) to build a business case for a solar company to pursue power purchase agreements with major data center operators like Amazon.
Tech used: Pandas, NumPy, Matplotlib, exponential growth modeling, data cleaning/wrangling.
Highlights: Goes beyond a technical exercise - ties the analysis directly to a business recommendation (targeting Amazon's energy-matching initiative), with clear visualizations of current vs. projected data center counts by country.

Password Manager Application

What it does: A secure, interactive password manager with master-password authentication, encrypted credential storage, and an in-notebook UI for adding and viewing saved passwords.
Tech used: cryptography (Fernet symmetric encryption), hashlib (SHA-256 master password hashing), ipywidgets for the interactive UI.
Highlights: Refactored from procedural script into a clean PasswordManager class with a proper separation of logic and UI - methods return (success, message) tuples instead of using input()/print(), making it easy to plug into any interface. Sensitive inputs are cleared after each use.
