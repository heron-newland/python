import haul

url = 'http://q1.fkncjdbd.info/pw/html_data/15/1905'
result = haul.find_images(url)

print(result.image_urls)
