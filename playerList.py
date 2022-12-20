class playList:
    def __init__(self, id, name):
        self.id = id
        self.name = name


playlist = [
    playList("PLHNwwBUMYsHYK4Klp5_YsHbPMecplf_-7", "Livingroom Stream"),
    playList("UULFAimZZtQYPMkBPA-8VEMrvg", "비오토프 갤러리 biotope gallery Videos"),
    playList("PL6cBY6KLoZ_FsdV8ViAeMrMpJ8VlhwPF6", "Painter Yushkevich Victor Nikolaevich."),
    playList("PLsRHC_C5DDaM21SwCw7UJx1W_1uwCt3yq", "🔆 Sunset Collection"),
    playList("PLuMd8MwW5DCCTVh-arTiSlufN_a2XKFEY", "Sketchbook Tour Compilation"),
    playList("UULFayNbjHNdphueeBy0tPNIig", "Heilwasserklang ch Videos"),
    playList("UULF3Kk8tvhHkWMMfKBb0q0X9g", "Foo the Flowerhorn Videos"),
    playList("UULFuM_RUD-2-3dyIsBQHNorTA", "ActionAdventureTwins Videos"),
    playList("PLcDFnATD_aoxSaoJWw3NUn4c3lCJ_CSXq", "Rain Walk"),
    playList("PL6poUgHngiIFjE2nqpoRbE7Wm1QBmAP9r", "Southwest Airlines Inflight")
]

videoList = []


# 1 = Video, 0 = Livestream
class youtubeLink:
    def __init__(self, link, type, name, length=0):
        self.link = link
        self.type = type
        self.name = name
        self.length = length
