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


"""
Goal of this file: only a single solution type in markdown. 
"""
GENERIC_SOLUTION_RE = re.compile(
    r'#<START_SOLUTION\s+(\d+)>\s*'
    r'(.*?)'
    r'#<END_SOLUTION\s+\1>',
    re.DOTALL
)
# GENERIC_SOLUTION_RE = re.compile(
#     r'#<START_SOLUTION\s+(\d+)>\s*'
#     r'([\s\S]*?)'
#     r'#<END_SOLUTION\s+\1>',
#     re.DOTALL
# )




"""
Match markdown pattern of type: 
<!-- START_SOLUTION 1 -->
<!-- END_SOLUTION 1 -->
"""

#can we do in markdown so we dont need to write answer number but just get next one in sequence 
MD_BLOCK_RE = re.compile(
    r'<!-- START_SOLUTION\s+(\d+)\s*-->'
    r'(.*?)'
    r'<!-- END_SOLUTION\s+\1\s*-->',
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

def detect_file_solution(content: str):
    """Checks whether first character of each line is a !, which indicates file solution
    Args:
        content (str): a multiline string
    """
    #print("Receive content: ", content)
    x = content.split("\n")
    #print(x)
    x = [l[0] for l in x if len(l)>0] #remove empty spaces
    output = [True if l=="!" else False for l in x]
    
    return output

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

                #print(type(cell["source"])) #this fucker is a list
                #print(cell["source"][0])
                #text += "".join(cell["source"]) + "\n"  #this is somehow per line, we need it per block
                code = "".join(cell["source"]).rstrip()
                #print(code)

                text += "```py\n" + code +"\n```"#code[:index] + "\n```" + code[index:]
            elif cell["cell_type"] == "markdown":
                text += "".join(cell["source"]) + "\n"
    else:#.py
        text = file.read_text()

    solutions = {}
    #for sol_type, num_str, content in GENERIC_SOLUTION_RE.findall(text):
    for num_str, content in GENERIC_SOLUTION_RE.findall(text):
        num = int(num_str)
        #print(f"NARKO: {NARKO},{type(NARKO)}")
        #print(num_str,content)
        # Handle FILE_SOLUTION
        content_check = detect_file_solution(content)
        if True in content_check: #case: file solution.. not robust.. can not handle mixed types, im not smart enough for that
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
            
            solutions[num] = f"#Run from jupyter by executing solution file {inner} in a code block\n#The solution files contains:\n{content}"  # treat as normal solution
            continue
        # Store SOLUTION or FILE_SOLUTION normally
        solutions[num] = content.rstrip()
    #print(solutions)


    return solutions

def check_fence_strict(sol_content):
    parts = sol_content.split("```")
    #if len(parts) < 3:
    #    return False, len(parts)  # Doesn't even have a full block
    #print(parts)
    # Check if the content immediately following the first fence 
    # starts with 'py' or 'python'
    if len(parts)<3:
        return False, False
    tag_area = parts[1].strip().lower()
    contains_start_tag = (tag_area.startswith("py") or tag_area.startswith("python"))
    if len(parts)==3:
        return contains_start_tag, True 
    else:
        contains_start_tag, False
#    return not (tag_area.startswith("py") or tag_area.startswith("python")), len(parts)

def inject_into_markdown(md_file: Path, solutions: dict, output_dir: str):
    md = md_file.read_text()
    # def repl(match):
    #     num_str, _ = match.groups()
    #     key = int(num_str)

    #     if key not in solutions:
    #         return match.group(0)  # leave untouched

    #     sol_content = solutions[key]
    #     # injected = (
    #     #         f"<!-- START_SOLUTION {num_str} -->\n"
    #     #         f"??? tip \"Solution\"\n"
    #     #         f"    ```\n"
    #     #         f"{indent(sol_content, '    ')}\n"
    #     #         f"    ```\n"
    #     #         f"<!-- END_SOLUTION {num_str} -->"
    #     #     )
    #     injected = (
    #     f"<!-- START_SOLUTION {num_str} -->\n"
    #     f"??? tip \"Solution\"\n"
    #     f"{indent(sol_content, '    ')}\n"
    #     f"<!-- END_SOLUTION {num_str} -->"
    #     )
    #     return injected

    def repl(match):
        num_str, _ = match.groups()
        key = int(num_str)

        if key not in solutions:
            return match.group(0)

        sol_content = solutions[key]


        """
        # Check if solution already contains code fences
        has_fence = "```" in sol_content
        is_code_type = "```py" in sol_content
        
        # #has_end_fence_only = has_fence and not has_start_fence
        # has_end_fence = "```" in sol_content and "```py" not in sol_content
        # has_both_fences = has_start_fence==True and has_end_fence_only==False and has_fence==True
        # if "mixed" in sol_content:
        #     print(sol_content)
        #     print(has_fence)
        #     print(has_start_fence)
        #     print(has_end_fence_only)
        #     print(has_both_fences)
        #     print(list(re.findall("```",sol_content)))
        #     print("output_ ",check_fence_strict(sol_content))
        if is_code_type:
            has_begin_fence, has_end_fence = check_fence_strict(sol_content)
            
            if has_begin_fence and has_end_fence:
                # Do NOT wrap again — indent as-is
                #indented = indent(sol_content.rstrip(), "    ")
                sol_content = sol_content.rstrip()
            elif has_begin_fence and not has_end_fence: #case: end tags in code block will loose braces
                # Wrap in ``` and indent
                #indented = indent(sol_content.rstrip(), "        ") + "\n    ```"
                sol_content = sol_content.rstrip() + "\n```"
            elif has_end_fence and not has_begin_fence: 
                sol_content = "```py\n"+sol_content.rstrip()
            elif not has_begin_fence and not has_end_fence:
                #indented = "    ```py\n" + indent(sol_content.rstrip(), "        ") + "\n    ```"
                sol_content = "```py\n" + sol_content.rstrip() + "\n```"

        indented = indent(sol_content.rstrip(), "    ")

        injected = (
            f"<!-- START_SOLUTION {num_str} -->\n"
            f"??? tip \"Solution\"\n"
            f"{indented}\n"
            f"<!-- END_SOLUTION {num_str} -->"
        )

        return injected
        """

        has_fence = "```" in sol_content
        has_start_fence = "```py" in sol_content 
        has_end_fence_only = "```" in sol_content and "```py" not in sol_content

        has_both_fences = has_start_fence==True and has_end_fence_only==False and has_fence==True
        

        if "mixed" in sol_content:
            print(sol_content)
            print(has_fence)
            print(has_start_fence)
            print(has_end_fence_only)
            print(has_both_fences)
            print(list(re.findall("```",sol_content)))
            print("output_ ",check_fence_strict(sol_content))
            #has_begin_fence, has_end_fence = check_fence_strict(sol_content)
            
        if has_both_fences:
            # Do NOT wrap again — indent as-is
            #indented = indent(sol_content.rstrip(), "    ")
            sol_content = sol_content.rstrip()
        elif has_start_fence and not has_end_fence_only: #case: end tags in code block will loose braces
            # Wrap in ``` and indent
            #indented = indent(sol_content.rstrip(), "        ") + "\n    ```"
            sol_content = sol_content.rstrip() + "\n```"
        elif has_end_fence_only: 
            sol_content = "```py\n"+sol_content.rstrip()
        else:
            #indented = "    ```py\n" + indent(sol_content.rstrip(), "        ") + "\n    ```"
            sol_content = "```py\n" + sol_content.rstrip() + "\n```"

        indented = indent(sol_content.rstrip(), "    ")

        injected = (
            f"<!-- START_SOLUTION {num_str} -->\n"
            f"??? tip \"Solution\"\n"
            f"{indented}\n"
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

