import re

def normalize_phone(phone_number: str) -> str:
    # keep '+' sign (but only at start of string), or keep numbers
    pattern = r"^\+|\d+"
    plus_sign = "+"
    internation_code = "38"

    # lstrip() simplifies handling of cases when there's some spaces beform '+' sign
    matches = re.findall(pattern, phone_number.lstrip())

    if len(matches) > 0:
        # at this point we have only allowed symbols
        cleared_phone_number = "".join(matches)

        # the only thing left is to add internation code - and we're good to go
        result_number: str
        if not cleared_phone_number.startswith(plus_sign):
            if cleared_phone_number.startswith(internation_code):
                # only plus needed
                result_number = plus_sign + cleared_phone_number
            else:
                # add internation code as well
                result_number = plus_sign + internation_code + cleared_phone_number
        else:
            # number is already formatted correcly
            result_number = cleared_phone_number

        return result_number
    else:
        # log warning and fallback to empty string to avoid crash
        print(f"Log: we have completely malformed phone_number here: {phone_number}")
        return ""



def test_normalize():
    raw_numbers = [
        "067\\t123 4567",
        "(095) 234-5678\\n",
        "+380 44 123 4567",
        "test_for_crash",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    pre_sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    
    # exclude failed results
    sanitized_numbers = list(filter(lambda x: len(x) > 0, pre_sanitized_numbers))
    print("Sanitized numbers are:\n", sanitized_numbers)


test_normalize()