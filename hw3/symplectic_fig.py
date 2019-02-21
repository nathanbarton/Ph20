import numpy as np
import matplotlib.pyplot as plt

import sho

x0 = 1
v0 = 0
tmax = 25
h = .05

data_exp = sho_euler_explicit(x0,v0,tmax,h)
data_imp = sho_euler_implicit(x0,v0,tmax,h)
time = np.linspace(0, tmax, int(tmax/h)+1)


fig, axs = plt.subplots(2,1)

axs[0].plot(data_exp[0,:],data_exp[1,:])
axs[0].set_aspect('equal', 'box')
axs[0].set_title('Euler phase space')
axs[0].set_ylabel('Explicit Position')

axs[1].plot(data_imp[0,:],data_imp[1,:])
axs[1].set_aspect('equal', 'box')
axs[1].set_ylabel('Implicit Position')
axs[1].set_xlabel('Velocity')

plt.savefig("fig/exp_imp_phase.eps", dpi=300)


data_sym = sho_euler_symplectic(x0,v0,tmax,h)

fig, axs = plt.subplots()

axs.plot(data_sym[0,:],data_sym[1,:])
axs.set_aspect('equal', 'box')
axs.set_title('Symplectic Euler Phase Space')
axs.set_ylabel('Position')
axs.set_xlabel('Velocity')

plt.savefig("fig/symplectic_phase_plot.eps", dpi=300)


energy_sym =  np.power(data_sym[0,:], 2) + np.power(data_sym[1,:], 2)

plt.plot(time,energy_sym)
plt.title('Symplectic Euler SHO energy')
plt.ylabel('Total System Energy')
plt.xlabel('Time')

plt.savefig("fig/symplectic_energy.eps", dpi=300)



x0 = 1
v0 = 0
tmax = 10000
h = .05

data_sym_long = sho_euler_symplectic(x0,v0,tmax,h)
data_analytic_long = sho_analytic(x0,v0,tmax,h)

time_long = np.linspace(0, tmax, int(tmax/h)+1)

fig, axs = plt.subplots(2,1)

axs[0].plot(time_long,data_sym_long[0,:], label='Symplectic')
axs[0].plot(time_long,data_analytic_long[0,:], label='Analytic')
axs[0].set_title('Symplectic Euler SHO')
axs[0].set_ylabel('Position')

axs[0].set_xlim(tmax-25,tmax)

axs[1].plot(time_long,data_sym_long[1,:], label='Symplectic')
axs[1].plot(time_long,data_analytic_long[1,:], label='Analytic')
axs[1].set_ylabel('Velocity')
axs[1].set_xlabel('Time')

axs[1].set_xlim(tmax-25,tmax)

axs[1].legend()

plt.savefig("fig/symplectic_plot.eps", dpi=300)