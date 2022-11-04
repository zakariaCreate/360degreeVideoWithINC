const http = require("http");
const fs = require("fs");
var url = require('url');
// const hostname = 'localhost';
const hostname = '10.0.1.1';
const port = 3000;
// 1) encode the ply file to draco
// 2) send the drc file to join_server.js

const server = http.createServer(function(req, res) {
    let hologram = req.url.split('/')[1]; //getting the hologram id. example : [/,hologram0.ply]
    let id = hologram.split("."); // [hologram0,.ply]
    let command = " ";
    command = "./NFV-SDN-Holograms/draco/build_dir/draco_encoder -point_cloud -i ./holograms/"+hologram+" -o ./encoderOut/"+id[0]+".drc -qp 15";
    const { exec } = require('child_process');

    exec(command, (error, stdout, stderr) => {
      if (error) {
        console.error(`error: ${error.message}`);
        return;
      }

      if (stderr) {
        console.error(`stderr: ${stderr}`);
        return;
      }

      console.log("Done Encoding!");
      let file = "./encoderOut/"+id[0]+".drc";
      if(fs.existsSync(file)){
        console.log(id[0]+".drc file exist.");}
      else{
        console.log(id[0]+".drc file doesn't exist.");
      }
      fs.readFile(file, function(err, content) {
          if (err) {
            console.log("Error Occoured.");
            res.end();
          }
          else {
            res.end(content);
            console.log("The encoded "+ id[0] +".drc has been sent.");
          }
      });
      console.log(`stdout:\n${stdout}`);
    });

    // version without the encoder
    // let file = "./encoderOut/"+id[0]+".drc";
    // if(fs.existsSync(file)){
    //    console.log(id[0]+".drc file exist.");}
    //  else{
    //    console.log(id[0]+".drc file doesn't exist.");
    //  }
    // fs.readFile(file, function(err, content) {
    //     if (err) {
    //       console.log("Error Occoured.");
    //       res.end();
    //     }
    //     else {
    //       res.end(content);
    //       console.log("The encoded "+ id[0] +".drc has been sent.");
    //     }
    // });
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
