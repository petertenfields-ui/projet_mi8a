const socket = new WebSocket(`ws://${window.location.host}/ws/visual`)

socket.onopen = () => {
    console.log("stuff1");
};

socket.onmessage = (event) =>{
    const audio = JSON.parse(event.data);
    // appeler la fonction pour dessiner
};

socket.onclose = () => {
    console.log("ferme");
};
// Pour garder le lien avec le browser ouvert (voir visualisation dans api/websocket.py)
setInterval(() => {
    if (socket.readyState === WebSocket.OPEN){
        socket.send('ping');
    }
}, 20000);

