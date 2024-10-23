class hewan:
    def suara(self):
        raise NotImplementedError("subclass harus mengimplementasikan metode ini")
    
class kucing(hewan):
    def suara(self):
        return "meong!"
    
class sapi(hewan):
    def suara(self):
        return "MOOOOOOOOOOOOOOOOOOOOOOOOOOO"
    
    def cetak_suara(hewan):
        print(hewan.suara())
        
                