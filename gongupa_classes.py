# -*- coding: utf-8 -*-
import pygame
import math
from random import randint
import time
import pyautogui
import os

fps = 68
co_ile_strzal = fps / 10
pygame.init()
class Info:
    def __init__(self):
        self.images = [pygame.image.load('img/weapon.png').convert_alpha()]
        self.width_weapon, self.height_weapon = screen_width / 33.391304347826086, screen_height / 85
        self.width_bullet, self.height_bullet = screen_width / 307.2, screen_height / 86.4
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h
rozmiar = (screen_width, screen_height)
window = pygame.display.set_mode(rozmiar)
pygame.display.set_caption('Gongupa')
infoo = Info()
class Player:
    def __init__(self, krzak, bunkier, skin):
        self.skin = skin
        self.bunkier = bunkier
        self.krzak = krzak
        self.refreshing = False
        self.zm_targowa = None # w self.none_life jako rozpoznanie klikni�cia. 
        self.x = round(screen_width / 2)
        self.y = round(screen_height / 2)
        self.previous_x = self.x
        self.previous_y = self.y
        self.max = round(screen_width / 30.72)
        self.health = round(self.max) # 50
        self.health_x = self.x - (self.max / 2)# 25
        self.health_y = self.y - (screen_height / 24.685714285714287)# 35
        self.max_rect = pygame.rect.Rect(self.health_x, self.health_y, self.max, screen_height / 172.8) # 5
        self.health_rect = pygame.Rect(self.health_x, self.health_y, self.health, screen_height / 172.8)
        self.zyje = True
        self.tracenie_zyc = self.max / 100 # 0.5
        self.predkosc_poz = 0
        self.predkosc_pion = 0
        self.max_predkosc_normal = screen_width / 100 # 15
        self.przyspieszenie_normal = screen_width / 6144
        self.max_predkosc = self.max_predkosc_normal
        self.przyspieszenie = self.przyspieszenie_normal
        self.direction = 0
        self.zwalnianie = screen_width / 153600 # 0.01
        self.player_score = 0##
        self.die = pygame.font.Font.render(pygame.font.SysFont('arial', round(screen_width / 15.36)), 'Game over!!!', True, (0, 0, 0))#anty aliasing - teoretyczne ulepszenie tekstu
        self.player_score_napis = pygame.font.SysFont('arial', round(screen_width / 30.72)).render(f'money: {self.player_score}', True, (0, 0, 0))
        self.playerplayerplayer = pygame.image.load(f'img/playerplayer{self.skin}.png').convert_alpha()
        self.height = screen_height / 17.28
        self.width = self.height
        self.playerplayer = pygame.transform.scale(self.playerplayerplayer, (self.width, self.height))
        self.player = pygame.transform.rotate(self.playerplayer, self.direction)
        self.player_rect = self.player.get_rect(center = (self.x, self.y))
        self.hitboxhitbox = pygame.Rect(self.x - (self.playerplayer.get_width() - self.height / 10) / 2, self.y - (self.playerplayer.get_height() - self.width / 10) / 2, self.playerplayer.get_width() - self.height / 10, self.playerplayer.get_height() - self.width / 10)
        self.strzaly_gongupy = []
        self.czy_najezda = False
        self.kiedy_najezda_kolor = (130, 135, 133)
        self.normalny_kolor = (81, 89, 86)
        self.czy_jest_w_bunkrze = False
        self.again = pygame.font.Font.render(pygame.font.SysFont('arial', round(screen_height / 33.44)), 'again', True, (0, 0, 0))#anty aliasing - teoretyczne ulepszenie tekstu
        self.menu = pygame.font.Font.render(pygame.font.SysFont('arial', round(screen_height / 33.44)), 'menu', True, (0, 0, 0))#anty aliasing - teoretyczne ulepszenie tekstu
        self.again_button = pygame.rect.Rect(screen_width / 2 - screen_width / 15.36, screen_height / 2, round(screen_height / 33.44), round(screen_height / 33.44) / 1.6666666666666667)
        self.menu_button = pygame.rect.Rect(screen_width / 2 + screen_width / 15.36, screen_height / 2, round(screen_height / 33.44), round(screen_height / 33.44) / 1.6666666666666667)
        self.again_button_hitbox = pygame.rect.Rect(screen_width / 2 - screen_width / 15.36, screen_height / 2, round(screen_height / 33.44), round(screen_height / 33.44) / 1.6666666666666667)
        self.menu_button_hitbox = pygame.rect.Rect(screen_width / 2 + screen_width / 15.36, screen_height / 2, round(screen_height / 33.44), round(screen_height / 33.44) / 1.6666666666666667)
        self.color_again = self.normalny_kolor
        self.color_menu = self.normalny_kolor
        self.gongupa_refresh = False
        self.previous_health = self.health
        self.wrocwroc = pygame.image.load('img/wroc.png')
        self.wroc = pygame.transform.scale(self.wrocwroc, (round(screen_width /  3.072 / 2 / 2), round(screen_height / 2.4 / 2 / 2)))
        self.wroc_hitbox = pygame.Rect(screen_width - self.wroc.get_width(), 0, self.wroc.get_width(), self.wroc.get_height())
        self.menu_bool = False # przy wroc czy w��czy� menu
        self.click_wroc = True
    def refresh(self):
        self.click_wroc = True
        self.refreshing = True
        self.x = round(screen_width / 2)
        self.y = round(screen_height / 2)
        self.max = round(screen_width / 30.72)
        self.previous_x = self.x
        self.previous_y = self.y
        self.health = self.max
        self.health_x = round(self.x - (self.max / 2))# 25
        self.health_y = round(self.y - (screen_height / 24.685714285714287))# 35
        self.max_rect = pygame.rect.Rect(self.health_x, self.health_y, self.max, screen_height / 172.8) # 5
        self.health_rect = pygame.Rect(self.health_x, self.health_y, self.health, screen_height / 172.8)
        self.zyje = True
        self.czy_jest_w_bunkrze = False
        self.predkosc_poz = 0
        self.predkosc_pion = 0
        self.direction = 0
        self.player = pygame.transform.rotate(self.playerplayer, self.direction)
        self.player_rect = self.player.get_rect(center = (self.x, self.y))
        self.strzaly_gongupy = []
        self.zm_targowa = None
        self.przyspieszenie = self.przyspieszenie_normal
        self.max_predkosc = self.max_predkosc_normal
        self.previous_health = self.health
        self.player_score = 0
        self.player_score_napis = self.player_score_napis = pygame.font.SysFont('arial', round(screen_width / 30.72)).render(f'money: {self.player_score}', True, (0, 0, 0))
    def obliczanie_kierunku(self):
        pos = pygame.mouse.get_pos()
        x_dist = pos[0] - self.x
        y_dist = -(pos[1] - self.y)
        angle = math.degrees(math.atan2(y_dist, x_dist))
        self.direction = angle
    def tick(self, keys):
        if self.refreshing:
            self.refreshing = False
        if self.zyje:
            self.player_score_napis = pygame.font.SysFont('arial', round(screen_width / 30.72)).render(f'money: {self.player_score}', True, (0, 0, 0))
            self.gongupa_refresh = False
            self.health_x = round(self.x - (self.max / 2))# 25
            self.health_y = round(self.y - (screen_height / 24.685714285714287))# 35
            self.max_rect = pygame.rect.Rect(self.health_x, self.health_y, self.max, screen_height / 172.8) # 5
            self.health_rect = pygame.Rect(self.health_x, self.health_y, self.health, screen_height / 172.8)
            self.player = pygame.transform.rotate(self.playerplayer, self.direction)
            self.hitboxhitbox = pygame.Rect(self.x - (self.playerplayer.get_width() - self.height / 10) / 2, self.y - (self.playerplayer.get_height() - self.width / 10) / 2, self.playerplayer.get_width() - self.height / 10, self.playerplayer.get_height() - self.width / 10)
            self.player_rect = self.player.get_rect(center = (self.x, self.y))
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.predkosc_pion -= self.przyspieszenie
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.predkosc_pion += self.przyspieszenie
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.predkosc_poz += self.przyspieszenie
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.predkosc_poz -= self.przyspieszenie  
            if self.predkosc_poz > self.max_predkosc:
                self.predkosc_poz -= self.przyspieszenie
            for strzala in self.strzaly_gongupy:
                if self.hitboxhitbox.colliderect(strzala.bullet_hitbox):
                    if not any(bunker.colliderect(self.hitboxhitbox) for bunker in self.bunkier.bunkers_hitbox):
                        self.health -= self.tracenie_zyc
                        self.strzaly_gongupy.remove(strzala)################################################################################################ tutaj!!!!!!!!!!!!!!!!!!!!
            if self.wroc_hitbox.collidepoint(pygame.mouse.get_pos()) and not self.click_wroc:
                if pygame.mouse.get_pressed()[0]:
                    self.menu_bool = True
            if self.hitboxhitbox.colliderect(self.krzak.krzak_hitbox):
                self.przyspieszenie = self.przyspieszenie_normal / 3
                self.max_predkosc = self.max_predkosc_normal / 3
            if not self.hitboxhitbox.colliderect(self.krzak.krzak_hitbox):
                self.przyspieszenie = self.przyspieszenie_normal
                self.max_predkosc = self.max_predkosc_normal
            if self.health <= 0:
                self.zyje = False
                self.health = 0
            self.x += self.predkosc_poz
            self.y += self.predkosc_pion
            self.previous_x = self.x
            self.previous_y = self.y
            if self.x < 0:
                self.predkosc_poz = 0
                self.x = 0
            elif self.x > screen_width:
                self.predkosc_poz = 0
                self.x = screen_width
            if self.y < 0:
                self.predkosc_pion = 0
                self.y = 0
            elif self.y > screen_height:
                self.predkosc_pion = 0
                self.y = screen_height
            if self.predkosc_poz > self.max_predkosc:
                self.predkosc_poz -= self.przyspieszenie
            elif self.predkosc_poz < self.max_predkosc * -1:
                self.predkosc_poz += self.przyspieszenie
            if self.predkosc_pion > self.max_predkosc:
                self.predkosc_pion -= self.przyspieszenie
            elif self.predkosc_pion < self.max_predkosc * -1:
                self.predkosc_pion += self.przyspieszenie
            if self.predkosc_poz < 0:
                self.predkosc_poz += self.zwalnianie
            elif self.predkosc_poz > 0:
                self.predkosc_poz -= self.zwalnianie
            if self.predkosc_pion < 0:
                self.predkosc_pion += self.zwalnianie
            elif self.predkosc_pion > 0:
                self.predkosc_pion -= self.zwalnianie
            if pygame.mouse.get_pressed()[0]:
                self.click_wroc = True
            else:
                self.click_wroc = False
    def none_life(self):
        if self.again_button_hitbox.collidepoint(pygame.mouse.get_pos()):
            self.color_again = self.kiedy_najezda_kolor
            if pygame.mouse.get_pressed()[0]:
                self.gongupa_refresh = True
                self.zm_targowa = 'again'
                self.refresh()
        else:
            self.color_again = self.normalny_kolor
        if self.menu_button_hitbox.collidepoint(pygame.mouse.get_pos()):
            self.color_menu = self.kiedy_najezda_kolor
            if pygame.mouse.get_pressed()[0]:
                self.zm_targowa = 'menu'
        else:
            self.color_menu = self.normalny_kolor
        if not self.zm_targowa == 'menu' and not self.zm_targowa == 'again':
            self.zm_targowa = 'none'
        window.blit(self.die, (round(screen_width / 2 - screen_width / 30.72), round(screen_height / 4.32)))
        pygame.draw.rect(window, self.color_again, self.again_button)
        window.blit(self.again, (round(screen_width / 2 - screen_width / 15.36), round(screen_height / 2.16)))
        pygame.draw.rect(window, self.color_menu, self.menu_button)
        window.blit(self.menu, (round(screen_width / 2 + screen_width / 15.36), round(screen_height / 2.16)))
        pygame.display.update()
    def draw(self):
        if self.health > round(self.max / 5):
            color = (69, 245, 66)
        else:
            color = (222, 11, 29)
        pygame.draw.rect(window, (83, 94, 83), self.max_rect)
        pygame.draw.rect(window, color, self.health_rect)
        window.blit(self.player, self.player_rect)
        window.blit(self.wroc, (screen_width - self.wroc.get_width(), 0))
        window.blit(self.player_score_napis, (0, 0))
