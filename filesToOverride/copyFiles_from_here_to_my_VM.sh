cp ./Makefile /home/p4/tutorials/utils/Makefile
cp ./run_exercise.py /home/p4/tutorials/utils/run_exercise.py
cp ./switch_runner.cpp /home/vagrant/behavioral-model/targets/simple_switch_grpc/switch_runner.cpp

echo -e "\n**********************************"
echo "You need to rebuild the switches after changing this file :"
echo "/home/vagrant/behavioral-model/targets/simple_switch_grpc/switch_runner.cpp"
echo "To build the switche u need to run this : "
echo "./buildSwitches.sh"
echo -e "**********************************\n"
