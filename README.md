# handy_scripts_py

handy python scripts to use in bash

## how it works

### add bash files to path

bash files are the ones ending with **.sh** or with no extensions in this repository.

place them in a dir you want them to use for system path (`$PATH`)

> lets call it **path_dir**

add **path_dir** to `$PATH` by adding below code to end of `.bashrc` file:

`export PATH="path_dir:$PATH"`

> replace `path_dir` with your **path_dir**

### add module dir to bash files

make a dir for your modules.

> call path to each module as **module_path**

for each bash file add the correct path for execution

for example:

for line : `python3 "module_path" "$@"`

> replace `module_path` with **module_path**

### give access to execute

for each bash file you want to execute do this:

> call each file **file**

\$`chmod +x file`

### final note

now restart terminal and enjoy!
