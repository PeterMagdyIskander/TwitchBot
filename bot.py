import socket

HOST = "irc.twitch.tv"
PORT = 6667
NICK =input("what channel to send this message to : ")
PASS = 'oauth:el6nkk6rnfoodagsm5hak0x8llxo5y'

def send_message(message):
    s.send(bytes("PRIVMSG #" + NICK + " :" + message + "\r\n", "UTF-8"))

s = socket.socket()
s.connect((HOST, PORT))
s.send(bytes("PASS " + PASS + "\r\n", "UTF-8"))
s.send(bytes("NICK " + NICK + "\r\n", "UTF-8"))
s.send(bytes("JOIN #" + NICK + " \r\n", "UTF-8"))

choices=[
    'who is pokimane? 🙄🤭🤔🤫😰 in math: my solution ➗😊 in history: my queen 👑😣 in art: my canvas 🎨🥳 in science: my oxygen 💨😝 in geography: my world 🌎🤯',
    'TRUE KEKW TRUE KEKW TRUE KEKW TRUE KEKW TRUE KEKW TRUE KEKW TRUE KEKW TRUE KEKW TRUE KEKW ',
    '(◕‿◕✿) Dear Weebs in the chat AYAYA, you are sugoi AYAYA. Whatever is going on in your kokoro right now AYAYA, please know that you are kawaii and your story is not a filler AYAYA. You are loved (◕‿◕✿)',
    'I feel so bad for people who unironically like anime. Like, they didn\'t choose to be born with an IQ of 20 in a home with unloving parents. Imagine all the bullying they must experience at home, at school, and at the special services daycare. Let\'s stop bullying them, guys. They may be too retarded to understand that\'s what we\'re doing, but that doesn\'t mean we should pick on them. Thank you'   
]


m=int(input('from 0 to 3 : '))
send_message(choices[m])