import numpy as np
from scipy.interpolate import interp1d

# # 27-piece dataset (last two columns)
# data_27_pieces = [
#     [4.44089E-16, -1.45000E+01],
#     [3.00000E+00, -1.45000E+01],
#     [6.00000E+00, -1.44851E+01],
#     [7.00004E+00, -1.44610E+01],
#     [8.70051E+00, -1.43388E+01],
#     [1.04020E+01, -1.40201E+01],
#     [1.22046E+01, -1.33904E+01],
#     [1.32065E+01, -1.29371E+01],
#     [1.50100E+01, -1.19445E+01],
#     [1.82151E+01, -9.98243E+00],
#     [2.14178E+01, -8.45147E+00],
#     [2.46189E+01, -7.46417E+00],
#     [2.78193E+01, -6.72916E+00],
#     [3.10194E+01, -6.08842E+00],
#     [3.42197E+01, -5.49322E+00],
#     [4.02204E+01, -4.39222E+00],
#     [4.66217E+01, -3.09315E+00],
#     [5.30232E+01, -1.75629E+00],
#     [5.94245E+01, -5.00650E-01],
#     [6.58255E+01, 6.01964E-01],
#     [7.22261E+01, 1.55560E+00],
#     [7.90266E+01, 2.51935E+00],
#     [8.05267E+01, 2.72950E+00],
#     [8.20271E+01, 2.93201E+00],
#     [8.35274E+01, 3.11874E+00],
#     [8.50277E+01, 3.28847E+00],
#     [8.63655E+01,	3.42796E+00]
# ]
#
#
# def reshape_column_to_27_pieces(data_39_pieces_col1, target_data_27_pieces_col1):
#     """
#     Reshapes the first column of the 39-piece dataset into 27 pieces with the same
#     relative difference in distance as the target 27-piece dataset.
#
#     Parameters:
#     - data_39_pieces_col1: List of values from the first column of the 39-piece dataset.
#     - target_data_27_pieces_col1: List of values from the first column of the target 27-piece dataset.
#
#     Returns:
#     - Reshaped 27-piece data for the first column.
#     """
#     # Normalized indices for the 39-piece and 27-piece data
#     x_39 = np.linspace(0, 1, len(data_39_pieces_col1))
#     x_27 = np.linspace(0, 1, len(target_data_27_pieces_col1))
#
#     # Interpolate the 39-piece data to 27 pieces
#     interpolate_func = interp1d(x_39, data_39_pieces_col1, kind='linear')
#     reshaped_27_col1 = interpolate_func(x_27)
#
#     return reshaped_27_col1
#
#
# # Example data (first column of the new 39-piece dataset)
# data_39_pieces_col1 = [
#     0.0000E+00, 2.0777E+00, 4.8950E+00, 5.6056E+00, 6.5644E+00, 7.7653E+00, 9.2020E+00,
#     1.0864E+01, 1.2744E+01, 1.4829E+01, 1.7107E+01, 1.9564E+01, 2.2185E+01, 2.4956E+01,
#     2.7858E+01, 3.0875E+01, 3.3990E+01, 3.7181E+01, 4.0431E+01, 4.3720E+01, 4.7030E+01,
#     5.0339E+01, 5.3628E+01, 5.6876E+01, 6.0065E+01, 6.3177E+01, 6.6190E+01, 6.9089E+01,
#     7.1854E+01, 7.4471E+01, 7.6923E+01, 7.9195E+01, 8.1272E+01, 8.3145E+01, 8.4801E+01,
#     8.6230E+01, 8.7423E+01, 8.8374E+01
# ]
#
#
# # Example target data (first column of the 27-piece dataset you provided earlier)
# target_data_27_pieces_col1 = [
#     4.44089E-16, 3.00000E+00, 6.00000E+00, 7.00004E+00, 8.70051E+00, 1.04020E+01, 1.22046E+01,
#     1.32065E+01, 1.50100E+01, 1.82151E+01, 2.14178E+01, 2.46189E+01, 2.78193E+01, 3.10194E+01,
#     3.42197E+01, 4.02204E+01, 4.66217E+01, 5.30232E+01, 5.94245E+01, 6.58255E+01, 7.22261E+01,
#     7.90266E+01, 8.05267E+01, 8.20271E+01, 8.35274E+01, 8.50277E+01, 8.63655E+01
# ]
#
# # Reshape the first column of the 39-piece data to match the 27-piece structure
# reshaped_27_col1 = reshape_column_to_27_pieces(data_39_pieces_col1, target_data_27_pieces_col1)
#
# target_twist_39 = [20.,         20. ,        20.  ,       20.   ,      20.,         20.,
#  20.   ,      20.  ,       20.     ,    20.  ,       19.93012779 ,17.38105656,
#  14.60433568 ,11.88843532 , 9.18062142 , 6.50975033 , 4.7714802  , 3.66577912,
#   2.73069462 , 1.89225188 , 1.14105808 , 0.47106307 ,-0.12428942 ,-0.65080625,
#  -1.11517968, -1.52349385, -1.884398,   -2.2025173 , -2.47778103, -2.71258817,
#  -2.91155519, -3.08081674 ,-3.22781436, -3.35439884 ,-3.46191378, -3.55152144,
#  -3.62427552, -3.68088139, -3.72196621]
#
# for index, value in enumerate(target_twist_39):
#     target_twist_39[index] = -value
#
#
# reshaped_twist = reshape_column_to_27_pieces(target_twist_39 , data_27_pieces[:][1])
#
# # Print the reshaped 27 pieces
# for value in reshaped_27_col1:
#     print(value)


