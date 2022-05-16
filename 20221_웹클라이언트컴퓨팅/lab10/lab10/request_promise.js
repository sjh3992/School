let request = require('request')
let fs = require('fs');

console.log(__dirname);

const work1 = () => new Promise(resolve => request('http://www.naver.com', (err, res, body) => resolve(body)));
const work2 = (body) => new Promise(resolve => fs.writeFile(__dirname + "/result/naver_page.html", body, (err) => resolve(err)));
const work3 = (err) => new Promise(resolve => resolve(err ? 'error occurred: ' + err : 'The file(naver_page.html) was saved!'));
const urgenWork = () => console.log('긴급 작업');

work1()
  .then((body) => {console.log('naver page requested: '); return work2(body); })
  .then(err => {console.log('page file saved: '); return work3(err); })
  .then(res => {console.log(res); });
urgenWork();