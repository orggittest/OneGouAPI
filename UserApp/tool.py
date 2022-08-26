import random

# 验证码生成工具
from django.http import HttpResponse
from PIL import Image, ImageDraw, ImageFont
from django.core.cache import cache

# 随机验证码生成工具
def _random_str(start, end):
    return chr(random.randint(start, end))


def new_code_str(len):

    code_str = ''
    for _ in range(len):
        flag = random.randint(0, 2)
        start, end = (ord('a'), ord('z')) if flag == 1 \
            else (ord('A'), ord('Z')) if flag == 2 \
            else (ord('0'), ord('9'))

        code_str += _random_str(start, end)

    return code_str


def new_img_code(request):

    # 创建画布
    img = Image.new('RGB', (80, 40), (100, 100, 0))

    # 从画布中获取画笔
    draw = ImageDraw.Draw(img, 'RGB')

    # 创建字体对象和字体颜色
    font_color = (0, 20, 100)
    font = ImageFont.truetype(font='static/fonts/buding.ttf' ,size=20)

    str_yan = new_code_str(6)
    # 写入缓存待用
    cache.set('yanzhengma', str_yan, 2000)
    print(str_yan)
    # 开始画内容
    draw.text((5, 5), str_yan, font=font, fill=font_color)

    for _ in range(100):
        x = random.randint(0, 80)
        y = random.randint(0, 40)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        draw.point((x, y), (r, g, b))

    # 将画布写入内存字节数组中
    from io import BytesIO
    buffer = BytesIO()
    img.save(buffer, 'png')  # 写入

    return HttpResponse(content=buffer.getvalue(),
                        content_type='image/png')
