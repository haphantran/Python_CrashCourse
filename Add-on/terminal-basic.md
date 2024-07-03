# Essential Git Bash Commands for Beginners

This guide covers the most basic commands you'll need to navigate Git Bash on Windows. These commands are similar to those used in Linux bash shells.

## Opening Git Bash

1. Right-click in a folder or on your desktop
2. Select "Git Bash Here" from the context menu

## Essential Commands

### 1. pwd (Print Working Directory)

Use this command to show your current location in the file system.

```bash
pwd
```

Example output:
```
/c/Users/YourUsername/Documents
```

### 2. ls (List Directory Contents)

Use this command to see the files and folders in your current directory.

```bash
ls
```

To see hidden files as well, use:

```bash
ls -a
```

### 3. cd (Change Directory)

Use this command to navigate between folders.

- To move into a subdirectory:
  ```bash
  cd DirectoryName
  ```

- To move up one level to the parent directory:
  ```bash
  cd ..
  ```

- To move to your home directory:
  ```bash
  cd ~
  ```

- To move to a specific path:
  ```bash
  cd /c/Users/YourUsername/Documents
  ```

Remember: In Git Bash, Windows drives are accessed using /c/, /d/, etc., instead of C:, D:, etc.

## Tips:

- Use the Tab key to autocomplete file and directory names.
- Use the up and down arrow keys to navigate through previously used commands.
- Git Bash is case-sensitive, so be careful with capitalization in file and directory names.
