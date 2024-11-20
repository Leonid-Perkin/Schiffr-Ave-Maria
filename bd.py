import sqlite3
cipher_dict = {
    'А': ['Ангел', 'Архангел', 'Аминь'],
    'Б': ['Благодать', 'Божий Сын', 'Благословение'],
    'В': ['Вера', 'Воскресение', 'Великое чудо'],
    'Г': ['Грех', 'Господь', 'Глава Церкви'],
    'Д': ['Дух Святой', 'День', 'Дар'],
    'Е': ['Евангелие', 'Елей', 'Ежедневное благословение'],
    'Ё': ['Ёжик духовный', 'Ёмкость благодати'],
    'Ж': ['Жертвоприношение', 'Жизнь вечная', 'Жизнь Христова'],
    'З': ['Завет', 'Закон Божий', 'Знамение'],
    'И': ['Иисус', 'Икона', 'Имя святое'],
    'Й': ['Йогин', 'Йога молитвы'],
    'К': ['Крест', 'Крещение', 'Князь небесный'],
    'Л': ['Лавра', 'Лик святого', 'Лазарь'],
    'М': ['Молитва', 'Мира', 'Монастырь'],
    'Н': ['Небо', 'Ночь молитвы', 'Надежда'],
    'О': ['Образ', 'Огненное очищение', 'Окружение святое'],
    'П': ['Покаяние', 'Писание', 'Пастырь'],
    'Р': ['Распятие', 'Рождение', 'Радость'],
    'С': ['Святость', 'Слово Божье', 'Свет'],
    'Т': ['Троица', 'Тельце', 'Теология'],
    'У': ['Утро молитвы', 'Успение', 'Утешение'],
    'Ф': ['Фавор', 'Филадельфия', 'Фаворит'],
    'Х': ['Христос', 'Храм', 'Хвала'],
    'Ц': ['Церковь', 'Царство Небесное', 'Цветение'],
    'Ч': ['Чудо', 'Чистота', 'Чтение Святых Писаний'],
    'Ш': ['Шествие', 'Шампанское', 'Школа молитвы'],
    'Щ': ['Щедрость', 'Щит веры', 'Щедрость Божественная'],
    'Ы': ['Ылия', 'Ыскренность веры'],
    'Э': ['Эпоха благодати', 'Эфес', 'Эхо слов святых'],
    'Ю': ['Юродивый', 'Юность веры', 'Юго-восточные святые'],
    'Я': ['Явление', 'Язык веры', 'Ягоды райские'],
    'A': ['Angel', 'Archangel', 'Amen'],
    'B': ['Blessing', 'Bethlehem', 'Bible'],
    'C': ['Christ', 'Church', 'Covenant'],
    'D': ['Divine', 'David', 'Discipleship'],
    'E': ['Eternal', 'Eucharist', 'Evangelist'],
    'F': ['Faith', 'Fellowship', 'Forgiveness'],
    'G': ['Grace', 'Glory', 'God'],
    'H': ['Heaven', 'Holy Spirit', 'Hope'],
    'I': ['Immanuel', 'Inspiration', 'Incarnation'],
    'J': ['Jesus', 'Joseph', 'Judgment'],
    'K': ['Kingdom', 'King', 'Knowledge'],
    'L': ['Lord', 'Light', 'Love'],
    'M': ['Mercy', 'Ministry', 'Messiah'],
    'N': ['Nazareth', 'New Testament', 'Noble'],
    'O': ['Omnipotent', 'Obedience', 'Olive Tree'],
    'P': ['Prayer', 'Praise', 'Prophet'],
    'Q': ['Queen of Heaven', 'Quietude', 'Quintessence'],
    'R': ['Resurrection', 'Redemption', 'Righteousness'],
    'S': ['Salvation', 'Sanctification', 'Spirit'],
    'T': ['Trinity', 'Truth', 'Temple'],
    'U': ['Unity', 'Understanding', 'Uplifted'],
    'V': ['Virtue', 'Vicar', 'Veneration'],
    'W': ['Worship', 'Wisdom', 'Witness'],
    'X': ['Xenophilia', 'Xenia', 'Xenon'],
    'Y': ['Yahweh', 'Yoke', 'Yearning'],
    'Z': ['Zion', 'Zeal', 'Zionism'],
    ' ': [' ']
}
def create_db_and_insert_data():
    conn = sqlite3.connect('cipher_db.sqlite')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cipher (
            letter TEXT PRIMARY KEY,
            phrase_1 TEXT,
            phrase_2 TEXT,
            phrase_3 TEXT
        )
    ''')
    for letter, phrases in cipher_dict.items():
        phrase_1 = phrases[0]
        phrase_2 = phrases[1] if len(phrases) > 1 else None
        phrase_3 = phrases[2] if len(phrases) > 2 else None
        cursor.execute("INSERT OR REPLACE INTO cipher (letter, phrase_1, phrase_2, phrase_3) VALUES (?, ?, ?, ?)",
                       (letter, phrase_1, phrase_2, phrase_3))
    conn.commit()
    conn.close()
    print("Данные успешно добавлены в базу данных.")
create_db_and_insert_data()