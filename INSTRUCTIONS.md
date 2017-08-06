# Instructions

Telegram, as of Aug 2017, comes in three flavors:

1. Smartphone app
2. Desktop app
3. Web app

On both the desktop and web apps, you can type the first `/` to list the available commands,
and traverse through them with the arrow keys. If you press `Enter` (`Return`), you'll send the
command directly, but the bot needs the command to be followed by the verb you want to conjugate.  
Press `Tab` instead and it will autocomplete the command and place a space after it so you just
have to type in the verb.

On the smartphone apps, there is a little `/` button, right next to the *send* button. On touch,
the app shows the available commands; pressing one of them sends the command, while *holding* one
of them will autocomplete the command, followed by a space, where you can just input the verb.

The `/` button looks like this: ![slash button](./slash.png)

## The bot
The bot is accessible under the username [@verb_conjugator_bot](https://t.me/verb_conjugator_bot).

## Querying
To query for a verb, you must send `/language verb`. See examples below for each implemented language:

* Swedish: `/swedish läsa`
* Japanese:
  * `/japanese yomu`
  * `/japanese よむ`

**Do** note that I didn't write any *kanji* for Japanese. Since verbs can have more than one
associated *kanji*, you should always use either *hiragana* or *rōmaji*.