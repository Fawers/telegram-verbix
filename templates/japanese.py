from mako.template import Template


TEMPLATE = Template("""\
**Verb:** ${data['verb']}
**Class:** ${data['verb class']}
**Related Kanji:** ${', '.join(data['related kanji'])}

% for form in data['forms']:
**${form['name']}**
% if 'kana' in form:\
## simple form; only one kana
${form['kana']}

% else:
## complex form; has affirmative/negative and formality levels
% for situation in ('Affirmative', 'Negative'):
*${situation}*
% for formality in form[situation]:
${formality['formality']}: ${formality['kana']}
% endfor  ## formality

% endfor  ## situation
% endif
% endfor  ## form
""")


def render_response(data):
    """Render the template and insert forms. Return result."""
    message = TEMPLATE.render(data=data).strip()

    verbix_button = verbix_url_button(data['verb'], data['url'])
    jisho_buttons = jisho_links_buttons(data['related kanji'],
                                        data['jisho links'])

    buttons = {
        'inline_keyboard':
            verbix_button['inline_keyboard'] +
            jisho_buttons['inline_keyboard']
    }

    return (message, buttons)


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
