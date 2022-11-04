const http = require("http");
const fs = require("fs");
var glob = require('glob');

const server = http.createServer(function(req, res) {
  let hologram = req.url.split('/')[1];
  glob("/home/p4/tutorials/exercises/HologramStreaming/holograms/*",function(err,files){
    if (err) {
      console.log("No more file");
      res.end();
    }
    else{
      for(let i =0;i<files.length;i++){
        if (hologram.match(files[i].split('holograms/')[1])){
          let file = __dirname +'/holograms/'+ hologram;
          fs.access(file, fs.constants.F_OK, err => {
            //check that we can access  the file
            console.log(`${file} ${err ? "does not exist" : "exists"}`);
          });

          fs.readFile(file, function(err, content) {
            if (err) {
              console.log("No such file.");
              res.end();
            } else {
              res.end(content);
              console.log('The hologram-'+ i +' has been sent.');
            }});

            break;
        }
      }
    }
  });
});
server.listen(3000, function() {
  console.log("Server running on port 3000");
});
