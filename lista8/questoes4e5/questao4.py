# Questão 4
class Point2D:
    def __init__(self, x: float, y: float):
        self.coord = (x, y)

class Polygon:
    def __init__(self, points: list[Point2D], color: str):
        self.points = points
        self.color = color

class Polygons:
    def __init__(self):
        self.polygons = []
    
    def add_polygon(self, polygon: Polygon, name: str):
        # Salva o polígono como uma tupla de polígono e nome
        self.polygons.append((polygon, name))

    def remove_polygon(self, name: str):
        for i in range(len(self.polygons)):
            if self.polygons[i][1] == name:
                del self.polygons[i]
                '''
                Para evitar problemas com os índices após apagar um elemento, quando um polígono é removido, a função chama a si mesma com os mesmos parâmetros. Após uma iteração percorrer toda lista sem remover nada, todos processos são finalizados sem fazer mais nada
                '''
                self.remove_polygon(name)
                break

    def save_to_file(self, filename: str):
        with open(filename, 'w') as f:
            f.write('name,x,y,color\n')
            for i in range(len(self.polygons)):
                for j in range(len(self.polygons[i][0].points)):
                    # Verifica se o elemento atual é o último, caso for, não adiciona uma nova linha no final
                    if (j == len(self.polygons[i][0].points) - 1 and i == len(self.polygons) - 1):
                        f.write(f"{self.polygons[i][1]},{self.polygons[i][0].points[j].coord[0]},{self.polygons[i][0].points[j].coord[1]},{self.polygons[i][0].color}")
                    else:
                        f.write(f"{self.polygons[i][1]},{self.polygons[i][0].points[j].coord[0]},{self.polygons[i][0].points[j].coord[1]},{self.polygons[i][0].color}\n")
            f.close()
    
    def load_from_file(self, filename:str):
        # Sobrescreve a lista de polígonos, caso já exista
        self.polygons = []
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f.readlines()]
            # Começa o índice em 1 para pular o cabeçalho
            i = 1
            while i < len(lines):
                # Verifica a posição das vígulas para saber o intervalo que corresponde a cada elemento do polígono
                j = i
                end_of_name = 0
                while lines[j][end_of_name] != ',':
                    end_of_name += 1
                end_of_x = end_of_name + 1
                while lines[j][end_of_x] != ',':
                    end_of_x += 1
                end_of_y = end_of_x + 1
                while lines[j][end_of_y] != ',':
                    end_of_y += 1
                name = str(lines[j][:end_of_name])
                points = []
                color = str(lines[j][end_of_y + 1:])
                # Enquanto o nome continuar sendo o mesmo, adiciona os pontos em uma mesma lista,
                # Quando diferir, cria um novo polígono com as informações atuais e adiciona à lista de polígonos
                while j < len(lines) and lines[j][:end_of_name] == name:
                    # O código considera que o arquivo está no formato do método 'save_to_file',
                    # Onde os pontos de um mesmo polígonos estão em linhas subsequentes
                    points.append(Point2D(float(lines[j][end_of_name + 1:end_of_x]),float(lines[j][end_of_x + 1:end_of_y])))
                    j = j + 1
                    if j != len(lines):
                        end_of_name = 0
                        while lines[j][end_of_name] != ',':
                            end_of_name += 1
                        end_of_x = end_of_name + 1
                        while lines[j][end_of_x] != ',':
                            end_of_x += 1
                        end_of_y = end_of_x + 1
                        while lines[j][end_of_y] != ',':
                            end_of_y += 1
                polygon = Polygon(points, color)
                self.add_polygon(polygon, name)
                # Altera o valor de i para pular todos os pontos do polígono anterior
                i = j

if __name__ == '__main__':
    p1 = Point2D(0,2)
    p2 = Point2D(3,7)
    p3 = Point2D(1,9)
    triangle = Polygon([p1,p2,p3], 'green')
    test = Polygons()
    test.add_polygon(triangle, 'triangle')
    p1 = Point2D(1,2)
    p2 = Point2D(5,7)
    p3 = Point2D(0,9)
    p4 = Point2D(1,3)
    p5 = Point2D(0,0)
    p6 = Point2D(10,2)
    hexagon = Polygon([p1,p2,p3,p4,p5,p6], 'blue')
    test.add_polygon(hexagon, 'hexa')
    test.remove_polygon('hexa')
    test.save_to_file('test.csv')
    load = Polygons()
    load.load_from_file('test.csv')