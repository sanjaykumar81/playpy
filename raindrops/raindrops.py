def convert(number):
    ppp_dic = {"3" : "Pling", "5" : "Plang", "7" : "Plong"}
    msg =""
    if number % 3 ==0:
        msg = ppp_dic[str(3)]
    if number % 5 ==0:
        msg = msg + ppp_dic[str(5)]
    if number % 7 ==0:
        msg = msg + ppp_dic[str(7)]
    if (number%2 == 0 or number%2 == 1) and msg == "":
        msg= str(number)

    return  msg
