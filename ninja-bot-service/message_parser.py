import re

from telethon.tl.types import Message
from datetime import datetime


def parse_trading_update(message: Message):
    strategies = {}
    pattern = re.compile(r'([A-Z\s]+)\nTrades: (\d+) \| Wins: (\d+) \| Losses: (\d+) \| Profit: ([\d.]+)%', re.MULTILINE)

    matches = pattern.findall(message.message)

    for match in matches:
        strategy_name, trades, wins, losses, profit = match
        strategies[strategy_name.strip()] = {
            "trades": int(trades),
            "wins": int(wins),
            "losses": int(losses),
            "profit": float(profit)
        }

    return strategies


def parse_ninja_account_update(message: Message):
    parsed_data = {}
    pattern = re.compile(r'''
        [^\w\s]*\sBalance:\s(?P<balance_amount>\d+\.\d+)\s(?P<balance_currency>\w+)\n\n
        [^\w\s]*\sStrategy:\s(?P<strategy_amount>\d+\.\d+)\s(?P<strategy_currency>\w+)\n\n
        [^\w\s]*\sStrategy\sStatus:\s(?P<strategy_status>.+?)\n\n
        [^\w\s]*\sWithdrawal:\s(?P<withdrawal_amount>\d+\.\d+)\s(?P<withdrawal_currency>\w+)\n\n
        .*?\n\n
        .*?\n\n
        [^\w\s]*\sIncome:\s(?P<income>\d+\.\d+)
    ''', re.VERBOSE)

    match = pattern.search(message.message)

    if match:
        result = match.groupdict()
        result['strategy_status'] = [status.strip() for status in result['strategy_status'].split('|')]

        parsed_data = {
            'balance': {'amount': float(result['balance_amount']), 'currency': result['balance_currency']},
            'strategy': {'amount': float(result['strategy_amount']), 'currency': result['strategy_currency']},
            'withdrawal': {'amount': float(result['withdrawal_amount']), 'currency': result['withdrawal_currency']},
            'strategy_status': result['strategy_status'],
            'income': float(result['income'])
        }

    return parsed_data


def parse_bot_trading_update(message: Message):
    strategies = {}
    pattern = re.compile(r'''
            [^\w\s]*\s(?P<strategy_name>[A-Z\s]+)\n
            [^\w\s]*\sTotal\strades:\s(?P<trades>\d+)\n
            [^\w\s]*\sSuccessful:\s(?P<successful>\d+)\n
            [^\w\s]*\sUnsuccessful:\s(?P<unsuccessful>\d+)\n
            [^\w\s]*\sProfit:\s(?P<profit>[\d.]+)%
        ''', re.VERBOSE)

    matches = pattern.finditer(message.message)

    for match in matches:
        strategy_name = match.group('strategy_name').strip()
        trades = int(match.group('trades'))
        successful = int(match.group('successful'))
        unsuccessful = int(match.group('unsuccessful'))
        profit = float(match.group('profit'))

        strategies[strategy_name] = {
            "trades": trades,
            "successful": successful,
            "unsuccessful": unsuccessful,
            "profit": profit
        }

    print(int(message.date.timestamp()))
    print(message.id)

    return strategies
