def say_number(numeral):
    numbers = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    groups = ['', 'Thousand', 'Million', 'Billion', 'Trillion', 'Quadrillion', 'Quintillion']

    if numeral == 0:
        return 'Zero.'

    words = ''
    group_index = 0

    while numeral > 0:
        group = numeral % 1000
        hundreds = group // 100
        tens_and_ones = group % 100

        group_words = ''

        if hundreds > 0:
            group_words += f"{numbers[hundreds]} Hundred"
            if tens_and_ones > 0:
                group_words += ' '

        if tens_and_ones > 0:
            if tens_and_ones < 20:
                group_words += f"{numbers[tens_and_ones]}"
            else:
                tens_place = tens_and_ones // 10
                ones_place = tens_and_ones % 10
                group_words += f"{tens[tens_place]}"
                if ones_place > 0:
                    group_words += f"-{numbers[ones_place]}"

        if group_index > 0 and group_words:
            group_words += f" {groups[group_index]}"

        words = f"{group_words} {words}"
        numeral //= 1000
        group_index += 1

    return words.strip() + '.'

print(say_number(6))