class Weapon:
    def __init__(self, x, y, speed, damage, bunker, gongupa, player):
        self.player = player
        self.gongupa = gongupa
        self.bunker = bunker
        self.direction = 0
        self.speed = speed
        self.damage = damage
        self.x = x
        self.clock = 0
        self.y = y
        self.weaponweaponweapon = pygame.image.load('img/weapon.png').convert_alpha()
        self.weaponweapon = pygame.transform.scale(self.weaponweaponweapon, (infoo.width_weapon, infoo.height_weapon))
        self.weapon = pygame.transform.rotate(self.weaponweapon, self.direction)
        self.bullets = []
        self.plus_punkt = False
    def refresh(self):
        self.clock = 0
        self.bullets = []
    def update_position(self, player_x, player_y):
        self.x = player_x
        self.y = player_y
    def obliczanie_kierunku(self):
        pos = pygame.mouse.get_pos()
        x_dist = pos[0] - self.x
        y_dist = -(pos[1] - self.y)
        angle = math.degrees(math.atan2(y_dist, x_dist))
        self.direction = angle
    def tick(self):
        self.obliczanie_kierunku()
        if self.plus_punkt:
            self.plus_punkt = False
        if pygame.mouse.get_pressed()[0]:  # Je�li lewy przycisk myszy jest wci�ni�ty
            if self.clock > co_ile_strzal:
                self.clock = 0
                pozycja_kursora = pygame.mouse.get_pos()
                self.bullets.append(Bullet(self.x, self.y, pozycja_kursora[0], pozycja_kursora[1], self.speed * 5))
                 
        for pocisk in self.bullets:
            pocisk.tick()
            for bunker in self.bunker.bunkers_hitbox:
                if pocisk.bullet_hitbox.colliderect(bunker) and self.player.hitboxhitbox.colliderect(bunker):
                    self.bullets.remove(pocisk)
            if pocisk.clock_time_of_life_bullet >= fps * 5: # liczba sekund do usuni�cia
                self.bullets.remove(pocisk)
            if pocisk.bullet_hitbox.colliderect(self.gongupa.gongupagongupa_hitbox):
                self.plus_punkt = True
        self.clock += 1
    def draw(self):
        for bullet in self.bullets:
            bullet.draw()

        # Oblicz przesuni�cie
        offset_distance = 20  # Odleg�o��, na jak� chcemy wysun�� bro�
        offset_x = offset_distance * math.cos(math.radians(self.direction))
        offset_y = -offset_distance * math.sin(math.radians(self.direction))
        # Oblicz now� pozycj� broni
        new_x = self.x + offset_x
        new_y = self.y + offset_y
        rotated_weapon = pygame.transform.rotate(self.weaponweapon, self.direction)
        weapon_rect = rotated_weapon.get_rect(center=(new_x, new_y))
        window.blit(rotated_weapon, weapon_rect.topleft)
