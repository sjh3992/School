let request = require('request')
let fs = require('fs');
const { resolve } = require('path');

console.log(__dirname);

const work1 = () => new Promise(resolve => resolve(request('http://www.naver.com')));
const work2 = (err, res, body) => new Promise(resolve => fs.writeFile(__dirname | "/result/naver_page.html"), (body) => resolve(body));
const work3 = (err) => new Promise(resolve => resolve(err ? err : 'The file(naver_page.html) was saved!'));
const urgenWork = () => console.log('긴급 작업');

work1()
  .then((err, res, body) => {console.log('naver page requested: '); return work2(err, res, body); })
  .then(err => {console.log('page file saved: '); return work3(err); })
  .then(res => {console.log(res); });
urgenWork();