var exec = require('child_process').exec; 
var cmdStr = 'ipconfig';
exec(cmdStr, function(err,stdout,stderr){
    if(err) {
        console.log('get weather api error:'+stderr);
    } else {
        console.log(stdout);
    }
});