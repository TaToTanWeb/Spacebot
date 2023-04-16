function save_config() {
	// preparing the config data
	let config = {token: document.getElementById('token-input').value, patterns: {}}
	document.getElementsByTagName('commands-field')[0].childNodes.forEach((commandBox) => {
		let key = commandBox.firstChild.value;
		let value = commandBox.lastChild.value;
		config.patterns[key] = value;
	})


	// performing request
	fetch('/save', {
		method: 'POST', body: JSON.stringify(config),
		headers: {'Content-Type': 'application/json'}
	}).then(response => response.json())
	.then(result => {
		const banner = document.getElementById('notification-banner');
		if (result.ok) {
			// ok
			banner.textContent = 'Success!';
		} else {
			// not ok, displaying result.reason
			banner.textContent = 'Error: ' + result.reason;
		}

		banner.classList.add('show');
	});
}