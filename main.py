from RsrvCurrModel import RsrvCurr

curr_code = input ("Enter currency code: ")

response = RsrvCurr(curr_code)

print ("Reserve Currency Exchange Rates")
print (f"{curr_code}-USD:{response.response_data().toUSD}")
print (f"{curr_code}-GBP:{response.response_data().toGBP}")
print (f"{curr_code}-EUR:{response.response_data().toEUR}")
print (f"{curr_code}-JPY:{response.response_data().toJPY}")