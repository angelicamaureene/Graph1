import matplotlib.pyplot as plt
import numpy as np

# Data from image
conditions = ['Sleep', 'No Sleep']
means = [31.6458525, 55.8545865]
sems = [4.919191, 5.352139]

# Set APA style parameters
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']

fig, ax = plt.subplots(figsize=(6, 5), dpi=300)

# Bar plot
x_pos = np.arange(len(conditions))
bars = ax.bar(x_pos, means, yerr=sems, align='center', alpha=0.8, ecolor='black', capsize=5, width=0.4, color=['#d9d9d9', '#7f7f7f'])

# Axis labels and limits
ax.set_ylabel('Average Time to Complete Proof (s)', fontsize=12, fontweight='bold')
ax.set_xlabel('Sleep Condition', fontsize=12, fontweight='bold', labelpad=10)
ax.set_xticks(x_pos)
ax.set_xticklabels(conditions, fontsize=11)
ax.set_ylim(0, 70)

# Remove top and right spines for APA style
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Ensure clean gridless background
ax.grid(False)

plt.tight_layout()
plt.savefig('apa_graph.png', dpi=300, bbox_inches='tight')
print("Graph generated successfully.")
