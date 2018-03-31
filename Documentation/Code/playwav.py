# Written by Tariq A.
# Thanks to https://www.rototron.info for inspiring me to use the numpy FFT
# https://www.wavtones.com/functiongenerator.php allowed me to generate audio signals
# https://www.audiocheck.net/audiofrequencysignalgenerator_sweep.php allowed me to generate audio signals
# Additional wav files were found online and are put in Documentation/Impl.../Med../

# Main purpose is visualizing the Human Audio Spectrum ~16 Hz - ~16 kHz
# Current implementaion of this python program exits (when audio file reaches NULL) with a value error





import alsaaudio as alsa
import wave
from struct import unpack
import numpy as NP
import os as OS
import sys as SYS






#-------------------------------------------------------------------------
# VARs
WAVFILE = str(SYS.argv[1])
print("\nMain purpose is visualizing the Human Audio Spectrum ~16 Hz - ~16 kHz")
print("\n")
print("Input file: " + WAVFILE)

FREQ_DOMAIN = [0,0,0,0,0,0,0,0,0,0]
weighting = [2,2,8,8,16,16,32,32,64,64] 
FREQ_LVL_CUR=[0,0,0,0,0,0,0,0,0,0]
#FREQ_LVL_CUR_THRES=[0,0,0,0,0,0,0]     #Thresholding frequency levels in Real-time
FREQ_LVL_REF = ["' ____________'","' |___________'","' ||__________'","' ||||________'","' ||||||||____'","' ||||||||||||'"]
FREQ_DOMAIN_CEILING = 20           #Domain roof. FYI: floor is at 0
FREQ_DOMAIN_NUM_RANGES = 10
AMP= []
# End of #VARs
#-------------------------------------------------------------------------



#-------------------------------------------------------------------------
# WAVSAMPLE
# Audio setup
WAVSAMPLE = wave.open(WAVFILE,'r')
SAMPLING_RATE = WAVSAMPLE.getframerate()
NUM_CH = WAVSAMPLE.getnchannels()
BLOCKS = 4096    #2^x

print ("Blocks at a time: " + str(BLOCKS))
print("The number of channels: "+ str(NUM_CH))
print("The sampling rate: " + str(SAMPLING_RATE) + " Hz")
print("\n")
# End of #WAVSAMPLE
#-------------------------------------------------------------------------





#-------------------------------------------------------------------------
# ALSA
ALSA_OUT = alsa.PCM(alsa.PCM_PLAYBACK, alsa.PCM_NORMAL)
ALSA_OUT.setchannels(NUM_CH)
ALSA_OUT.setrate(SAMPLING_RATE)
ALSA_OUT.setformat(alsa.PCM_FORMAT_S16_LE)
ALSA_OUT.setperiodsize(BLOCKS)
# End of #ALSA
#-------------------------------------------------------------------------








#-------------------------------------------------------------------------
# Return AMP array index corresponding to a particular frequency
def piff(arG):
   return int(2*BLOCKS*arG/SAMPLING_RATE) #arG = 1 --> (2*4096*1)/22050
   
def GET_LVLs(data, BLOCKS,SAMPLING_RATE):
   global FREQ_DOMAIN

   # Convert raw data (ASCII string) to numpy array
   data = unpack("%dh"%(len(data)/2),data)
   data = NP.array(data, dtype='h')

   # Apply FFT - real data
   FFT=NP.fft.rfft(data)
   # Remove last element in array to make it the same size as BLOCKS
   FFT=NP.delete(FFT,len(FFT)-1)
   
   
   
   # Find average 'amplitude' for specific frequency ranges in Hz
   AMP = NP.abs(FFT)   #absolute
   
   FREQ_DOMAIN[0]= int(NP.mean(AMP[piff(0):piff(30):1]))                    # 0  
   FREQ_DOMAIN[1]= int(NP.mean(AMP[piff(35)  :piff(100):1]))               # 40 -
   FREQ_DOMAIN[2]= int(NP.mean(AMP[piff(150)  :piff(300):1]))              # 47 
   FREQ_DOMAIN[3]= int(NP.mean(AMP[piff(320)  :piff(500):1]))              # 94 - 
   FREQ_DOMAIN[4]= int(NP.mean(AMP[piff(600) :piff(1000):1]))              # 1
   FREQ_DOMAIN[5]= int(NP.mean(AMP[piff(1100) :piff(2500):1]))             
   FREQ_DOMAIN[6]= int(NP.mean(AMP[piff(3000) :piff(5000):1]))             
   FREQ_DOMAIN[7]= int(NP.mean(AMP[piff(5000):piff(7000):1]))
   FREQ_DOMAIN[8]= int(NP.mean(AMP[piff(7100):piff(10000):1]))
   FREQ_DOMAIN[9]= int(NP.mean(AMP[piff(10100):piff(16000):1]))
   
   
   # Tidy up column values 
   FREQ_DOMAIN=NP.divide(NP.multiply(FREQ_DOMAIN,weighting),1000000)
   # Set floor at 0 and ceiling at 20 
   FREQ_DOMAIN=(FREQ_DOMAIN.clip(00,FREQ_DOMAIN_CEILING))
   FREQ_DOMAIN = FREQ_DOMAIN.astype(int)        #convert Domain to int, floats is not interesting atm

   return FREQ_DOMAIN
#-------------------------------------------------------------------------







#-------------------------------------------------------------------------
# Read audio sample
data = WAVSAMPLE.readframes(BLOCKS)

try:
    print("Initializing main loop (Exit with Ctrl + C)")
    print("\n\n")
    # print lables: Frequency Level Vector.....f0 range, f1 range,....,etc
    print("                           0-30         30          150          320           600          1100         3k           5k           7.1k         10.1k")
    print("Freq. LVL Vect             f0R          f1R         f2R          f3R           f4R          f5R          f6R          f7R          f8R          f9R")
    
    # Main loop (Exit with Ctrl + C)
    while data!='':
       ALSA_OUT.write(data)
       FREQ_DOMAIN=GET_LVLs(data, BLOCKS,SAMPLING_RATE)     

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
    
       
     
    

       data = WAVSAMPLE.readframes(BLOCKS)


    WAVESAMPLE.close()
except KeyboardInterrupt:
    
    WAVSAMPLE.close()


#-------------------------------------------------------------------------