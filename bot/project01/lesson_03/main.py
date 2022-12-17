def price_with_ndc(price):
    ndc = 20 / 100
    new_price = price + ndc * price
    return new_price


print(price_with_ndc(130))


def stock_with_ndc(price1, price2, stock):
    ndc = 20 / 100
    new_price1 = price1 + ndc * price1
    new_price2 = price2 + ndc * price2
    price = new_price1 + new_price2
    stock_price = price - price * (stock / 100)
    return stock_price


print(stock_with_ndc(130, 150, 25))
