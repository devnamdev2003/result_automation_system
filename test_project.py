from project import read_text, download_image, find_src
import requests


def main():
    print("dev")
    # test_read_text()
    test_download_image()
    # test_find_src()


def test_read_text():
    url = 'https://th.bing.com/th/id/OIP.G6y1MKGfHYuvMn2rj24gpQHaF7?pid=ImgDet&rs=1'
    image_name = 'img.jpg'
    result = download_image(url, image_name)
    if result != True:
        print("Image is not downloaded")
    text = read_text(image_name)
    if "ABCDE" not in text:
        print("not present")
    if "FGHIK" not in text:
        print("not present")
    if "LMNOP" not in text:
        print("not present")
    if "QRSTV" not in text:
        print("not present")
    if "XYZ" not in text:
        print("not present")


def test_download_image():
    url = 'https://th.bing.com/th/id/OIP.G6y1MKGfHYuvMn2rj24gpQHaF7?pid=ImgDet&rs=1'
    image_name = 'img.jpg'
    result = download_image(url, image_name)
    if result != True:
        print("Image is not downloaded")


def test_find_src():
    response = requests.get('http://result.rgpv.ac.in/result/BErslt.aspx')
    link = find_src(response.text)
    url = f'http://result.rgpv.ac.in/result/{link}'
    if download_image(url, 'd.jpg') != True:
        print("Source is not find")


if __name__ == "__main__":
    main()
