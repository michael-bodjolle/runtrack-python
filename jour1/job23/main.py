def draw_rectangle():

    x = '-'
    y = '|'

    width = int(input('Largeur\n'))
    height = int(input('Hauteur\n'))

    print(x*width)

    for index in range(0, height):
        print(y + ' ' * (width - 2 )+ y)
        
    print(x*width)     
    


draw_rectangle()


