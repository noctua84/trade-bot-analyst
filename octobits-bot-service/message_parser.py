import re

from telethon.tl.types import Message


def parse_trade_update(message: Message):
    data = {'message_id': message.id, 'timestamp': int(message.date.timestamp())}

    pattern = re.compile(r'''
            [^\w\s]*\sTotal\ deals:\s(?P<total_deals>\d+)\n
            [^\w\s]*\sSuccessful:\s(?P<successful>\d+)\n
            [^\w\s]*\sUnsuccessful:\s(?P<unsuccessful>\d+)\n
            [^\w\s]*\sPercentage\ of\ profit:\s(?P<profit_percentage>[0-9.]+)\ %
        ''', re.VERBOSE)

    match = pattern.search(message.message)

    if match:
        result = match.groupdict()

        data['total_deals'] = int(result['total_deals'])
        data['successful'] = int(result['successful'])
        data['unsuccessful'] = int(result['unsuccessful'])
        data['profit_percentage'] = float(result['profit_percentage'])

    return data


def parse_octobits_account_update(message: Message):
    data = {'message_id': message.id, 'timestamp': int(message.date.timestamp())}

    pattern = re.compile(r'''
            [^\w\s]*\sCurrent\ balance:\s(?P<current_balance>[0-9.]+)\s(?P<current_currency>\w+)\n\n
            .*?\n\n
            [^\w\s]*\sTotal\ withdrawal:\s(?P<total_withdrawal>[0-9.]+)\s(?P<withdrawal_currency>\w+)\n\n
            .*?\n\n
        ''', re.VERBOSE)

    match = pattern.search(message.message)

    if match:
        result = match.groupdict()

        # Current balance
        data['current_balance'] = {
            'amount': float(result['current_balance']),
            'currency': result['current_currency']
        }

        # Total withdrawal
        data['total_withdrawal'] = {
            'amount': float(result['total_withdrawal']),
            'currency': result['total_withdrawal_currency']
        }

    return data
