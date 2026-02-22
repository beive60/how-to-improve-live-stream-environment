from PIL import Image, ImageDraw

width, height = 1920, 1080
grid_size = 100

# #b35a7d = RGB(179, 90, 125)
# アルファ値を3% (約8/255) に低減し、線幅の増加による過剰な主張を相殺する
line_color = (179, 90, 125, 8) 
line_weight = 10

img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# 線幅(width)パラメータを適用
for x in range(0, width, grid_size):
    draw.line([(x, 0), (x, height)], fill=line_color, width=line_weight)
for y in range(0, height, grid_size):
    draw.line([(0, y), (width, y)], fill=line_color, width=line_weight)

img.save('grid_bg.png')