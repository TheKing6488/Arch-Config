# Nautilus VSCode Extension Installation

This guide explains how to install the "Open in VSCode" and "Open in Ghostty" extension for the Nautilus file manager.

## Installation Steps

### 1. Download the repository
```bash
wget https://github.com/TheKing6488/Arch-Config/archive/refs/heads/main.zip -O temp.zip
```

### 2. Extract files and clean up
```bash
unzip temp.zip && rm temp.zip
```

### 3. Install the extension
```bash
sudo mv Arch-Config-main/Gnome/open_in_vscode.py /usr/share/nautilus-python/extensions
sudo mv Arch-Config-main/Gnome/open_in_ghostty.py /usr/share/nautilus-python/extensions
```

### 4. Restart Nautilus to apply changes
```bash
nautilus -q
```

### 5. Clean up temporary files
```bash
rm -r Arch-Config-main
```

### 6. Install nautilus-python
```bash
sudo pacman -S nautilus-python
```
## After installation
Right-click on files or folders in Nautilus to see the "Open in VSCode" option.
