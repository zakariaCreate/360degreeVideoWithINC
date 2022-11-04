import * as THREE from 'three';
import Stats from 'three/addons/libs/stats.module.js';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { PLYLoader } from 'three/addons/loaders/PLYLoader.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

let container, stats;
let camera, scene, renderer;

init();
animate();

function init() {

    container = document.createElement( 'div' );
    document.body.appendChild( container );

    // Creating Scene

    scene = new THREE.Scene();
    scene.background = new THREE.Color( 0xa0a0a0 );
    scene.fog = new THREE.Fog( 0xa0a0a0, 10, 50 );


    // Creating Ground

    const mesh = new THREE.Mesh( new THREE.PlaneGeometry( 200, 200 ), new THREE.MeshPhongMaterial( { color: 0x999999, depthWrite: false } ) );
    mesh.rotation.x = - Math.PI / 2;
    scene.add( mesh );

    // Creating Lights

    const hemiLight = new THREE.HemisphereLight( 0xffffff, 0x444444 );
    hemiLight.position.set( 0, 20, 0 );
    scene.add( hemiLight );

    // Creating renderer

    renderer = new THREE.WebGLRenderer( { antialias: true } );
    renderer.setPixelRatio( window.devicePixelRatio );
    renderer.setSize( window.innerWidth, window.innerHeight );
    renderer.outputEncoding = THREE.sRGBEncoding;
    renderer.shadowMap.enabled = true;
    container.appendChild( renderer.domElement );
    //container.appendChild( renderer.domElement );

    // Creating Camera

    camera = new THREE.PerspectiveCamera( 45, window.innerWidth / window.innerHeight, 1, 100 );
    camera.position.set( 1,1, 3 );6

    const controls = new OrbitControls( camera, renderer.domElement );
    controls.enableZoom = true;
    controls.target.set( 0, 0, 0 );
    controls.update();

    // Creating Stats

    stats = new Stats();
    container.appendChild( stats.dom );

    // resize

    window.addEventListener( 'resize', onWindowResize );

    // Creating PLYLoader file

    const loader = new PLYLoader();

    // Loading files

    loadLoop(loader,scene);

}

//This function will create the file directory for using in loader
// and the url address for sending request for decoding
async function loadLoop(loader,scene){
    let decode_url = "";

    for(let i=1051; i<1351; i++){
            let num_i = i.toString();
            let filename = "";
            decode_url = "";
            //file directory address
            filename = filename.concat("/decoded/",num_i,".ply");
            //url address for decoding request sending to server
            decode_url = decode_url.concat("http://localhost:8080/",num_i,".drc");

            //check if the decoded file exist in folder or not:
            // if yes, pass the file directory, loader and scene to the loader function
            // if no, loop until the file be created in the folder
            // await will use to make the process synchronous
           /* while(true){
                if(await resolveWait(decode_url)){
                    streamHologram(filename,loader,scene);
                    break;
                }
                else{
                    continue;
                }
            }*/
            await resolveWait(decode_url);
            streamHologram(filename,loader,scene);
        }
}

// This function will send request to the server for decoding targeted file
// the promise will use to make the process synchronous


function resolveWait(url){
	return new Promise(function(resolve,reject){
	  var oXHR = new XMLHttpRequest();

	  oXHR.open("GET", url, true);
	  oXHR.onreadystatechange = function (oEvent) {
	      if (oXHR.readyState === 4) {
		  if (oXHR.status === 200) {
		     //console.log(oXHR.responseText) //typed 200 for each file
		     console.log("we receiveed a request");
		     resolve(1);
		  } else {
		     reject(new Error('Error occoured!! from reject function'));
		     console.log("Error", oXHR.statusText);
		  }
	      }
	  };
	oXHR.send(null);
	});
}



// This function will load the ply files in the Chrome browser
function streamHologram (file, loader, scene){

    loader.load( file, function ( geometry ) {

        geometry.computeVertexNormals();

        const material = new THREE.PointsMaterial( { size: 0.01, vertexColors: true } );
        const mesh = new THREE.Points( geometry, material );

        mesh.position.x =  0;
        mesh.position.y =  0;
        mesh.position.z =  0;
        mesh.scale.multiplyScalar( 0.0006 );
	scene.remove(mesh);/*new line*/
        scene.add( mesh );
       /* setTimeout(function(){
            scene.remove(mesh);
        },700);*/

    });
}


function onWindowResize() {

    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();

    renderer.setSize( window.innerWidth, window.innerHeight );

}

function animate() {

    render();
    stats.update();
    requestAnimationFrame( animate );

}

function render() {

    renderer.render( scene, camera );

}
