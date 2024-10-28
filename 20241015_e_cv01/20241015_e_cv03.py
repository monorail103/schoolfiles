import random

def generate_random_pgm(filename, width, height):
    max_val = 255
    with open(filename, 'w') as f:
        f.write(f'P2\n{width} {height}\n{max_val}\n')
        for _ in range(height):
            row = ' '.join(str(random.randint(0, max_val)) for _ in range(width))
            f.write(row + '\n')

generate_random_pgm('random_image.pgm', 640, 480)

# PGMファイルを表示
import cv2
cv2.imshow('image', cv2.imread('random_image.pgm', 1))
cv2.waitKey(0)
cv2.destroyAllWindows()