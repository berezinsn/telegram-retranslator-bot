# TELEGRAM RETRANSLATOR <br>
## About:
<br>This is the Telegram client such reads one (or more) Telegram group(s) and then copy and push the post content to another group by passing through the "prohibited words" filter

<br>This way (Client approach) chosen as per BOT approach is not allow you to join the existing group in case if you're not an admin and have no way to add it manually

## How to use <br>
**prerequisite:** >=python3.8 <br><br>
**install the venv by passing the following command:** <br>
`virtualenv venv -p python3` <br><br>
**activate virtual environment** <br>
`source venv/bin/activate` <br><br>
**install required libs** <br>
`pip install -r requirements.txt` <br><br>
**create config file with the following fields:**


    # get api_id and api_hash from the Telegram API 
    client_api_id = "set_your_value"
    client_api_hash = "set_your_value"
    # to check chat_id values, just send the repost to @getmyid_bot
    source_chat_id = -100113xxxxxx 
    destination_chat_id = -10015xxxxxx
    # the list of prohibited keywords should be filled 
    black_list = []

<br><br>
**NOTE:** during the first start the app will create the service_account.session file. Just authorize your acc using the phone number for this



