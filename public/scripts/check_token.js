function check_token(input) {
    const API_URL = 'https://api.telegram.org/bot';

    // accessing some basic information about the bot
    fetch(`${API_URL}${input.value}/getMe`)
        .then(response => response.json())
        .then(data => {
            // data = {"ok": true, "result": {"id": 2002483655, "first_name": "<NAME>"}}
            if (data.ok) {
                // updating UI
                document.getElementById('name').textContent = data.result.first_name;

                // requesting the profile image
                fetch(`${API_URL}${input.value}/getUserProfilePhotos?user_id=${data.result.id}`)
                    .then(response => response.json())
                    .then(images => {
                        // images = {"ok": true, "result": {"total_count": <N>,"photos": [[{"file_id":"<FILE_ID>"}]]}}
                        if (images.ok) {
                            if (images.result.total_count > 0) {
                                // parsing the highest-resolution file_id
                                let file_id = images.result.photos[0][images.result.photos.total_count - 1].file_id;
                                
                                // preparing to display the profile image
                                fetch(`${API_URL}${input.value}/getFile?file_id=${file_id}`)
                                .then(response => response.json())
                                .then(file => {
                                    if (file.ok) {
                                        // updating the UI with the bot profile picture
                                        document.getElementById('profile-image').src = 
                                            `https://api.telegram.org/file/bot${input.value}/${image.result.file_path}`;
                                    } else {
                                        // unknown error.
                                    }
                                });
                            } else {
                                // the bot has no profile image.
                            }
                        } else {
                            // unknown error
                        }
                    })
                

                // display the commands interface
                add_command();
            } else {
                // token is not valid.
            }
        });
}