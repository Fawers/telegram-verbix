TEMPLATE = """\
Verb: {verb}
Class: {verb_class}
Related Kanji: {comma_separated_kanji}

"""

SIMPLE_FORM_TEMPLATE = """\
*{form[name]}*
{form[kana]}

"""

# tricky
# might want to try mako to render these
COMPLEX_FORM_TEMPLATE = """\
*{name}*
_Affirmative_
· {form[Affirmative][formality]}: {form[Affirmative][kana]}

_Negative_
· {form[Negative][formality]}: {form[Negative][kana]}
"""

def _render_simple_form(form):
    pass


def _render_complex_form(form):
    pass


def render_response(data):
    """Render the template and insert forms. Return result."""
    message = TEMPLATE.format(
        verb=data['verb'], verb_class=data['verb class'],
        comma_separated_kanji=', '.join(data['related kanji']))

    for form in data['forms']:
        if 'kana' in form:
            message += _render_simple_form(form)

        else:
            message += _render_complex_form(form)

    return message
    # TODO: return message + inline buttons


def verbix_url_button(verb, url):
    """Return a Telegram inline button with the Verbix URL."""
    return {
        'inline_keyboard': [[{'text': f'Verbix: {verb}', 'url': url}]]
    }


def jisho_links_buttons(kanji_list, links):
    """
    Return Telegram inline buttons for each of the kanji, each pointing
    to its respective Jisho.org page.
    """
    return {
        'inline_keyboard': [
            [{'text': f'Jisho: {kanji}', 'url': link}]
            for kanji, link in zip(kanji_list, links)
        ]
    }
    for kanji, link in zip(kanji_list, links):
        pass
