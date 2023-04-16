import requests, json


async def handle_update(app, request, bot_id):
	# getting telegram update in JSON
	update = await request.json()
	print(update)

	if 'message' in update:
		text = update['message']['text']
		chat = update['message']['chat']['id']
		# retrieving the stored configuration for the bot
		config = app.config.get(bot_id)

		if text in config['patterns']:
			# match! respond with the corresponding text.
			url = app.url.format(config['token'], f'sendMessage?chat_id={chat}&text={config["patterns"][text]}')
			requests.get(url)