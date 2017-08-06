# Telegram Verbix

Bem-vindo ao repositório do **Telegram Verbix**!

(Looking for the English version? [Click here](./README.md))

| Conteúdo                          |
| --------------------------------- |
| [Sobre](#sobre)                   |
| [Licenciamento](#licenciamento)   |
| [Instalação](#instalação)         |
| [Execução](#execução)             |
| [Contribuições](#contribuições)   |
| [Instruções](#instruções)         |

***

## Sobre
Este é um repositório que trata de idiomas e gramática. Sendo mais específico, sobre conjugação
de verbos.

Eu iniciei este projeto por causa da necessidade de consultar a conjugação de alguns verbos em
em Sueco sem precisar abrir o navegador. A grande maioria de nós é adepta aos smartphones; é
de grande conveniência conseguir fazer várias coisas através de apenas um aplicativo. No meu caso,
eu gosto de programar bots na plataforma do [Telegram](https://telegram.org/). Receber conjugações
dos verbos no meu aplicativo de mensagens de escolha torna as coisas mais fáceis. E eu espero que
ajude outras pessoas também.

## Licenciamento
Eu escolhi a licença Creative Commons BY 4.0 porque, apesar de gostar da GPL, não acho que combina
a pregação de liberdade deles com a imposição de tornar o código alheio aberto. Com a CC BY 4.0,
você pode usar este *software* em projetos tanto pessoais quanto comerciais, modificar o fonte para
se adaptar às suas necessidades, etc. Para mais informações, segue até o arquivo contendo a
[licença](./LICENSE) (em inglês).

**Observação**: Este software usa conteúdo explícito do [verbix](http://www.verbix.com/).
**De forma alguma** a licença usada neste repositório anula, cancela, substitui (ou derivados) a
licença original do verbix.

## Instalação
Clone este repositório:

    git clone https://github.com/Fawers/telegram-verbix.git

(opcional) Crie um ambiente virtual e ative-o:

    python3 -m virtualenv .venv
    . ./.venv/bin/activate

Instale as dependências:

    pip install -r requirements.txt


## Execução
Para executar o bot, você vai precisar criar um arquivo chamado `project.ini` de onde o script
lerá algumas configurações. Abaixo segue o modelo para o arquivo:

    [bot]
    token = your-telegram-bot-token
    reporter_id = your-telegram-user-id

Você consegue um token de bot falando com o [@botfather](https://t.me/botfather).  
Você pode saber seu id de usuário falando com o [@my_id_bot](https://t.me/my_id_bot).


## Contribuições
Mesmo de sempre: *fork*, crie um novo *branch*, coda, *commit*, *push*, *pull request*.

***

# Instruções
Para instruções de como usar o bot, siga para o arquivo de [instruções](./INSTRUCTIONS-ptbr.md).
