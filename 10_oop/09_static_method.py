class ChaiUtils:
    @staticmethod
    def clean_ingrediants(text):
       return [item.strip() for item in text.split(",")]
    
 
raw = "water , milk , honey "

cleaned = ChaiUtils.clean_ingrediants(raw)
print(cleaned)

