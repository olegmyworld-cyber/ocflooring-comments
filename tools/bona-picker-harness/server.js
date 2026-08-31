const http=require('http'),fs=require('fs'),path=require('path');
const dir=__dirname;
http.createServer((req,res)=>{
  const u=req.url.split('?')[0];
  let f=null,ct='text/html';
  if(u==='/bundle.js'){f=path.join(dir,'..','bona-pkg-loader-v3-min.js');ct='application/javascript';}
  else if(u==='/flooring-services-near-me/floor-refinishing')f=path.join(dir,'hub.html');
  else if(u==='/'||u==='/index'||u==='/home')f=path.join(dir,'home.html');
  else f=path.join(dir,'other.html');
  fs.readFile(f,(e,d)=>{if(e){res.writeHead(404);res.end('nf');}else{res.writeHead(200,{'content-type':ct});res.end(d);}});
}).listen(8471,()=>console.log('serving on 8471'));
