from sendblue import Sendblue
import keys

sendblue = Sendblue(keys.SENDBLUE_API_KEY, keys.SENDBLUE_API_SECRET)

sendblue.send_message('+18018851059', {
    'content': 'Hi penis'
    
})
