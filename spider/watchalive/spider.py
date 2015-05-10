# coding: utf8

import commands
import time
import traceback
import json
from sendmail import send_mail

def now():
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

def online_now(wanted, previous_player, online_player):
    print "PREVIOUS_PLAYER"
    print "=" * 50
    print ",".join(previous_player).encode("utf8")
    print ""  
    print ""  
    print "ONLINE_PLAYER"
    print "=" * 50
    print ",".join(online_player).encode("utf8")

    result = []
    for player in wanted:
        if (player in online_player.keys()) and (player not in previous_player):
            result.append(player)
    return result

def send(result, online_player, receiver):
    text = ""
    for player in result:
        text += "%s 开直播了\n%s\n%s" % (online_player[player]["playerName"].encode("utf8"), online_player[player]["playerTitle"].encode("utf8"), online_player[player]["link"].encode("utf8")) + '\n'
    send_mail(receiver, ','.join(result).encode("utf8") + " 开直播了!", text)

if __name__ == '__main__':
    first = True
    previous_player = []

    while(True):
        try: 
            status, output = commands.getstatusoutput('scrapy crawl douyu')
            online_player = {}

# receivers = ["niminjiecide@outlook.com"]

            json_file = open('playerlist.json')
            print "Reading playerlist.json..."
            for line in json_file:
                player = json.loads(line)
                online_player[player["playerName"]] = player
            json_file.close()

            if first:
                print "Start program"
                previous_player = online_player.keys()
                first = False
                continue

            wanted_ni = [u"张宁_xiao8", u"星际笨哥", u"qq_NuAJii", u"棋客", u"HistYyKk", u"iGXiGua", u"Cloudy", u"yyfyyf", u"IG430", u"scboy", u"DD"]
            wanted_liu = [u"IG430", u"ig_June", u"夏天的枫__"]

            result_ni = online_now(wanted_ni, previous_player, online_player)
            result_liu = online_now(wanted_liu, previous_player, online_player)

            print now() + "NI RESULT: " + str(result_ni)
            print now() + "LIU RESULT: " + str(result_liu)
            if result_liu:
                send(result_liu, online_player, ["louis0519@qq.com"])
            if result_ni:
                send(result_ni, online_player, ["niminjiecide@outlook.com"])

            previous_player = online_player.keys()
        except Exception, info:
            print traceback.print_exc()
            print info
            continue
        time.sleep(120)

