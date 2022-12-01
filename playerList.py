class youtubeLink:
    def __init__(self, link, type, name, length=0):
        self.link = link
        self.type = type
        self.name = name
        self.length = length

# 30 minutes should be the minimum

list = [
    youtubeLink("https://www.youtube.com/watch?v=QOjmvL3e7Lc", 0, "Tokyo Livecam"),
    youtubeLink("https://www.youtube.com/watch?v=-HAi_5IIAYg", 0, "Deerfield Beachcam"),
    youtubeLink("https://www.youtube.com/watch?v=seEkN2AFhBw", 0, "Harbour Village Bonaire Coral Reef"),
    youtubeLink("https://www.youtube.com/watch?v=odVgCqN6FXM", 0, "Utopia Village Reef Wall Camera"),
    youtubeLink("https://www.youtube.com/watch?v=ydYDqZQpim8", 0, "Namibia: Live stream in the Namib Desert"),
    youtubeLink("https://www.youtube.com/watch?v=JJqXeRFsLjE", 0, "KC Zoo Penguin Cam"),
    youtubeLink("https://www.youtube.com/watch?v=y1QoP1AgAlY", 0, "Raccoon Cam \"Living Room\""),
    youtubeLink("https://www.youtube.com/watch?v=N1QWE0eQDVI", 0, "LIVE Barn Owl Florida"),
    youtubeLink("https://www.youtube.com/watch?v=JnJhFYhIjFs", 0, "Port of Helsinki - West harbour - north cam"),
    youtubeLink("https://www.youtube.com/watch?v=m9ZzkweZKcM", 0, "Wetter-Panorama – 24/7 LIVE Stream Webcams Österreich"),
    youtubeLink("https://www.youtube.com/watch?v=JQnxefImhu8", 0, "Monterey Bay Aquarium"),
    youtubeLink("https://www.youtube.com/watch?v=RQA5RcIZlAM", 0, "Tokyo Shinjuku Live Cam"),
    youtubeLink("https://www.youtube.com/watch?v=qHJMkze8lPg", 0, "東京駅丸の内口　ライブカメラ"),
    youtubeLink("https://www.youtube.com/watch?v=emI8r2dfk6g", 0, "Main Street Livecam, Canmore, Alberta "),
    youtubeLink("https://www.youtube.com/watch?v=B0YjuKbVZ5w", 0, "Grand Avenue Bridge in Glenwood Springs Live Camera"),
    youtubeLink("https://www.youtube.com/watch?v=1EiC9bvVGnk", 0, "Jackson Hole Wyoming USA Town Square Live Cam - SeeJH.com"),
    youtubeLink("https://www.youtube.com/watch?v=V00D4K9OshI", 0, "LONDON BUS RIDES ✨ DIGEST 🔴 LIVE CHAT 💫"),
    youtubeLink("https://www.youtube.com/watch?v=FKLlUa23eCY", 0, "Berlin Bus Rides 🔴 Live Chat"),
    youtubeLink("https://www.youtube.com/watch?v=NKzejBusnE8", 0, "Views of Three Sisters from A Bear & Bison Inn"),
    youtubeLink("https://www.youtube.com/watch?v=zomZywCAPTA", 1, "4K CABVIEW Bar - Bijelo Polje -102 tunnels -96 bridges -1029m", 12377),
    youtubeLink("https://www.youtube.com/watch?v=oN8q7p57nZw", 1, "ASMR Night Truck Driving 1.5 Hours", 6119),
    youtubeLink("https://www.youtube.com/watch?v=V03JLp2rdKc", 1, "Walking New York City on a Spring-like Day", 2354),
    youtubeLink("https://www.youtube.com/watch?v=kasGRkfkiPM", 1, "Bob Ross - Mountain Summit (Season 13 Episode 10)", 1666),
    youtubeLink("https://www.youtube.com/watch?v=pw5ETGiiBRg", 1, "Bob Ross - Valley View (Season 21 Episode 1)", 1652),
    youtubeLink("https://www.youtube.com/watch?v=KYlM2zJnNWY", 1, "Bob Ross - Cabin in the Hollow (Season 31 Episode 5)", 1519),
    youtubeLink("https://www.youtube.com/watch?v=mT0RNrTDHkI", 1, "Bob Ross - One Hour Special - The Grandeur of Summer", 3582),
    youtubeLink("https://www.youtube.com/watch?v=tWeUZxEfda0", 1, "Jungle In The House 'The Unknown Jungle World'", 1855),
    youtubeLink("https://www.youtube.com/watch?v=VYO8Biwffns", 1, "Portland Rain Walk, Peak Autumn Northwest District Binaural Audio 4k", 2849),
    youtubeLink("https://www.youtube.com/watch?v=NjvFF2Kvx1U", 1, "STARDEW VALLEY Chill gameplay for relax or study", 29962),
    youtubeLink("https://www.youtube.com/watch?v=kt0qIFPQBJg", 1, "Relaxing First Person Horse Ride in Witcher 3: Wild Hunt", 5065),
    youtubeLink("https://www.youtube.com/watch?v=zsfUlbtSo2k", 1, "The Witcher 3 - Music & Ambience - Walking to Novigrad", 2940),
    #youtubeLink("https://www.youtube.com/watch?v=Pd_xzpHibKE", 1, "Geralt Travels On Horseback To Novigrad - The Witcher 3", 4965),  #to dark for monitor
    youtubeLink("https://www.youtube.com/watch?v=L6vwrxDc3TA", 0, "DERustic Inn @ Jackson Hole"),
    youtubeLink("https://www.youtube.com/watch?v=fyOVKyaKJq4", 1, "Switzerland 4K - Scenic Relaxation Film With Inspiring Music", 3650),
    youtubeLink("https://www.youtube.com/watch?v=KGuCGd726RA", 0, "Live NYC Brooklyn Bridge & Manhattan cam"),
    youtubeLink("https://www.youtube.com/watch?v=5E2ycdUi2m8", 1, "★ 4K 🇦🇹 Bludenz - Arlberg - Giselabahn", 32572),
    youtubeLink("https://www.youtube.com/watch?v=b-PyEswUenE", 0, "THE WORLD LIVE ORIGINAL PROGRAM"),
    youtubeLink("https://www.youtube.com/watch?v=-SMKVJO_wGo", 1, "Snowfall in The Lofoten Islands, Norway, Nature Sounds for Sleep", 12147),
    youtubeLink("https://www.youtube.com/watch?v=wuzPzIbZk5Q", 1, "Aqualink | MEGA Lab | Hawaii live stream", 42899),
    youtubeLink("https://www.youtube.com/watch?v=kVQC7KSbcqM", 1, "Bahamas Underwater Cam Stream", 42898),
    #youtubeLink("https://www.youtube.com/watch?v=86YLFOog4GM", 0, "Nasa Live Stream - Earth From Space : Live Views from the ISS"), # not supported under tv
    youtubeLink("https://www.youtube.com/watch?v=ddZu_1Z3BAc", 0, "NASA LIVE Stream From The ISS"),
    youtubeLink("https://www.youtube.com/watch?v=f3MybR_9wpQ", 0, "LIVE View of Earth & Moon From Artemis I Orion"),
    youtubeLink("https://www.youtube.com/watch?v=1-iS7LArMPA", 0, "EarthCam Live: Times Square in 4K"),
    youtubeLink("https://www.youtube.com/watch?v=3rDjPLvOShM", 1, "[9:56 Hours] Train Journey to the Norwegian", 35549),
    youtubeLink("https://www.youtube.com/watch?v=KuDR6e29eGI", 1, "[4K UHD] RED DEAD REDEMPTION 2 - FULL GAME - 4K HDR Full Gameplay", 102669),
    youtubeLink("https://www.youtube.com/watch?v=pBvezl-975I", 1, "DE Stray (PS5) 4K 60FPS HDR Gameplay - (Full Game)", 12192),
    youtubeLink("https://www.youtube.com/watch?v=X2z9mwLQEfk", 1 , "Uncharted: The Lost Legacy (PS5) 4K HDR Gameplay - (Full Game)", 13614),
    youtubeLink("https://www.youtube.com/watch?v=ixllGOX0Evw", 1, "GOD OF WAR RAGNAROK Gameplay Walkthrough FULL GAME", 65414),
    youtubeLink("https://www.youtube.com/watch?v=pSY74-B7M2c", 1, "ELDEN RING Gameplay Walkthrough FULL GAME (4K 60FPS) No Commentary", 60517),
    youtubeLink("https://www.youtube.com/watch?v=Ou6UsEf1J_o", 1, "The Legend of Zelda: Breath of the Wild - Full Game (No Commentary)", 65857),
    youtubeLink("https://www.youtube.com/watch?v=ZY5js5jW9LI", 1, "Fallout 4 - Longplay (Main Quest) Full Game Walkthrough [No Commentary]", 86172),
    youtubeLink("https://www.youtube.com/watch?v=1i_MIsdXXoc", 1, "Assassin's Creed Origins Full Walkthrough Gameplay - No Commentary (PC Longplay)", 81553),
    youtubeLink("https://www.youtube.com/watch?v=byJ5to20C6I", 1, "Tomb Raider (1996) Playthrough (No Commentary)", 15976),
    youtubeLink("https://www.youtube.com/watch?v=BvXUR_ynn7k", 1, "Mafia 1 - Full Game Walkthrough", 31411),
    youtubeLink("https://www.youtube.com/watch?v=cn_taKva-AQ", 1, "The Witcher 3: Wild Hunt FULL Walkthrough Gameplay - No Commentary (PC Longplay)", 118619),
    youtubeLink("https://www.youtube.com/watch?v=pf_FyT1DK3o", 1, "Sonic Mania Plus playthrough ~Longplay~", 14617),
    youtubeLink("https://www.youtube.com/watch?v=c63Y2f0MZ24", 1, "Tomb Raider II (1997) Playthrough (No Commentary)", 16916),
    youtubeLink("https://www.youtube.com/watch?v=jIChmYpYv_8", 1, "Fallout 3 - Longplay Main Quest Full Game Walkthrough (No Commen", 43064),
    youtubeLink("https://www.youtube.com/watch?v=Z-t4kEfmxgA", 1, "Quality Of Life (2022) Part 2 -NYC Graffiti Documentary-", 1951),
    youtubeLink("https://www.youtube.com/watch?v=5Gg-SACDXnc", 1, "Quality Of Life (2022) Part 3 -NYC Graffiti Documentary-", 2452),
    youtubeLink("https://www.youtube.com/watch?v=8VyxskhCl3U", 1, "Quality Of Life (2022) Part 4 -NYC Graffiti Documentary-", 2726),
    youtubeLink("https://www.youtube.com/watch?v=XQhv3OWPKJs", 1, "Quality Of Life (2022) Part 5 -NYC Graffiti Documentary-", 2245),
    youtubeLink("https://www.youtube.com/watch?v=c3uJUrvI2zc", 1, "[4K] 100 KYOTO GARDENS　京都の日本庭園 100", 2750),
    youtubeLink("https://www.youtube.com/watch?v=iUX-5wvtrlY", 1, "ZEN GARDEN AMBIANCE mit entspannenden leichten Regengeräuschen", 28646),
    youtubeLink("https://www.youtube.com/watch?v=GWBTv99fZCQ", 1, "Rain On Japanese Zen Garden In Modern Home At Night", 28546),
    youtubeLink("https://www.youtube.com/watch?v=s5kZ9XyXUhE", 1, "Sommeratmosphäre #Zeichnung #Sommer #Künstler - Viktor Yushkevich. #118 ", 2572),
    youtubeLink("https://www.youtube.com/watch?v=WdXhL5dyQM8", 1, "風景画の描き方B 77778c　金子一郎 ", 5146),
    youtubeLink("https://www.youtube.com/watch?v=-HPaYPvDylo", 1, "3 Hour Pencil Drawing: Hokusai's \"The Great Wave Off Kanagawa\"", 11276),
    youtubeLink("https://www.youtube.com/watch?v=38An7JQUADo", 1, "ASMR 3 Hours of drawing with pastels", 12314),
    youtubeLink("https://www.youtube.com/watch?v=eoN7r2dR8Uc", 1, "ASMR - Pencil on Wood Scratching (no talking) | Drawing an Old Barn in the Woods Episode 3!", 2417),
    youtubeLink("https://www.youtube.com/watch?v=iuPSEdduXXc", 1, "The Haywain Triptych - Hieronymus Bosch", 2200),
    youtubeLink("https://www.youtube.com/watch?v=vvw3PLFfbTo", 1, "Seoul Heavy Snow Walk Compilation Entspannendes Ambiente Schlaf", 10736),
    youtubeLink("https://www.youtube.com/watch?v=6QWgrhfbILU", 1, "Bob Ross Telling Stories For 8 Hours", 28648),
    youtubeLink("https://www.youtube.com/watch?v=p7G1lkYIFTM", 1, "Brooklyn Bridge to the Bronx via FDR Drive", 2673),
    youtubeLink("https://www.youtube.com/watch?v=RNRlAIyV-8Y", 1, "#23 Fluid Art for Fun, Acrylic Pour", 658),
    youtubeLink("https://www.youtube.com/watch?v=b2RUiHAoI-I", 1, "asmr draw with me (real time + no talking)", 3050),
    youtubeLink("https://www.youtube.com/watch?v=DNcn7McQsx8", 1, "\"Reflections\" How to paint an Oil landscape study for tones and shapes in a time-lapse", 681),
    youtubeLink("https://www.youtube.com/watch?v=Lt1K46od0-A", 1, "Acrylic Painting for Beginners/ Step by Step Painting/Landscape Painting", 908),
    youtubeLink("https://www.youtube.com/watch?v=y0eWVWx8hfI", 1, "Beautiful Peaceful Landscape/ Acrylic Painting for Beginners/ Easy to Paint", 1259),
    youtubeLink("https://www.youtube.com/watch?v=X7KJ7yDJDGk", 1, "Call of Duty 1 FULL Game Walkthrough - No Commentary ", 15296),
    youtubeLink("https://www.youtube.com/watch?v=NGxPoZx-LHU", 1, "Guild Wars 2 Human Mesmer Mirage Leveling Level 1 - 8", 4376),
    youtubeLink("https://www.youtube.com/watch?v=1doLQIpRp6g", 1, "Guild wars 2 Gameplay trying out this Game", 20102),
    youtubeLink("https://www.youtube.com/watch?v=xCwOtXCgxPM", 1, "World of Warcraft gameplay - No Commentary", 12604),
    youtubeLink("https://www.youtube.com/watch?v=l-VqPn1rUAE", 1, "[ENG] 나무 숲을 집으로 | 물멍 | Tree Forest | Aquarium | MulMung", 1169),
    youtubeLink("https://www.youtube.com/watch?v=bRPl2wR7pe4", 1, "NATURAL JUNGLE STYLE AQUASCAPE", 1260),
    youtubeLink("https://www.youtube.com/watch?v=sQBc85gg7HU", 1, "The Last Episode (Teardown + The Entire Series in One Video)", 10080),
    youtubeLink("https://www.youtube.com/watch?v=2BfHMnDOteA", 1, "Venice, Italy Walking Tour 2022", 14106),
    youtubeLink("https://www.youtube.com/watch?v=vyeZbyEvZ28", 1, "How to Draw a House in Two Point Perspective: Modern House", 683),
    youtubeLink("https://www.youtube.com/watch?v=FeUaC9cOjEg", 1, "How to Draw a House in 1-Point Perspective: Step by Step", 958),
    youtubeLink("https://www.youtube.com/watch?v=ACcFYF7N1dw", 1, "The best summer landscape. Composer: Viktor Yushkevich.", 1906),
    youtubeLink("https://www.youtube.com/watch?v=E7nnRc-F0dc", 1, "(Christoph Columbus, die Entdeckung des Landes). Künstler-Viktor", 7082),
    youtubeLink("https://www.youtube.com/watch?v=QngPGg4plVM", 1, "(Dorfleben) Acrylbild. Künstler - Viktor Juschkewitsch. #93 Fotos 2021.", 3186)
]
