class Ejderha:
    def __init__(self, ad, renk, guc=50, korun=10):
        self.ad = ad
        self.renk = renk
        self.guc = guc
        self.korun = korun

    def bilgi(self):
        return f"🐉 Ben {self.ad}! Rengim {self.renk}, gücüm {self.guc}."

    def ates_puskur(self):
        return f"🔥 {self.ad} ateş püskürttü! Hasar: {self.guc * 2}"

    def savun(self):
        return f"🛡️ {self.ad} korundu! Korunma puanı {self.korun * 3}"
