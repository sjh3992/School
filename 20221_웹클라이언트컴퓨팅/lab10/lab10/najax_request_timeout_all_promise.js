let najax = $ = require('najax');
let request = require('request')
let fs=require('fs');

console.log(__dirname);

const workt1 = () => new Promise(resolve => setTimeout(() => resolve('작업1 완료!'),1000));
const workt2 = () => new Promise(resolve => setTimeout(() => resolve('작업2 완료!'),2000));
const workt3 = () => new Promise(resolve => setTimeout(() => resolve('작업3 완료!'),3000));

const workg1 = () => new Promise(resolve => $.get('https://www.google.com', (res) => resolve(res)));
const workg2 = (res) => new Promise(resolve => fs.writeFile(__dirname+"/result/google_page.html", res, (err) => resolve(err)));
const workg3 = (err) => new Promise(resolve => resolve(err ? 'error occurred: ' + err : 'google page file created'));

const work1 = () => new Promise(resolve => request('http://www.naver.com', (err, res, body) => resolve(body)));
const work2 = (body) => new Promise(resolve => fs.writeFile(__dirname + "/result/naver_page.html", body, (err) => resolve(err)));
const work3 = (err) => new Promise(resolve => resolve(err ? 'error occurred: ' + err : 'The file(naver_page.html) was saved!'));

const workAll1 = () => Promise.all([workg1(), workt1(), work1()]);
const workAll2 = (res) => Promise.all([workg2(res[0]), workt2(), work2(res[1])]);
const workAll3 = (err) => Promise.all([workg3(err[0]), workt3(), work3(err[1])]);

const urgentWork = () => console.log('긴급 작업');

workAll1()
  .then(res => {console.log('pages received: ' + res[1]); return workAll2(res); })
  .then(err => {console.log('page files saved: ' + err[1]); return workAll3(err); })
  .then(res => {console.log(res); });

urgentWork();
