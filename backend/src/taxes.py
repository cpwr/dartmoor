import argparse
import calendar
import requests

from datetime import date, timedelta
from functools import partial


STATUS_SUCCESS = 'SUCCESS'
STATUS_ERROR = 'ERROR'


def get_headers(app_id, token):
    content_type = "application/json;charset=utf8"
    return {
        "Content-Type": content_type,
        "id": app_id,
        "token": token,
    }

current_year = date.today().year
last_day_of_month = lambda month: date(
    year=current_year,
    month=month,
    day=int(list(filter(
        lambda x: x.isdigit(),
        calendar.month(current_year, month).replace("\n", " ").split(" ")))[-1]
    )
)
first_day_of_month = partial(date, year=current_year, day=1)

periods = {
    x + 1: [
        first_day_of_month(month=x * 3 or 1),
        last_day_of_month(month=x * 3 + 3 or 3)
    ] for x in range(0, 4)
}

format_date = lambda d: d.strftime("%d-%m-%Y")


def fetch_data(app_id, token, account_id, period_index):
    first_day, last_day = periods.get(period_index, [None, None])
    if not first_day or not last_day:
        print("WRONG START OR END PERIOD DATES")
        return

    params = {
        "startDate": format_date(first_day),
        "endDate": format_date(last_day),
        "acc": account_id,
    }
    try:
        resp = requests.get(
            "https://acp.privatbank.ua/api/statements/transactions",
            params=params,
            headers=get_headers(app_id, token),
        )
    except:
        print("ERROR GETTING TRANSACTION INFO FROM BANK")
        return {}
    else:
        data = resp.json()
        # print(data["transactions"][0:2])
        if resp.ok:
            if data.get("status") == STATUS_SUCCESS:
                return
        else:
            if data.get("status") == STATUS_ERROR:
                print(f"ERROR: {data['message']}, code: {data['code']}")
                return


def fetch_currency_rates(app_id, token, first_day, last_day):
    if last_day - first_day > timedelta(days=15):
        return {}

    params = {
        "startDate": format_date(first_day),
        "endDate": format_date(last_day),
    }
    try:
        resp = requests.get(
            "https://acp.privatbank.ua/api/proxy/currency/history",
            params=params,
            headers=get_headers(app_id, token),
        )
    except:
        print("ERROR GETTING TRANSACTION INFO FROM BANK")
        return {}
    else:
        return resp.json()


def get_dates(start, end, days_in_chunk=14):
    number_of_intervals = int((end - start).days / days_in_chunk)
    yield start
    last_processed = start
    for i in range(number_of_intervals):
        last_processed += timedelta(days=days_in_chunk)
        yield last_processed
    yield end


def get_date_ranges(start, end):
    if not isinstance(start, date) or not isinstance(end, date):
        print("ERROR PARSING DATES RANGE")
        return

    dates = sorted(list(set(get_dates(start, end))))
    return [dates[i: i + 2] for i, el in enumerate(dates)][:-1]


def get_currency_rates_for_the_period(app_id, token, period_index):
    between_dates = periods.get(period_index, [None, None])
    return {
        f"{first_day} - {last_day}": fetch_currency_rates(
            first_day=first_day,
            last_day=last_day,
            app_id=app_id,
            token=token,
        )
        for first_day, last_day in get_date_ranges(*between_dates)
    }


parser = argparse.ArgumentParser(description='Calculate taxes and income amounts')

parser.add_argument(
    '--id', '-i',
    type=str,
    dest='id',
    help='a string that contains your app\'s ID',
    required=True,
)
parser.add_argument(
    '--token', '-t',
    type=str,
    dest='token',
    help='a string that contains your token',
    required=True,
)
parser.add_argument(
    '--acc', '-a',
    type=str,
    dest='account_id',
    help='Account number to get data for',
    required=True,
)
parser.add_argument(
    '--period', '-p',
    type=int,
    dest='period',
    help='an integer to specify a period',
    choices=[1, 2, 3, 4],
    required=True,
)

args = parser.parse_args()
print(f"WILL FETCH DATA FOR THE {args.period} PERIOD")

app_id = args.id
token = args.token
account_id = args.account_id
period_index = args.period

fetch_data(
    app_id=app_id,
    token=token,
    account_id=account_id,
    period_index=period_index,
)

print(get_currency_rates_for_the_period(
    app_id=app_id,
    token=token,
    period_index=period_index,
))

