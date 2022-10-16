"""4. Наприклад маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfe kdno400we(nw,kowe%00koi!jn35pijnp4 6ij7k5j78p3kj546p4 65jnpoj35po6j345" 
-> просто потицяв по клавi =)
   Створіть ф-цiю, яка буде отримувати довільні рядки на зразок цього та яка обробляє наступні випадки:
-  якщо довжина рядка в діапазоні 30-50 (включно) -> прiнтує довжину рядка, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всіх чисел та окремо рядок без цифр та знаків лише з буквами (без пробілів)
-  якщо довжина більше 50 -> щось вигадайте самі, проявіть фантазію =)"""


s = "qw9s8d"

def write_length(s):
    if len(s) > 29 and len(s) < 51:
        numbers = sum(i.isdigit() for i in s)
        letters = sum(i.isalpha() for i in s)
        print(f"Length: {len(s)}. Letters: {letters}. Numbers: {numbers}")
    elif len(s) < 31:
        sum_all = 0
        all_letters = ""
        for i in s:
            if i.isdigit():
                sum_all += int(i)
            elif i.isalpha():
                all_letters += i             
        print(f"Sum of all numbers: {sum_all} Only letters: {all_letters}")
    else: 
        print(f"All uppercase: {s.upper()}.")
        
write_length(s)
