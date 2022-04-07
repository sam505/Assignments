# operation computes provincial taxes for the input gross income...
def computeProvTaxes(grossIncome):  # Step 2.1.1
    if grossIncome <= 39147.00:
        tax = grossIncome * 0.087
    elif 39147.01 <= grossIncome <= 78294.00:
        tax = (grossIncome - 39147.01) * 0.145 + 3405.789
    elif 78294.01 <= grossIncome <= 139780.00:
        tax = (grossIncome - 78294.01) * 0.158 + 5676.31355 + 3405.789
    elif 139780.01 <= grossIncome <= 195693.00:
        tax = (grossIncome - 139780.01) * 0.178 + 9714.78642 + 5676.31355 + 3405.789
    elif 195693.00 <= grossIncome <= 250000.00:
        tax = (grossIncome - 195693.00) * 0.198 + 9952.51222 + 9714.78642 + 5676.31355 + 3405.789
    elif 250000.01 <= grossIncome <= 500000.00:
        tax = (grossIncome - 250000.01) * 0.20 + 10752.786 + 9952.51222 + 9714.78642 + 5676.31355 + 3405.789
    elif 500000.01 <= grossIncome <= 1000000.00:
        tax = (grossIncome - 250000.01) * 0.213 + 49999.998 + 10752.786 + 9952.51222 + 9714.78642 + 5676.31355 + \
              3405.789
    else:
        tax = (grossIncome - 1000000.01) * 0.218 + 106499.99787 + 49999.998 + 10752.786 + 9952.51222 + 9714.78642 + \
              5676.31355 + 3405.789
    return tax


# operation computes federal taxes for the input gross income
def computeFedTaxes(grossIncome):  # Step 2.1.2

    if grossIncome <= 50197.00:
        tax = grossIncome * 0.15
    elif 50197.01 <= grossIncome <= 100392.00:
        tax = (grossIncome - 50197.01) * 0.205 + 7529.55

    elif 100392.01 <= grossIncome <= 155625.00:
        tax = (grossIncome - 100392.01) * 0.26 + 10289.97295 + 7529.55
    elif 155625.01 <= grossIncome <= 221708.00:
        tax = (grossIncome - 155625.01) * 0.29 + 14360.5774 + 10289.97295 + 7529.55
    else:
        tax = (grossIncome - 221708.00) * 0.33 + 19164.0671 + 14360.5774 + 10289.97295 + 7529.55
    return tax


### Beginning of Step 3 - Computing employee's CPP
def computeCPP(grossIncome):
    tax = grossIncome * 0.057
    if tax > 3499.80:
        tax = 3499.80
    return tax


### Beginning of Step 4 - Computing employee's EI
def computeEI(grossIncome):
    tax = grossIncome * 0.0158
    if tax > 952.74:
        tax = 952.74
    return tax


def computeHealthPremium(grossIncome):
    if grossIncome <= 22000.00:
        premium_tax = 0
    elif 22000 < grossIncome <= 38000.00:
        premium_tax = (grossIncome - 22000.00) * 0.06
        if premium_tax > 300:
            premium_tax = 300
    elif 38000 < grossIncome <= 50000.00:
        premium_tax = (grossIncome - 38000.00) * 0.06 + 300
        if premium_tax > 450:
            premium_tax = 450
    elif 50000 < grossIncome <= 74000.00:
        premium_tax = (grossIncome - 50000.00) * 0.25 + 450
        if premium_tax > 600:
            premium_tax = 600
    elif 74000 < grossIncome <= 202000.00:
        premium_tax = (grossIncome - 74000.00) * 0.25 + 600
        if premium_tax > 750:
            premium_tax = 750
    else:
        premium_tax = (grossIncome - 202000.00) * 0.25 + 750
        if premium_tax > 900:
            premium_tax = 900

    return premium_tax


# Function computes net incomes by invoking
def computeNetIncomes(grossIncomeList):  # Step 2
    net_income = []
    deductions = computeDeductions(grossIncomeList)
    for i in range(len(grossIncomeList)):
        net_income.append(grossIncomeList[i] - deductions[i])
    return net_income


# Function computes net incomes by invoking
def computeDeductions(grossIncomeList):  # Step 2
    deductions_list = []
    for grossIncome in grossIncomeList:
        premium_tax = computeHealthPremium(grossIncome)
        ei = computeEI(grossIncome)
        cpp = computeCPP(grossIncome)
        fed_taxes = computeFedTaxes(grossIncome)
        prov_taxes = computeProvTaxes(grossIncome)
        deductions_list.append(premium_tax + ei + cpp + fed_taxes + prov_taxes)
    return deductions_list
