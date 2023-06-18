import os

def create_sitemap(folder_path, website_url, max_links_per_sitemap):
    # Dosya listesini alın
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".html"):
                file_list.append(os.path.join(root, file))

    # Sitemap dosyalarını oluşturun
    sitemap_count = 1
    link_count = 0
    for file_path in file_list:
        if link_count % max_links_per_sitemap == 0:
            sitemap_file = f"sitemap{sitemap_count}.xml"
            if sitemap_count > 1:
                # İlk sitemap dosyasının sonunu kapatın
                with open(sitemap_file_path, "a") as sitemap:
                    sitemap.write("</urlset>")

            sitemap_file_path = os.path.join(folder_path, sitemap_file)
            with open(sitemap_file_path, "w") as sitemap:
                sitemap.write('<?xml version="1.0" encoding="UTF-8"?>\n')
                sitemap.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

            sitemap_count += 1

        # URL'yi sitemap dosyasına ekle
        with open(sitemap_file_path, "a") as sitemap:
            sitemap.write(f'\t<url>\n\t\t<loc>{website_url}/{file_path}</loc>\n\t\t<lastmod></lastmod>\n\t\t<changefreq></changefreq>\n\t\t<priority>1.0</priority>\n\t</url>\n')

        link_count += 1

    # Son sitemap dosyasının sonunu kapatın
    with open(sitemap_file_path, "a") as sitemap:
        sitemap.write("</urlset>")

# Örnek kullanım
folder_path = "C:\\Users\\cem\\Documents\\GitHub\\gfgfg"  # Klasör yolunu buraya girin
website_url = "https://avseetv2023.netlify.app"  # Web sitesi URL'sini buraya girin
max_links_per_sitemap = 300  # Her sitemap dosyasındaki maksimum link sayısı

create_sitemap(folder_path, website_url, max_links_per_sitemap)
