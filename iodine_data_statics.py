import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import scipy.optimize as opt

plt.rcParams['font.family'] = ['YaHei Consolas Hybrid']  # 用来正常显示中文标签
# 测量日期
measure_data = np.array(
    ['2.20', '2.21', '2.22', '2.23', '2.24', '2.25', '2.26', '2.27', '2.28', '3.1', '3.2', '3.3', '3.4',
     '3.5', '3.6'])
# 本底计数
background_count = np.array([186, 199, 189, 170, 219, 213, 158, 188, 187, 174, 187, 184, 425, 451, 521])
# 冷开水计数1
cooled_boiled_water_count_1 = np.array(
    [13170, 11241, 10691, 9936, 8961, 8482, 7873, 6494, 6494, 5061, 4582, 4196, 10157, 10115,
     10185])
# 冷开水百分比1
cooled_boiled_water_percentage_1 = np.array(
    [99.83, 98.46, 100.64, 98.44, 98.3, 101.95, 97.93, 99.88, 98.17, 99.87, 103.54,
     104.53, 103.54, 99.97, 101.53])
# 冷开水计数2
cooled_boiled_water_count_2 = np.array(
    [13152, 11173, 10666, 9989, 9044, 8540, 7767, 6521, 6521, 4931, 4754, 4344, 10048, 10053,
     9997])
# 冷开水百分比2
cooled_boiled_water_percentage_2 = np.array(
    [101.02, 99.24, 103.69, 98.77, 100.75, 100.44, 101.74, 98.68, 98.58, 101.84, 100.87,
     98.67, 100.87, 101.1, 102.67])

# 冷开水计数3
cooled_boiled_water_count_3 = np.array(
    [13187, 11188, 10844, 9939, 9107, 8470, 7817, 6490, 6490, 4910, 4637, 4255, 9967, 10042,
     10052])
# 冷开水百分比3
cooled_boiled_water_percentage_3 = np.array(
    [99.06, 102.02, 98.55, 99.01, 97.32, 100.07, 100.27, 99.98, 99.79, 102.44, 103.72,
     100.49, 103.72, 98.94, 100.49])

# 冷开水计数4
cooled_boiled_water_count_4 = np.array(
    [13333, 11293, 10737, 10010, 8983, 8682, 7900, 6552, 6552, 4970, 4766, 4209, 10080, 10107,
     10101])
# 冷开水百分比4
cooled_boiled_water_percentage_4 = np.array(
    [99.11, 98.6, 101.95, 99.44, 101.82, 95.95, 99.75, 99.02, 99.05, 99.24, 99.43,
     102.43, 99.4, 101.2, 98.67])
# 冷开水计数5
cooled_boiled_water_count_5 = np.array(
    [12969, 11129, 10878, 9944, 9041, 8687, 7756, 6521, 6521, 5007, 4700, 4291, 10181, 10089,
     10060])
# 冷开水百分比5
cooled_boiled_water_percentage_5 = np.array(
    [100.62, 100.49, 98.26, 100.19, 98.58, 98.54, 102.11, 99.86, 99.79, 103.62, 101.57,
     101.5, 100.57, 100.3, 100.5])
# 矿泉水计数1
spring_water_count_1 = np.array(
    [13131, 11005, 10711, 9851, 9001, 8382, 7726, 6541, 6541, 5044, 4737, 4195, 9876, 10166, 10068])
# 矿泉水百分比1
spring_water_percentage_1 = np.array(
    [100.04, 101.89, 100.55, 99.85, 101.51, 103.7, 99.64, 99.6, 99.96, 96.73, 96.83, 99.85,
     96.83, 97.83, 100.67])
# 矿泉水计数2
spring_water_count_2 = np.array(
    [13039, 11226, 10748, 9921, 9065, 8356, 7790, 6481, 6481, 5033, 4650, 4317, 9917, 9955, 10061])
# 矿泉水百分比2
spring_water_percentage_2 = np.array(
    [101.33, 98.39, 99.5, 99.21, 100.53, 100.47, 98.99, 98.65, 97.6, 100.59, 99.05, 99.58,
     99.05, 100.05, 98.05])
# 矿泉水计数3
spring_water_count_3 = np.array(
    [13146, 11260, 10861, 9907, 8888, 8435, 7700, 6330, 6330, 4954, 4764, 4349, 9947, 9888, 10073])
# 矿泉水百分比3
spring_water_percentage_3 = np.array(
    [100.53, 99.95, 98.69, 100.08, 102.07, 99.89, 100.84, 101.22, 103.15, 102.46, 98.82, 94.21,
     98.82, 99.82, 99.82])

# 矿泉水计数4
spring_water_count_4 = np.array(
    [13035, 11146, 10697, 10009, 8942, 8484, 7908, 6486, 6486, 5029, 4776, 4213, 9964, 9982, 10091])
# 矿泉水百分比4
spring_water_percentage_4 = np.array(
    [100.56, 99.16, 102.31, 99.45, 102.31, 99.27, 97.84, 99.25, 99.15, 102.1, 98.75, 99.72,
     98.75, 97.75, 94.75])
