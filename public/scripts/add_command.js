function add_command() {
    // creates the necessary elements
    // and appends them to the DOM.
    const commandBox = document.createElement('div');
    const commandName = document.createElement('input');
    const commandResponse = document.createElement('textarea');
    const saveButton = document.getElementById('save-button');

    commandBox.classList.add('command-box');
    commandName.classList.add('command-name');
    commandResponse.classList.add('command-response');

    commandName.placeholder = '/command';
    commandResponse.placeholder = 'Type the message here..';

    commandName.oninput = check_input;
    commandResponse.oninput = check_input;

    commandBox.append(commandName, commandResponse);
    document.getElementsByTagName('commands-field')[0].append(commandBox);
    saveButton.style.display = 'inline';
}