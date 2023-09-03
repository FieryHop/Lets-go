
import spacy

# Загрузка модели языка
nlp = spacy.load('en_core_web_sm')

# Текст для обработки
text = "Apple is looking at buying U.K. startup for $1 billion"

# Обработка текста
doc = nlp(text)

# Вывод результатов обработки
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
          token.shape_, token.is_alpha, token.is_stop)
