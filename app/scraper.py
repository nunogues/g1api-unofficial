
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pydantic import TypeAdapter, ValidationError, HttpUrl

from app.schemas import News


START_URL = "https://g1.globo.com/"
USER_AGENT = "G1API/0.1"

http_url_adapter = TypeAdapter(HttpUrl)


def get_meta(soup, *, name=None, prop=None, itemprop=None):
    if name:
        attrs = {"name": name}
    elif prop:
        attrs = {"property": prop}
    elif itemprop:
        attrs = {"itemprop": itemprop}
    else:
        return None

    tag = soup.find("meta", attrs=attrs)

    if not tag:
        return None

    return tag.get("content")


def clean_image_url(value, base_url):
    if not isinstance(value, str):
        return None

    value = value.strip()

    if value.lower() in {"", "none", "null", "undefined"}:
        return None

    value = urljoin(base_url, value)

    try:
        http_url_adapter.validate_python(value)
    except ValidationError:
        return None

    return value


def scrape_news(url: str) -> News | None:
    response = requests.get(
        url,
        timeout=10,
        headers={"User-Agent": USER_AGENT},
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    title = get_meta(soup, prop="og:title")
    article_url = get_meta(soup, prop="og:url") or url

    image_url = clean_image_url(
        get_meta(soup, prop="og:image"),
        url,
    )

    summary = (
        get_meta(soup, prop="og:description")
        or get_meta(soup, name="description")
    )

    published_at = get_meta(
        soup,
        itemprop="datePublished",
    )

    updated_at = get_meta(
        soup,
        itemprop="dateModified",
    )

    if not title:
        return None

    return News(
        title=title,
        url=article_url,
        image_url=image_url,
        summary=summary,
        published_at=published_at,
        updated_at=updated_at,
    )


def get_news(limit=5):
    if limit < 1:
        return []

    response = requests.get(
        START_URL,
        timeout=10,
        headers={"User-Agent": USER_AGENT},
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.select("a.feed-post-link")

    news = []
    seen_urls = set()

    for link in links:
        href = link.get("href")

        if not href:
            continue

        url = urljoin(START_URL, href)

        if url in seen_urls:
            continue

        seen_urls.add(url)

        try:
            article = scrape_news(url)

            if article:
                news.append(article)

        except (
            requests.RequestException,
            ValidationError,
            ValueError,
        ) as error:
            print(f"Erro ao extrair {url}: {error}")

        if len(news) >= limit:
            break

    return news
