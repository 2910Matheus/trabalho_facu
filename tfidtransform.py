import csv
from sklearn.feature_extraction.text import TfidfVectorizer

frases = []
with open ('frases_risco.csv', 'r', encoding='utf-8') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    for linha in leitor_csv:
        if linha:
            frases.append(linha[0])


vectorizar = TfidfVectorizer()
X = vectorizar.fit_transform(frases)

print(vectorizar.get_feature_names_out())

print(X.toarray())
