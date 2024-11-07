import pygame
import random
import time

pygame.init()
# ----- Gera tela principal
WIDTH = 870
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('🏃🏽‍♂️🏃🏽‍♀️RUN GAME🏃🏽‍♀️🏃🏽‍♂️')


# ----- Carrega imagens
# Carregando a imagem de fundo
imagem_inicio = pygame.image.load('assets/img/FUNDO_inicio.png').convert()
imagem_inicio = pygame.transform.scale(imagem_inicio, (WIDTH, HEIGHT))
imagem_inicio_rect = imagem_inicio.get_rect()
imagem_inicio_rect_2 = imagem_inicio_rect.copy()
imagem_inicio_rect_2.x -= imagem_inicio_rect_2.width
speed_fundo = 10 

# ----- Função para mostrar a tela inicial
def show_start_screen():
    window.blit(imagem_inicio, imagem_inicio_rect)
    window.blit(imagem_inicio, imagem_inicio_rect_2)
    
    # Fonte maior e cor rosa choque brilhante para o título
    title_font = pygame.font.SysFont(None, 72)
    title = title_font.render("RUN GAME", True, (135, 206, 250))  # Vermelho Sangue
    


    
    # Fonte menor para a história
    font = pygame.font.SysFont(None, 40)
    story = [
        " Você está em uma estrada a qual passa muitas crianças! ",
        " É preciso que desvie das barricadas ",
        " para não causar acidentes",
        " e preservar a própria segurança! ",
        "",

    ]

    font_inicio = pygame.font.SysFont(None, 30)
    inicio = font_inicio.render("Clique em qualquer botão para iniciar o jogo.", True, (0, 0, 139))


    # Desenha o título
    window.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 4))
    pygame.display.flip()
    
    # Desenha a história de forma animada
    for i, line in enumerate(story):
        rendered_line = ""
        for char in line:
            rendered_line += char
            text = font.render(rendered_line, True, (255, 255, 255)) ### branco 
            window.blit(imagem_inicio, imagem_inicio_rect)
            window.blit(imagem_inicio, imagem_inicio_rect_2)
            window.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 4))
            for j in range(i):
                previous_text = font.render(story[j], True, (255, 255, 255)) ## branco 
                window.blit(previous_text, (WIDTH // 2 - previous_text.get_width() // 2, HEIGHT // 3 + 40 * (j + 1)))
            window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 3 + 40 * (i + 1)))
            pygame.display.flip()
            pygame.time.wait(50)  # Delay de 50ms entre cada letra

    window.blit(inicio, (WIDTH // 2 - inicio.get_width() // 2, HEIGHT // 38))
    pygame.display.flip()

    # Aguarda o jogador pressionar uma tecla ou botão do mouse para iniciar o jogo
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP:
                waiting = False


show_start_screen()

