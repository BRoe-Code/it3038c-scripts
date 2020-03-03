process.stdout.write("Hello. What is your name? ")

process.stdin.on('data', function(data) {
	console.log("Hello " + data.toString())

});

process.on('exit', function() {
	console.log'Thsnks for the info!')
