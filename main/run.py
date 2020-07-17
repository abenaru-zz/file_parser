from main.application import Main
from utils.system.logging import SystemLoggingHandler


def main():
    logger = SystemLoggingHandler('green', 'Abner Eduardo Ferreira')
    logger(print, 'I love you')


APPLICATION = Main(__name__ == '__main__')
APPLICATION(main, 10)
