# -*- coding: utf-8 -*-
import pygame
from gongupa_classes import *
import math
import os

pygame.init()
pygame.display.set_caption('Gongupa')
money = 0
title_screen = Title_Screen()
def level(player, gongupa, gongupa_weapon, weapon, teleporter, organizator, bunker, krzak, title_screen):
    global money
    title_screen.find_all_skins()
    run = True
    suma_do_dodania_money = 0
    czy_napewno = True
    czy_aktualizowac_suma_do_dodania_money = True
    while run:
        events = pygame.event.get()
        pygame.time.Clock().tick(fps)
        if player.zyje:
            for event in events:
                if event.type == pygame.QUIT:
                    czy_napewno = False
                    run = False
                    for i in range(title_screen.czy_usuwac):
                        file_path = f'img//playerplayer{len(title_screen.skins) - 1}.png'
                        if os.path.exists(file_path):
                            os.remove(file_path)
                            title_screen.liczba_wystepujacych_skinow -= 1
                            title_screen.player_images = [pygame.image.load(f'img/playerplayer{i}.png') for i in range(1, title_screen.liczba_wystepujacych_skinow + 1)]
                            title_screen.skins = [pygame.transform.scale(image, (int(screen_height // 17.28), int(screen_height // 17.28))) for image in title_screen.player_images]
                            title_screen.skins.append(title_screen.pluses[0])
            try:                
                keys = pygame.key.get_pressed()
            except:
                pass
            player.strzaly_gongupy = gongupa_weapon.bullets
            gongupa.strzaly_gracza = weapon.bullets
            gongupa.obliczanie_kierunku()
            gongupa_weapon.update_position()
            weapon.obliczanie_kierunku()
            player.obliczanie_kierunku()
            weapon.update_position(player.x, player.y)
            player.tick(keys)
            teleporter.tick()
            gongupa_weapon.tick()
            gongupa.tick()
            weapon.tick()
            if weapon.plus_punkt:
                player.player_score += 1
                money += 1
            organizator.tick()
            if czy_napewno:
                window.fill((32, 212, 53))
                bunker.draw()
                krzak.draw()
                organizator.draw()
                teleporter.draw()
                gongupa.draw()
                gongupa_weapon.draw()
                player.draw()
                weapon.draw()
            else:
                window.fill((32, 212, 53))
        else:
            czy_aktualizowac_suma_do_dodania_money = False
            window.fill((32, 212, 53))
            for event in events:
                if event.type == pygame.QUIT:
                    run = False
            player.none_life()
            if player.zm_targowa == 'again':
                title_screen.money = money
                window.fill((32, 212, 53))
                player.zyje = True
                organizator.plus_hps = 0
                organizator.liczba_dostepnych_dodan_plytek = 10
                player.refresh()
                gongupa.refresh()
                weapon.refresh()
                gongupa_weapon.refresh()
            player.none_life()
            if player.zm_targowa == 'menu':
                title_screen.money = money
                menu(money)
                break
        if czy_aktualizowac_suma_do_dodania_money:
            suma_do_dodania_money = player.player_score
            # money = player.player_score
        if player.menu_bool:
            suma_do_dodania_money = 0
            player.refresh()
            gongupa.refresh()
            weapon.refresh()
            gongupa_weapon.refresh()
            player.menu_bool = False
            # title_screen.money = money
            menu(money)
            break
        pygame.display.update()
def menu(money):
    # global  title_screen, money, krzak, bunker, player, organizator, gongupa, teloporter, gongupa_weapon
    # krzak = Krzak()
    # bunker = Bunker()
    # player = Player(krzak, bunker, title_screen.ktory_pokazuje + 1) # z powodu liczenia index w
    # player.player_score = money
    # organizator = Organization(player)
    # gongupa = Gongupa(player, organizator, krzak, bunker)
    # teloporter = Teloporter(player, gongupa)
    # gongupa_weapon = Gongupa_weapon(round((screen_width // 307.2 + screen_height // 172.8) // 2), round((screen_width // 307.2 + screen_height // 172.8) // 2), gongupa, player, bunker)
    # player.strzaly_gongupy = gongupa_weapon.bullets
    # weapon = Weapon(player.x, player.y, round((screen_width // 307.2 + screen_height // 172.8) // 2), round((screen_width // 307.2 + screen_height // 172.8) // 2), bunker, gongupa, player)
    czy_wypelniac = True
    run = True
    x = title_screen.x
    y = title_screen.y
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    run = False
                    for i in range(title_screen.czy_usuwac):
                        file_path = f'img//playerplayer{len(title_screen.skins) - 1}.png'
                        if os.path.exists(file_path):
                            os.remove(file_path)
                            title_screen.liczba_wystepujacych_skinow -= 1
                            title_screen.player_images = [pygame.image.load(f'img/playerplayer{i}.png') for i in range(1, title_screen.liczba_wystepujacych_skinow + 1)]
                            title_screen.skins = [pygame.transform.scale(image, (int(screen_height // 17.28), int(screen_height // 17.28))) for image in title_screen.player_images]
                            title_screen.skins.append(title_screen.pluses[0])
        if title_screen.draw_czy_wybor == 'wybor':
            if title_screen.tick():
                krzak = Krzak()
                bunker = Bunker()
                player = Player(krzak, bunker, title_screen.ktory_pokazuje + 1) # z powodu liczenia index w
                player.player_score = money
                organizator = Organization(player)
                gongupa = Gongupa(player, organizator, krzak, bunker)
                teloporter = Teloporter(player, gongupa)
                gongupa_weapon = Gongupa_weapon(round((screen_width // 307.2 + screen_height // 172.8) // 2), round((screen_width // 307.2 + screen_height // 172.8) // 2), gongupa, player, bunker)
                player.strzaly_gongupy = gongupa_weapon.bullets
                weapon = Weapon(player.x, player.y, round((screen_width // 307.2 + screen_height // 172.8) // 2), round((screen_width // 307.2 + screen_height // 172.8) // 2), bunker, gongupa, player)
                player.player_score = title_screen.money
                level(player, gongupa, gongupa_weapon, weapon, teloporter, organizator, bunker, krzak, title_screen)
                break
            window.fill((32, 212, 53))
            title_screen.draw()
            window.blit(title_screen.game_name, (x - 100, y - 200))
            pygame.display.update()
        else:
            window.fill((32, 212, 53))
            title_screen.drawing_tick()
            pygame.display.update()
if __name__ == '__main__':
    menu(money) # 1038 linijek kodu.