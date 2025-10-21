from PIL import Image

weixin_img_path = "/root/DeepSeekOCR/img/微信成员.png"
output_path = "/root/DeepSeekOCR/output_img/weixin/crop_img_1.png"
def crop_img(img_path: str, output_path: str, left: int, upper: int, right: int, lower: int):
    image = Image.open(img_path)
    print(image)
    box = (left, upper, right, lower)
    cropped_image = image.crop(box)
    cropped_image.save(output_path)
    image.close()
    return cropped_image
    

def gen_output_path(num_part: int):
    for num in range(num_part):
        yield f"/root/DeepSeekOCR/output_img/weixin/crop_img_{num}.png"
        

if __name__ == "__main__":
    crop_img(weixin_img_path, output_path,0, 0, 227, 50)
    weixin_num = 215
    paths = gen_output_path(weixin_num)
    for i in range(weixin_num):
        crop_img(weixin_img_path, next(paths), 0, (i * 50), 204, ((i + 1) * 50))