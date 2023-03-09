def test_integration():
    html1 = """contact.html"""
    html2 = """ D:/2em_semetre/Auto/Учебные материалы/exercice/localweb/momo/Page-d'accueil.html"""
    expected_titles = [
        'Titre de l\'article 1', 'Titre de l\'article 2', 'Titre de l\'article 3',
        'Titre de l\'article 4', 'Titre de l\'article 5'
    ]
    assert extract_article_titles(html1 + html2) == expected_titles