class Gongupa_weapon:
    def __init__(self, speed, damage, gongupa, player, bunker):
        self.bunker = bunker
        self.player = player
        self.player_x = self.player.x
        self.player_y = self.player.y
        self.direction = 0
        self.speed = speed
        self.damage = damage
        self.gongupa = gongupa
        self.x = self.gongupa.x
        self.clock = 0
        self.y = self.gongupa.y
        self.weaponweaponweapon = pygame.image.load('img/weapon.png').convert_alpha()
        self.weaponweapon = pygame.transform.scale(self.weaponweaponweapon, (infoo.width_weapon, infoo.height_weapon))
        self.weapon = pygame.transform.rotate(self.weaponweapon, self.direction)
        self.bullets = []
    def update_position(self):
        self.player_x = self.player.x
        self.player_y = self.player.y
        self.x = self.gongupa.x
        self.y = self.gongupa.y
    def refresh(self):
        self.clock = 0
        self.bullets = []
    def tick(self):
        self.x = self.gongupa.x
        self.y = self.gongupa.y
        self.weapon = pygame.transform.rotate(self.weaponweapon, self.direction)
        if self.clock > co_ile_strzal:
            self.clock = 0
            x_dist = (self.player_x - self.x)
            y_dist = -(self.player_y - self.y)
            angle = math.degrees(math.atan2(y_dist, x_dist))
            self.direction = angle
            cel_x, cel_y = self.player_x, self.player_y
            pocisk = Bullet(self.x, self.y, cel_x, cel_y, self.speed * 5)
            self.bullets.append(pocisk)
        for pocisk in self.bullets:
            for bunker in self.bunker.bunkers_hitbox:
                if pocisk.bullet_hitbox.colliderect(bunker) and self.gongupa.gongupagongupa_hitbox.colliderect(bunker):
                    self.bullets.remove(pocisk)
            pocisk.tick()
            if pocisk.clock_time_of_life_bullet > 68 * 5: # liczba sekund do usuni�cia
                self.bullets.remove(pocisk)
        self.clock += 1
    def draw(self):
        for bullet in self.bullets:
            bullet.draw()
        offset_distance = 20
        offset_x = offset_distance * math.cos(math.radians(self.direction))
        offset_y = -offset_distance * math.sin(math.radians(self.direction))
        new_x = self.x + offset_x
        new_y = self.y + offset_y
        rotated_weapon = pygame.transform.rotate(self.weaponweapon, self.direction)
        weapon_rect = rotated_weapon.get_rect(center=(new_x, new_y))
        window.blit(rotated_weapon, weapon_rect.topleft)
class Bullet:
    def __init__(self, start_x, start_y, cel_x, cel_y, predkosc=5.0):
        self.x = round(start_x - (screen_width / 384.0))
        self.y = round(start_y - (screen_height / 216.0))
        self.bullet = pygame.Rect(self.x, self.y, infoo.width_bullet, infoo.height_bullet)
        self.bullet_hitbox = pygame.Rect(self.x, self.y, infoo.width_bullet, infoo.height_bullet)# width, height.
        self.predkosc = predkosc
        roznica_x = cel_x - start_x
        roznica_y = cel_y - start_y
        odleglosc = math.hypot(roznica_x, roznica_y)  
        self.clock_time_of_life_bullet = 0
        self.czy_warto = False
        if odleglosc != 0:
            self.przesuniecie_x = (roznica_x / odleglosc) * self.predkosc
            self.przesuniecie_y = (roznica_y / odleglosc) * self.predkosc
        else:
            self.przesuniecie_x = 0
            self.przesuniecie_y = 0
    def tick(self):
        self.x += self.przesuniecie_x
        self.y += self.przesuniecie_y
        self.bullet = pygame.Rect(self.x, self.y, infoo.width_bullet, infoo.height_bullet)
        self.bullet_hitbox = pygame.Rect(self.x, self.y, infoo.width_bullet, infoo.height_bullet)
        self.bullet.topleft = (self.x, self.y)  # Aktualizacja pozycji prostok�ta
        self.clock_time_of_life_bullet += 1
    def draw(self):
        pygame.draw.rect(window, (101, 110, 103), self.bullet)
