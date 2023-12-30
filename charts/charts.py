import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['Alquiler', 'Comida', 'Agua', 'Luz', 'Gas', 'Movil', 'Gasoil', 'Cole Thiago', 'Extraescolares', 'Aquaservice', 'Préstamo', 'Seguros']
    values = [790, 500, 20, 60, 60, 45, 60, 150, 50, 32, 160, 75]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()