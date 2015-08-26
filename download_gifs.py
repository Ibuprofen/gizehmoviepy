import json
import os.path
from subprocess import call

gifs = [('http://media.giphy.com/media/IK2MR7rp2eUOQ/giphy.gif', 'IK2MR7rp2eUOQ'),
('http://media.giphy.com/media/4ZP2Otq5tQbSM/giphy.gif', '4ZP2Otq5tQbSM'),
('http://media.giphy.com/media/codjKjCXkegyk/giphy.gif', 'codjKjCXkegyk'),
('http://media.giphy.com/media/mKI9lgC8ALsGs/giphy.gif', 'mKI9lgC8ALsGs'),
('http://media.giphy.com/media/vng1ghYqQHFOo/giphy.gif', 'vng1ghYqQHFOo'),
('http://media.giphy.com/media/HLOaVqFZb6SNG/giphy.gif', 'HLOaVqFZb6SNG'),
('http://media.giphy.com/media/13mjtmImvfNf32/giphy.gif', '13mjtmImvfNf3'),
('http://media.giphy.com/media/ZAseSBcoRly1i/giphy.gif', 'ZAseSBcoRly1i'),
('http://media.giphy.com/media/xwmy7azQcHXCU/giphy.gif', 'xwmy7azQcHXCU'),
('http://media3.giphy.com/media/CzqUKYVMY6sUM/giphy.gif', 'CzqUKYVMY6sUM'),
('http://media.giphy.com/media/m7yzbDgdkWbmM/giphy.gif', 'm7yzbDgdkWbmM'),
('http://media.giphy.com/media/Xn2TpDGEEl2O4/giphy.gif', 'Xn2TpDGEEl2O4'),
('http://media.giphy.com/media/PDXoH6PzNxmOA/giphy.gif', 'PDXoH6PzNxmOA'),
('http://media.giphy.com/media/v2vdWBun97jtS/giphy.gif', 'v2vdWBun97jtS'),
('http://media.giphy.com/media/Q4CVs6ungrxvO/giphy.gif', 'Q4CVs6ungrxvO'),
('http://media.giphy.com/media/TqkuOoKtmYI80/giphy.gif', 'TqkuOoKtmYI80'),
('http://media.giphy.com/media/ZiqUNfVR8YfsY/giphy.gif', 'ZiqUNfVR8YfsY'),
('http://media.giphy.com/media/yKo95S5czzSKI/giphy.gif', 'yKo95S5czzSKI'),
('http://media.giphy.com/media/zjoFA3fCBdX6U/giphy.gif', 'zjoFA3fCBdX6U'),
('http://media.giphy.com/media/9H319cbTmgts4/giphy.gif', '9H319cbTmgts4'),
('http://media.giphy.com/media/8iRAtRERgJEZy/giphy.gif', '8iRAtRERgJEZy'),
('http://media.giphy.com/media/FQAikp95qxSyQ/giphy.gif', 'FQAikp95qxSyQ'),
('http://media.giphy.com/media/wQgvjkPjg8wmc/giphy.gif', 'wQgvjkPjg8wmc'),
('http://media.giphy.com/media/susSBnDhL2gnK/giphy.gif', 'susSBnDhL2gnK'),
('http://media.giphy.com/media/RkAwUt4dQF1tu/giphy.gif', 'RkAwUt4dQF1tu'),
('http://media.giphy.com/media/Lq5MRfpQKxZoA/giphy.gif', 'Lq5MRfpQKxZoA'),
('http://media.giphy.com/media/Wf3WU2rKYHu8M/giphy.gif', 'Wf3WU2rKYHu8M'),
('http://media.giphy.com/media/GY93OAKN5DMME/giphy.gif', 'GY93OAKN5DMME'),
('http://media.giphy.com/media/yvAzoTBh5hmCc/giphy.gif', 'yvAzoTBh5hmCc'),
('http://media.giphy.com/media/xKLLuUK0BlBOE/giphy.gif', 'xKLLuUK0BlBOE'),
('http://media1.giphy.com/media/kF3Pa1jZx8nhm/giphy.gif', 'kF3Pa1jZx8nhm'),
('http://media.giphy.com/media/5fBH6zaBGEqAPB8Tdkc/giphy.gif', '5fBH6zaBGEqAPB8Tdkc'),
('http://media.giphy.com/media/3o85xAg8LCrPOHxyMM/giphy.gif', '3o85xAg8LCrPOHxyMM'),
('http://media.giphy.com/media/3o85xndeHesudYg6s0/giphy.gif', '3o85xndeHesudYg6s0')]



# download them
for url, id in gifs:
  if os.path.isfile("./web/gifs/" + id + ".gif"):
    print id + " already exists"
  else:
    call(["wget", url, "-O", "./web/gifs/" + id + ".gif"])
