document.addEventListener('DOMContentLoaded', function(){
    const marcoPoloMessage = document.querySelector('[name=marco_polo_input]');
    const marcoPoloButton = document.querySelector('[name=marco_polo_button]');
    const marcoPoloArrayMessage = document.querySelector('[name=marco_polo_array_input]');
    const marcoPoloArrayButton = document.querySelector('[name=marco_polo_array_button]');
    const marcoPoloRangeMessage = document.querySelector('[name=marco_polo_range_input]');
    const marcoPoloRangeButton = document.querySelector('[name=marco_polo_range_button]');
    var ws = new WebSocket("ws://localhost:2000");

    ws.onopen = () => {
        console.log("connected");
        marcoPoloButton.onclick = () => {
            ws.send("solo " + marcoPoloMessage.value);
        }
        marcoPoloArrayButton.onclick = () => {
            ws.send("array " + marcoPoloArrayMessage.value);
            }
        marcoPoloRangeButton.onclick = () => {
            ws.send("range " + marcoPoloRangeMessage.value);
            }

    }


}, false)