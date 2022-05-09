# 1
# import requests
# import json
# import sqlite3
# url = "https://wallhaven.cc/api/v1/search"
# key = "TyGuzQ0QcwIluIoD1mUhi2bCEyIpNUtu"
# payload = {"apikey": key, "sorting": "favorites", "purity": "100", "q": "eyes"}
# r = requests.get(url, params=payload)
# # print(r.headers)
# # print(r.status_code)
# # print(r.text)
# # res = r.json()
# #
# #
# # with open("wallpapers.json", "w") as file:
# #     json.dump(res, file, indent=4)
#
# with open("wallpapers.json", "r") as file:
#     res = json.load(file)
#
# wallpapers_numb = res["data"]
#
# for i in range(1, len(wallpapers_numb)):
#     views = res["data"][i]["views"]
#     favorites = res["data"][i]["favorites"]
#     category = res["data"][i]["category"]
#     image_url = res["data"][i]["url"]
#     # print(f"views: {views}\nfavorites:{favorites}\ncategory: {category}\nurl: {image_url}\n")
#
#
# # ქვემოთ მოყვანილი ცხრილი ინახავს არსებული wallpaper-ების id-ს url კოდს, ნახვების რაოდენობას, რამდენის საყვარელი სურათია, კატეგორიასა და გვერდზე დადების თარიღსა და დროს
#
# # conn = sqlite3.connect("wallpapers.sqlite")
# # cursor = conn.cursor()
# # cursor.execute('''CREATE TABLE wallpapers
# #                 (id VARCHAR(10),
# #                 url VARCHAR(100),
# #                 views INTEGER,
# #                 favorites INTEGER,
# #                 category VARCHAR(10),
# #                 create_date DATETIME);''')
#
# # wallpapers_list = []
# # for i in range(1, len(wallpapers_numb)):
# #     wallpapers_list_info = []
# #     wall_item = res["data"][i]
# #     wallpapers_list_info.extend([wall_item["id"], wall_item["url"], wall_item["views"], wall_item["favorites"], wall_item["category"], wall_item["created_at"]])
# #     wallpapers_list.append(wallpapers_list_info)
# # print(wallpapers_list)
# #
# # cursor.executemany('''INSERT INTO wallpapers (id, url, views, favorites, category, create_date) values (?, ?, ?, ?, ?, ?)''', wallpapers_list)
# # conn.commit()





