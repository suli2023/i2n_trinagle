class Filehandler:
    def write_file(self, text):
        fp = open("adat.txt", "a", encoding="utf-8")
        fp.write(text)
        fp.write("\n")
        fp.close()
