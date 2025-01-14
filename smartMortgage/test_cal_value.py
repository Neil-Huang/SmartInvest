import numpy as np
from matplotlib import pyplot as plt
import matplotlib

#numpy计算复利
# periodic_payment = -np.pmt(rate=0.056/12, nper=300, pv=35 *10000)
# print("每月的按揭还款额: " + str(round(periodic_payment, 2)))

# 参考: [[Python]等额本息房贷计算器 - Fia - 博客园](https://www.cnblogs.com/FiaFia/p/8580414.html)
#       [等额本息法_百度百科](https://baike.baidu.com/item/%E7%AD%89%E9%A2%9D%E6%9C%AC%E6%81%AF%E6%B3%95/11049926)
# 工具: [招商银行 -- 个人贷款计算器](https://www.cmbchina.com/CmbWebPubInfo/Cal_Loan_Per.aspx?chnl=dkjsq)
#      [贷款计算器](https://jinrong.sogou.com/calculator#)


def monthlyPayment(principal, year_rate=0.049, year_duration=30):
    """
    等额本息

    Args:
        principal (int): 贷款金额
        year_rate (float): 贷款利率
        year_duration (int): 贷款年限

    Returns:
        result_1 (float): 总利息
    """


    monthly_rate = year_rate / 12
    #monthly_rate = year_rate / (12 * 100)   # convert 4.9 to 0.049 and  monthly interest rate
    month_amounts = year_duration * 12

    # 每月月供
    monthly_payment = (principal * monthly_rate * (1 + monthly_rate) ** month_amounts) / ((1 + monthly_rate) ** month_amounts - 1)

    #总利息
    total_interest_payable = monthly_payment * month_amounts - principal
    # print('-----------------------------------')
    # print ('Total interest payable is %.2f ' % total_interest_payable)

    dic_monthly_payment = {}
    for i in range (1, month_amounts + 1):
        #每月应还利息
        monthly_interest_payable = principal * monthly_rate * ((1 + monthly_rate) ** month_amounts - (1 + monthly_rate) ** (i - 1 ))/ ((1 + monthly_rate) ** month_amounts -1)
        #每月应还本金
        monthly_principal_payable = principal * monthly_rate * (1 + monthly_rate) ** (i - 1)/ ((1 + monthly_rate) ** month_amounts -1)
        #每月利息占比
        monthly_interest_percentage = monthly_interest_payable * 100 / monthly_payment

        dic_monthly_payment[i] = round(monthly_payment,2)
        # print('-----------------------------------')
        # print ('%dth monthly payment is : %.2f (Interest: %.2f and Principal: %.2f)' % (i, monthly_payment,monthly_interest_payable,monthly_principal_payable))
        # print('%dth month interest percentage is %.2f %%' % (i,monthly_interest_percentage))

    return dic_monthly_payment


def monthlyPayment2(principal, year_rate, year_duration):
    """等额本金"""
    monthly_rate = year_rate / 12
    #monthly_rate = year_rate / (12 * 100)  # convert 4.9 to 0.049 and  monthly interest rate
    month_amounts = year_duration * 12

    # 每月应还本金
    monthly_principal_payable = principal / month_amounts
    total_interest_payable =0 #总利息

    dic_monthly_payment = {}
    for i in range(1, month_amounts + 1):
        # 每月应还利息
        monthly_interest_payable = (principal - monthly_principal_payable*(i-1)) * monthly_rate
        total_interest_payable += monthly_interest_payable
        # 每月月供
        monthly_payment = monthly_principal_payable + monthly_interest_payable

        dic_monthly_payment[i] = round(monthly_payment,2)
        #print('-----------------------------------')
        #print('%dth monthly payment is : %.2f (Interest: %.2f and Principal: %.2f)' % (
        #i, monthly_payment, monthly_interest_payable, monthly_principal_payable))

    # print(round(total_interest_payable,2))
    return dic_monthly_payment


# 定义变量
house_price    = 127 * 10000  # 房子总价
current_wealth =  80 * 10000  # 当前可用资金
loan_rate = 0.052  # 贷款利率
loan_years = 25  # 贷款年限


house_yearly_i_rate = 0.01  #房子每年增值率
family_month_income  = 1.0  *10000   #家庭每月收入
family_month_expense = 0.5  *10000  #家庭每月支出


