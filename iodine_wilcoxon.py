import scipy.stats
import numpy as np
import xlrd

data_columns = [1, 3, 5, 7]
workbook = xlrd.open_workbook('data2018.xls')
sheet = workbook.sheet_by_index(0)


def wilcox_test(standard, test):
    result = scipy.stats.ranksums(standard, test)
    # result = scipy.stats.wilcoxon(standard, test, zero_method='wilcox', correction=False)

    return result


def get_data(standard_start, test_start, standard_length=3, test_length=3):
    standard_data = []
    test_data = []
    for column in data_columns:
        standard_temp = 0.0
        test_temp = 0.0
        for i in range(standard_length):
            standard_temp += sheet.cell(standard_start + i, column).value / standard_length
            test_temp += sheet.cell(test_start + i, column).value / test_length
        standard_data.append(standard_temp)
        test_data.append(test_temp)
    return np.array(standard_data), np.array(test_data)


def calculate(name, standard_start, test_start, standard_length=3, test_length=3):
    print('start calculate %s' % name)
    (standard_data, test_data) = get_data(standard_start, test_start, standard_length, test_length)
    # print('standard')
    # print(standard_data)
    # print('test_data')
    # print(test_data)
    (s, p) = wilcox_test(standard_data, test_data)
    print('static: %f , p-value: %f' % (s, p))


calculate('矿泉水6.8', 9, 12)
calculate('矿泉水7.3', 50, 53)
calculate('矿泉水7.28', 90, 93)
calculate('矿泉水8.18', 130, 133)

calculate('普通水6.8', 17, 20)
calculate('普通水7.3', 57, 60)
calculate('普通水7.28', 97, 100)
calculate('普通水8.18', 137, 140)

calculate('纯净水6.8', 24, 27)
calculate('纯净水7.3', 64, 67)
calculate('纯净水7.28', 104, 107)
calculate('纯净水8.18', 144, 147)

calculate('离子水6.8', 31, 34)
calculate('离子水7.3', 71, 74)
calculate('离子水7.28', 111, 114)
calculate('离子水8.18', 151, 154)

calculate('0.9%盐水6.8', 38, 41)
calculate('0.9%盐水7.3', 78, 81)
calculate('0.9%盐水7.28', 118, 121)
calculate('0.9%盐水8.18', 158, 161)
