from currency_bot import run_currency_bot

if __name__ == '__main__':
    with open('currency bot/token_1.txt', 'r') as f:
        TOKEN = f.readline()

    # # run bot
    run_currency_bot(TOKEN)
