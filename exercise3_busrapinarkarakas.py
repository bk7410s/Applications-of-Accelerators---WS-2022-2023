#magnetic rigidty calculation
#m_0 ,mass value needed ,which particle used for calculation / unit (u)
#T ,energy value ,MeV
#q , charge of  particle
#c,speed of light m/s
import math
def get_rigidity(m_0,q,T):
 
     c=299792458
     sigma=(T/(m_0*931.5))+1
     v=math.sqrt(1-(1/(sigma)**2))*c;    
     q_Coloumb=q*1.602e-19;
     magnetic_rigidity= (sigma*v*m_0*1.661e-27) / (q_Coloumb)
     print("magnetic rigidity is equal to",magnetic_rigidity,"T.m")

# you can write in the shell below functions,respectively
#get_rigidity(238,28,45220) this is for question 1
#get_rigidity(197,77,81000) this is for question 2
#get_rigidity(0.000548,1,10000) this is for electrons/question 3