#!/bin/bash

node WebServer.js &
node Server.js &
open -a "Google Chrome" http://localhost:3000/PLY-hologram.html
