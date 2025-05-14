import matplotlib.pyplot as plt
import seaborn as sns

# Configurações de estilo para os gráficos
plot_config= {
        "axes.facecolor": "#111",     # Cor de fundo dos gráficos
        "figure.facecolor": "#111",   # Cor de fundo da figura
        "text.color": "white",        # Cor do texto
        "axes.labelcolor": "white",   # Cor dos rótulos dos eixos
        "xtick.color": "white",       # Cor dos ticks do eixo x
        "ytick.color": "white",       # Cor dos ticks do eixo y
        "axes.edgecolor": "white",    # Cor das bordas dos gráficos
        "axes.spines.top": False,     # Ativar ou remover borda superior
        "axes.spines.right": False,   # Ativar ou remover borda direita
        "axes.grid": True,            # Ativar ou remover grade
        "grid.color": "#222",         # Cor da grade
        "grid.linestyle": "--",       # Estilo da grade
        "figure.figsize": (15, 6)     # Tamanho padrão da figura
    }

# Função para o Matplotlib
def set_matplotlib():
    plt.style.use(plot_config)

# Função para o Seaborn
def set_seaborn():
    sns.set_theme(rc= plot_config)