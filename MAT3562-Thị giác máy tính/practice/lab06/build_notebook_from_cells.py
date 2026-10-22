# -*- coding: utf-8 -*-
"""
build_notebook_from_cells.py
Reads cells/*.md and cells/*.py, executes them, and writes lab06.ipynb
"""
import sys
import os
import io
import json
import base64
import time
import glob
import cv2
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

print("Starting build_notebook_from_cells.py...")

cell_files = sorted(glob.glob("cells/*"))
print(f"Found {len(cell_files)} cell files.")

notebook_cells = []
global_env = {}

code_exec_count = 0

for filepath in cell_files:
    filename = os.path.basename(filepath)
    is_code = filename.endswith(".py")
    is_md = filename.endswith(".md")
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = [l + '\n' for l in content.splitlines()]
    if lines:
        lines[-1] = lines[-1].rstrip('\n')
        
    if is_md:
        notebook_cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": lines
        })
        print(f"Added markdown cell: {filename}")
        
    elif is_code:
        code_exec_count += 1
        print(f"Executing code cell #{code_exec_count}: {filename} ...")
        
        old_stdout = sys.stdout
        stdout_buf = io.StringIO()
        sys.stdout = stdout_buf
        
        cell_outputs = []
        
        try:
            exec(content, global_env)
            
            # Capture figures
            fig_nums = plt.get_fignums()
            for fnum in fig_nums:
                fig = plt.figure(fnum)
                buf = io.BytesIO()
                fig.savefig(buf, format='png', bbox_inches='tight', dpi=100)
                buf.seek(0)
                b64_data = base64.b64encode(buf.read()).decode('utf-8')
                cell_outputs.append({
                    "output_type": "display_data",
                    "data": {
                        "image/png": b64_data,
                        "text/plain": ["<Figure size ...>"]
                    },
                    "metadata": {}
                })
                plt.close(fig)
                
        except Exception as e:
            import traceback
            traceback.print_exc(file=stdout_buf)
            print(f"ERROR executing {filename}: {e}", file=sys.stderr)
        finally:
            sys.stdout = old_stdout
            
        out_text = stdout_buf.getvalue()
        if out_text:
            cell_outputs.insert(0, {
                "output_type": "stream",
                "name": "stdout",
                "text": [l + '\n' for l in out_text.splitlines(keepends=True)]
            })
            
        notebook_cells.append({
            "cell_type": "code",
            "execution_count": code_exec_count,
            "metadata": {},
            "outputs": cell_outputs,
            "source": lines
        })
        print(f"  -> Finished {filename} with {len(cell_outputs)} outputs.")

# Construct final notebook dict
notebook_json = {
    "cells": notebook_cells,
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3 (ipykernel)",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.10.8"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 5
}

out_notebook = "lab06.ipynb"
with open(out_notebook, "w", encoding="utf-8") as f:
    json.dump(notebook_json, f, ensure_ascii=False, indent=2)

print("\n========================================================")
print(f"SUCCESS: Generated {out_notebook}")
print(f"Total cells: {len(notebook_cells)} ({code_exec_count} code cells)")
print(f"File size: {os.path.getsize(out_notebook) / 1024:.2f} KB")
print("========================================================")
