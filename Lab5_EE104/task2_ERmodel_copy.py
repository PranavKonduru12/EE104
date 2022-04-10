#http://apmonitor.com/che263/index.php/Main/PythonDynamicSim 
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def tank(h, t, er1, er2, er3, er4,):
   # constants 
   c1 = 10    # Covid patients entering ICU
   c2 = 5    # Covid patients leaving ICU
   # Ac = 2      # m^2 (Equivalent to no. of nurses, beds, doctors)
   A_er = er1 + er2 + er3       # m^2 (Equivalent to no. of nurses (er1), doctors (er2), beds (er3))
   A_icu = A_er + er4 # For ICU, it will be all of the above with respirators, nurses, and beds
   # inflow of general patients coming into the ER
   qin = 20   # m^3/hr
   # outflow
   qout1 = c1 * h[0]**0.5
   qout2 = c2 * h[1]**0.5
   # differential equations
   dhdt1 = (qin   - qout1) / A_er
   dhdt2 = (qout1 - qout2) / A_icu
   # overflow conditions
   if h[0]>=1 and dhdt1>=0:
       dhdt1 = 0
   if h[1]>=1 and dhdt2>=0:
       dhdt2 = 0
   dhdt = [dhdt1,dhdt2]
   return dhdt

# integrate the equations
t = np.linspace(0,10) # times to report solution
h0 = [0,0]            # initial conditions for height
#doc = 10
#nurse = 5
#bed = 20
#vent = 30
er = (10, 5, 20, 30)
# tank(h0, doc, nurse, beds, vent, t)
y = odeint(tank,h0, t, er) # integrate

# plot results
plt.figure(1)
plt.plot(t,y[:,0],'b-')
plt.plot(t,y[:,1],'r--')
plt.xlabel('Time (hrs)')
plt.ylabel('Height (m)')
plt.legend(['h1','h2'])
plt.show()