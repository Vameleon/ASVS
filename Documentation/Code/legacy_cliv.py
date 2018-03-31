FREQ_LVL_REF = ["' ____________'","' |___________'","' ||__________'","' ||||________'","' ||||||||____'","' ||||||||||||'"]
FREQ_LVL_CUR=[0,0,0,0,0,0,0,0,0,0]
# print lables: Frequency Level Vector.....f0 range, f1 range,....,etc
print("                           0-30         30          150          320           600          1100         3k           5k           7.1k         10.1k")
print("Freq. LVL Vect             f0R          f1R         f2R          f3R           f4R          f5R          f6R          f7R          f8R          f9R")

for i in range (0,FREQ_DOMAIN_NUM_RANGES):
            if FREQ_DOMAIN[i] == 0:
                 FREQ_LVL_CUR[i]=FREQ_LVL_REF[0]
            elif FREQ_DOMAIN[i] <=4 and FREQ_DOMAIN[i] > 0:
                 FREQ_LVL_CUR[i]=FREQ_LVL_REF[1]
            elif FREQ_DOMAIN[i] <=8 and FREQ_DOMAIN[i] > 4:
                 FREQ_LVL_CUR[i]=FREQ_LVL_REF[2]
            elif FREQ_DOMAIN[i] <=12 and FREQ_DOMAIN[i] > 8:
                 FREQ_LVL_CUR[i]=FREQ_LVL_REF[3]
            elif FREQ_DOMAIN[i] <=16 and FREQ_DOMAIN[i] > 12:
                 FREQ_LVL_CUR[i]=FREQ_LVL_REF[4]
            elif FREQ_DOMAIN[i] <=FREQ_DOMAIN_CEILING and FREQ_DOMAIN[i] > 16:
                 FREQ_LVL_CUR[i]=FREQ_LVL_REF[5]

       OS.system("echo -en " + str(FREQ_DOMAIN) + str(FREQ_LVL_CUR[0]) + str(FREQ_LVL_CUR[1]) + str(FREQ_LVL_CUR[2]) + str(FREQ_LVL_CUR[3]) +str(FREQ_LVL_CUR[4]) +str(FREQ_LVL_CUR[5]) +str(FREQ_LVL_CUR[6]) + str(FREQ_LVL_CUR[7]) + str(FREQ_LVL_CUR[8])+ str(FREQ_LVL_CUR[9]) + "\r")