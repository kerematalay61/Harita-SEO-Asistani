"""
Yapay zeka yorum oluşturucusu için anahtar kelimeleri yönetir.
"""
keywords_by_category = {
    "beyaz_esya": ["çamaşır makinesi servisi", "buzdolabı tamiri", "fırın onarımı"],
    "teknoloji": ["televizyon kurulumu", "akıllı cihaz desteği"],
    "temizlik": ["süpürge tamiri", "filtre değişimi"]
}

def get_keywords(category):
    return keywords_by_category.get(category, [])

def add_keyword(category, keyword):
    if category not in keywords_by_category:
        keywords_by_category[category] = []
    if keyword not in keywords_by_category[category]:
        keywords_by_category[category].append(keyword)

def list_all_keywords():
    return keywords_by_category
