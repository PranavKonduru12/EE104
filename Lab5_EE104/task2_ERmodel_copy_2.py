#http://apmonitor.com/che263/index.php/Main/PythonDynamicSim 
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def er(h, t, c1, c2):
   # constants 
   #c1 = 10    # Covid patients entering ICU
   #c2 = 5    # Covid patients leaving ICU
   # Ac = 2      # m^2 (Equivalent to no. of nurses, beds, doctors)
   A_er = 25        # m^2 (Equivalent to no. of nurses (er1), doctors (er2), beds (er3))
   A_icu = 25 # For ICU, it will be all of the above with respirators, nurses, and beds
   # inflow of general patients coming into the ER
   qin = 20   # m^3/hr
   # outflow
   qout1 = c1 * h[0]**0.5 # Rate of patients entering ICU
   qout2 = c2 * h[1]**0.5 # Rate of patients leaving ICU
   # differential equations
   dhdt1 = (qin   - qout1) / A_er
   dhdt2 = (qout1 - qout2) / A_icu
   # overflow conditions
   if h[0]>=100 and dhdt1>=0:
       dhdt1 = 0
   if h[1]>=100 and dhdt2>=0:
       dhdt2 = 0
   dhdt = [dhdt1,dhdt2]
   return dhdt

# integrate the equations
t = np.linspace(0, 23, 47) # times to report solution
h = [0,0]            # initial conditions for height
#doc = 10
#nurse = 5
#bed = 20
#vent = 30
#er = (10, 5, 20, 30)
#beds = (50)
c = (10, 5)
#beds = (25)
# tank(h0, doc, nurse, beds, vent, t)
y = odeint(er,h, t, c) # integrate

# plot results
plt.figure(1)
plt.plot(t,y[:,0],'b-')
plt.plot(t,y[:,1],'r--')
plt.xlabel('Time (hrs)')
plt.ylabel('Beds')
plt.legend(['h1','h2'])
plt.show()