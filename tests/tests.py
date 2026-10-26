import requests
from datetime import datetime
from bs4 import BeautifulSoup

def metas(soup, key):
    tags = []
    for attr in ("property", "name", "itemprop"):
        tags += soup.find_all("meta", attrs={attr: key})
    return [t["content"].strip() for t in tags if t.get("content")]

def original_image(url):
    i = url.rfind("https://")
    return url[i:] if i > 0 else url

def parse(url):
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(r.text, "html.parser")

    og_img = (metas(soup, "og:image") or [None])[0]
    pub = metas(soup, "datePublished")[0]
    mod = metas(soup, "dateModified")[0]

    fotos = []
    for b in soup.select('[data-block-type="backstage-photo"]'):
        img = b.find("img")
        src = img and (img.get("data-src") or img.get("src"))
        srcset = [s.get("data-srcset") or s.get("srcset")
                  for s in b.find_all("source")]
        cap = b.find("figcaption")
        fotos.append({
            "src": src,
            "srcset": [s for s in srcset if s],
            "legenda": cap.get_text(" ", strip=True) if cap else None,
        })

    return {
        "titulo": metas(soup, "og:title")[0].removesuffix(" | G1"),
        "descricao": metas(soup, "og:description")[0],
        "publicado": datetime.fromisoformat(pub),
        "atualizado": datetime.fromisoformat(mod),
        "secoes": metas(soup, "article:section"),
        "imagem": og_img,
        "imagem_original": og_img and original_image(og_img),
        "paragrafos": [
            b.get_text(" ", strip=True)
            for b in soup.select('[data-block-type="unstyled"]')
        ],
        "fotos": fotos,
    }