class Gongupa:
    def __init__(self, player, organizator, krzak, bunker):
        self.bunker = bunker
        self.czy_jest_w_bunkrze = False
        self.krzak = krzak
        self.organizator = organizator
        self.x = round(screen_width / 1.28)
        self.y = round(screen_height / 17.28)
        self.player = player
        self.player_x = self.player.x
        self.player_y = self.player.y
        self.player_score = self.player.player_score
        self.direction = 0
        self.max = screen_width / 30.72
        self.health = self.max # 50
        self.health_x = round(self.x - (self.max / 2))# 25
        self.health_y = round(self.y - (screen_height / 24.685714285714287))# 35
        self.max_rect = pygame.rect.Rect(self.health_x, self.health_y, self.max, round(screen_height / 172.8)) # 5
        self.health_rect = pygame.Rect(self.health_x, self.health_y, self.health, round(screen_height / 172.8))
        self.zyje = True
        self.tracenie_zyc = self.max / 100 # 0.5
        self.gongupagongupagongupa = pygame.image.load('img/gongupa.png').convert_alpha()
        self.height = screen_height / 17.28
        self.gongupagongupa = pygame.transform.scale(self.gongupagongupagongupa, (round(screen_height / 17.28), round(screen_height / 17.28))) # 50
        self.width = self.height
        self.gongupagongupa_hitbox = pygame.Rect(self.x - (self.gongupagongupa.get_width() - self.height / 10) / 2, self.y - (self.gongupagongupa.get_height() - self.width / 10) / 2, self.gongupagongupa.get_width() - self.height / 10, self.gongupagongupa.get_height() - self.width / 10)
        self.gongupa = pygame.transform.rotate(self.gongupagongupa, self.direction)
        self.gongupa_rect = self.gongupa.get_rect(center = (self.x, self.y))
        self.przyspieszenie_normal = screen_width / 6144
        self.zwalnianie = screen_width / 153600 # 0.01
        self.max_speed_normal = screen_width / 300 # 15
        self.przyspieszenie = self.przyspieszenie_normal
        self.max_speed = self.max_speed_normal
        self.speed_poz = 0
        self.speed_pion = 0
        self.strzaly_gracza = []
        roznica_x = self.player_x - self.x
        roznica_y = self.player_y - self.y
        odleglosc = math.hypot(roznica_x, roznica_y)
        self.przesuniecie_x = (roznica_x / odleglosc) * self.speed_poz
        self.przesuniecie_y = (roznica_y / odleglosc) * self.speed_pion
        self.los_y = randint(1, 2) # 1 jako na d�, 2 jako na g�r�
        self.los_x = randint(1, 2) # 1 jako doprzodu
        self.mozna_y = True
        self.mozna_x = True
        self.czy_warto = False
    def refresh(self):
        # self.player_score = self.player.player_score
        self.czy_warto = False
        self.organizator.liczba_dostepnych_dodan_plytek += 10
        self.x = round(screen_width / 1.28)
        self.y = round(screen_height / 17.28)
        self.player_x = self.player.x
        self.player_y = self.player.y
        self.direction = 0
        self.max = round(screen_width / 30.72)
        self.health = self.max # 50
        self.health_x = round(self.x - (self.max / 2))# 25
        self.health_y = round(self.y - (screen_height / 24.685714285714287))# 35
        self.max_rect = pygame.rect.Rect(self.health_x, self.health_y, self.max, screen_height / 172.8) # 5
        self.health_rect = pygame.Rect(self.health_x, self.health_y, self.health, screen_height / 172.8)
        self.zyje = True
        self.gongupagongupa_hitbox = pygame.Rect(self.x, self.y, self.gongupagongupa.get_width(), self.gongupagongupa.get_height())
        self.gongupa = pygame.transform.rotate(self.gongupagongupa, self.direction)
        self.gongupa_rect = self.gongupa.get_rect(center = (self.x, self.y))
        self.przyspieszenie = screen_width / 6144
        self.zwalnianie = screen_width / 153600 # 0.01
        self.max_speed = screen_width / 300 # 15
        self.speed_poz = 0
        self.speed_pion = 0
        self.strzaly_gracza = []
        roznica_x = self.player_x - self.x
        roznica_y = self.player_y - self.y
        odleglosc = math.hypot(roznica_x, roznica_y)
        self.przesuniecie_x = (roznica_x / odleglosc) * self.speed_poz
        self.przesuniecie_y = (roznica_y / odleglosc) * self.speed_pion
        self.mozna_y = True
        self.mozna_x = True
        self.los_y = randint(1, 2) # 1 jako na d�, 2 jako na g�r�
        self.los_x = randint(1, 2) # 1 jako doprzod
        self.przyspieszenie = self.przyspieszenie_normal
        self.max_speed = self.max_speed_normal
    def obliczanie_kierunku(self):
        pos = (self.player_x, self.player_y)
        x_dist = pos[0] - self.x
        y_dist = -(pos[1] - self.y)
        angle = math.degrees(math.atan2(y_dist, x_dist))
        self.direction = angle
    def tick(self):
        self.czy_warto = False
        if self.player.gongupa_refresh:
            self.refresh()
        self.health_x = round(self.x - (self.max / 2))# 25
        self.health_y = round(self.y - (screen_height / 24.685714285714287))# 35
        self.max_rect = pygame.rect.Rect(self.health_x, self.health_y, self.max, screen_height / 172.8) # 5
        self.health_rect = pygame.Rect(self.health_x, self.health_y, self.health, screen_height / 172.8)
        self.player_x = self.player.x
        self.player_y = self.player.y
        self.gongupagongupa_hitbox = pygame.Rect(self.x, self.y, self.gongupagongupa.get_width(), self.gongupagongupa.get_height())
        self.gongupa = pygame.transform.rotate(self.gongupagongupa, self.direction)
        self.gongupa_rect = self.gongupa.get_rect(center = (self.x, self.y))
        self.player_score = self.player.player_score
        for strzala in self.strzaly_gracza:
                if self.gongupagongupa_hitbox.colliderect(strzala.bullet_hitbox):
                    if not any(bunker.colliderect(self.gongupagongupa_hitbox) for bunker in self.bunker.bunkers_hitbox):
                        self.health -= self.tracenie_zyc
                        self.strzaly_gracza.remove(strzala)
        if self.gongupagongupa_hitbox.colliderect(self.krzak.krzak_hitbox):
            self.przyspieszenie = self.przyspieszenie_normal / 3
            self.max_speed = self.max_speed_normal / 3
        if self.health <= 0:
            self.zyje = False
            self.health = 0
            self.refresh()
        if self.y < self.player_y:
            if (self.player_y - self.y) > (screen_width / 5.12):
                self.mozna_y = True
                self.speed_pion += self.przyspieszenie
            else:
                if self.mozna_y:
                    self.los_y = randint(1, 2)
                    self.mozna_y = False
                if self.los_y == 1:
                    self.speed_pion += self.przyspieszenie
                elif self.los_y == 2:
                    self.speed_pion -= self.przyspieszenie
        elif self.y > self.player_y:
            if (self.y - self.player_y) > (screen_width / 5.12):
                self.mozna_y = True
                self.speed_pion -= self.przyspieszenie
            else:
                if self.mozna_y:
                    self.los_y = randint(1, 2)
                    self.mozna_y = False
                if self.los_y == 1:
                    self.speed_pion += self.przyspieszenie
                elif self.los_y == 2:
                    self.speed_pion -= self.przyspieszenie
        if self.x < self.player_x:
            if (self.player_x - self.x) > (screen_width / 5.12):
                self.mozna_x = True
                self.speed_poz += self.przyspieszenie
            else:
                if self.mozna_x:
                    self.los_x = randint(1, 2)
                    self.mozna_x = False
                if self.los_x == 1:
                    self.speed_poz += self.przyspieszenie
                elif self.los_x == 2:
                    self.speed_poz -= self.przyspieszenie
        elif self.x > self.player_x:
            if (self.x - self.player_x) > (screen_width / 5.12):
                self.mozna_x = True
                self.speed_poz -= self.przyspieszenie
            else:
                if self.mozna_x:
                    self.los_x = randint(1, 2)
                    self.mozna_x = False
                if self.los_x == 1:
                    self.speed_poz += self.przyspieszenie
                elif self.los_x == 2:
                    self.speed_poz -= self.przyspieszenie
        self.x += self.speed_poz
        self.y += self.speed_pion
        if self.speed_poz > self.max_speed:
            self.speed_poz -= self.przyspieszenie
        elif self.speed_poz < self.max_speed * -1:
            self.speed_poz = self.max_speed * -1
        if self.speed_pion > self.max_speed:
            self.speed_pion = self.max_speed
        elif self.speed_pion < self.max_speed * -1:
            self.speed_pion = self.max_speed * -1
        if self.speed_poz < 0:
            self.speed_poz += self.zwalnianie
        elif self.speed_poz > 0:
            self.speed_poz -= self.zwalnianie
        if self.speed_pion < 0:
            self.speed_pion += self.zwalnianie
        elif self.speed_pion > 0:
            self.speed_pion -= self.zwalnianie
        if self.x < 0:
            self.predkosc_poz = 0
            self.x = 0
        elif self.x > screen_width:
            self.predkosc_poz = 0
            self.x = screen_width
        if self.y < 0:
            self.predkosc_pion = 0
            self.y = 0
        elif self.y > screen_height:
            self.predkosc_pion = 0
            self.y = screen_height
    def draw(self):
        if self.health > self.max / 10:
            color = (69, 245, 66)
        else:
            color = (222, 11, 29)
        pygame.draw.rect(window, (83, 94, 83), self.max_rect)
        pygame.draw.rect(window, color, self.health_rect)
        window.blit(self.gongupa, self.gongupa_rect)
