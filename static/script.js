// AI Assistant Functionality
document.getElementById('startChat').addEventListener('click', function() {
    document.getElementById('chatBox').style.display = 'block';
});



// Appointment Form Submission
document.getElementById('appointmentForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const doctor = document.getElementById('doctor').value;
    const date = document.getElementById('date').value;
    
    if (doctor && date) {
        alert(`Appointment booked with ${doctor} on ${date}`);
    }
});
