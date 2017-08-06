# Telegram Verbix

Welcome to the **Telegram Verbix** repository page!

(Procurando pela versão em Português? [Clique aqui](./README-ptbr.md))

| Table of Contents             |
| ----------------------------- |
| [About](#about)               |
| [License](#license)           |
| [Installation](#installation) |
| [Running](#running)           |
| [Contributing](#contributing) |
| [Instructions](#instructions) |

***

## About
This is a repository about languages (as in tongues), and grammar. More specifically,
verb conjugating.

I started this project with the need to query some verb conjugations in Swedish without really
having to open the browser. Since we're all mostly on smartphones now, it's just convenient to have
one app do many things for us. In my case, I do some bot programming on the [Telegram](https://telegram.org/)
platform. Having verbs conjugated on the messenger app is easier for me, just as I think it will be
for other people.

## License
As for the licensing, I chose to go with *Creative Commons BY 4.0*. Even though I like the GPL,
I don't think the source disclosure enforcement is a good example of the freedom they preach so
much about. With CC BY 4.0, you're free to use this software for both private and commercial
projects, modify the source code to adapt to your own needs, etc. Head to the [LICENSE](./LICENSE)
file for further information.

**Note**: This software explicitely uses content from [verbix](http://www.verbix.com/). **In no way**
does the license used in this repositoy nullify, void, replace, or any derivatives of these, the
ones from verbix itself.

## Installation
Clone this repository:

    git clone https://github.com/Fawers/telegram-verbix.git

(optional) Create a virtualenv and activate it:

    python3 -m virtualenv .venv
    . ./.venv/bin/activate

Install the dependencies:

    pip install -r requirements.txt


## Running
In order to run the bot, you'll need to create a file called `project.ini`, which the script
can read some configuration from. Template is as follows:

    [bot]
    token = your-telegram-bot-token
    reporter_id = your-telegram-user-id

You can get a bot token by talking to the [@botfather](https://t.me/botfather).  
You can get your user id by talking to [@my_id_bot](https://t.me/my_id_bot).


## Contributing
Same as usual: fork, checkout to new branch, code, commit, push, pull request.

***

# Instructions
For instructions on how to actually use the bot, head to the [instructions](./INSTRUCTIONS.md) file.
