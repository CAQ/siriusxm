# -*- coding: utf-8 -*-
import datetime, urllib2, json
import twitter # https://github.com/bear/python-twitter


CHANNEL = "symphonyhall"

if __name__ == "__main__":
  now = datetime.datetime.utcnow()
  now_time = now.strftime("%m-%d-%H:%M:00")
  conn = urllib2.urlopen("https://www.siriusxm.com/metadata/pdt/en-us/json/channels/" + CHANNEL + "/timestamp/" + now_time)
  content = conn.read()
  curr_schedule = json.loads(content)

  last_time = None
  last_schedule = None
  try:
    with open("schedule." + CHANNEL + ".last") as f:
      for line in f:
        (last_time, last_schedule) = line.split("\t")
        last_schedule = json.loads(last_schedule)
  except:
    pass

  c1 = curr_schedule
  del c1["channelMetadataResponse"]["metaData"]["dateTime"]
  l1 = last_schedule
  if l1 is not None:
    del l1["channelMetadataResponse"]["metaData"]["dateTime"]
  if c1 != l1:
    with open("schedule." + CHANNEL + ".last", "a") as fw:
      fw.write(now_time + "\t" + content + "\n")
    with open("tokens.txt") as f:
      (ck, cs, atk, ats) = f.readline().strip().split("\t")
    api = twitter.Api(consumer_key=ck, consumer_secret=cs, access_token_key=atk, access_token_secret=ats)
    status = api.PostUpdate("[" + str(now) + "] Siruis XM channel " + CHANNEL + " schedule has changed at " + now_time + " UTC.")
