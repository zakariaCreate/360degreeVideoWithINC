// Server for Decoding with draco_decoder
const fs = require('fs');
const http = require('http');
var url = require('url');
const host = 'localhost'; //10.0.1.1 10.0.2.2
const port = 45333;

const server = http.createServer(function (req,res){
  send_decoded_hologram();
  async function send_decoded_hologram(){
    res.setHeader("Access-Control-Allow-Origin", "*"); //added to resolve "No 'Access-Control-Allow-Origin' " error
    let address = url.parse(req.url,true); //localhost:8080/0.ply
    var Url = address.href;
    // console.log(Url); // /0.ply
    var fileNum = Url.split("/")[1];  // [/,0.ply]
    fileNum = fileNum.split(".")[0]; // [0,ply]
    await get_encoded_hologram(fileNum); //0
    id = fileNum
    const { exec } = require('child_process');
    let path = "./decoded/hologram"+id+".ply";
    command = "./draco/build_dir/draco_decoder -i ./encoded/hologram"+id+".drc  -o ./decoded/hologram"+id+".ply";
    // subExec.exec(command);
    exec(command, (error, stdout, stderr) => {
      if (error) {
        console.error(`error: ${error.message}`);
        return;
      }

      if (stderr) {
        console.error(`stderr: ${stderr}`);
        return;
      }
      res.end(path);
      console.log(`stdout:\n${stdout}`);
    });

}
});
  // Listen to port 8080
server.listen(port, host, () => {
    console.log(`Server is running on http:${host}:${port}`);
});



// get_encoded_hologram(id) function will send req to Server_Encoder for drc file
function get_encoded_hologram(id){ //0
  new_url = "http://10.0.1.1:3000"+"/hologram"+id+".ply";
  return new Promise(function(resolve,reject){
    http.get(new_url,function(response){ // sending the request to Server_Encoder.js for getting the drc file
      const fileStream = fs.createWriteStream("./encoded/hologram"+id+".drc"); // hologram0.drc ///todo
      response.pipe(fileStream);
      fileStream.on("finish",function(){
        resolve(fileStream.close());
        reject(new Error('Error occoured!!'));
        console.log('Encoded hologram'+id+'.drc has been downloaded.');
        let path = "./encoded/hologram"+id+".drc";
        if (fs.existsSync(path)){
          console.log("Downloaded hologram"+id+".drc file exist.");
        }
        else {
          res.writeHead(404);}
      });
    });
  });
}
