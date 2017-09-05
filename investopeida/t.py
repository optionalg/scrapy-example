from rake_nltk import Rake

r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.

#r = Rake(<language>) # To use it in a specific language supported by nltk.

# If you want to provide your own set of stop words and punctuations to
# r = Rake(<list of stopwords>, <string of puntuations to ignore>)

r.extract_keywords_from_text('egypt looses 310m in inflation')

r.get_ranked_phrases() # To get keyword phrases ranked highest to lowest.
