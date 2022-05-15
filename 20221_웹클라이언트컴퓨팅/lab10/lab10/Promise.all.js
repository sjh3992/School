const work = (data) => {
  return new Promise((resolve)=>resolve(data));
}

const single = work(3);
single.then((res)=>console.log(res));

const parallel = Promise.all([work(5),work(6)])
parallel.then((res)=>console.log(res));

//const parallel2 = new Promise([work(7),work(8)])
const parallel2 = Promise.all([work(7),work(8)]);
parallel2.then((res)=>console.log(res));