# NFV-SDN-Holograms

**For Client side - WebXR Webpage**<br />
1) Clone this project
2) Clone three.js repository from [three.js github](https://github.com/mrdoob/three.js/) and put it in the same directory of "PLY-hologram.html" code.
3) Download dataset of [PLY files](http://plenodb.jpeg.org/pc/8ilabs/). Then copy just "Ply" folder and Paset it in the same directory of "PLY-hologram.html" code.
4) Clone [draco repository](https://github.com/google/draco) and build it inside the NFV-SDN-Hologram project folder.
5) Run WebServer.js in one terminal
6) Run Server.js in another terminal
7) In the chrome browser type "localhost:3000/PLY-hologram.html" to run the program.

**Inside NFV-SDN-Holograms folder you should have:**
* three (cloned from three.js github)<br />
* draco (cloned from draco github)<br />
* PLY-hologram.html<br />
* PlyScript.js<br />
* Server.js<br />
* WebServer.js<br />
* Run.sh<br />
* Bash.sh<br />
* main.css<br /><br />

**In one terminal run the WebServer.js to serve the webpage and in another terminal run the Server.js to decode the requested files**
**Then in a Chrome browser type "localhost:3000/PLY-hologram.html"**

**For Encoding and Decoding**<br />
First you need to clone [draco repository](https://github.com/google/draco) and build it inside the NFV-SDN-Hologram project folder.
The "PLY-holograms.html" file will send a request to port:8080 to decode the targeted files before loading and then read the decoded files from "decoded" folder, 
render and show in the Chrome browser.

