import os
from LevelParts.Level import *
from LevelParts.Menu.MainMenu import *
from LevelParts.Menu.PauseMenu import *
from Widgets.MashineLearning.NeuralNetwork import *
"""

Do the whole program

"""

#Импорт картинок


def true_image_import():
    union_unit_types = [LightInfantryType, HeavyInfantryType, CavalryType, LongDistanceSoldierType, AlchemistType]
    order_unit_types = [LightInfantryType, HeavyInfantryType, CavalryType, LongDistanceSoldierType, HealerType]
    animation_types = [MotionlessAnimationType, MovementAnimationType, DealinDamageAnimationType,
                       TakingDamageAnimationType, DeathAnimationType]
    number = 0

    Another_Images = {}
    Another_Images["castle union"] = pygame.image.load('images/zdanie_soyuz.png').convert_alpha()
    number += 1
    Another_Images["square"] = pygame.image.load('images/ploschad.png').convert_alpha()
    number += 1
    Another_Images["castle order"] = pygame.image.load('images/zdanie_orden.png').convert_alpha()
    number += 1
    Another_Images["bruschatka"] = pygame.image.load('images/bruschatka.png').convert_alpha()
    number += 1

    Union_Units_Images = {}
    for unit_type in union_unit_types:
        Union_Units_Images[unit_type] = {}
        for animation in animation_types:
            massive = []
            for i in range(animation_duration[animation]):
                file_name = "images/" + "Union" + unit_type + animation + str(i) + ".png"
                current_image = pygame.image.load(file_name).convert_alpha()
                massive.append(current_image)
                number += 1
            Union_Units_Images[unit_type][animation] = [animation_duration[animation], massive]

    Order_Units_Images = {}
    for unit_type in order_unit_types:
        Order_Units_Images[unit_type] = {}
        for animation in animation_types:
            massive = []
            for i in range(animation_duration[animation]):
                file_name = "images/" + "Order" + unit_type + animation + str(i) + ".png"
                current_image = pygame.image.load(file_name).convert_alpha()
                massive.append(current_image)
                number += 1
            Order_Units_Images[unit_type][animation] = [animation_duration[animation], massive]

    return Another_Images, Union_Units_Images, Order_Units_Images


# Импорт нейросети


def input_Neural_Network(file_name):
    file_obj = open(file_name, 'r')
    matrix = []
    shift = []
    for i in range(len(NNLayers)-1):
        matrix.append(np.zeros((NNLayers[i + 1], NNLayers[i]), dtype=float))
        for j in range(NNLayers[i+1]):
            for k in range(NNLayers[i]):
                matrix[i][j][k] = float(file_obj.readline())
    for i in range(len(NNLayers)-1):
        shift.append(np.zeros((NNLayers[i + 1], 1), dtype=float))
        for j in range(NNLayers[i+1]):
            shift[i][j][0] = float(file_obj.readline())
    file_obj.close()
    return matrix, shift


# файл запуска программы


os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
clock = pygame.time.Clock()
level_screen = pygame.display.set_mode((int(LevelXSize*DrawingCoefficient), int(LevelYSize*DrawingCoefficient)))
main_screen = pygame.display.set_mode((int(ScreenXSize*DrawingCoefficient), int(ScreenYSize*DrawingCoefficient)))
main_menu_screen = pygame.display.set_mode((int(MainMenuXSize*DrawingCoefficient), int(MainMenuYSize*DrawingCoefficient)))
pause_menu_screen = pygame.display.set_mode((int(PauseMenuXSize*DrawingCoefficient), int(PauseMenuYSize*DrawingCoefficient)))
main_screen.blit(main_menu_screen, (0, 0))
main_screen.blit(level_screen, (0, 0))
main_screen.blit(pause_menu_screen, (0, 0))
Order_Network = NeuralNetwork(input_Neural_Network("Widgets/MashineLearning/differentAI/OrderNN0.txt"), "order")
Union_Network = NeuralNetwork(input_Neural_Network("Widgets/MashineLearning/differentAI/UnionNN0.txt"), "union")
Test_Level = Level(map_drawer, level_screen, true_image_import(), [False, True], [0, Union_Network])
Main_Menu = MainMenu(main_menu_screen)
Pause_Menu = PauseMenu(pause_menu_screen)
pygame.display.update()
finished = False
flag = False
is_level = True
is_pause = False
is_main_menu = False


def activate_pause_menu():
    pause_menu_screen.set_alpha(255)
    level_screen.set_alpha(100)
    main_menu_screen.set_alpha(0)
    is_pause = True
    is_main_menu = False
    is_level = False





number = 0

while not finished:
    clock.tick(FPS)
    Result = 0
    if is_level:
        Test_Level.draw()
        Result = Test_Level.update()
        number += 1
    elif is_pause:
        Result = Pause_Menu.update()
    elif is_main_menu:
        Result = Main_Menu.update()

    if Result==1:
        finished = True
        print("Победил первый город")
    elif Result==2:
        finished = True
        print("Победил второй город")
    pygame.display.update()
    for event in pygame.event.get():
        answer = ""
        if is_level:
            answer = Test_Level.game_event(event)
        elif is_pause:
            answer = Pause_Menu.game_event(event)
        elif is_main_menu:
            answer = Main_Menu.game_event(event)
        if answer == "exit":
            finished = True
        elif answer == "resume":
            pause_menu_screen.set_alpha(0)
            level_screen.set_alpha(255)
            main_menu_screen.set_alpha(0)
            is_pause = False
            is_main_menu = False
            is_level = True
        elif answer == "pause":
            pause_menu_screen.set_alpha(255)
            level_screen.set_alpha(0)
            main_menu_screen.set_alpha(0)
            is_pause = True
            is_main_menu = False
            is_level = False
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()

