# Hologram Streaming + loading on browser + BW monitoring

## How to run this ?
0. Download the VM from here : https://github.com/jafingerhut/p4-guide/blob/master/bin/README-install-troubleshooting.md
1. Clone this repository.
2. Go to NFV-SDN-Holograms folder and clone draco + three.js (rename three.js to three)
3. adapt the code of the following files :
  - /home/p4/tutorials/utils/run_exercise.py
  - /home/p4/tutorials/utils/Makefile
<br />in a similar way it was done in ./useful_files/run_exercise_01-07-2022_p4VM.py and ./useful_files/Makefile_01-07-2022_p4VM resp.
<br />Note :
  - in ./useful_files/run_exercise_01-07-2022_p4VM.py check the code between the comment : "new code starts here" and the comment "the new code ends here"
  - in ./useful_files/Makefile_01-07-2022_p4VM we only add this flag --emit-externs
4. go back to this Folder and run ./run.sh to launch the simulation
5. use ./cleanRepo.sh to delete all drc ply and logs files
6. to change the simulation behavior u need to change /home/p4/tutorials/utils/run_exercise.py
7. to change the extern written in c++ change here /home/vagrant/behavioral-model/targets/simple_switch_grpc/switch_runner.cpp and rebuild the switches by running ./buildSwitches.sh inside useful_files folder
<br />check the files :
  - ./useful_files/switch_runner_with_extern_08-09-2021_p4VM.cpp
  - ./p4CodeWithExtern_examples/basic_with_extern_call.p4