# 矿泉水计数5
spring_water_count_5 = np.array(
    [13215, 11188, 10648, 9820, 8968, 8426, 7766, 6276, 6276, 5006, 4683, 4246, 9914, 9978, 10227])

# 矿泉水百分比5
spring_water_percentage_5 = np.array(
    [101.65, 100.8, 101.5, 99.27, 99.69, 99.34, 101.22, 102.3, 102.42, 97.76, 100.75, 100.49,
     100.75, 101.75, 99.66])
# 生理盐水计数1
normal_saline_count_1 = np.array(
    [13253, 11342, 10759, 9988, 8910, 8713, 7830, 6439, 6439, 5090, 4827, 4288, 10212, 10040, 10297])

# 生理盐水百分比1
normal_saline_percentage_1 = np.array(
    [100.16, 99.12, 100.49, 102.21, 101.81, 96.27, 98.81, 101.21, 102.25, 100.34, 96.23, 100.1,
     96.23, 96.78, 98.81])

# 生理盐水计数2
normal_saline_count_2 = np.array(
    [13175, 11285, 10837, 9957, 9200, 8691, 7865, 6591, 6591, 4887, 4782, 4233, 10137, 10018, 10267])
# 生理盐水百分比2
normal_saline_percentage_2 = np.array(
    [101.63, 100.44, 101.35, 98.72, 98.05, 99.31, 98.97, 99.97, 101.07, 105.81, 99.19, 100.14,
     99.19, 99.22, 96.97])
# 生理盐水计数3
normal_saline_count_3 = np.array(
    [13316, 11159, 10755, 9906, 9067, 8779, 7855, 9379, 6379, 5004, 4714, 4246, 10096, 9994, 10075])

# 生理盐水百分比3
normal_saline_percentage_3 = np.array(
    [98.35, 101.35, 100.52, 100.88, 99.93, 95.61, 100.14, 100.0, 101.69, 100.45, 101.63,
     105.04, 101.63, 101.53, 97.14])

# 生理盐水计数4
normal_saline_count_4 = np.array(
    [13508, 11328, 10738, 9847, 9068, 8687, 7896, 6533, 6533, 5007, 4876, 4252, 10089, 10182, 10059])

# 生理盐水百分比4
normal_saline_percentage_4 = np.array(
    [98.81, 99.1, 101.68, 101.23, 101.76, 98.09, 99.47, 99.98, 99.65, 103.05, 97.25, 100.58,
     97.25, 97.41, 99.47])

# 生理盐水计数5
normal_saline_count_5 = np.array(
    [13246, 11431, 10682, 9877, 8977, 8638, 7969, 6474, 6474, 5010, 4812, 4228, 10122, 10208, 10165])

# 生理盐水百分比5
normal_saline_percentage_5 = np.array(
    [98.43, 99.86, 10838.0, 101.35, 101.1, 100.97, 97.95, 99.63, 98.25, 99.97, 96.91, 102.27,
     96.91, 96.87, 98.95])
# 对照源计数1
reference_source_count_1 = np.array(
    [12960, 11283, 10766, 9873, 9001, 8484, 7830, 6567, 6567, 4903, 4588, 4255, 10154, 10250,
     10108])

# 对照源百分比1
reference_source_percentage_1 = np.array(
    [101.08, 98.98, 99.65, 98.71, 101.09, 99.38, 98.6, 99.63, 98.02, 101.6, 103.74, 101.94,
     103.74, 102.74, 98.1])

# 对照源计数2
reference_source_count_2 = np.array(
    [13138, 11103, 10676, 9942, 8981, 8531, 7509, 6661, 6610, 4984, 4685, 4300, 9896, 10010,
     10108])

# 对照源百分比2
reference_source_percentage_2 = np.array(
    [98.76, 100.5, 100.84, 98.39, 100.69, 99.47, 102.73, 98.35, 97.29, 100.04, 101.46,
     97.88, 101.46, 100.46, 96.33])

# 对照源计数3
reference_source_count_3 = np.array(
    [13214, 11158, 10604, 9895, 8840, 8425, 7879, 6349, 6592, 4976, 4674, 4176, 10118, 10272,
     10036])

# 对照源百分比3
reference_source_percentage_3 = np.array(
    [99.71, 101.75, 100.24, 100.1, 101.07, 98.1, 97.269, 100.22, 100.07, 100.52, 102.36,
     98.84, 102.36, 103.36, 100.07])

# 对照源计数4
reference_source_count_4 = np.array(
    [12892, 11095, 10644, 9834, 9009, 8402, 7664, 6381, 6349, 5001, 4677, 4221, 10219, 10039,
     10141])

# 对照源百分比4
reference_source_percentage_4 = np.array(
    [101.92, 99.27, 99.64, 102.11, 99.29, 101.11, 97.46, 100.23, 101.31, 98.69, 99.79,
     99.03, 99.79, 99.09, 101.31])

# 对照源计数5
reference_source_count_5 = np.array(
    [13207, 11005, 10637, 9823, 8890, 8321, 7812, 6380, 6380, 5005, 4687, 4349, 10166, 10021,
     10092])

