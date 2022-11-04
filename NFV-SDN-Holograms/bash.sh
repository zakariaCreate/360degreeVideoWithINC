#!/bin/bash

cd draco/build_dir
counter=1051
#1350
while [ $counter -le 1350 ]
do
./draco_encoder -point_cloud -i ../../Ply/longdress_vox10_$counter.ply -o ../../encoderOut/$counter.drc
#./draco_decoder  -i ../../encoderOut/$counter.drc -o ../../decoded/$counter.ply
((counter++))
done

echo All 300 done!
