#!/bin/bash

cd /home/vagrant/behavioral-model
echo -e '\n\n* we are here : *\n\n'
pwd
echo -e '\n\n'
sleep 0.5
./autogen.sh
./configure

echo -e '\n\n* we are here : *\n\n'
pwd
echo -e '\n\n'

sleep 0.5

make && sudo make install && sudo ldconfig \
&& cd targets/simple_switch_grpc \
&& echo -e '\n\n* we are here : *\n\n' \
&& pwd \
&& echo -e '\n\n' \
&& sleep 0.5 \
&& make && sudo make install && sudo ldconfig \
&& cd ../.. \
&& echo -e '\n\n* we are here : *\n\n' \
&& pwd \
&& echo -e '\n\n' ;
