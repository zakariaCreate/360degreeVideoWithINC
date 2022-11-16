#!/bin/bash

cd /home/vagrant/behavioral-model
./autogen.sh
./configure --enable-debugger --with-pi
make
# Only run the following two commands if there were no errors from the previous command:
sudo make install
sudo ldconfig
# Simple_switch_grpc target
cd targets/simple_switch_grpc
# ./autogen.sh
./configure --with-thrift
make
# Only run the following two commands if there were no errors from the previous command:
sudo make install
sudo ldconfig
