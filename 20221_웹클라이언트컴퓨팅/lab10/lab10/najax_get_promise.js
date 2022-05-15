let najax = $ = require('najax');
let fs=require('fs');


const work1 = () => new Promise(resolve => $.get('https://www.google.com', (res) => resolve(res)));
const work2 = (res) => new Promise(resolve => fs.writeFile(__dirname+"/result/google_page.html", res, (err) => resolve(err)));
const work3 = (err) => new Promise(resolve => resolve(err ? 'error occurred: ' + err : 'file created'));
const urgentWork = () => console.log('긴급 작업');

work1()
  .then(res => {console.log('google page received:'); return work2(res); })
  .then(err => {console.log('page file saved:'); return work3(err); })
  .then(res => {console.log(res); });
urgentWork();
