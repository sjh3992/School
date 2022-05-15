const MyPromise = require("./MyPromise_v2");

const work1 = () => new MyPromise(resolve => setTimeout(() => resolve('작업1 완료!'),1000));
const work2 = () => new MyPromise(resolve => setTimeout(() => resolve('작업2 완료!'),2000));
const work3 = () => new MyPromise(resolve => setTimeout(() => resolve('작업3 완료!'),3000));
 urgentWork = () => console.log('긴급 작업');

work1()
  .then(msg1 => {console.log('done after 1s:' + msg1); return work2(); })
  .then(msg2 => {console.log('done after 3s:' + msg2); return work3(); })
  .then(msg3 => console.log(`done after 6s:${msg3}`));
urgentWork();