class Teloporter:
    def __init__(self, player, gongupa):
        self.player = player
        self.gongupa = gongupa
        self.one_x = round(screen_width / 3.84)#400
        self.one_y = round(screen_height / 2.16)#400
        self.two_x = round(screen_width / 2.1942857142857144)
        self.two_y = round(screen_height / 2.16) # 62!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!(nie to!!!!!!!!!!!!!!!!!!!!!!!!)
        self.holding_player = 0 # zero jako nie, 1 jako one, 2 jako two
        self.holding_gongupa = 0 # zero jako nie, 1 jako one, 2 jako two
        self.oneone = pygame.image.load('img/teleporter.png')
        self.one = pygame.transform.scale(self.oneone, (round(screen_height / 13.935483870967742), round(screen_height / 13.935483870967742)))
        self.one_hitbox = pygame.Rect(self.one_x, self.one_y, self.one.get_width(), self.one.get_height())
        self.twotwo = pygame.image.load('img/teleporter.png')
        self.two = pygame.transform.scale(self.twotwo, (round(screen_height / 13.935483870967742), round(screen_height / 13.935483870967742)))
        self.two_hitbox = pygame.Rect(self.two_x, self.two_y, self.two.get_width(), self.two.get_height())
        self.cooldown_time = 1  # czas w sekundach
        self.last_teleport_time = 0
    def tick(self):
        current_time = time.time()
        if current_time - self.last_teleport_time > self.cooldown_time:
            if self.player.hitboxhitbox.colliderect(self.one_hitbox) and not self.holding_player == 1:
                self.player.x = self.two_x
                self.player.y = self.two_y
                self.holding_player = 2
                self.last_teleport_time = current_time
            elif self.player.hitboxhitbox.colliderect(self.two_hitbox) and not self.holding_player == 2:
                self.player.x = self.one_x
                self.player.y = self.one_y
                self.holding_player = 1
                self.last_teleport_time = current_time
            if self.gongupa.gongupagongupa_hitbox.colliderect(self.one_hitbox) and not self.holding_gongupa == 1:
                self.gongupa.x = self.two_x
                self.gongupa.y = self.two_y
                self.holding_gongupa = 2
                self.last_teleport_time = current_time
            elif self.gongupa.gongupagongupa_hitbox.colliderect(self.two_hitbox) and not self.holding_gongupa == 2:
                self.gongupa.x = self.one_x
                self.gongupa.y = self.one_y
                self.holding_gongupa = 1
                self.last_teleport_time = current_time
        if not (self.player.hitboxhitbox.colliderect(self.two_hitbox) or self.player.hitboxhitbox.colliderect(self.one_hitbox)):
            self.holding_player = 0
        if not (self.gongupa.gongupagongupa_hitbox.colliderect(self.two_hitbox) or self.gongupa.gongupagongupa_hitbox.colliderect(self.one_hitbox)):
            self.holding_gongupa = 0
    def draw(self):
        window.blit(self.one, (self.one_x, self.one_y))
        window.blit(self.two, (self.two_x, self.two_y))
class Plus_hp:
    def __init__(self, player):
        self.piorunpiorun = pygame.image.load('img/piorun.png')
        self.piorun = pygame.transform.scale(self.piorunpiorun, (round(screen_height / 36.0), round(screen_height / 36.0))) # 24
        self.x = randint(0, screen_width - self.piorun.get_width())
        self.y = randint(0, screen_height - self.piorun.get_height())
        self.hitbox = pygame.Rect(self.x, self.y, self.piorun.get_width(), self.piorun.get_height())
        self.plus_hp = 10 # ile dodaje
        self.player = player
        self.liczba_dodan = 10
    def draw(self):
        window.blit(self.piorun, (self.x, self.y))
class Organization:
    def __init__(self, player):
        self.liczba_dostepnych_dodan_plytek = 10
        self.clock = 0
        self.plus_hps = []
        self.player = player
    def tick(self):
        for i in self.plus_hps:
            if self.player.hitboxhitbox.colliderect(i.hitbox):
                self.player.health += i.plus_hp
                if self.player.health > self.player.max:
                    self.player.health = self.player.max
                self.plus_hps.remove(i)
        self.clock += 1
        if self.clock >= 68 * 3 and self.liczba_dostepnych_dodan_plytek > 0:
            self.clock = 0
            self.liczba_dostepnych_dodan_plytek -= 1
            self.plus_hps.append(Plus_hp(self.player))
    def draw(self):
        for i in self.plus_hps:
            i.draw()
