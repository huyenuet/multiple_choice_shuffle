function shuffle_test() {
    var python = require("python-shell");
    var path = require("path");
    var file_input = document.getElementById("file_input").value;

    // document.getElementById("file_input").value = "";

    var options = {
        scriptPath: path.join(__dirname, '/engine/'),
        pythonPath: 'usr/local/bin/python3',
        args: [file_input],
    };

    var shuffled_file = new python('main.py', options);
    shuffled_file.end(function (err, code, message) {
        swal("hiii")
    })
}