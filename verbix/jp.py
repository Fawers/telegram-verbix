from verbix.base import Verbix, VerbixError, VerbNotFoundError


class Japanese(Verbix):
    HALF_COLUMN = 'pure-u-xl-1-2'

    TENSE_FULL_WIDTH = '.pure-u-1-2'
    TENSE_HALF_WIDTH = '.pure-u-1-3'

    def __init__(self):
        super().__init__('Japanese')

    def conjugate(self, verb):
        try:
            soup = self.query_verb(verb)
        except VerbNotFoundError:
            return f'Could not find verb "{verb}" in the database. :('
        except VerbixError:
            return 'An error occurred while accessing Verbix. Please try again.'

        verbtable = soup.select_one(self.SELECT_VERBTABLE)

        tables = verbtable.select(self.SELECT_FORMS)

        # Table 0 refers to the verb class;
        # Table 1 has the related kanji (glossary lookup);
        # Tables 2 to 18 contain the actual forms and their inflections.

        verb_class = tables[0].select_one('span').text

        kanji = tables[1].select('span.normal')[2:]
        kanji = [k.text for k in kanji]

        kana = []

        for i in range(2, 19):
            t = tables[i]
            form = t.select_one('h2').text

            if self.HALF_COLUMN in t['class']:
                # there is only kana to retrieve here
                kana.append(
                    (form, t.select(
                        self.TENSE_HALF_WIDTH)[1].select_one('span').text))

            else:
                # there is kana and plain/polite to retrieve here, both
                # affirmative and negative
                affirmative_negative = t.select(self.TENSE_FULL_WIDTH)[2:4]

                # WARNING: Extreme LOL-zone below - proceed at your own risk
                kana.extend(
                    (form, a_n.select_one('h3').text, politeness, word)
                    for a_n in affirmative_negative
                    for row in a_n.select('tr')
                    for politeness in (row.select_one('.pronoun').text,)
                    for word in (row.select_one('.normal').text,))

        return (verb_class, kanji, kana)


japanese = Japanese()
