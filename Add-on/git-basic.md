# Git Basics Tutorial

Git is a distributed version control system that helps you track changes in your code over time. This tutorial will guide you through the fundamental concepts and commands of Git.

## Table of Contents
- [Git Basics Tutorial](#git-basics-tutorial)
  - [Table of Contents](#table-of-contents)
  - [1. Installation](#1-installation)
  - [2. Configuration](#2-configuration)
  - [3. Creating a Repository](#3-creating-a-repository)
  - [4. Basic Git Workflow](#4-basic-git-workflow)
    - [Adding Files](#adding-files)
    - [Committing Changes](#committing-changes)
    - [Checking Status](#checking-status)
    - [Viewing History](#viewing-history)
  - [5. Branching](#5-branching)
  - [6. Merging](#6-merging)
  - [7. Remote Repositories](#7-remote-repositories)
  - [8. Pulling Changes](#8-pulling-changes)

## 1. Installation

First, download and install Git from [git-scm.com](https://git-scm.com/).

## 2. Configuration

After installation, set up your identity:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## 3. Creating a Repository

To start a new Git repository:

1. Create a new directory for your project
2. Navigate to that directory in the terminal
3. Initialize the repository:

```bash
git init
```

## 4. Basic Git Workflow

The basic Git workflow involves three main areas:

1. Working Directory: Where you edit your files
2. Staging Area: Where you prepare changes for a commit
3. Repository: Where Git stores the history of your project

### Adding Files

To add files to the staging area:

```bash
git add filename
```

To add all changes:

```bash
git add .
```

### Committing Changes

To commit staged changes:

```bash
git commit -m "Your commit message"
```

### Checking Status

To see the current status of your repository:

```bash
git status
```

### Viewing History

To view the commit history:

```bash
git log
```

## 5. Branching

Branches allow you to work on different versions of your project simultaneously.

To create a new branch:

```bash
git branch branch-name
```

To switch to a branch:

```bash
git checkout branch-name
```

To create and switch to a new branch in one command:

```bash
git checkout -b new-branch-name
```

## 6. Merging

To merge changes from one branch into another:

1. Switch to the branch you want to merge into
2. Use the merge command:

```bash
git merge branch-name
```

## 7. Remote Repositories

To add a remote repository:

```bash
git remote add origin https://github.com/username/repo-name.git
```

To push your changes to a remote repository:

```bash
git push -u origin main
```

To clone an existing repository:

```bash
git clone https://github.com/username/repo-name.git
```

## 8. Pulling Changes

To fetch and merge changes from a remote repository:

```bash
git pull origin main
```

---

This is a basic introduction to Git. As you become more comfortable with these concepts, you can explore more advanced features and workflows. Remember, practice is key to mastering Git!
