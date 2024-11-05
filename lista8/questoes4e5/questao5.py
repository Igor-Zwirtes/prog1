# Questão 5
from questao4 import *
import turtle

def plot_polygons(poly: Polygons):
    # Verifica o menor e maior valor de ocorrência no eixo x e eixo y dentre todos polígonos na lista
    # E define as coordenada as serem exibidas com uma unidade extra de distância destes máximos e mínimos
    max_x, min_x, max_y, min_y = 0, 0, 0, 0
    for polygon in poly.polygons:
        for point in polygon[0].points:
            x, y = point.coord
            max_x = max(max_x, x)
            min_x = min(min_x, x)
            max_y = max(max_y, y)
            min_y = min(min_y, y)
    turtle.Screen().setworldcoordinates(min_x-1, min_y-1, max_x+1, max_y+1)
    turtle.tracer(0, 0)
    plotter = turtle.Turtle()
    plotter.speed(0)
    plotter.penup()
    # Para cada um dos póligonos, percorre uma linha entre os pontos na ordem a qual foram adicionados
    # E finaliza ligando o último e o primeiro ponto para fechar o polígono
    for i in range(len(poly.polygons)):
        plotter.pencolor(poly.polygons[i][0].color)
        for j in range(len(poly.polygons[i][0].points)):
            plotter.goto(poly.polygons[i][0].points[j].coord[0], poly.polygons[i][0].points[j].coord[1])
            plotter.pendown()
        plotter.goto(poly.polygons[i][0].points[0].coord[0], poly.polygons[i][0].points[0].coord[1])
        plotter.penup()
    plotter.hideturtle()
    turtle.done()

if __name__ == '__main__':
    casa = Polygons()
    # Realiza o teste solicitado com o arquivo 'casa.csv', enviado na pasta 'questoes4e5'
    casa.load_from_file('casa.csv')
    plot_polygons(casa)