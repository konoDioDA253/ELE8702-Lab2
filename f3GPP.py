#---------------------------------------------------------------
# ----------------------- Section RMa---------------------------
# --------------------------------------------------------------

import math

def formula_3GPP(d, d_3d, d_BP, d_3D, dPrime_BP, h, h_BS, h_UT, f_c) :
# LOS
    print("entered 3GPP formula function")
    PL = 3
    return PL

    # PL1_RMaLOS = 20 * math.log10( [40 * d_3d * f_c] / 3) + min(0.03 * pow(h,1.72), 10) * math.log10(d) \
    #     - min(0.044 * pow(h, 1.72), 14.77) + 0.002*math.log10(h) * d_3d

    # PL2_RMaLos = PL1_RMaLOS * d_BP + 40 * math.log10(d_3d / d_BP)
        

    # # NLOS

    # PL_RMaNLOS = max(PL1_RMaLOS, PLPrime_RMaNLOS)

    # PLPrime_RMaNLOS = 161.04 - 7.1 * math.log10(W) + 7.5 * math.log10(h) - [24.37 - 3.7 * pow((h/h_BS),2)] \
    #     * math.log10(h_BS) + (43.42 - 3.1 * math.log10(h_BS)) * (math.log10(d_3D) -3) \
    #         + 20 * math.log10(f_c) - (3.2*math.pow((math.log10(11.75 * h_UT)),2) - 4.97) 

    # #---------------------------------------------------------------
    # # ----------------------- Section UMa---------------------------
    # # --------------------------------------------------------------


    # # LOS 

    # PL1_UMALOS = 28 + 22 * math.log10(d_3D) + 20 * math.log10(f_c)

    # PL2_UMALOS = 28 + 40 * math.log10(d_3D) + 20 * math.log10(f_c) - 9 * math.log10(pow(dPrime_BP,2)+ \
    #     math.pow([h_BS - h_UT],2))

    # # NLOS 

    # PL_UMaNLOS = max(PLUMaLOS, PLPrime_UMaNLOS)

    # PLPrime_UMaNLOS = 13.54 + 39.08 * math.log10(d_3D) + 20 * math.log10(f_c) - 0.6 (h_UT - 1.5)

    # OptionalPL = 32.4 + 20 * math.log10(f_c) + 30 * math.log10(d_3D)

    # #---------------------------------------------------------------
    # # ----------------------- Section UMi---------------------------
    # # --------------------------------------------------------------
        
    # # LOS

    # PL1_UMiLOS = 32.4 + 21 * math.log10(d_3D) + 20 * math.log10(f_c)

    # PL2_UMiLOS = 32.4 + 40 * math.log10(d_3D) + 20 * math.log10(f_c) - 9.5 * \
    #     math.log10(math.pow(dPrime_BP,2) + math.pow([h_BS - h_UT],2))

    # # NLOS 

    # PL1_UMiNLOS = 32.4 + 21 * math.log10(d_3D) + 20 * math.log10(f_c)
    # PL2_UMiNLOS = 32.4 + 40 * math.log10(d_3D) + 20 * math.log10(f_c) \
    #     - 9.5 * math.log10(math.pow(dPrime_BP,2) + math.pow([h_BS - h_UT],2))