class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
class Slider:
    def __init__(self, x, y, w, h, min_val, max_val):
        self.rect = pygame.rect.Rect(x, y, w, h)
        self.min_val = min_val
        self.max_val = max_val
        self.val = self.min_val
        self.sliding  = False
    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)
        knob_x = self.rect.x + int((self.val / self.max_val) * self.rect.width)
        pygame.draw.circle(screen, (0, 0, 0), (knob_x, self.rect.centery), 10)
    def update(self):
        mouse_pressed = pygame.mouse.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if mouse_pressed[0] and self.rect.collidepoint(mouse_x, mouse_y):
            self.sliding = True
        elif not mouse_pressed[0]:
            self.sliding = False
        if self.sliding:
            self.val = int(((mouse_x - self.rect.x) / self.rect.width) * self.max_val)
            self.val = max(self.min_val, min(self.val, self.max_val))

class Title_Screen:
    def __init__(self):
        self.money = 0
        self.suwaki_do_jazdy_x_one = screen_width - round(screen_width / 7.15)
        self.suwaki_do_jazdy_x_two = screen_width - round(screen_width / 7.15)
        self.suwaki_do_jazdy_x_three = screen_width - round(screen_width / 7.15)
        self.slider_r = Slider(screen_width - round(screen_width / 7.15) - round(screen_width / 15.36), screen_height / 2 + screen_height / 1.728 / 1.5, round(screen_width / 7.15), round(screen_height / 40), 0, 255)
        self.slider_g = Slider(screen_width - round(screen_width / 7.15) - round(screen_width / 15.36), screen_height / 2 + screen_height / 1.728 / 2, round(screen_width / 7.15), round(screen_height / 40), 0, 255)
        self.slider_b = Slider(screen_width - round(screen_width / 7.15) - round(screen_width / 15.36), screen_height / 3 + screen_height / 1.728 / 1.5, round(screen_width / 7.15), round(screen_height / 40), 0, 255)
        self.sliders = [self.slider_r, self.slider_g, self.slider_b]
        # self.liczba_wystepujacych_skinow = 7
        # self.player_images = [pygame.image.load(f'img/playerplayer{i}.png') for i in range(1, self.liczba_wystepujacych_skinow + 1)]
        # self.skins = [pygame.transform.scale(image, (int(screen_height / 17.28), int(screen_height / 17.28))) for image in self.player_images]
        self.find_all_skins()
        self.czy_usuwac = 0
        self.ktory_pokazuje = 0
        self.pokazowy = self.skins[self.ktory_pokazuje]
        self.x = round(screen_width / 2.3630769230769233)
        self.y = round(screen_height / 4.32)
        self.width = round(screen_width / 8.777142857142858) 
        self.height = round(screen_height / 6.912)
        plusespluses = [pygame.image.load(f'img/plus{i}.png') for i in range(1, 3)]
        self.pluses = [pygame.transform.scale(image, (int(screen_height / 17.28), int(screen_height / 17.28))) for image in plusespluses] # 62 x 62
        self.pluses_hitbox = pygame.Rect(self.x + self.width / 4, self.y + self.height, self.pluses[0].get_width(), self.pluses[0].get_height())
        self.x_y = (self.x, self.y)
        self.czy_najezda = False
        self.kiedy_najezda_kolor = (130, 135, 133)
        self.normalny_kolor = (81, 89, 86)
        self.game_name = pygame.font.Font.render(pygame.font.SysFont('arial', round(screen_height / 8.64)), 'Gongupa', True, (0, 0, 0))#anty aliasing - teoretyczne ulepszenie tekstu
        self.play_title = pygame.font.Font.render(pygame.font.SysFont('arial', round(screen_height / 8.64)), 'Play', True, (0, 0, 0))#anty aliasing - teoretyczne ulepszenie tekstu
        self.play_button = pygame.rect.Rect(self.x, self.y, self.width, self.height)
        self.hitbox_play_button = pygame.Rect(self.x, self.y, self.width, self.height)
        self.arow_right, self.arow_left = pygame.rect.Rect(self.x + self.width, self.y + self.height, round(self.width / 2), round(self.height / 2)), pygame.rect.Rect(self.x - self.width / 2, self.y + self.height, round(self.width / 2), round(self.height / 2))
        self.arow_right_hitbox, self.arow_left_hitbox = pygame.Rect(self.x + self.width, self.y + self.height, round(self.width / 2), round(self.height / 2)), pygame.Rect(self.x - self.width / 2, self.y + self.height, round(self.width / 2), round(self.height / 2))
        self.czy_najezda_right, self.czy_najezda_left = False, False
        self.color_normalny_wybor = (215, 0, 0)
        self.color_najezda_wybor = (155, 0, 0)
        self.color_left = self.color_normalny_wybor
        self.color_right = self.color_normalny_wybor
        self.trzyma = False
        self.ktory_bedzie_w_grze = 'img/playerplayer1.png'
        self.skins.append(self.pluses[0])
        self.trzyma_plus = False
        self.czy_mozna_przejsc_do_gry = True
        self.draw_rect =  pygame.rect.Rect(screen_width / 2 - screen_width / 3.072 / 2, screen_height / 2 - screen_height / 1.728 / 2, screen_width  / 3.072, screen_height / 1.728)
        self.draw_rect_hitbox = pygame.Rect(screen_width / 2 - screen_width / 3.072 / 2, screen_height / 2 - screen_height / 1.728 / 2, screen_width  / 3.072, screen_height / 1.728)
        self.circles = []
        self.draw_czy_wybor = 'wybor'
        self.first_click = True
        self.tla_napis = pygame.font.Font.render(pygame.font.SysFont('arial', round(screen_height / 8.64)), 'kolor:', True, (0, 0, 0))#anty aliasing - teoretyczne ulepszenie tekstu
        # self.skin_color = [pygame.rect.Rect(screen_width / 2 + screen_width / 3.072, screen_height / 2 - screen_height / 1.728 / 2, round(screen_width / 15.36), round(screen_height / 8.64)), pygame.Rect(screen_width / 2 + screen_width / 3.072, screen_height / 2 - screen_height / 1.728 / 2, round(screen_width / 15.36), round(screen_height / 8.64)), (252, 226, 196)]
        # self.white_color = [pygame.rect.Rect(screen_width / 2 + screen_width / 3.072, screen_height / 2 - screen_height / 1.728 / 2 + round(screen_height / 8.64) + screen_height / 1536, round(screen_width / 15.36), round(screen_height / 8.64)), pygame.Rect(screen_width / 2 + screen_width / 3.072, screen_height / 2 - screen_height / 1.728 / 2, round(screen_width / 15.36), round(screen_height / 8.64)), (252, 252, 252)]
        self.suwaki = [pygame.rect.Rect(screen_width - round(screen_width / 7.15), screen_height / 2 + screen_height / 1.728 / 1.5, round(screen_width / 7.15), round(screen_height / 40)), pygame.rect.Rect(screen_width - round(screen_width / 7.15), screen_height / 2 + screen_height / 1.728 / 2 , round(screen_width / 7.15), round(screen_height / 40)), pygame.rect.Rect(screen_width - round(screen_width / 7.15), screen_height / 3 + screen_height / 1.728 / 1.5, round(screen_width / 7.15), round(screen_height / 40))]
        self.suwaki_hitbox = [pygame.Rect(screen_width - round(screen_width / 7.15), screen_height / 2 + screen_height / 1.728 / 1.5, round(screen_width / 7.15) - round(screen_width / 153.6), round(screen_height / 40)), pygame.Rect(screen_width - round(screen_width / 7.15), screen_height / 2 + screen_height / 1.728 / 2 , round(screen_width / 7.15) - round(screen_width / 153.6), round(screen_height / 40)), pygame.Rect(screen_width - round(screen_width / 7.15), screen_height / 3 + screen_height / 1.728 / 1.5, round(screen_width / 7.15) - round(screen_width / 153.6), round(screen_height / 40))]
        self.suwaki_do_jazdy = [pygame.rect.Rect(self.suwaki_do_jazdy_x_one, screen_height / 2 + screen_height / 1.728 / 1.5, round(screen_width / 153.6), round(screen_height / 43.2)), pygame.rect.Rect(self.suwaki_do_jazdy_x_two, screen_height / 2 + screen_height / 1.728 / 2, round(screen_width / 153.6), round(screen_height / 43.2)), pygame.rect.Rect(self.suwaki_do_jazdy_x_three, screen_height / 3 + screen_height / 1.728 / 1.5, round(screen_width / 153.6), round(screen_height / 43.2))]
        # self.suwaki_do_jazdy_hitbox = [pygame.Rect(self.suwaki_do_jazdy_x_one, screen_height / 2 + screen_height / 1.728 / 1.5, round(screen_width / 153.6), round(screen_height / 43.2)), pygame.Rect(self.suwaki_do_jazdy_x_two, screen_height / 2 + screen_height / 1.728 / 2, round(screen_width / 153.6), round(screen_height / 43.2)), pygame.Rect(self.suwaki_do_jazdy_x_three, screen_height / 3 + screen_height / 1.728 / 1.5, round(screen_width / 153.6), round(screen_height / 43.2))]
        self.r = 0
        self.g = 0
        self.b = 0
        self.draw_rect_color = (self.slider_r.val, self.slider_g.val, self.slider_b.val)
        self.jednostka_suwaki_jazda = round(screen_width / 7.15) / 255
        self.roznica = round(screen_width / 153.6 / 255)
        self.dokad = (screen_width / 2 + screen_width / 3.072, screen_width / 2 + screen_width / 3.072 + round(screen_width / 7.15))
        self.dlugosc_poza_suwakiem = screen_width - round(screen_width / 7.15)
        self.zapiszzapisz = pygame.image.load('img/zapisz.png')
        self.zapisz = pygame.transform.scale(self.zapiszzapisz, (round(screen_width / 9.90967741935484), round(screen_height / 2.618181818181818)))
        self.zapisz_hitbox = pygame.rect.Rect(0, 0, self.zapisz.get_width(), self.zapisz.get_height())
        self.slider_r_pen = Slider(screen_width / 51.2, screen_height / 2 + screen_height / 1.728 / 1.5, round(screen_width / 7.15), round(screen_height / 40), 0, 255)
        self.slider_g_pen = Slider(screen_width / 51.2, screen_height / 2 + screen_height / 1.728 / 2, round(screen_width / 7.15), round(screen_height / 40), 0, 255)
        self.slider_b_pen = Slider(screen_width / 51.2, screen_height / 3 + screen_height / 1.728 / 1.5, round(screen_width / 7.15), round(screen_height / 40), 0, 255)
        self.sliders_pen = [self.slider_r_pen, self.slider_g_pen, self.slider_b_pen]
        self.drawing_color = (round(self.slider_r_pen.val), round(self.slider_g_pen.val), round(self.slider_b_pen.val))
        self.draw_circle = Circle(round(screen_width / 51.2), round(screen_height / 2 + screen_height / 8.64), round(screen_width / 76.8), self.drawing_color)
        self.wrocwroc = pygame.image.load('img/wroc.png')
        self.wroc = pygame.transform.scale(self.wrocwroc, (round(screen_width /  3.072 / 2), round(screen_height / 2.4 / 2 / 2)))
        self.wroc_hitbox = pygame.Rect(0, self.zapisz.get_height() + 17.28, self.wroc.get_width(), self.wroc.get_height())
    def find_all_skins(self):
        i = 1
        while True:
            if not os.path.exists(f'img/playerplayer{i}.png'):
                break
            i+=1
        self.liczba_wystepujacych_skinow = i - 1
        self.player_images = [pygame.image.load(f'img/playerplayer{i}.png') for i in range(1, self.liczba_wystepujacych_skinow + 1)]
        self.skins = [pygame.transform.scale(image, (int(screen_height / 17.28), int(screen_height / 17.28))) for image in self.player_images]
    def drawing_tick(self):
        # self.czy_usuwac = True
        x, y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and self.draw_rect_hitbox.collidepoint((x, y)):
            if not self.first_click:
                circle = Circle(x, y, screen_height / 172.8, self.drawing_color)
                self.circles.append(circle)
        if not pygame.mouse.get_pressed()[0]:
            self.first_click = False
        for slider in self.sliders:
            slider.update()
        for slider_pen in self.sliders_pen:
            slider_pen.update()
        if pygame.mouse.get_pressed()[0] and not self.first_click and not self.trzyma and self.wroc_hitbox.collidepoint((x, y)):
            self.draw_czy_wybor = 'wybor'
            self.slider_r.val, self.slider_g.val, self.slider_b.val = 0, 0, 0
            self.slider_r_pen.val, self.slider_g_pen.val, self.slider_b_pen.val = 0, 0, 0
            self.circles.clear()
            self.first_click = True
            self.ktory_pokazuje = 0
        self.draw_rect_color = (self.slider_r.val, self.slider_g.val, self.slider_b.val)
        self.drawing_color = (round(self.slider_r_pen.val), round(self.slider_g_pen.val), round(self.slider_b_pen.val))
        self.suwaki_do_jazdy = [pygame.rect.Rect(self.suwaki_do_jazdy_x_one, screen_height / 2 + screen_height / 1.728 / 1.5, round(screen_width / 153.6), round(screen_height / 43.2)), pygame.rect.Rect(self.suwaki_do_jazdy_x_two, screen_height / 2 + screen_height / 1.728 / 2, round(screen_width / 153.6), round(screen_height / 43.2)), pygame.rect.Rect(self.suwaki_do_jazdy_x_three, screen_height / 3 + screen_height / 1.728 / 1.5, round(screen_width / 153.6), round(screen_height / 43.2))]
        if pygame.mouse.get_pressed()[0] and self.zapisz_hitbox.collidepoint((x, y)):
            self.czy_usuwac += 1
            self.liczba_wystepujacych_skinow += 1
            pyautogui.screenshot(f'img/playerplayer{self.liczba_wystepujacych_skinow}.png', region=(round(screen_width / 2 - screen_width / 3.072 / 2), round(screen_height / 2 - screen_height / 1.728 / 2), round(screen_width  / 3.072), round(screen_height / 1.728)))
            self.draw_czy_wybor = 'wybor'
            self.slider_r.val, self.slider_g.val, self.slider_b.val = 0, 0, 0
            self.slider_r_pen.val, self.slider_g_pen.val, self.slider_b_pen.val = 0, 0, 0
            self.circles.clear()
            self.first_click = True
            self.ktory_pokazuje = 0
            self.player_images = [pygame.image.load(f'img/playerplayer{i}.png') for i in range(1, self.liczba_wystepujacych_skinow + 1)]
            self.skins = [pygame.transform.scale(image, (int(screen_height / 17.28), int(screen_height / 17.28))) for image in self.player_images]
            self.skins.append(self.pluses[0])
        pygame.draw.rect(window, self.draw_rect_color, self.draw_rect)############################################################################################
        self.draw_circle = Circle(round(screen_width / 51.2), round(screen_height / 2 + screen_height / 8.64), round(screen_width / 76.8), self.drawing_color)
        for circle in self.circles:
            circle.draw(window)
        window.blit(self.tla_napis, (screen_width / 2 + screen_width / 3.072 - round(screen_width / 15.36) - screen_width / 50, screen_height / 2 - screen_height / 1.728 / 2))
        self.draw_circle.draw(window)
        window.blit(self.wroc, (0, self.zapisz.get_height() + 17.28))
        for slider in self.sliders:
            slider.draw(window)
        for slider_pen in self.sliders_pen:
            slider_pen.draw(window)
        window.blit(self.zapisz, (0, 0))
    def tick(self):
        pos = pygame.mouse.get_pos()
        if not pygame.mouse.get_pressed()[0]:
            self.trzyma_plus = False
        if self.arow_left_hitbox.collidepoint(pos):
            self.color_left = self.color_najezda_wybor
            if pygame.mouse.get_pressed()[0] and not self.trzyma:
                self.trzyma = True
                self.ktory_pokazuje -= 1
                if self.ktory_pokazuje < 0:
                    self.ktory_pokazuje = len(self.skins) - 1
        else:
            self.color_left = self.color_normalny_wybor
        if self.arow_right_hitbox.collidepoint(pos):
            self.color_right = self.color_najezda_wybor
            if pygame.mouse.get_pressed()[0] and not self.trzyma:
                self.trzyma = True
                self.ktory_pokazuje += 1
                if self.ktory_pokazuje > len(self.skins) - 1:
                    self.ktory_pokazuje = 0
        else:
            self.color_right = self.color_normalny_wybor
        if self.ktory_pokazuje == len(self.skins) - 1:
            self.czy_mozna_przejsc_do_gry = False
            if self.pluses_hitbox.collidepoint(pos):
                self.skins[len(self.skins) - 1] = self.pluses[1]
                if pygame.mouse.get_pressed()[0]:
                    if not self.trzyma_plus:
                        self.draw_czy_wybor = 'draw'
                        self.trzyma_plus = True
            else:
                self.skins[len(self.skins) - 1] = self.pluses[0]
        else:
            self.czy_mozna_przejsc_do_gry = True
        if not self.trzyma:
            if self.hitbox_play_button.collidepoint(pos):
                self.czy_najezda = True
                if pygame.mouse.get_pressed()[0] and self.czy_mozna_przejsc_do_gry:
                    return True
            else:
                self.czy_najezda = False
        if not pygame.mouse.get_pressed()[0]:
            self.trzyma = False
        self.pokazowy = self.skins[self.ktory_pokazuje]
    def draw(self):
        if self.czy_najezda:
            pygame.draw.rect(window, self.kiedy_najezda_kolor, self.play_button)
        else:
            pygame.draw.rect(window, self.normalny_kolor, self.play_button)
        pygame.draw.rect(window, self.color_left, self.arow_left)
        pygame.draw.rect(window, self.color_right, self.arow_right)
        try:
            window.blit(self.pokazowy, (self.x + self.width / 4, self.y + self.height))
        except:
            pass
        window.blit(self.play_title, (self.x, self.y))
        window.blit(pygame.font.Font.render(pygame.font.SysFont('arial', round(screen_height / 8.64)), f'money: {self.money}', True, (0, 0, 0)), (self.x, self.y + self.width + round(screen_height / 1536)))
