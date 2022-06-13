import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        record_sum_day = 0
        for i in self.records:

            if i.date == dt.date.today():
                record_sum_day += i.amount
        return record_sum_day

    def get_week_stats(self):
        get_week_sum = 0
        for i in self.records:
            week = dt.timedelta(weeks=1)
            if i.date > (dt.date.today() - week):
                get_week_sum += i.amount
        return get_week_sum


class Record:
    def __init__(self, amount, comment='', date=None):
        self.amount = amount
        self.comment = comment
        if date is not None:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        else:
            self.date = dt.datetime.now().date()
        
class CashCalculator(Calculator):
    USD_RATE = 36.52
    EURO_RATE = 43.42

    def get_today_cash_remained(self, currency):
        cash_sum = self.get_today_stats()
        if currency == 'usd':
            cash_rest = round((self.limit - cash_sum) / self.USD_RATE, 2)
            currency = 'USD'
        elif currency == 'eur':
            cash_rest = round((self.limit - cash_sum) / self.EURO_RATE, 2)
            currency = 'Euro'
        else:
            cash_rest = round(self.limit - cash_sum, 2)
            currency = 'руб'

        if cash_rest > 0:
            return f'На сегодня осталось {cash_rest} {currency}'
        elif cash_rest < 0:
            return f'Денег нет! твой долг: '\
                   f'{abs(cash_rest)} {currency}'
        else:
            return 'Денег нет!'


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        calories_sum = self.get_today_stats()
        calories_rest = self.limit - calories_sum
        if calories_rest > 0:
            return f'Сегодня можно съесть что-нибудь ещё '\
                   f'с калорийностью не более {calories_rest} кКал'
        else:
            return 'Хватит есть!'
