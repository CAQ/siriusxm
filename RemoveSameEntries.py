# -*- coding: utf-8 -*-
import json, gzip


CHANNEL = "symphonyhall"

if __name__ == "__main__":
  c0 = 0
  c1 = 0
  with gzip.open("schedule." + CHANNEL + ".last.gz", "rb") as f, gzip.open("schedule." + CHANNEL + ".last.1.gz", "wb") as fw:
    last = None
    for line in f:
      c0 += 1
      (last_time, last_schedule) = line.split("\t")
      last_schedule_obj = json.loads(last_schedule)
      del last_schedule_obj["channelMetadataResponse"]["metaData"]["dateTime"]
      if last_schedule_obj != last:
        c1 += 1
        fw.write(last_time + "\t" + last_schedule)
        last = last_schedule_obj

  print "Read", c0, "lines. Write", c1, "lines."
