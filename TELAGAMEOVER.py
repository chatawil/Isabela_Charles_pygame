# import Começo

# # Função para exibir a tela de "Game Over"
# def show_game_over_screen():
#     window.fill((135, 206, 250))  
#     font = pygame.font.SysFont(None, 72)
#     game_over_text = font.render("GAME OVER", True, (255, 0, 0))  
#     window.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))

#     # Mensagem de reinício
#     restart_font = pygame.font.SysFont(None, 40)
#     restart_text = restart_font.render("Quer jogar novamente?"," Clique em qualquer tecla para reiniciar", True, (255, 255, 255))  # Branco
#     window.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 50))
    
#     pygame.display.flip()

#     # Aguarda o jogador pressionar uma tecla para reiniciar o jogo
#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()
#             if event.type == pygame.KEYUP:
#                 waiting = False
#                 show_start_screen()  # Chama a função da tela de início