"""
Es wird sich alles einverleibt, kurze Haltung für den Hype\n
Marketinggeniestreich, Playlistaktivistenvibe\n
Deutschrap für Schaumschläger, wir bleiben Bombenleger (yeah)\n
Du bist der Werbeträger und wir die Würdenträger\n
"""
import time


class playList:
    def __init__(self, id, name):
        self.id = id
        self.name = name


# 1 = Video, 0 = Livestream
class youtubeLink:
    def __init__(self, link, type, name, length=0):
        self.link = link
        self.type = type
        self.name = name
        self.length = length


playListTesting = [
    playList("PLHNwwBUMYsHYK4Klp5_YsHbPMecplf_-7", "Livingroom Stream"),
    playList("UULFAimZZtQYPMkBPA-8VEMrvg", "비오토프 갤러리 biotope gallery Videos")
]

playlist = [
    playList("PLHNwwBUMYsHYK4Klp5_YsHbPMecplf_-7", "Livingroom Stream"),
    playList("UULFAimZZtQYPMkBPA-8VEMrvg", "비오토프 갤러리 biotope gallery Videos"),
    playList("PL6cBY6KLoZ_FsdV8ViAeMrMpJ8VlhwPF6", "Painter Yushkevich Victor Nikolaevich."),
    playList("PLsRHC_C5DDaM21SwCw7UJx1W_1uwCt3yq", "🔆 Sunset Collection"),
    playList("PLuMd8MwW5DCCTVh-arTiSlufN_a2XKFEY", "Sketchbook Tour Compilation"),
    playList("UULFayNbjHNdphueeBy0tPNIig", "Heilwasserklang ch Videos"),
    playList("UULF3Kk8tvhHkWMMfKBb0q0X9g", "Foo the Flowerhorn Videos"),
    playList("PLmgMIv_--P1LApuqFs79Dtu5xngLrEM70", "Abandoned Mines"),
    playList("PLcDFnATD_aoxSaoJWw3NUn4c3lCJ_CSXq", "Rain Walk"),
    playList("PL6poUgHngiIFjE2nqpoRbE7Wm1QBmAP9r", "Southwest Airlines Inflight"),
    playList("PL41b0O3MiKnaE5oEcbrYU4BUMqcBafban", "NA106-Full ROV Hercules Dives"),
    playList("PLt72GzVTEThVqZR8j8u9M4bIilP-wRjSU", "Cabview"),
    playList("PLt72GzVTEThUdNFCZyg7mp0EOZUaCdqdL", "POV"),
    playList("UULFzkjgi_ssPh82uiro89uvNA", "Asu Videos"),
    playList("UULF31Pcer7qyXce13vLuTBjEg", "회색벌레 GreyWorm Videos"),
    playList("UULFdXhLXHoyexAm81i6kD4rYg", "木根  Mugen Woong Videos"),
    playList("UULF-CL-3OSWgL2PMdXcS0Bhcw", "FERRET WONDERLAND Videos"),
    playList("UULF4PbOLgmxoUUPaSI9qZwjtg", "苔テラリウム専門-道草ちゃんねる‐ Videos"),
    playList("UULFYmna5rFHIesFteksAvFOfg", "Dr. Plants Videos"),
    playList("PLJlUatrCOiFFRhaMj9WHyhSYErKlLMLSz", "Sketchbook Tours :]"),
    playList("PLbmPIXWNT8TOspS9_DN1oGkD5egqt2b-9", "World of Warcraft (Longplay/Lore/Commentary)"),
    playList("PLbmPIXWNT8TMFxFdjIYu5ardaL-JleFuf", "Guild Wars 2 (Longplay/Lore/Commentary)"),
    playList("PLGWGc5dfbzn9XgNxXmYpDZlDMy3ZLUyEw", "Minecraft [500 - 599]"),
    playList("PLomb3VSQH7wjgtTfy1cDproNuqpMI4d3h", "The Moon"),
    playList("PLomb3VSQH7whY_McCtAiSkafvWyiYd0hr", "space shuttle"),
    playList("PLcIs13BXKaKP8JbnXgDGC4LHkhKtQjtEx", "Abandoned"),
    playList("UULF6L605Bf_h3VII43Sqi0CCg", "nickz aquascape Videos"),
    playList("PLTpc4xYnColcHW7cExsErYMJlu6Fm7o9o", "Season 8"),
    playList("PLTpc4xYnColdbrZcbFRLUCn6l9h_NUFdV", "Season 7"),
    playList("PLTpc4xYnColdezBYnrci0WyMzb29_Mhtd", "Season 6"),
    playList("UULFpSIGHxvNRXyROheVp-QnnQ", "NCFORMULA Videos"),
    playList("PLlQWnS27jXh9yJXG7NxGG8XJsSE9ziIvz", "Mit offenen Karten | ARTE"),
    playList("PLhGeNYH-50KZzep96xKRkYLaBSJcAGwEZ", "Blow Up – Filme analysiert | ARTE"),
    playList("UULFVJXKQF5Er-B2Lf5PCu3Vrg", "Japanese Woodcarving TAKABA Videos"),
    playList("PLm8I5TkIJrVndzPY9rNjsR1-sJu4AItyC", "Ten Minute World History (Chronological)"),
    playList("PLm8I5TkIJrVniI4w5g5xQO--h8DYWulx2", "Ten Minute German History (Chronological)"),
    playList("PLDbSvEZka6GGm9cigiCJImOCKj6XZ9-gY", "Epicly Later'd"),
    playList("UULFjFxPoj7j3s8gECyZSM3Qjg", "Yurara Sarara Videos"),
    playList("PLGibX_M6gXLJFgF852lIBW--P4jZ_ThJP", "LKW Mitfahrt (Führerstandsmitfahrt)"),
    playList("PLzsxGmGx959pfVDRDoUOFjESxRYSwmXKJ", "Truck away - dashcam videos"),
    playList("UULFd0zIZlbgvEifm_hd3FwlBQ", "vewn Videos"),
    playList("UULFd0zIZlbgvEifm_hd3FwlBQ", "Chrisweeet Videos"),
    playList("UULFwRH985XgMYXQ6NxXDo8npw", "Kurzgesagt Videos"),
    playList("UULFB4TfJF97Ki1Ko4ZbgmmBFg", "내츄럴팟 NATURALLPOT Videos"),
    playList("UULFgiKpZ_zSDlmAYCS4wHJmXA", "The Creative Scaper"),
    playList("PLZuWPpOcX8wpcx24c6OCNz_kfdjzyXcEq", "sketchbook tour"),
    playList("PLRcvJ6ZVfvpvfUbEZHTXZkGn3YF3GBoER", "Sketchbook tour"),
    playList("PLlIcc-4qRNMrtaKLzMkHm-7DDThzjUFZF", "Sketchbook Tour"),
    playList("PLKozNXkP6ssfbo98ZUUbHjhTySBaUrrCB", "Sketchbook Tour"),
    playList("PLvt5Y9djRDM4v9qqnr_WzesbpPP0KM180", "Sketchbook tour"),
    playList("PLqiv4thFjAjXnIQ9yaDIJcRlhl3-han9s", "Sketchbook Tour"),
    playList("UULFEDMq9pI5h18GsNtvgzsrlg", "Danny Hawk Videos"),
    playList("UULFruu9ub1fYnRAnkzk6yx9tg", "Mountain Rug Cleaning Videos"),
    playList("UULF6gNjP1W4FXWExT5QpYkmhQ", "Ollie Bye Videos"),
    playList("UULFpjFEZsP53Ci-9in9Px3_tQ", "Khey Pard Videos"),
    playList("PLQifxFROE1seZYh6LCodPd4ctsrYkAL_t", "5 Minutes with"),
    playList("PLjT8FJrqdfGJxPZbC_NXne4oOAfVnN3Qw", "Offseason"),
    playList("UULFw-s1IFJKuJEUioERBC-u4g", "121 kn: pure culture"),
    playList("PLjW1ObFDddxNu8bA8-J_FYh-_S6v270PW", "Adventure Time"),
    playList("UULFTlA4-jdTkMFYib0iwOdAEg", " 기묘한 동물 사전 "),
    playList("PL0KX7kvoKj6IApzr8l2OjWmgHPqtlxTKW", "THE WITCHER 3 [PS5 4K 60FPS] WILD HUNT - Full Game"),
    playList("PL34fG-GHBEr0V2TgC16qlIatA5ILIYl7F", "Die Siedler IV - Fear Fortress"),
    playList("PLJrsvGPaUcqcreVcUDhNSdao3DJES-g90", "PC | AGE OF EMPIRES DEFINITIVE EDITION | ALL CAMPAIGNS "),
    playList("PLB9TwM3jkQo2N2TcXbzajqjJcBXqzPhAY", "Age Of Mythology Walkthrough No Commentary"),
    playList("UULFKjB92k3hLVX-AQNnM4jlig", "Leon Rudolph Videos"),
    playList("UULF_mV4ef9A6QhGRpziGDZp6Q", "Ontrack"),
    playList("PL9jGpLlUQb1IOTNDz4PjDcy9hVWAZP11t", "Animal Crossing New Horizons"),
    playList("PLbmPIXWNT8TMFxFdjIYu5ardaL-JleFuf", "Guild Wars 2 (Longplay/Lore/Commentary)"),
    playList("PL2XOPpYaVR48Ccftgn7GC5Qzzmhf3y01T", "Avatar: The Last Airbender - Season 1 | Full Episodes"),
    playList("PL2XOPpYaVR488hwV0AGTGiMxZ-rjtL48T", "Avatar: The Last Airbender - Season 2 | Full Episodes"),
]

videoList = []
timeStamp = time.time()
list = []
