fig/explicit_plot.eps fig/explicit_error.eps fig/explicit_error_vs_h.eps fig/explicit_energy.eps:
	python explicit_fig.py
	
fig/implicit_plot.eps fig/implicit_error.eps fig/implicit_error_vs_h.eps fig/implicit_energy.eps:
	python implicit_fig.py
	
fig/exp_imp_phase.eps fig/symplectic_phase_plot.eps fig/symplectic_energy.eps fig/symplectic_plot.eps:
	python symplectic_fig.py
	
main.pdf : fig/explicit_plot.eps fig/explicit_error.eps fig/explicit_error_vs_h.eps fig/explicit_energy.eps fig/implicit_plot.eps fig/implicit_error.eps fig/implicit_error_vs_h.eps fig/implicit_energy.eps fig/exp_imp_phase.eps fig/symplectic_phase_plot.eps fig/symplectic_energy.eps fig/symplectic_plot.eps
	pdflatex main.tex