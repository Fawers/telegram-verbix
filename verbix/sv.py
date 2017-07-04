from verbix.base import Verbix, VerbixError, VerbNotFoundError


class Swedish(Verbix):
    def __init__(self):
        super().__init__('Swedish')

    def conjugate(self, verb):
        try:
            soup = self.query_verb(verb)
        except VerbNotFoundError:
            return f'Could not find verb "{verb}" in the database. :('
        except VerbixError:
            return 'An error occurred while accessing Verbix. Please try again.'

        verbtable = soup.select_one(self.SELECT_VERBTABLE)

        forms = verbtable.select(self.SELECT_FORMS)

        infinitive, supine, gerund = forms[0].select('span')

        imperative = forms[-1].select('span')[1]

        tenses = verbtable.select(self.SELECT_TENSES)

        present, past = tenses[0], tenses[2]
        present = present.select('span')[1]
        past = past.select('span')[1]

        return self._build_info(
            infinitive=infinitive, supine=supine, gerund=gerund,
            imperative=imperative, present=present, past=past,
            url=self.get_url(verb))

    def _build_info(self, **data):
        infinitive = data.pop('infinitive')
        supine = data.pop('supine')
        gerund = data.pop('gerund')
        imperative = data.pop('imperative')
        present = data.pop('present')
        past = data.pop('past')
        url = data.pop('url')

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
            'url': url
        }


swedish = Swedish()
