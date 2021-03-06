import sys
import os

if len(sys.argv) != 2:
    print("Please provide arguments")
    exit(0)

name = sys.argv[1]

os.chdir('./statements/latex')

if os.path.exists('{}.tex'.format(name)):
    os.system('xelatex -interaction=batchmode {}.tex'.format(name))


extension = ["{}.aux", "{}.fls", "{}.log",
             "{}.out", "{}.fdb_latexmk", "{}.synctex.gz"]

for ext in extension:
    if os.path.exists(ext.format(name)):
        os.remove(ext.format(name))

if os.path.exists('__latexindent_temp.tex'):
    os.remove('__latexindent_temp.tex')


if os.path.exists('{}.pdf'.format(name)):
    os.replace('{}.pdf'.format(name), '../pdf/{}.pdf'.format(name))
else:
    print("Failed to generate pdf")
