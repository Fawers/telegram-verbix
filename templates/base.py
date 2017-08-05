def verbix_url_button(verb, url):
    """Return a Telegram inline button with the Verbix URL."""
    return {
        'inline_keyboard': [[{'text': f'Verbix: {verb}', 'url': url}]]
    }
