"""
Du willst Vorbild sein und die Welt ganz gerne retten\n
Dann gib keine Workshops, kannst du selber nicht mal rappen\n
Doch noble Absicht, schlechter Ansatz geht über Gehabe\n
Rap vermarktet sich gerade, die Aussage bleibt Blamage\n

Ja man feiert euern Sound, wer feiert was ihr sagt\n
Ich feil an meinem Sound, jeder Part ein Unikat\n
Resort Pöbel Sports, schlau und aggressiv\n
Ihr versteckt euch hinter Beats und macht auf künstlich primitiv\n

Opfer kiff mal deinen Joint, mach mal deinen Stich\n
Aber tue uns nen Gefallen und behalt den Rotz für dich\n
Zwei Tracks, deiner Toy-Gang geh'n die Themen aus\n
Ich lass das Leben laufen, du pflegst deinen Lebenslauf\n

Im gleichen Atemzug wird von Realness fantasiert\n
Deutschrap liebt den Heldenepos, gibt sich Riefenstahlisiert\n
Liebt den Opfermythos wie die Dolchstoßlegende\n
Doch ist letztendlich versnobter als ein Golfklubgelände\n

Und glotzt nicht auf den Inhalt, sondern auf den Preis\n
Grün, gelb und lila bilden weiß\n
Auch Feminismus lässt sich ganz leicht antwerken (shake your ass)\n
MTV und Nike machen Hip-Hop wieder urban\n

Es wird sich alles einverleibt, kurze Haltung für den Hype\n
Marketinggeniestreich, Playlistaktivistenvibe\n
Deutschrap für Schaumschläger, wir bleiben Bombenleger (yeah)\n
Du bist der Werbeträger und wir die Würdenträger\n

Und wer du bist ist kein Argument für mich\n
Dich nicht zu hinterfragen, du musst es ertragen, dass\n
Es keine Rolle spielt welche Rolle du bespielst\n
Wie soll ich dich ernstneh'm wenn du das nicht kapierst\n
"""


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
    playList("PLomb3VSQH7whY_McCtAiSkafvWyiYd0hr", "space shuttle")
]

videoList = []


# 1 = Video, 0 = Livestream
class youtubeLink:
    def __init__(self, link, type, name, length=0):
        self.link = link
        self.type = type
        self.name = name
        self.length = length
