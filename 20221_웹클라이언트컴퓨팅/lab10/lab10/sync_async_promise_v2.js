const MyPromise = require("./MyPromise_v2");

const works1 = () => new MyPromise(resolve => resolve('동기 작업1 완료!'));
const works2 = () => new MyPromise(resolve => resolve('동기 작업2 완료!'));
const works3 = () => new MyPromise(resolve => resolve('동기 작업3 완료!'));
const works4 = () => new MyPromise(resolve => resolve('동기 작업4 완료!'));
const workt1 = () => new MyPromise(resolve => setTimeout(() => resolve('비동기 작업1 완료!'),1000));
const workt2 = () => new MyPromise(resolve => setTimeout(() => resolve('비동기 작업2 완료!'),2000));
const workt3 = () => new MyPromise(resolve => setTimeout(() => resolve('비동기 작업3 완료!'),3000))
urgentWork = () => console.log('긴급 작업');

let fProm = works1()
  .then(msg => {console.log(`done works4:${msg}`); return 'final0'; })
  .then(msg => {console.log('done works1:' + msg); return works2(); })
  .then(msg => {console.log('done works2:' + msg); return works3(); })
  .then(msg => {console.log(`done works3:${msg}`); return workt1(); })
  .then(msg => {console.log(`done workt1:${msg}`); return workt2(); })
  .then(msg => {console.log(`done workt2:${msg}`); return workt3(); })
  .then(msg => {console.log(`done workt3:${msg}`); return works4(); })
  .then(msg => {console.log(`done works4:${msg}`); return new MyPromise(resolve => resolve('final1')); })
  .then(msg => {console.log(`done works5:${msg}`); return 'final11'; })
urgentWork();

fProm
  .then(msg => {console.log('done fProm:' + msg); return works3(); })
  .then(msg => {console.log(`done works3:${msg}`); return workt1(); })
  .then(msg => {console.log(`done workt1:${msg}`); return workt2(); })
  .then(msg => {console.log(`done workt2:${msg}`); return workt3(); })
  .then(msg => {console.log(`done workt3:${msg}`); return works4(); })
  .then(msg => {console.log(`done works4:${msg}`); return new MyPromise(resolve => resolve('final2')); })
  .then(msg => console.log(`done all:${msg}`) );