class Bunker:
    def __init__(self):
        self.bunkers = [pygame.rect.Rect(round(screen_width / 6.84), round(screen_height / 2.16), round(screen_width / 15.36), round(screen_height / 4.32)), pygame.rect.Rect(round(screen_width / 1.352112676056338), round(screen_height / 2.16), round(screen_width / 15.36), round(screen_height / 4.32))]
        self.bunkers_hitbox = [pygame.Rect(round(screen_width / 6.84), round(screen_height / 2.16), round(screen_width / 15.36), round(screen_height / 4.32)), pygame.Rect(round(screen_width / 1.352112676056338), round(screen_height / 2.16), round(screen_width / 15.36), round(screen_height / 4.32))]
    def draw(self):
        for bunker in self.bunkers:
            pygame.draw.rect(window, (87, 75, 62), bunker)
class Krzak:
    def __init__(self):
        self.krzakkrzak = pygame.image.load('img/krzak.png')
        self.krzak = pygame.transform.scale(self.krzakkrzak, (screen_width / 4.042105263157895, screen_height / 4.32)) # 380 x 200
        self.krzak_hitbox = pygame.rect.Rect(screen_width / 1.9948051948051948, screen_height / 86.4, self.krzak.get_width(), self.krzak.get_height())
    def draw(self):
        window.blit(self.krzak, (screen_width / 1.9948051948051948, screen_height / 86.4))