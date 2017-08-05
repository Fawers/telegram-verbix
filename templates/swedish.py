from templates.base import verbix_url_button

TEMPLATE = """
Infinitive: %s
Supine: %s
Gerund: %s
Imperative: %s

Present: %s
Past: %s
""".strip()


def render_response(data):
    """Render the template and insert forms. Return result."""

    def format(tuple):
        v, f = tuple
        if f == 'orto':
            return '_%s_' % v
        elif f == 'irregular':
            return '*%s*' % v
        else:
            return v

    infinitive = format(data['forms']['infinitive'])
    supine = format(data['forms']['supine'])
    gerund = format(data['forms']['gerund'])
    imperative = format(data['forms']['imperative'])
    present = format(data['tenses']['present'])
    past = format(data['tenses']['past'])

    message = TEMPLATE \
        % (infinitive, supine, gerund, imperative, present, past)

    url_button = verbix_url_button(data['verb'], data['url'])

    return (message, url_button)
