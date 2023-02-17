#---------------------------------------------------------------
# ----------------------- Section RMa---------------------------
# --------------------------------------------------------------

import math

def formula_3GPP(d, d_2D, d_3d, d_BP, d_3D, dPrime_BP, h, h_BS, h_UT, f_c) :
    
    PL_RMaLOS, PL_RMaNLOS, PL_UMaLOS, PL_UMaNLOS, OptionalPL_UMaNLOS, PL_UMiLOS, PL_UMiNLOS = 0

    # LOS

    PL1_RMaLOS = 20 * math.log10( [40 * d_3d * f_c] / 3) + min(0.03 * pow(h,1.72), 10) * math.log10(d) \
        - min(0.044 * pow(h, 1.72), 14.77) + 0.002*math.log10(h) * d_3d

    PL2_RMaLos = PL1_RMaLOS * d_BP + 40 * math.log10(d_3d / d_BP)
    # PL2_RMaLos = 20 * math.log10( [40 * d_3d * f_c] / 3) + min(0.03 * pow(h,1.72), 10) * math.log10(d) \
    #     - min(0.044 * pow(h, 1.72), 14.77) + 0.002*math.log10(h) * d_3d + 40 * math.log10(d_3d / d_BP) 
    if d_2D < 10 :
        PL_RMaLOS = 0
    if d_2D < d_BP and 10 < d_2D :
        PL_RMaLOS = PL1_RMaLOS
    if d_2D < 10000 and d_BP < d_2D :
        PL_RMaLOS = PL2_RMaLos
    if d_2D > 10000  :
        PL_RMaLOS = 100

    # NLOS


    PLPrime_RMaNLOS = 161.04 - 7.1 * math.log10(W) + 7.5 * math.log10(h) - [24.37 - 3.7 * pow((h/h_BS),2)] \
        * math.log10(h_BS) + (43.42 - 3.1 * math.log10(h_BS)) * (math.log10(d_3D) -3) \
            + 20 * math.log10(f_c) - (3.2*math.pow((math.log10(11.75 * h_UT)),2) - 4.97) 

    PL_RMaNLOS = max(PL1_RMaLOS, PLPrime_RMaNLOS)

#---------------------------------------------------------------
# ----------------------- Section UMa---------------------------
# --------------------------------------------------------------


    # LOS 
    PL1_UMaLOS = 28 + 22 * math.log10(d_3D) + 20 * math.log10(f_c)

    PL2_UMaLOS = 28 + 40 * math.log10(d_3D) + 20 * math.log10(f_c) - 9 * math.log10(pow(dPrime_BP,2)+ \
        math.pow([h_BS - h_UT],2))
    if d_2D < 10 :
        PL_UMaLOS = 0
    elif d_2D < dPrime_BP and 10 < d_2D :
        PL_UMaLOS = PL1_UMaLOS
    elif d_2D < 5000 and dPrime_BP < d_2D :
        PL_UMaLOS = PL2_UMaLOS
    elif d_2D > 5000  :
        PL_UMaLOS = 100


    # NLOS 


    PLPrime_UMaNLOS = 13.54 + 39.08 * math.log10(d_3D) + 20 * math.log10(f_c) - 0.6 (h_UT - 1.5)

    PL_UMaNLOS = max(PL_UMaLOS, PLPrime_UMaNLOS)

    OptionalPL_UMaNLOS = 32.4 + 20 * math.log10(f_c) + 30 * math.log10(d_3D)

#---------------------------------------------------------------
# ----------------------- Section UMi---------------------------
# --------------------------------------------------------------
        
    # LOS

    PL1_UMiLOS = 32.4 + 21 * math.log10(d_3D) + 20 * math.log10(f_c)

    PL2_UMiLOS = 32.4 + 40 * math.log10(d_3D) + 20 * math.log10(f_c) - 9.5 * \
        math.log10(math.pow(dPrime_BP,2) + math.pow([h_BS - h_UT],2))

    if d_2D < 10 :
        PL_UMiLOS = 0
    elif d_2D < dPrime_BP and 10 < d_2D :
        PL_UMiLOS = PL1_UMaLOS
    elif d_2D < 5000 and dPrime_BP < d_2D :
        PL_UMiLOS = PL2_UMaLOS
    elif d_2D > 5000  :
        PL_UMiLOS = 100
    # NLOS 

    # PL1_UMiNLOS = 32.4 + 21 * math.log10(d_3D) + 20 * math.log10(f_c)
    # PL2_UMiNLOS = 32.4 + 40 * math.log10(d_3D) + 20 * math.log10(f_c) \
    #     - 9.5 * math.log10(math.pow(dPrime_BP,2) + math.pow([h_BS - h_UT],2))

    PLPrime_UMiNLOS = 22.4 + 35.4 * math.log10(d_3D) + 21.3 * math.log10(f_c) - 0.3 (h_UT - 1.5)

    PL_UMiNLOS = max(PL_UMiLOS, PLPrime_UMiNLOS)


    return PL_RMaLOS, PL_RMaNLOS, PL_UMaLOS, PL_UMaNLOS, OptionalPL_UMaNLOS, PL_UMiLOS, PL_UMiNLOS
