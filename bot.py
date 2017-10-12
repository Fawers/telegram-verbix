import os
import re
import configparser
import traceback as tb

import telepot

import misc
import verbix
import settings
import templates


COMMAND_PATTERN = re.compile(
    r'^/(%s)(?: (.*))?' % '|'.join(settings.AVAILABLE_LANGUAGES))


bot = telepot.Bot(settings.TELEGRAM_BOT_TOKEN)
reporter_id = settings.TELEGRAM_REPORTER_ID

@misc.threaded
def handle_message(msg):
    message = msg['text']
    chat_id = msg['chat']['id']

    match = COMMAND_PATTERN.match(message)

    if not match:
        return

    bot.sendChatAction(chat_id, 'typing')

    language = match.group(1)
    verb = match.group(2)

    if verb is None:
        bot.sendMessage(
            chat_id, 'Tell me the verb you want me to conjugate along with '
            'the command!\nExample: `/swedish sjunga`', parse_mode='markdown')
        return

    try:
        verb_data = getattr(verbix, language).conjugate(verb)
        response = getattr(templates, language).render_response(verb_data)
        bot.sendMessage(chat_id, response[0], parse_mode='markdown',
                        reply_markup=response[1])

    except verbix.VerbNotFoundError as vnf:
        bot.sendMessage(chat_id, f'Couldn\'t find the verb _{vnf}_. :(',
                        parse_mode='markdown')

    except verbix.VerbixError:
        bot.sendMessage(
            chat_id,
            'Something happened while connecting to Verbix, and I could not '
            'complete your request. Please try again while I send a report to '
            'my developer.')
        bot.sendMessage(
            reporter_id,
            f'Search for {language}:{verb}\n\n{tb.format_exc()}.')

    except Exception:
        bot.sendMessage(
            chat_id,
            'Something strange happened while processing your request. '
            'Please try again while I let my developer know about this.')
        bot.sendMessage(
            reporter_id,
            f'Exception raised with message {message}:\n\n{tb.format_exc()}')


def handle_inline(query):
    id = query['id']
    verb = query['query']

    if verb == '':
        return

    unique_id = os.urandom(10).hex()

    bot.answerInlineQuery(id, cache_time=0, results=[{
        'type': 'article',
        'id': unique_id,
        'title': verb,
        'description': 'verbet "%s"' % verb,
        'input_message_content': {
            'message_text': 'Verbet: %s\n_Läser in..._' % verb,
            'parse_mode': 'markdown'
        }
    }])


def handle_chosen_inline(result):
    print(result)
    info = _get_verb_info(result['query'])

    print(info)

    bot.editMessageText(result['result_id'], text=info, parse_mode='markdown')


if __name__ == '__main__':
    bot.message_loop(
        handle_message, relax=0.5, timeout=5, run_forever='Listening...')