# 39 data points (x-values and y-values)


"""Array with updated radial positions, ie BB_RWT_ae"""
r_39 = np.array([0., 2.07767195, 4.89499511, 5.60555892, 6.56440452, 7.76529891,
                 9.20200906, 10.86414662, 12.74443974, 14.82938354, 17.10651199,
                 19.56439791, 22.18538107, 24.95595662, 27.85846433, 30.875244,
                 33.98967425, 37.18097837, 40.43149613, 43.72045083, 47.03018224,
                 50.33887482, 53.62782952, 56.87626961, 60.06549605, 63.1768098,
                 66.19047296, 69.08882533, 71.85420669, 74.47103451, 76.92268741,
                 79.19462169, 81.27229364, 83.1453149, 84.80121944, 86.22961891,
                 87.42324144, 88.37377636, 89.07602948])

"""Array with twists from single point design"""
twist_39 = np.array([20., 20., 20., 20., 20., 20., 20., 20., 20., 20.,
                 19.93012779, 17.38105656, 14.60433568, 11.88843532,
                 9.18062142, 6.50975033, 4.7714802, 3.66577912, 2.73069462,
                 1.89225188, 1.14105808, 0.47106307, -0.12428942, -0.65080625,
                 -1.11517968, -1.52349385, -1.884398, -2.2025173, -2.47778103,
                 -2.71258817, -2.91155519, -3.08081674, -3.22781436,
                 -3.35439884, -3.46191378, -3.55152144, -3.62427552,
                 -3.68088139, -3.72196621])

"""
# Target r-values (27 data points) from master.htc file with scaled factor"""
scale_ratio_blade = 1.0388359746215876
r_27 = scale_ratio_blade * np.array([4.44089E-16, 3.00000E+00, 6.00000E+00, 7.00004E+00, 8.70051E+00,
                 1.04020E+01, 1.22046E+01, 1.32065E+01, 1.50100E+01, 1.82151E+01,
                 2.14178E+01, 2.46189E+01, 2.78193E+01, 3.10194E+01, 3.42197E+01,
                 4.02204E+01, 4.66217E+01, 5.30232E+01, 5.94245E+01, 6.58255E+01,
                 7.22261E+01, 7.90266E+01, 8.05267E+01, 8.20271E+01, 8.35274E+01,
                 8.50277E+01, 8.63655E+01])

# Interpolating the y-values from 39 points to match 27 points
twist_27_interp = np.interp(r_27, r_39, twist_39)

# Print the interpolated twist value
# print(twist_27_interp)

"""Actual twist is negative inside hawc2 so we put the minus sign"""
twist_27 = -twist_27_interp

print(twist_27)