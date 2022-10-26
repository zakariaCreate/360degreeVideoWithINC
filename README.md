# Hologram Streaming

## Stream Holograms between two nodes

1. Clone HologramStreaming repository.
2. Inside that folder create a new folder name : "holograms".
3. Put all the holograms ".ply" files in that "holograms" folder.
Note : name of the holograms should start with "hologram" and followed by a digit starting from 0. (example : "hologram0.ply, hologram1.ply" and so on.)
4. Run Server.js in one terminal by typing : node Server command.
5. Run Client.js in onother terminal by typing : node Client command.
Note : write the required command to install glob before running the .js files.


## Streaming holograms inside the network between two hosts

1. In your terminal, run: make run
   This will:
   * compile `basic.p4`, and
   * start the topology in Mininet
   * it will configure all hosts and all switches with the appropriate P4 program, table entries.

2. To ping between hosts in the topology:
   run the following command:
   mininet> h1 ping h2
   mininet> h3 ping h4

3. To stream through the network:
   run the following command: (Stream from host-1 to host-2)
   mininet> xterm h1 h2
   Node : h1> node Server
   Node : h2> node Client
