# 360 degree Video streaming + network load monitoring

## How to run this ?
0. Edit and not overwrite the files you have inside your VM by the files you have inside useful_files folder
1. Edit the Makefile located next to run_exercise.py by adding the flag --emit-externs to $(P4C)
2. Install all the modules needed by the python programs, check files *.log for errors
3. Rebuild the switch by running the build_switches.sh script (you may need to run it as sudo)
4. Execute ./run.sh
