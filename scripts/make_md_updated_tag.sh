#!/bin/bash

# !!! FILE TO BE RUN BY GH ACTIONS UPON PUSH TO MAIN AFTER PARSE TO DOCS !!!

# Retrieve the list of files that were updated in the previous commit
LATEST_UPDATED_FILES=$(git diff-tree --no-commit-id --name-only -r HEAD | grep "docs" |grep "\.md$")
# Retrieve the list of files that have been added/modified in current session:
# TRACKED_FILES=$(git diff --name-only | grep "docs" | grep "\.md$")
# UNTRACKED_FILES=$(git ls-files --others --exclude-standard | grep "docs" | grep "\.md$")
# printf "FOUND FILES:\nTRACKED:\n$TRACKED_FILES\nUNTRACKED:\n$UNTRACKED_FILES\n"

if [[ -n "$LATEST_UPDATED_FILES" ]]; then
    printf "Found files:\n$LATEST_UPDATED_FILES\nNow running tag update.\n"
else
    printf "No modifications to docs folder. Running tag update in case of initialization.\n"
fi

# Run script
python scripts/append_md_updates.py $LATEST_UPDATED_FILES
# python scripts/append_md_updates.py $TRACKED_FILES $UNTRACKED_FILES
