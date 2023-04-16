function check_input(event) {
    if (event.target.classList.contains('command-name')) {
        // always include a leading slash and remove spaces
        event.target.value = (event.target.value[0] != '/' ? '/' : '') + event.target.value.replaceAll(' ', '');
    }

    // prepare for the next command input in case it's the last one
    if (event.target.parentNode == document.getElementsByTagName('commands-field')[0].lastChild) {
        add_command();
    }
}