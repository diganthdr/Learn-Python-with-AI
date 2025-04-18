
# 🧠 Git Basics Cheat Sheet for Beginners

Welcome to your Git learning journey! Here's a handy guide to the essential Git concepts and commands you'll learn today.

---

## 📘 Concepts to Know

- **Git**: A distributed version control system.
- **Repository**: A project folder tracked by Git.
- **Working Directory**: Your project files.
- **Staging Area**: Files ready to be committed.
- **Commit**: A snapshot of your changes.
- **Branch**: A parallel version of the repo.
- **Remote**: A version of your project hosted online (e.g., on GitHub).

---

## 🛠️ Setup

```bash
# Install Git (from https://git-scm.com/)
# Then configure your name and email:
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

---

## 📁 Start a New Project

```bash
mkdir my-project
cd my-project
git init
```

---

## 📝 Track and Save Changes

```bash
git status              # See changes
git add filename        # Stage one file
git add .               # Stage all changes
git commit -m "Message" # Commit with a message
```

---

## 📜 See Your History

```bash
git log                 # Full history
git log --oneline       # Short version
git show                # See details of last commit
```

---

## ☁️ Work with GitHub

### Push Existing Repo

```bash
git remote add origin https://github.com/yourname/repo.git
git branch -M main
git push -u origin main
```

### Clone an Existing Repo

```bash
git clone https://github.com/someuser/repo.git
```

---

## 🔄 Keep Your Repo Updated

```bash
git pull   # Pull latest changes
git push   # Push your commits
```

---

## 🌱 Branching (Intro)

```bash
git branch new-feature       # Create new branch
git checkout new-feature     # Switch to new branch
git checkout -b bugfix       # Create + switch
git merge new-feature        # Merge branch into current
```

---

## 🧰 Quick Reference

| Command | Purpose |
|--------|---------|
| `git init` | Initialize repo |
| `git add .` | Stage all |
| `git commit -m` | Commit |
| `git status` | See changes |
| `git push` | Push to GitHub |
| `git pull` | Pull updates |
| `git branch` | See branches |
| `git checkout` | Switch branch |

---

Happy Coding! 🚀

---

## 🧪 Hands-On Exercises

### Exercise 1: Initialize a Repository
1. Create a new folder called `my-first-repo`.
2. Open terminal in that folder.
3. Run:
   ```bash
   git init
   touch README.md
   git add README.md
   git commit -m "Initial commit"
   ```

### Exercise 2: Make a Few Commits
1. Add a new file called `about.txt`, write a short paragraph about yourself.
2. Add and commit the file.
3. Modify the file and commit again.

### Exercise 3: Push to GitHub
1. Create a new repo on GitHub (no README).
2. Connect your local repo:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git branch -M main
   git push -u origin main
   ```

### Exercise 4: Clone and Modify
1. Clone any public repository of your choice:
   ```bash
   git clone https://github.com/someuser/somerepo.git
   ```
2. Make a small change, and push it (if you own the repo) or create a pull request.

### Exercise 5: Branch and Merge
1. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
2. Add a new file or make a change, commit it.
3. Switch back to `main` and merge:
   ```bash
   git checkout main
   git merge feature-branch
   ```

---

✅ Practice these steps to become confident with Git basics!
