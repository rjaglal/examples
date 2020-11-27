def discount_calculation(income: int) -> float:
    """
    The function calculates the discount depending on the income. The income input is of type integer and
    the discount is of type float

    :param income: Integer income used to decide the discount
    :return: The function returns the discount which is a float
    """

    discount = 0.0

    if 0 <= income <= 10000:
        discount = 0.2
    elif 10001 <= income <= 30000:
        discount = 0.1
    elif income >= 30000:
        discount = 0.05

    return discount


if __name__ == '__main__':

    # Over here you will need to look at your teacher examples on how to accept input in c++
    print('Please enter housing value and income range: ')

    # In my example I am hard coding the values, but you will need to read them in from the user.
    housing_value = 500000
    income_range = 9000

    # At this point I am calculating the discount as a decimal. According to the question it is questing that it
    # be from a function.
    print(discount_calculation(income_range))

    # At this point I am taking the discount as a decimal and multiplying it by the housing_value to find the
    # discount as money
    discount_as_money = discount_calculation(income_range) * housing_value
    print(discount_as_money)

    # At this point I am finding out the discounted price of the house. I am taking the housing value and minus the
    # discount as money
    discounted_price = housing_value - discount_as_money
    print(discounted_price)

    # Output as request by the question
    # Please remember to type cast.
    # As shown below I am type casting the discount_as_money decimal to an integer and then I am casting it to a string
    # The same is casting is repeated for discounted_price
    print('Discount is $' + str(int(discount_as_money)) + ' and discounted price is $' + str(int(discounted_price)))
