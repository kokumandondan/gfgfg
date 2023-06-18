import os

def generate_sitemap(html_files, sitemap_name):
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for i, file in enumerate(html_files):
        sitemap += f'\t<url>\n\t\t<loc>http://cem.com/{file}</loc>\n\t</url>\n'
        if (i + 1) % 300 == 0 or (i + 1) == len(html_files):
            sitemap += '</urlset>'
            with open(f'{sitemap_name}_{i // 14000 + 1}.xml', 'w') as f:
                f.write(sitemap)
            sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
            sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

# Klasördeki HTML dosyalarını listeleme
folder_path = 'C:\\Users\\cem\\Documents\\GitHub\\gfgfg'  # Klasör yolunu buraya girin
html_files = [file for file in os.listdir(folder_path) if file.endswith('.html')]

# Sitemap dosyası oluşturma
generate_sitemap(html_files, 'cem_sitemap')