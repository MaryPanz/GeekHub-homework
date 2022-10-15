s = "qw9s8d"

def write_length(s):
    if len(s) > 29 and len(s) < 51:
        numbers = sum(i.isdigit() for i in s)
        letters = sum(i.isalpha() for i in s)
        print(f"Length: {len(s)}. Letters: {(letters)}. Numbers: {(numbers)}")
    elif len(s) < 31:
        sum_all = 0
        all_letters = ""
        for i in s:
            if i.isdigit():
                sum_all += int(i)
            else:
                all_letters += i             
        print(f"Sum of all numbers: {sum_all} Only letters: {all_letters}")
    else: 
        print(f"All uppercase: {s.upper()}.")
        
write_length(s)
