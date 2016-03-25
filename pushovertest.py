import httplib, urllib

conn = httplib.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.urlencode({
    "token": "aA2bEjV2CqtwavfNFLTVCCb7cCbofT",
    "user": "ukV5ZvQedvmEAuUKtsSPPoH77gdDVa",
    "message": "fall detected",
   "title": "Sentinel Active Monitor",
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()
