def test_extract_article_titles():
    html = """
        <html>
            <body>
                <h1>Titre de l'article 1</h1>
                <h2>Titre de l'article 2</h2>
                <h3>Titre de l'article 3</h3>
            </body>
        </html>
    """
    expected_titles = ['Titre de l\'article 1', 'Titre de l\'article 2', 'Titre de l\'article 3']
    assert extract_article_titles(html) == expected_titles