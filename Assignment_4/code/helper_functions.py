import numpy as np
import pandas as pd


def extract_and_order_statistics(wsps, chan_df, seeds):
    """
    Extract and order:
     - wsp, max, mean, min for the points
     - wsp, mean_max, mean_mean, mean_min for the mean lines
    """

    # extract hawc2 wind and channel to plot from the HAWC2 stats
    val_wsp, val_max, val_mean, val_min = chan_df['wsp'], chan_df['max'], chan_df['mean'], chan_df['min']
    val_wsp, val_max, val_mean, val_min = np.array(val_wsp), np.array(val_max), np.array(val_mean), np.array(val_min)
    i_val = np.argsort(val_wsp)

    # Get mean of max/mean/min
    mean_max = np.average(val_max[i_val].reshape(-1, seeds), axis=1)
    mean_mean = np.average(val_mean[i_val].reshape(-1, seeds), axis=1)
    mean_min = np.average(val_min[i_val].reshape(-1, seeds), axis=1)

    points = {
        'wsp': val_wsp[i_val],
        'max': val_max[i_val],
        'mean': val_mean[i_val],
        'min': val_min[i_val]
    }

    lines = {
        'wsp': wsps,
        'max': mean_max,
        'mean': mean_mean,
        'min': mean_min
    }

    return points, lines


def extract_and_combine_DEL(wsps, chan_df, seeds, m):
    """
    Extract and combine DEL values (del4, del4, del5, del8, del10, del12) from chan_df.
    
    Parameters:
        wsps (array-like): Wind speed values for each simulation.
        chan_df (DataFrame): Dataframe with DEL columns for each wind speed.
        seeds (int): Number of seeds used for averaging.
        m (int): [3, 4, 5, 8, 10, 12]
        
    Returns:
        points (dict): Ordered DEL values (mean of del4, del4, etc.) for each wind speed.
        lines (dict): Mean DEL values over seeds for each wind speed.
    """
    if m not in [3, 4, 5, 8, 10, 12]:
        raise ValueError("Wrong m value given!")
    else:
        del_col = f'del{m}'
    
    # Extract wind speed data and DEL columns
    val_wsp = np.array(chan_df['wsp'])
    
    # Sort indices based on wind speed
    i_val = np.argsort(val_wsp)
    
    # Initialize dictionaries to store ordered DEL values
    points = {'wsp': val_wsp[i_val]}
    lines = {'wsp': wsps}

    # Extract and order the DEL data for this column
    
    del_data = np.array(chan_df[del_col])[i_val]
    
    # Using Miner's Rule
    del_values = del_data.reshape(-1, seeds)
    combined_del = (np.sum(del_values ** m , axis=1)  / seeds) ** (1 / m) # m is the WOhler Exponent
    # TODO: CHECK THAT VALUES MATCH TXT!!!!!
   
    # Store the mean values in the dictionaries
    points['del'] = del_data
    lines['del'] = combined_del

    return points, lines


def propability_wsp(wsp, wind_class, step=1):
    """
    Calculate propability of wsp based on standard (AEP lecture, p. 15)

    If you give "wsp" as np.array you will get np.array!!!
    """
    # Referense wind spped of the class
    if wind_class == 'I':
        V_ref = 50      
    elif wind_class == 'II':
        V_ref = 42.5
    elif wind_class == 'III':
        V_ref = 37.5
    else:
        raise ValueError('Wrong "wind_class" given. It should be "I"/"II"/"III"')
    u = 0.2*V_ref

    return np.exp(-((wsp-step/2)/(2*u/np.sqrt(np.pi)))**2) - np.exp(-((wsp+step/2)/(2*u/np.sqrt(np.pi)))**2)


def lifetime_eq_load(R_eq_list, P_wsp_list, m, n_seeds=1, n_eq_L=1E7, n_T=(20*365*24*60*60)):
    """
    Calculate lifetime equivalant loads (Taesong slides p. 41)

    Supposedly "n_seeds=1" for things to work?!
    """
    n_TS = n_T / n_seeds

    # Just in case we accidentaly give list
    R_eq_list = np.array(R_eq_list)
    P_wsp_list = np.array(P_wsp_list)

    return ((1/n_eq_L) * np.sum(R_eq_list**m * P_wsp_list * n_TS))**(1/m)


def calculate_AEP_per_wsp(power_arr, P_wsp_arr, hours_per_year=8760):
    """
    Calculate AEP per wsp in GWh
    """
    AEP_per_wsp = power_arr * P_wsp_arr * hours_per_year / 1E9

    return AEP_per_wsp 


# JUST FOR TESTING:
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    
    # propability_list_big = []
    # wsp_list = np.arange(1, 24, 1)
    # for wind_class in ['I', 'II', 'III']:
    #     propability_list = []
    #     for wsp in wsp_list:
    #         propability_list.append(propability_wsp(wsp, wind_class))
        
    #     print(sum(propability_list))
    #     propability_list_big.append(propability_list)


    # plt.figure()
    # for i in range(3):
    #     plt.plot(wsp_list, propability_list_big[i])
    # plt.xlim(0, 25)
    # plt.ylim(0, 0.25)
    # plt.grid()
    # plt.show()
    
    # R_eq_list = [
    #     46860.78173262,
    #     60533.72498661,
    #     59165.75222735,
    #     49669.98028487,
    #     48249.13096179,
    #     41188.70573419,
    #     40341.05873765,
    #     39077.21951565,
    #     37340.02415617,
    #     36937.69987989,
    #     39649.01740049,
    #     43179.18330751,
    #     41795.27733207,
    #     42207.91706777,
    #     46612.72861644,
    #     48856.4751121,
    #     49077.04325018,
    #     54465.85842442,
    #     53021.0998996,
    #     54357.18578793
    # ]

    P_wsp_list = [
        0.06442809,
        0.0709227,
        0.07472189,
        0.07591763,
        0.0747455,
        0.07155162,
        0.06675382,
        0.06080169,
        0.05413969,
        0.04717648,
        0.04026251,
        0.03367663,
        0.02762128,
        0.02222493,
        0.01755019,
        0.01360521,
        0.01035688,
        0.00774379,
        0.00568809,
        0.0041053
    ]

    R_eq_list = [
        17528.85012336,
        17980.90689827,
        18424.01358451,
        18954.59389128,
        19614.57007687,
        20024.96591811,
        20163.54249103,
        20119.58099582,
        20215.68591207,
        20691.56928174,
        21365.45685207,
        22022.12272444,
        22418.16234013,
        22617.88916884,
        23863.27556859,
        24139.13997924,
        24091.16722585,
        25119.5457805, 
        24834.12472743,
        25542.50181907,
    ]

    m = 10
    Lifetime_fatigue_load = lifetime_eq_load(R_eq_list, P_wsp_list, m=m, n_seeds=1, n_eq_L=1E7, n_T=(20*365*24*60*60))

    # Lifetime_fatigue_load = Lifetime_fatigue_load * 1.25

    # target = 129826.22850291798
    target = 31017.45970934247

    print((target-Lifetime_fatigue_load)/target*100)


