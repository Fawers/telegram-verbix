from verbix.base import Verbix, VerbixError, VerbNotFoundError


class Swedish(Verbix):
    LANGUAGE_CODE = 21
    TEMPLATE_CODE = 121

    def conjugate(self, verb):
        soup = self.query_verb(verb)

        forms = soup.select(self.SELECT_FORMS)

        infinitive, supine, gerund = forms[0].select('span')

        imperative = forms[4].select('span')[1]

        tenses = soup.select(self.SELECT_TENSES)

        present, past = tenses[0], tenses[2]
        present = present.select('span')[1]
        past = past.select('span')[1]

        return self._build_info(
            infinitive=infinitive, supine=supine, gerund=gerund,
            imperative=imperative, present=present, past=past,
            url=self._verb_safe_url(verb), verb=verb)

    def _build_info(self, **data):
        infinitive = data.pop('infinitive')
        supine = data.pop('supine')
        gerund = data.pop('gerund')
        imperative = data.pop('imperative')
        present = data.pop('present')
        past = data.pop('past')
        url = data.pop('url')
        verb = data.pop('verb')

        return {
            'forms': {
                'infinitive': (infinitive.text, infinitive.get('class')[0]),
                'supine': (supine.text, supine.get('class')[0]),
                'gerund': (gerund.text, gerund.get('class')[0]),
                'imperative': (imperative.text, imperative.get('class')[0])
            },
            'tenses': {
                'present': (present.text, present.get('class')[0]),
                'past': (past.text, past.get('class')[0])
            },
            'url': 'http://www.verbix.com/find-verb/',  # TODO fix this $#!t,
            'verb': verb
        }


swedish = Swedish()
