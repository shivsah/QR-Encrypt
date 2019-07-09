function generateQRCode() {
	var data = document.getElementById("data").value
	eel.generate_qr(data)
}
function get_Message(){
	var message = document.getElementById("message").value
	let n = await eel.get_message(message)(setImage)
	console.log("Got this from Python: "+n);
}
function setImage(base64) {
	document.getElementById("qr").src = base64
}
