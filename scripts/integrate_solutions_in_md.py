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


"""
Match python pattern of type: 
#<START_SOLUTION 1>
#<END_SOLUTION 1>
"""
SOLUTION_RE = re.compile(
    r'#<START_(SOLUTION)\s+(\d+)>\s*(.*?)#<END_\1\s+\2>',
    re.DOTALL
)

"""
Match markdown pattern of type: 
<!-- START_<MATH>_SOLUTION 1 -->
<!-- END_<MATH>_SOLUTION 1 -->
"""
MD_BLOCK_RE = re.compile(
    r'<!-- START_(SOLUTION|MATH_SOLUTION)\s+(\d+)\s*-->'
    r'(.*?)'
    r'<!-- END_\1\s+\2\s*-->',
    re.DOTALL
)

def extract_solutions(py_file: Path):
    text = py_file.read_text()
    solutions = {}

    for sol_type, num, content in SOLUTION_RE.findall(text):
        key = (sol_type, int(num))
        solutions[key] = content.rstrip()
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

    DEBUG = False 
    out_folder_name = "complete"

    if DEBUG: 
        all_md_exc_files = glob('tests/RAW/**/*.md', recursive=True)
        complete_dir = f"tests/{out_folder_name}"
        print("!Running solution integrator in DEBUG setting...!")
    else:
        all_md_exc_files = glob('exercises/RAW/**/*.md', recursive=True)
        complete_dir = f"exercises/{out_folder_name}"
    os.makedirs(complete_dir, exist_ok=True)
    for md_file in all_md_exc_files:
        root_dir = md_file.rsplit("/",1)[0]
        py_file = f"{root_dir}/sol.py"
        solutions = extract_solutions(Path(py_file))
        
        dst_path = root_dir.replace("RAW",f"{out_folder_name}")
        os.makedirs(dst_path,exist_ok=True)
        print(f"Integrating {py_file} solutions into {dst_path}/{md_file}")
        inject_into_markdown(md_file=Path(md_file), solutions=solutions, output_dir=dst_path)
        shutil.copyfile(py_file, f"{dst_path}/sol.py")
        
    print(f"Finished integrating solutions from python scripts into markdown files. Output dir: {complete_dir}")
    print(f"Integrated {len(all_md_exc_files)} files.")



