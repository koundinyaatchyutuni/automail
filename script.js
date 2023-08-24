var jsdom = require("jsdom");
var JSDOM = jsdom.JSDOM;
global.document = new JSDOM(html).window.document;
document.getElementById('upload-form').addEventListener('submit', function(event) {
    event.preventDefault();
    let formData = new FormData();
    formData.append('excel-file', document.getElementById('excel-file').files[0]);
    document.write("hello it is working");
    fetch('/process', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById('response').textContent = data;
    });
});
