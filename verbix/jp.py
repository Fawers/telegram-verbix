from urllib.parse import quote as urlquote

from verbix.base import Verbix, VerbixError, VerbNotFoundError


class Japanese(Verbix):
    HALF_COLUMN = 'pure-u-xl-1-2'

    TENSE_FULL_WIDTH = '.pure-u-1-2'
    TENSE_HALF_WIDTH = '.pure-u-1-3'

    def conjugate(self, verb):
        soup = self.query_verb(verb)

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
            form = {'name': t.select_one('h2').text}

            if form['name'] == 'Provisional':
                # this is the exception to our rule: it's in a full-width
                # row, has both affirmative and negative but no level of
                # politeness. since it's only one, treat it here.
                affirmative, negative = t.select(self.TENSE_FULL_WIDTH)[2:4]

                form['Affirmative'] = affirmative.select_one('.normal').text
                form['Negative'] = negative.select_one('.normal').text

            elif self.HALF_COLUMN in t['class']:
                # there is only kana to retrieve here
                form['kana'] = t.select(self.TENSE_HALF_WIDTH)[1] \
                                .select_one('span').text

            else:
                # there is kana and politeness to retrieve here, both
                # affirmative and negative
                affirmative_negative = t.select(self.TENSE_FULL_WIDTH)[2:4]

                for situation in affirmative_negative:
                    # Literally just "Affirmative" or "Negative" here
                    situation_str = situation.select_one('h3').text
                    form[situation_str] = []

                    for row in situation.select('tr'):
                        # Either 'plain' or 'polite'
                        formality = row.select_one('.pronoun').text
                        # The actual inflectioned word
                        word = row.select_one('.normal').text

                        form[situation_str].append({
                            'formality': formality,
                            'kana': word})

            kana.append(form)

        return self._build_info(verb, verb_class, kanji, kana,
                                self._verb_safe_url(verb))

    def _build_info(self, verb, verb_class, kanji, kana, url):
        data = {
            'verb': verb,
            'verb class': verb_class,
            'related kanji': kanji,
            'jisho links': ['http://jisho.org/search/%s' % urlquote(k)
                            for k in kanji],
            'forms': kana,
            'url': url
        }

        return data


japanese = Japanese()
