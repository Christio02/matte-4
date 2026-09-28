import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 3 * np.pi, 1000)
# Piecewise solution: 0.5*sin(2t) before pi, 1.0*sin(2t) after pi
y = np.where(t < np.pi, 0.5 * np.sin(2 * t), np.sin(2 * t))

plt.figure(figsize=(9, 4.5))
plt.plot(t, y, "b-", linewidth=2, label=r"$y(t)$")
plt.axvline(
    x=np.pi,
    color="crimson",
    linestyle="--",
    alpha=0.7,
    label=r"Impulse at $t = \pi$",
)

# Custom tick marks in multiples of pi/2
ticks = [0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi, 5 * np.pi / 2, 3 * np.pi]
labels = [
    r"$0$",
    r"$\pi/2$",
    r"$\pi$",
    r"$3\pi/2$",
    r"$2\pi$",
    r"$5\pi/2$",
    r"$3\pi$",
]
plt.xticks(ticks, labels)

plt.title("Simple Harmonic Oscillator with Dirac Delta Impulse", fontsize=13)
plt.xlabel(r"Time $t$", fontsize=11)
plt.ylabel(r"Displacement $y(t)$", fontsize=11)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
