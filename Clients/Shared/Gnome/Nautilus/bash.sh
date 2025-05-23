#!/usr/bin/env bash
set -euo pipefail

# 1. Download the repository
wget https://github.com/TheKing6488/Configs/archive/refs/heads/main.zip -O temp.zip

# 2. Extract files and clean up
unzip temp.zip && rm temp.zip

# 3. Install the extension
sudo mv Configs-main/Clients/Shared/Gnome/Nautilus/open_in_vscode.py /usr/share/nautilus-python/extensions
sudo mv Configs-main/Shared/Gnome/Nautilus/open_in_ghostty.py /usr/share/nautilus-python/extensions

# 4. Restart Nautilus to apply changes
nautilus -q

# 5. Clean up temporary files
rm -r Arch-Config-main

# 6. Install nautilus-python
sudo pacman -S nautilus-python

