# 匿名函数
# f = lambda x, y: x + y
# print(f(1, 2))


# with open("kaoshi.txt", "r", encoding="utf-8") as f:
#     with open("da.txt", "w+", encoding="utf-8") as f1:
#         f1.write(f.read())


# x = [1, 2]
# y = [1, 2]
# print(x is y)  # 不光值要相等  id也要相等
#
# print(x == y)  # 值相等


# import pygame
#
# black = (0, 0, 0)
# white = (255, 255, 255)
# red = (255, 0, 0)
# green = (0, 255, 0)
#
#
# def draw_a_boy(screen, x, y):
#     pygame.draw.ellipse(screen, black, [x, y - 5, 10, 10])
#     pygame.draw.line(screen, red, [5 + x, 5 + y], [5 + x, 15 + y], 2)
#     pygame.draw.line(screen, red, [5 + x, 5 + y], [x - 5, 15 + y], 2)
#     pygame.draw.line(screen, red, [5 + x, 5 + y], [15 + x, 15 + y], 2)
#     pygame.draw.line(screen, black, [5 + x, 15 + y], [x - 5, 25 + y], 2)
#     pygame.draw.line(screen, black, [5 + x, 15 + y], [15 + x, 25 + y], 2)
#
#
# pygame.init()
# size = (700, 500)
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("a boy")
#
# done = False
# clock = pygame.time.Clock()
# x = 15
# y = 15
#
# while done == False:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#
#     pos = pygame.mouse.get_pos()
#     x = pos[0]
#     y = pos[1]
#
#     pygame.mouse.set_visible(False)
#
#     screen.fill(white)
#     draw_a_boy(screen, x, y)
#
#     clock.tick(20)
#     pygame.display.flip()
#
# pygame.quit()


def crea(pos=[0, 0]):
    def game(move_dir, Xstep, Ystep):
        pos[0] += pos[0] + move_dir[0] * Xstep
        pos[1] += pos[1] + move_dir[1] * Ystep
        return pos

    return game


game = crea()
print(game([1, -1], 1, 2))  # 往X轴正半轴移动  步长为1  往y轴负半轴移动  步长为2
