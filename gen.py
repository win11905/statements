import sys
import os

if len(sys.argv) != 2:
    print("please enter argv")
    exit(0)

name = sys.argv[1]

os.chdir('./statements/latex')

if os.path.exists('{}.tex'.format(name)):
    os.system('xelatex -interaction nonstopmode {}.tex'.format(name))

if os.path.exists('{}.aux'.format(name)):
    os.remove('{}.aux'.format(name))
if os.path.exists('{}.fls'.format(name)):
    os.remove('{}.fls'.format(name))
if os.path.exists('{}.log'.format(name)):
    os.remove('{}.log'.format(name))
if os.path.exists('{}.out'.format(name)):
    os.remove('{}.out'.format(name))
if os.path.exists('{}.fdb_latexmk'.format(name)):
    os.remove('{}.fdb_latexmk'.format(name))
if os.path.exists('__latexindent_temp.tex'):
    os.remove('__latexindent_temp.tex')
if os.path.exists('{}.synctex.gz'.format(name)):
    os.remove('{}.synctex.gz'.format(name))

if os.path.exists('{}.pdf'.format(name)):
    os.replace('{}.pdf'.format(name), '../pdf/{}.pdf'.format(name))
else:
    print("Failed to generate pdf")