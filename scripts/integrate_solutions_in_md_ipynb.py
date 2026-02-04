"""
Script is part of workflow for automatically integrating python solution content into markdown files to form complete solution form.
No dependencies. 
Does NOT handle cron-jobbing. 
"""
import shutil
import os 
from glob import glob 
import re
from pathlib import Path
from textwrap import indent
import json 


"""
Match python pattern of type: 
#<START_SOLUTION 1>
#<END_SOLUTION 1>
"""
# SOLUTION_RE = re.compile(
#     r'#<START_(SOLUTION)\s+(\d+)>\s*(.*?)#<END_\1\s+\2>',
#     re.DOTALL
# )

# GENERIC_SOLUTION_RE = re.compile(
#     r'#<START_(SOLUTION|MATH_SOLUTION|FILE_SOLUTION)\s+(\d+)>\s*'
#     r'(.*?)'
#     r'#<END_\1\s+\2>',
#     re.DOTALL
# )

GENERIC_SOLUTION_RE = re.compile(
    r'#<START_(SOLUTION|MATH_SOLUTION|FILE_SOLUTION)\s+(\d+)>\s*'
    r'(.*?)'
    r'#<END_\1\s+\2>',
    re.DOTALL
)


"""
Match markdown pattern of type: 
<!-- START_<MATH>_SOLUTION 1 -->
<!-- END_<MATH>_SOLUTION 1 -->
"""

#can we do in markdown so we dont need to write answer number but just get next one in sequence 
MD_BLOCK_RE = re.compile(
    r'<!-- START_(SOLUTION|FILE_SOLUTION|MATH_SOLUTION)\s+(\d+)\s*-->'
    r'(.*?)'
    r'<!-- END_\1\s+\2\s*-->',
    re.DOTALL
)
# MD_BLOCK_RE = re.compile(
#     r'<!-- START_SOLUTION\s+(\d+)\s*-->'
#     r'(.*?)'
#     r'<!-- END_\1\s+\2\s*-->',
#     re.DOTALL
# )

# MD_BLOCK_RE = re.compile(
#     r'<!-- START_SOLUTION\s+(\d+)\s*-->'
#     r'(.*?)'
#     r'<!-- END_SOLUTION\s+\1\s*-->',
#     re.DOTALL
# )

def extract_solutions(file: Path):
    """
    Extract SOLUTION, MATH_SOLUTION, FILE_SOLUTION blocks
    from both .py and .ipynb files.
    """

    # Read .ipynb as combined text of code cells
    if file.suffix == ".ipynb":
        nb = json.loads(file.read_text())
        text = ""
        #md_text = ""
        for cell in nb["cells"]:
            if cell["cell_type"] == "code":
                text += "".join(cell["source"]) + "\n"
            #elif cell["cell_type"] == "markdown":
            #    text += "".join(cell["source"]) + "\n"
    else:#.py
        text = file.read_text()

    solutions = {}
    for sol_type, num_str, content in GENERIC_SOLUTION_RE.findall(text):
        num = int(num_str)

        # Handle FILE_SOLUTION
        if sol_type == "FILE_SOLUTION":
            # content looks like: "!Ex3-Ex18.py - we need directory relative to root"
            inner = content.strip()
            fname = inner.lstrip("!").strip().lstrip("python ")
            
            #sol_path = file.parent / fname
            sol_path = f"{str(file).rsplit("/",1)[0]}/{fname}"
            sol_path = Path(sol_path)
            if not sol_path.exists():
                raise FileNotFoundError(
                    f"Referenced file '{fname}' not found for FILE_SOLUTION {num} "
                    f"in {file}"
                )

            content = sol_path.read_text().rstrip()
            solutions[("SOLUTION", num)] = content  # treat as normal solution
            continue

        # Store SOLUTION or MATH_SOLUTION normally
        solutions[(sol_type, num)] = content.rstrip()
    print(solutions)


    return solutions

def inject_into_markdown(md_file: Path, solutions: dict, output_dir: str):
    md = md_file.read_text()
    def repl(match):
        sol_type, num_str, _ = match.groups()
        key = (sol_type, int(num_str))

        if key not in solutions:
            return match.group(0)  # leave untouched

        sol_content = solutions[key]
        

        if sol_type == "MATH_SOLUTION":
            injected = (
                f"<!-- START_MATH_SOLUTION {num_str} -->\n"
                f"??? tip \"Solution\"\n"
                f"{indent(sol_content, '    ')}\n"
                f"<!-- END_MATH_SOLUTION {num_str} -->"
            )

        else:  # normal code solution
            injected = (
                f"<!-- START_SOLUTION {num_str} -->\n"
                f"??? tip \"Solution\"\n"
                f"    ```\n"
                f"{indent(sol_content, '    ')}\n"
                f"    ```\n"
                f"<!-- END_SOLUTION {num_str} -->"
            )
        return injected

    #print(MD_BLOCK_RE.findall(md))
    new_md = MD_BLOCK_RE.sub(repl, md)
    #print(new_md)
    file_name = str(md_file).rsplit("/",1)[-1]
    out_file = Path(f"{output_dir}/{file_name}")
    with open(out_file, 'a+') as f:
        out_file.write_text(new_md)
    
   
def convert_list_to_string(li: list) -> str: 
    s = ""
    for i, s_ in enumerate(li): 
        s+=s_
        if i<len(li)-1:
            s+="/"
    return s 

if __name__=="__main__":

    DEBUG = True
    out_folder_name = "complete"

    if DEBUG: 
        all_md_exc_files = glob('tests/RAW/*/*.md', recursive=False)
        complete_dir = f"tests/{out_folder_name}"
        print("!Running solution integrator in DEBUG setting...!")
    else:
        all_md_exc_files = glob('exercises/RAW/*/*.md', recursive=False)
        complete_dir = f"exercises/{out_folder_name}"
    os.makedirs(complete_dir, exist_ok=True)
    for md_file in all_md_exc_files:

        root_dir = md_file.rsplit("/",1)[0]
        ipynb_file = glob(f"{root_dir}/*.ipynb")
        print("HELLO: ", root_dir)
        if len(ipynb_file)>1:
            print(f"Error. Multiple ipynb-files detected:\n {ipynb_file}\n Aborting")
            raise Exception("ISSUE") 
        print(ipynb_file)
        ipynb_file = ipynb_file[0]
        solutions = extract_solutions(Path(ipynb_file))
        
        dst_path = root_dir.replace("RAW",f"{out_folder_name}")
        os.makedirs(dst_path,exist_ok=True)
        print(f"Integrating {ipynb_file} solutions into {dst_path}/{md_file}")
        inject_into_markdown(md_file=Path(md_file), solutions=solutions, output_dir=dst_path)
        shutil.copyfile(ipynb_file, f"{dst_path}/sol.py")
        
    print(f"Finished integrating solutions from python scripts into markdown files. Output dir: {complete_dir}")
    print(f"Integrated {len(all_md_exc_files)} files.")

"""
PROBLEM: .md files present in data/.. Need to restrict the glob search depth.
MAYBE solved atm, double check tmrw
"""

