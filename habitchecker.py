import datetime
import pytz
import urllib
import requests, json


def habitchecker(event,context):

  habitifyAPI = "e911d8dfbfa43e041017f29e314a7a58b3dc1dbd5e7e08d69a8a9cdaf1b9887f";
  beeminderAPI = "VKaxzd_iFFXTBKHSFLxt";
  habitId = "-MnPCMpqoXIkioanXawc";



  today = datetime.datetime.now(tz=pytz.timezone('Europe/Paris'))
  x = today.replace(microsecond=0)

  
  safe_string = urllib.parse.quote_plus(str(x))
  safe_string = safe_string.replace('+',"T")

  headers = {"Authorization":habitifyAPI}

  habitifyURL = "https://api.habitify.me/status/-MnPCMpqoXIkioanXawc" + "?target_date=" + safe_string


  r=requests.get(habitifyURL,headers=headers)
  j = r.json()
  habitify_status = j['data']['status']


  get_beeminder_url = "https://www.beeminder.com/api/v1/users/nmartinovic/goals/trackhabitsauto/datapoints.json?auth_token=VKaxzd_iFFXTBKHSFLxt"

  beeminder_data = requests.get(get_beeminder_url).json()

  temp = (str(x).split(' ')[0].split('-'))
  beeminderDate = ''.join(temp)


  if beeminder_data[0]['daystamp'] == beeminderDate:
    pass
  elif habitify_status == 'completed':
    requests.post("https://www.beeminder.com/api/v1/users/nmartinovic/goals/trackhabitsauto/datapoints.json?auth_token=VKaxzd_iFFXTBKHSFLxt&value=1")
  else:
    pass

  

  habitifyURL = "https://api.habitify.me/status/194E876E-E551-443A-BF4F-879528B7407B" + "?target_date=" + safe_string


  r=requests.get(habitifyURL,headers=headers)
  j = r.json()
  habitify_status = j['data']['status']

  get_beeminder_url = "https://www.beeminder.com/api/v1/users/nmartinovic/goals/pandaplanner/datapoints.json?auth_token=VKaxzd_iFFXTBKHSFLxt"

  beeminder_data = requests.get(get_beeminder_url).json()

  temp = (str(x).split(' ')[0].split('-'))
  beeminderDate = ''.join(temp)


  if beeminder_data[0]['daystamp'] == beeminderDate:
    pass
  elif habitify_status == 'completed':
    requests.post("https://www.beeminder.com/api/v1/users/nmartinovic/goals/pandaplanner/datapoints.json?auth_token=VKaxzd_iFFXTBKHSFLxt&value=1")
  else:
    pass

  habitifyURL = "https://api.habitify.me/status/-N-MZlah_RxI91gknyW7" + "?target_date=" + safe_string


  r=requests.get(habitifyURL,headers=headers)
  j = r.json()
  habitify_status = j['data']['status']

  get_beeminder_url = "https://www.beeminder.com/api/v1/users/nmartinovic/goals/kegs/datapoints.json?auth_token=VKaxzd_iFFXTBKHSFLxt"

  beeminder_data = requests.get(get_beeminder_url).json()

  temp = (str(x).split(' ')[0].split('-'))
  beeminderDate = ''.join(temp)


  if beeminder_data[0]['daystamp'] == beeminderDate:
    pass
  elif habitify_status == 'completed':
    requests.post("https://www.beeminder.com/api/v1/users/nmartinovic/goals/kegs/datapoints.json?auth_token=VKaxzd_iFFXTBKHSFLxt&value=1")
  else:
    pass