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
      last_schedule = json.loads(last_schedule)
      curr = last_schedule
      del curr["channelMetadataResponse"]["metaData"]["dateTime"]
      if curr != last:
        c1 += 1
        fw.write(last_time + "\t" + json.dumps(last_schedule) + "\n")
        last = curr

  print "Read", c0, "lines. Write", c1, "lines."