def cal_value(down_payment_rate=0.3, financial_yearly_return_rate=0.03, loan_type=1):
    """
    计算付款方式的价值

    Parameters
    ----------
    down_payment_rate: 首付比例
    financial_yearly_return_rate: 理财的年收益率
    loan_type: 贷款方式 1=等额本息 2=等额本金  默认为1

    Returns
    -------

        返回  房子资产,现金资产

        example:
        house_wealth,cash_wealth

    """

    years = loan_years
    down_payment = house_price * down_payment_rate  # 首付
    # 首付比例可能超过现有资金(优化)
    if down_payment > current_wealth:
        down_payment_rate = round(current_wealth / house_price, 2)
        down_payment = current_wealth

    # 先算出每月月供
    if loan_type == 1:
        dic_monthly_payment = monthlyPayment(house_price - down_payment, loan_rate, loan_years)
    else:
        # 等本每月的计算
        dic_monthly_payment = monthlyPayment2(house_price - down_payment, loan_rate, loan_years)

    # print(dic_monthly_payment)

    #房子增值
    house_wealth = house_price
    for this_year in range(0, years):
        house_wealth = house_wealth * (1 + house_yearly_i_rate)

    # 现金增值
    cash_wealth = current_wealth - down_payment
    # print(cash_wealth)

    #年利率计算理财要优化
    financial_monthly_return_rate = financial_yearly_return_rate / 12
    # print(financial_monthly_return_rate)
    for this_month in range(0, years * 12):
        cash_wealth = cash_wealth * (1 + financial_monthly_return_rate) + family_month_income - family_month_expense
        if this_month <= loan_years * 12:
            cash_wealth = cash_wealth - dic_monthly_payment[this_month + 1]

        # print(this_month + 1, " ", cash_wealth)

    hv, cv = round(house_wealth, 2), round(cash_wealth, 2)
    print("参数:首付", down_payment_rate, "年收益率", financial_yearly_return_rate,
          "贷款方式", '等息' if loan_type == 1 else '等本',
          "  总价:", round((hv + cv), 2), "房子资产:", hv, "现金资产:", cv)
    return hv, cv

#初始化图
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.88, 0.88])


def cal_value_and_show(down_payment_rate=0.3, financial_yearly_return_rate=0.03, loan_type=1):
    hv, cv = cal_value(down_payment_rate, financial_yearly_return_rate, loan_type)
    key = str(down_payment_rate * 10) + "" + str(financial_yearly_return_rate * 100) + "" + str(loan_type);
    x = [key]
    y = [cv]
    ax.bar(x, y, align='center')
    return hv, cv

"""
    结论: 
      如果理财能力 > 商贷  -> 低首付等息
      如果理财能力 <=商贷  -> 高付等本
"""

if __name__ == '__main__':
    # principal = int(input('Please input your loan amounts:'))
    # year_rate = float(input('Please input Year Debt Interest Rate:(such as 4.9,it means 4.9%)'))
    # year_duration = int(input('Please input Debt Year Duration:'))
    principal = 1000000
    year_rate = 4.9
    year_duration = 30
    #monthlyPayment(principal, year_rate, year_duration)
    #monthlyPayment2(principal, year_rate, year_duration)

    # 年收益不同
    # hv10, cv10 = cal_value_and_show(0.3, 0.02)
    # hv20, cv20 = cal_value_and_show(0.6, 0.02)
    # hv30, cv30 = cal_value_and_show(0.3, 0.02, 2)
    # hv40, cv40 = cal_value_and_show(0.6, 0.02, 2)

    #
    my_year_rate = 0.05
    hv10, cv10 = cal_value_and_show(0.3, my_year_rate)
    hv20, cv20 = cal_value_and_show(0.6, my_year_rate)
    hv30, cv30 = cal_value_and_show(0.3, my_year_rate, 2)
    hv40, cv40 = cal_value_and_show(0.6, my_year_rate, 2)





    # # 首付不同
    # cal_value_and_show(0.3, 0.02)
    # cal_value_and_show(0.4, 0.02)
    # cal_value_and_show(0.5, 0.02)
    # cal_value_and_show(0.6, 0.02)
    #
    # cal_value_and_show(0.3, 0.02, 2)
    # cal_value_and_show(0.4, 0.02, 2)
    # cal_value_and_show(0.5, 0.02, 2)
    # cal_value_and_show(0.6, 0.02, 2)


    # # 显示图
    # fig = plt.figure()
    # ax = fig.add_axes([0.1, 0.1, 0.88, 0.88])
    # x = ['31', '33', '36', '39']
    # y = [cv0, cv1, cv2, cv3]
    # ax.bar(x, y, align='center')
    #
    # x2 = ['61', '63', '66', '69']
    # y2 = [cv20, cv21, cv22, cv23]
    # ax.bar(x2, y2, color='g', align='center')
    #
    # x3 = ['312', '332', '362', '392']
    # y3 = [cv30, cv31, cv32, cv33]
    # ax.bar(x3, y3, align='center')
    #
    # x4 = ['612', '632', '662', '692']
    # y4 = [cv40, cv41, cv42, cv43]
    # ax.bar(x4, y4, color='y', align='center')

    #另一种图
    # fig2 = plt.figure()
    # ax2 = fig2.add_axes([0.1, 0.1, 0.88, 0.88])
    # ax2.plot(x,y,"ob")
    # ax2.plot(x2, y2)
    # ax2.plot(x3, y3)

    plt.show()
