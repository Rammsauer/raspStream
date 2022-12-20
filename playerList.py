class playList:
    def __init__(self, id, name):
        self.id = id
        self.name = name


playlist = [
    playList("PLHNwwBUMYsHYK4Klp5_YsHbPMecplf_-7", "Livingroom Stream"),
    playList("UULFAimZZtQYPMkBPA-8VEMrvg", "비오토프 갤러리 biotope gallery Videos"),
    playList("PL6cBY6KLoZ_FsdV8ViAeMrMpJ8VlhwPF6", "Painter Yushkevich Victor Nikolaevich."),
    playList("PLsRHC_C5DDaM21SwCw7UJx1W_1uwCt3yq", "🔆 Sunset Collection")
]

videoList = []


class youtubeLink:
    def __init__(self, link, type, name, length=0):
        self.link = link
        self.type = type
        self.name = name
        self.length = length
