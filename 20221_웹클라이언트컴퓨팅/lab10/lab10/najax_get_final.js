let najax = $ = require('najax');
let fs=require('fs');

let saveStatus = (err) => {
                       if(err) {
                           return console.log(err);
                       }
                       console.log("The file(google_page.html) was saved!");
};

let savePage = (response) => {
		   tableData = response;
                   //console.log(tableData);
                   fs.writeFile(__dirname+"/result/google_page.html", tableData, saveStatus);
};


function getData(callback) {
	var tableData;
	$.get('https://www.google.com', callback);
	return tableData;
}

// console.log(getData(savePage));
getData(savePage);
