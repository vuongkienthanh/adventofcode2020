import requests
cookies = {"_ga":"GA1.2.295712503.1619788418",
          "_gid":"GA1.2.1653412100.1619788418",
          "session":"53616c7465645f5f39d859e68ebd2dac3c2ca1ad9a39f68083ce05af734dca30bccf8eb9e071a3a83d199c0251f6318b"
}
def getdata(url, split=True):
    r = requests.get(url, cookies=cookies).text
    if split:
        return r.splitlines()
    else:
        return r