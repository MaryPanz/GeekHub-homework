"""2. Написати функцію <bank> , яка працює за наступною логікою: користувач робить вклад у розмірі 
<a> одиниць строком на <years> років під <percents> відсотків (кожен рік сума вкладу збільшується на цей відсоток, 
ці гроші додаються до суми вкладу і в наступному році на них також нараховуються відсотки). Параметр <percents> є 
необов'язковим і має значення по замовчуванню <10> (10%).
Функція повинна принтануть суму, яка буде на рахунку, а також її повернути (але округлену до копійок)."""

money = int(input("Money: "))
years = int(input("Years: "))

def bank(money, years, percent = 0.1):
    try:
        for i in range(years):
            result = "{:.2f}".format(money * (pow((1 + percent), 1 * (i + 1))))
        return f"Total: ${result}"
    except UnboundLocalError:
        return("Years can't be smaller than 0!")
  
print(bank(money, years, percent = 0.1))
