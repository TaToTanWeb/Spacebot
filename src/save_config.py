import os, requests, json

def save_config(app, data):
	# checking token validity by performing a "getMe"
	url = app.url.format(data.token, 'getMe')
	info = json.loads(requests.get(url).content)

	if info['ok']:
		# updating the database with the given data
		del data.patterns[''] # the last <input /> is always blank, so remove it
		app.config.put({'token': data.token, 'patterns': data.patterns}, key = str(info['result']['id']))

		# setting the webhook
		PROG_URL = os.getenv("DETA_SPACE_APP_HOSTNAME")
		set_url = app.url.format(data.token, f"setWebHook?url=https://{PROG_URL}/update/{info['result']['id']}")
		print(requests.get(set_url).content)
		return {'ok': True}
	else: return {'ok': False, 'reason': 'Invalid token.'}