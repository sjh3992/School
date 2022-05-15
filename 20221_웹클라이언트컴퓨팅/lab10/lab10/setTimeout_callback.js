// ES5의 예제
function work1(onDone) {
  setTimeout(() => onDone('작업1 완료!'), 1000);
}
function work2(onDone) {
  setTimeout(() => onDone('작업2 완료!'), 2000);
}
function work3(onDone) {
  setTimeout(() => onDone('작업3 완료!'), 3000);
}
function urgentWork() {
  console.log('긴급 작업');
}

// 실제 비동기 함수를 사용하는 예
work1(function(msg1) {
  console.log('done after 1s:' + msg1);
  work2(function(msg2) {
    console.log('done after 3s:' + msg2);
    work3(function(msg3) {
      console.log('done after 6s:' + msg3);
    });
  });
});

urgentWork();
