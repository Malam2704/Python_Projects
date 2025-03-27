import numpy as np
import matplotlib.pyplot as plt

# Set up the plot
plt.figure(figsize=(10, 8))

# Generate points for the demand curve
Q = np.linspace(0, 200, 100)
P_demand = 100 - 0.5*Q  # Demand equation P = 100 - 0.5Q

# Generate points for the marginal revenue curve
P_mr = 100 - Q  # MR = 100 - Q

# Plot the curves
plt.plot(Q, P_demand, 'b-', label='Demand')
plt.plot(Q, P_mr, 'r--', label='MR')
plt.axhline(y=10, color='g', label='MC')

# Mark the profit-maximizing point
Q_star = 90
P_star = 55
plt.plot([Q_star, Q_star], [0, P_star], 'k:', alpha=0.5)
plt.plot([0, Q_star], [P_star, P_star], 'k:', alpha=0.5)

# Fill producer surplus (PS)
ps_x = np.array([0, Q_star, Q_star])
ps_y = np.array([10, 10, P_star])
plt.fill(ps_x, ps_y, alpha=0.3, color='green', label='Producer Surplus')

# Fill deadweight loss (DWL)
Q_efficient = 180  # Where demand crosses MC
dwl_x = np.array([Q_star, Q_efficient, Q_star])
dwl_y = np.array([10, 10, P_star])
plt.fill(dwl_x, dwl_y, alpha=0.3, color='red', label='Deadweight Loss')

# Customize the plot
plt.grid(True, alpha=0.3)
plt.xlabel('Quantity')
plt.ylabel('Price')
plt.title('Monopoly Market with Producer Surplus and Deadweight Loss')
plt.legend()

# Set axis ranges
plt.xlim(0, 200)
plt.ylim(0, 100)

# Add text annotations
plt.text(Q_star-5, 5, 'Q*=90')
plt.text(5, P_star, 'P*=55')
plt.text(5, 12, 'MC=10')

plt.show()