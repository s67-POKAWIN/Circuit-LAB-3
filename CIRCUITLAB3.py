import matplotlib.pyplot as plt

RL = [0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000]
V_RL = [0.003, 4.51, 5.49, 5.73, 6.18, 6.39, 6.44, 6.52, 6.58, 6.62, 6.66, 6.70, 6.73]

I_RL_mA = [None] + [1000 * V_RL[i] / RL[i] for i in range(1, len(RL))]
P_RL_mW = [None] + [V_RL[i] * I_RL_mA[i] for i in range(1, len(RL))]

def plot_xy(x, y, xlabel, ylabel, title):
    x2, y2 = [], []
    for xi, yi in zip(x, y):
        if yi is not None:
            x2.append(xi)
            y2.append(yi)
    plt.figure()
    plt.plot(x2, y2, marker='o')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.show()

plot_xy(RL, V_RL, "RL (Ω)", "V(RL) (V)", "V(RL) vs RL")
plot_xy(RL, I_RL_mA, "RL (Ω)", "I(RL) (mA)", "I(RL) vs RL")
plot_xy(RL, P_RL_mW, "RL (Ω)", "P(RL) (mW)", "P(RL) vs RL (P = V×I)")
