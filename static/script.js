$(document).ready(function() {
    $('#chat-form').on('submit', function(e) {
        e.preventDefault();
        const userInput = $('#user-input').val();
        if (userInput.trim() === '') return;

        // Add user message to chat
        addMessage('user', userInput);

        // Clear input field
        $('#user-input').val('');

        // Send request to server
        $.ajax({
            url: '/get',
            type: 'POST',
            data: { msg: userInput },
            success: function(response) {
                // Add bot response to chat
                addMessage('bot', response.response);
            },
            error: function() {
                addMessage('bot', 'Sorry, I encountered an error. Please try again.');
            }
        });
    });

    function addMessage(sender, message) {
        const messageHtml = `
            <div class="message ${sender}">
                ${sender === 'bot' ? '<img src="/static/bot-avatar.png" alt="Bot Avatar" class="avatar">' : ''}
                <p>${message}</p>
            </div>
        `;
        $('#chatBox').append(messageHtml);
        $('#chatBox').scrollTop($('#chatBox')[0].scrollHeight);
    }
});