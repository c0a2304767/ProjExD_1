import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_fl_img = pg.image.load("fig/pg_bg.jpg")
    bg_fl_img = pg.transform.flip(bg_fl_img, True, False)
    kk_img = pg.image.load("fig/3.png") #練習2
    kk_img = pg.transform.flip(kk_img, True, False) #練習2
    kk_rct = kk_img.get_rect() #練習8-1:SurfaceからRectを抽出する
    kk_rct.center = 300, 200
    fps = 200

    tmr = 0
    while True:
        kk_x = 0
        kk_y = 0
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            kk_y -= 1
        if key_lst[pg.K_DOWN]:
            kk_y += 1
        if key_lst[pg.K_LEFT]:
            kk_x -= 1
        if key_lst[pg.K_RIGHT]:
            kk_x += 2
        kk_rct.move_ip((kk_x - 1, kk_y)) #演習課題2
        #kk_rct.move.ip((-1, 0)) #演習課題1
        x = -(tmr%3200)
        screen.blit(bg_img, [x, 0])
        screen.blit(bg_fl_img, [x+1600, 0])
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(kk_img, kk_rct)
        #screen.blit(kk_img, [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(fps)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()