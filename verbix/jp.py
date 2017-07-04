from verbix.base import Verbix, VerbixError, VerbNotFoundError


class Japanese(Verbix):
    def __init__(self):
        super().__init__('Japanese')

    def conjugate(self, verb):
        try:
            soup = self.query_verb(verb, lambda r: r.content.decode())
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

        kanji = tables[1].select('span.normal')[-2:]

        return (verb_class, kanji)

japanese = Japanese()
