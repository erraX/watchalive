var exec = require('child_process').exec,
    child;

child = exec('cd ../spider/watchalive && scrapy crawl douyu',
  function (error, stdout, stderr) {
    console.log('stdout: ' + stdout);
    console.log('stderr: ' + stderr);
    if (error !== null) {
      console.log('exec error: ' + error);
    }
});
