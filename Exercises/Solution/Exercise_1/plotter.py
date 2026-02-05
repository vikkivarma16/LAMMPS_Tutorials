import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Function to load data
# -----------------------------
def load_data(filename):
    try:
        data = np.loadtxt(filename, comments='#')
        return data[:, 0], data[:, 1]  # two columns
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return None, None


# -----------------------------
# Function to plot and save data
# -----------------------------
def plot_and_save(x, y, xlabel, ylabel, title, output_file):
    # Random color, avoiding white/light colors
    random_color = np.random.uniform(0.0, 0.85, size=3)

    plt.figure(figsize=(10, 6))
    plt.plot(
        x, y,
        marker='o',
        linestyle='-',
        color=random_color
    )
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Plot saved as {output_file}")
    plt.close()


# -----------------------------
# Main execution
# -----------------------------
if __name__ == '__main__':

    # Load data from files
    m_d_x, m_d_y = load_data('m_vs_d.txt')
    gamma_d_x, gamma_d_y = load_data('gamma_vs_d.txt')
    t_d_x, t_d_y = load_data('t_vs_d.txt')

    # Plot and save m_vs_d
    if m_d_x is not None and m_d_y is not None:
        plot_and_save(
            m_d_x, 1 / m_d_y,
            xlabel='d',
            ylabel='1/m',
            title='1/m vs d',
            output_file='m_vs_d.png'
        )

    # Plot and save gamma_vs_d
    if gamma_d_x is not None and gamma_d_y is not None:
        plot_and_save(
            gamma_d_x, gamma_d_y,
            xlabel='d',
            ylabel='1/γ',
            title='1/γ vs d',
            output_file='gamma_vs_d.png'
        )

    # Plot and save t_vs_d
    if t_d_x is not None and t_d_y is not None:
        plot_and_save(
            t_d_x, t_d_y,
            xlabel='d',
            ylabel='k_BT',
            title='k_BT vs d',
            output_file='t_vs_d.png'
        )