# 对照源百分比5
reference_source_percentage_5 = np.array(
    [99.37, 101.38, 100.84, 99.81, 101.9, 101.26, 98.09, 101.32, 102.39, 99.17, 99.95,
     96.87, 99.95, 99.85, 102.39])
# 冷开水平均
cooled_boiled_water_count = (cooled_boiled_water_count_1 + cooled_boiled_water_count_2 +
                             cooled_boiled_water_count_3 + cooled_boiled_water_count_4 +
                             cooled_boiled_water_count_5) / 5
# 矿泉水平均
spring_water_count = (spring_water_count_1 + spring_water_count_2 +
                      spring_water_count_3 + spring_water_count_4 +
                      spring_water_count_5) / 5
# 生理盐水平均
normal_saline_count = (normal_saline_count_1 + normal_saline_count_2 +
                       normal_saline_count_3 + normal_saline_count_4 +
                       normal_saline_count_5) / 5
# 对照组平均
reference_source_count = (reference_source_count_1 + reference_source_count_2 +
                          reference_source_count_3 + reference_source_count_4 +
                          reference_source_count_5) / 5
# 冷开水-矿泉水源计数比较
plt.figure()
plt.plot(measure_data, cooled_boiled_water_count, label='冷开水平均源计数', marker='o')
plt.plot(measure_data, spring_water_count, label='矿泉水平均源计数', marker='o')
plt.title('冷开水-矿泉水源计数比较')
plt.xlabel('日期')
plt.ylabel('源计数')
plt.legend()
plt.show()

# 冷开水-生理盐水源计数比较
plt.figure()
plt.plot(measure_data, cooled_boiled_water_count, label='冷开水平均源计数', marker='o')
plt.plot(measure_data, normal_saline_count, label='生理盐水平均源计数', marker='o')
plt.title('冷开水-生理盐水源计数比较')
plt.xlabel('日期')
plt.ylabel('源计数')
plt.legend()
plt.show()

# 矿泉水-生理盐水源计数比较
plt.figure()
plt.plot(measure_data, spring_water_count, label='矿泉水平均源计数', marker='o')
plt.plot(measure_data, normal_saline_count, label='生理盐水平均源计数', marker='o')
plt.title('矿泉水-生理盐水源计数比较')
plt.xlabel('日期')
plt.ylabel('源计数')
plt.legend()
plt.show()

# 冷开水-对照组源计数比较
plt.figure()
plt.plot(measure_data, cooled_boiled_water_count, label='冷开水平均源计数', marker='o')
plt.plot(measure_data, reference_source_count, label='对照组平均源计数', marker='o')
plt.title('冷开水-对照组源计数比较')
plt.xlabel('日期')
plt.ylabel('源计数')
plt.legend()
plt.show()

# 矿泉水-对照组源计数比较
plt.figure()
plt.plot(measure_data, spring_water_count, label='矿泉水平均源计数', marker='o')
plt.plot(measure_data, reference_source_count, label='对照组平均源计数', marker='o')
plt.title('矿泉水-对照组源计数比较')
plt.xlabel('日期')
plt.ylabel('源计数')
plt.legend()
plt.show()

# 生理盐水-对照组源计数比较
plt.figure()
plt.plot(measure_data, normal_saline_count, label='生理盐水平均源计数', marker='o')
plt.plot(measure_data, reference_source_count, label='对照组平均源计数', marker='o')
plt.title('生理盐水-对照组源计数比较')
plt.xlabel('日期')
plt.ylabel('源计数')
plt.legend()
plt.show()

# 计算序列的显著性差异
print('序列的显著性差异')
# 冷开水-参照组
r_cool_reference, p_cool_reference = stats.pearsonr(cooled_boiled_water_count, reference_source_count)
print([r_cool_reference, p_cool_reference])
# 矿泉水-参照组
r_spring_reference, p_spring_reference = stats.pearsonr(spring_water_count, reference_source_count);
print([r_spring_reference, p_spring_reference])
# 生理盐水-参照组
r_saline_reference, p_saline_reference = stats.pearsonr(normal_saline_count, reference_source_count)
print([r_saline_reference, p_saline_reference])

# 方差运算
print('方差运算')
diff_cool_reference = cooled_boiled_water_count - reference_source_count
diff_spring_reference = spring_water_count - reference_source_count
diff_saline_reference = normal_saline_count - reference_source_count
print(diff_cool_reference)
print(diff_spring_reference)
print(diff_saline_reference)
diff_cool_reference_mean = np.mean(diff_cool_reference)
diff_cool_reference_var = np.var(diff_cool_reference)
print((diff_cool_reference_mean, diff_cool_reference_var))

diff_spring_reference_mean = np.mean(diff_spring_reference)
diff_spring_reference_var = np.var(diff_spring_reference)
print((diff_spring_reference_mean, diff_spring_reference_var))

diff_saline_reference_mean = np.mean(diff_saline_reference)
diff_saline_reference_var = np.var(diff_saline_reference)
print((diff_saline_reference_mean, diff_saline_reference_var))
