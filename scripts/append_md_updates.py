import sys
import os
import glob
from datetime import datetime
import re

def get_files(path, extension, recursive=False, depth=-1):
    """
    A generator of filepaths for each file into path with the target extension.
    If recursive, it will loop over subfolders as well.
    If depth limit is set, it will not traverse into sub directories.

    Adapted from: https://stackoverflow.com/questions/58836239/find-all-files-with-an-extension-recursively
    """

    if not recursive:
        for file_path in glob.iglob(path + "/*." + extension):
            yield file_path
    else:
        # base_depth = path.count(os.sep)
        for root, dirs, files in os.walk(path):
            # delta_depth = root.count(os.sep) - base_depth
            # if depth > -1 and delta_depth > depth:
            #     dirs[:] = [] # Limit search to this directory

            for file_path in glob.iglob(root + "/*." + extension):
                yield file_path

def append_md_updates(files):
    """
        Appends 'last updated' tags to all markdown files in docs 
    """

    # Retrieve out string
    def get_out_string(fpath, time, head="", cond=True):
        if "docs/README.md" in fpath: # Write if file is Overview file
            return f"_Latest Website Update: {time}_\n\n"
        if cond: # Page update
            return f"_Latest Page Update: {time}_\n\n"
        return head # Return head if condition is false (file not updated)

    # Extend modified file paths and convert to set
    pwd = os.getcwd()
    file_set = {os.path.join(pwd, file) for file in files}

    # Retrieve all .md files in docs directory:
    all_md_files = get_files(os.path.join(pwd,'docs'), 'md', recursive=True)
        # depth=0 ensures recursing only happens one layer deep (e.g. into ex1-Intro.../, no deeper)

    # Time:
    time = datetime.today().strftime('%d-%m-%Y')

    # Loop over md files
    decision_log = lambda fpath, idx, state: print(f"{fpath.split("docs/")[1]}-->\n(IN = {idx}, modified = {state})")
    for fpath in all_md_files:
        with open(fpath, "r") as f:
            content = f.read()

        # Match time already found in docs file
        if m := re.search(r"\s*_Latest\s*(Page|Website)\s*Update:\s*\d+-\d+-\d+_\s*", content, re.IGNORECASE):

            # Split file wrt. head
            head, content = content[:m.end()], content[m.end():]
            
            # Refactor head to new date and write to file
            cond = fpath in file_set
            head = get_out_string(fpath, time, head=head, cond=cond)
            decision_log(fpath, 1, cond)

        else: # Write to file, as no time is specified
            head = get_out_string(fpath, time) # Page|Website
            decision_log(fpath, 2, True)

        # Write to file
        with open(fpath, "w") as f:
            f.write(head + content)

if __name__ == "__main__":
    append_md_updates(sys.argv[1:])
