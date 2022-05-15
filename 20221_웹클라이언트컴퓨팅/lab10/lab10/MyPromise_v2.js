function MyPromise(fn) {
//    this.status = undefined;
//    this.result = undefined;
//    this.onDone = undefined;
//    this.nextProm = undefined;
    this.cb = () => 0;
    this.resolve = (res) => {
        this.status = 'done';
        this.result = res;
        if(this.nextProm) {
            let innerProm = this.onDone(this.result);
            if(!(innerProm && innerProm.constructor && innerProm.constructor.name == 'MyPromise')) 
                innerProm = new MyPromise((resolve) => resolve(innerProm)); 
            innerProm.onDone = this.nextProm.onDone;
            innerProm.nextProm = this.nextProm.nextProm;
            while(innerProm.status == 'done' && innerProm.nextProm) {
                let n = innerProm.onDone(innerProm.result);
                if(!(n && n.constructor && n.constructor.name == 'MyPromise')) 
                    n = new MyPromise((resolve) => resolve(n)); 
                n.nextProm = innerProm.nextProm.nextProm;
                n.onDone = innerProm.nextProm.onDone;
                innerProm = n;
            }
        }
    }
    this.presolve = (res) => {
        this.presult = [...this.presult, res];
        if(++this.index == this.psize) this.resolve(this.presult);
        else this.pArray[this.index].then(res => this.presolve(res));
    }
    if(Array.isArray(fn)) {
        this.pArray = fn;
        this.psize = fn.length;
        this.index = 0;
        this.presult = [];
        this.pArray[this.index].then(res => this.presolve(res));
    }
    else fn(this.resolve);  //setTimeout(() => fn(this.resolve), 1);
}
MyPromise.prototype.then = function(onDone) {
    this.onDone = onDone;
    if(this.status == 'done') {
        let ret = this.onDone(this.result);
        return (ret && ret.constructor && ret.constructor.name == 'MyPromise') ?
                   ret : new MyPromise((resolve) => resolve(ret));
    }
    this.nextProm = new MyPromise(this.cb);
    return this.nextProm;
}
MyPromise.prototype.state = function() {
    const state = {
        status: this.status,
        result: this.result
    };
    return state;
}

module.exports = MyPromise;