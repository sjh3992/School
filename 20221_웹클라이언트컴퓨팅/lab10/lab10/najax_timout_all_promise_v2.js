let najax = $ = require('najax');
let fs=require('fs');
const MyPromise = require("./MyPromise_v2");


const workt1 = () => new MyPromise(resolve => setTimeout(() => resolve('작업1 완료!'),1000));
const workt2 = () => new MyPromise(resolve => setTimeout(() => resolve('작업2 완료!'),2000));
const workt3 = () => new MyPromise(resolve => setTimeout(() => resolve('작업3 완료!'),3000));

const workg1 = () => new MyPromise(resolve => $.get('https://www.google.com', (res) => resolve(res)));
const workg2 = (res) => new MyPromise(resolve => fs.writeFile(__dirname+"/result/google_page.html", res, (err) => resolve(err)));
const workg3 = (err) => new MyPromise(resolve => resolve(err ? 'error occurred: ' + err : 'google page file created'));

const workAll1 =() => new MyPromise([workg1(), workt1()]);
const workAll2 =(res) => new MyPromise([workg2(res[0]), workt2()]);
const workAll3 =(err) => new MyPromise([workg3(err[0]), workt3()]);

const urgentWork = () => console.log('긴급 작업');

workAll1()
  .then(res => {console.log('google page received: ' + res[1]); return workAll2(res); })
  .then(err => {console.log('google page files saved: ' + err[1]); return workAll3(err); })
  .then(res => {console.log(res); });

urgentWork();
