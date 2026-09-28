import matplotlib.pyplot as plt
import numpy as np

# Configure mathtext to use standard TeX computer modern style
plt.rcParams["mathtext.fontset"] = "cm"

# Time array from 0 to 3*pi
t = np.linspace(0, 3 * np.pi, 1000)

# Piecewise solution: 0.5*sin(2t) before t = pi, sin(2t) after t = pi
y = np.where(t < np.pi, 0.5 * np.sin(2 * t), np.sin(2 * t))

plt.figure(figsize=(9, 4.5))

# Plot displacement
plt.plot(t, y, "b-", linewidth=2, label=r"\(y(t)\)")

# Impulse location
plt.axvline(
    x=np.pi,
    color="crimson",
    linestyle="--",
    alpha=0.7,
    label=r"Impulse at \(t = \pi\)",
)

# Custom tick marks and LaTeX labels formatted with \(...\)
ticks = [0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi, 5 * np.pi / 2, 3 * np.pi]
labels = [
    r"$0$",
    r"\(\pi/2\)",
    r"\(\pi\)",
    r"\(3\pi/2\)",
    r"\(2\pi\)",
    r"\(5\pi/2\)",
    r"\(3\pi\)",
]
plt.xticks(ticks, labels)

# Plot labels and styling
plt.title(
    r"Simple Harmonic Oscillator: \(y'' + 4y = \delta(t - \pi)\)", fontsize=13
)
plt.xlabel(r"Time \(t\)", fontsize=11)
plt.ylabel(r"Displacement \(y(t)\)", fontsize=11)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="upper left")
plt.tight_layout()

plt.show()
