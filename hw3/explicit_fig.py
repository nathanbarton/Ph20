import numpy as np
import matplotlib.pyplot as plt

import sho

x0 = 1
v0 = 0
tmax = 25
h = .05

data_exp = sho_euler_explicit(x0,v0,tmax,h)
time = np.linspace(0, tmax, int(tmax/h)+1)

fig, axs = plt.subplots(2,1)

axs[0].plot(time,data_exp[0,:])
axs[0].set_title('Explicit Euler SHO')
axs[0].set_ylabel('Position')

axs[1].plot(time,data_exp[1,:])
axs[1].set_ylabel('Velocity')
axs[1].set_xlabel('Time')

plt.savefig("fig/explicit_plot.eps", dpi=300)



data_analytic = sho_analytic(x0,v0,tmax,h)
global_error_exp = data_analytic - data_exp

fig, axs = plt.subplots(2,1)

axs[0].plot(time,global_error_exp[0,:])
axs[0].set_title('Explicit Euler SHO error')
axs[0].set_ylabel('Position error')

axs[1].plot(time,global_error_exp[1,:])
axs[1].set_ylabel('Velocity error')
axs[1].set_xlabel('Time')

plt.savefig("fig/explicit_error.eps", dpi=300)


h_min = .001
h_max = .1
h_size = 10

h_values = np.linspace(h_min, h_max, h_size)

h_errors = np.zeros((2,h_size))
for i in range(h_size):
    h_errors[:,i] = np.amax(np.absolute(sho_analytic(x0,v0,tmax,h_values[i]) - sho_euler_explicit(x0,v0,tmax,h_values[i]) ), axis=1)
    
fig, axs = plt.subplots(2,1)

axs[0].plot(h_values,h_errors[0,:])
axs[0].set_title('Explicit Euler SHO error')
axs[0].set_ylabel('Position error')
axs[0].set_xlim(h_max,h_min)

axs[1].plot(h_values,h_errors[0,:])
axs[1].set_ylabel('Velocity error')
axs[1].set_xlabel('timestep size (h)')
axs[1].set_xlim(h_max,h_min)

plt.savefig("fig/explicit_error_vs_h.eps", dpi=300)


energy_exp =  np.power(data_exp[0,:], 2) + np.power(data_exp[1,:], 2)

plt.plot(time,energy_exp)
plt.title('Explicit Euler SHO energy')
plt.ylabel('Total System Energy')
plt.xlabel('Time')

plt.savefig("fig/explicit_energy.eps", dpi=300)


