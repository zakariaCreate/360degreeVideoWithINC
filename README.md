# Hologram Streaming + loading on browser + BW monitoring

## How to run this ?

1. Clone this repository.
2. Go to NFV-SDN-Holograms folder and clone draco + three.js (rename three.js to three)
3. go to filesToOverride folder, and run ./copyFiles_from_here_to_my_VM.sh and after that run ./buildSwitches.sh to build the switch, you have just replaced its source code
4. go back to this Folder and run ./run.sh to launch the simulation
5. use ./cleanRepo.sh to delete all drc ply and logs files
6. to change the simulation behavior u need to change /run_exercise.py /home/p4/tutorials/utils/run_exercise.py (cntrl + f zakaria)
7. to change the extern written in c++ change here /home/vagrant/behavioral-model/targets/simple_switch_grpc/switch_runner.cpp and rebuild the switches by running ./buildSwitches.sh inside filesToOverride folder
