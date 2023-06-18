
import csv

kodcuk = open("kod.txt", 'r', encoding="utf8")    # Satır verilerini al
kod = (kodcuk.read())

def create_html_file(row):
    # HTML şablonunu oluştur
    template = """
<html>
<head>
{kod}
<title>{title}</title>
</script>
</head>
<body>
<h1>{heading}</h1>
<p>{content}</p>
</body>
</html>
    """


    title = row[0]  # İlk sütun
    heading = row[1]  # İkinci sütun
    content = row[2]  # Üçüncü sütun


    # HTML dosyasını oluştur
    html_content = template.format(kod=kod, title=title, heading=heading, content=content)

    # HTML dosyasını kaydet
    filename = f"{title}.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)

# CSV dosyasını aç ve her satır için HTML dosyası oluştur
with open('data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # İlk satırı atla (başlık satırı)
    for row in reader:
        create_html_file(row)


C:\\Users\\cem\\Documents\\GitHub\\gfgfg