const http = require('http');
const fs = require('fs');
var glob = require('glob');

var url = "http://localhost:3000"

glob("/home/p4/HologramStream/holograms/*",function(err,files){
  if (err) {
    res.write("No more file" );
    res.end();
  }
  else{
    get_hologram();
    function hologram_req(new_url,i){
      return new Promise(function(resolve,reject){
        http.get(new_url,function(res){
          const fileStream = fs.createWriteStream("Client_holograms"+i+".ply");
          res.pipe(fileStream);
          fileStream.on("finish",function(){
            resolve(fileStream.close());
            reject(new Error('Error occoured!!'));
            console.log('Hologram-'+i+' has been downloaded.');
          });
        });
      });
    }
    async function get_hologram(){
        for(let i =0; i< files.length; i++){
          let hologram = files[i].split('holograms/')[1];
          let new_url = url+"/"+hologram;
          await hologram_req(new_url,i);}
      }
  }
});
