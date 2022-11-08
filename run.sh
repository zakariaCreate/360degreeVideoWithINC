mkdir -p encoderOut
mkdir -p NFV-SDN-Holograms/decoded/
mkdir -p NFV-SDN-Holograms/encoded/
rm NFV-SDN-Holograms/decoded/*
rm NFV-SDN-Holograms/encoded/*
rm encoderOut/*
make stop
make run
