var scrollableDiv = document.getElementById("chat-history");
window.onload = function() {
    scrollableDiv.scrollTop = scrollableDiv
        .scrollHeight;
        alert("Works")
}
// let divElement = document.getElementById('chat-history');
// divElement.scrollIntoView({ behavior: 'smooth', block: 'end' });