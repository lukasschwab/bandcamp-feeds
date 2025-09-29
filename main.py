import jsonfeed_wrapper as jfw
import jsonfeed as jf
from bs4 import BeautifulSoup as bs

BASE_URL_FORMAT = "https://{category}.bandcamp.com/music"
MAX_ITEMS = 20

def to_item(page_item, request_url):
    relative_path = page_item.a["href"]
    return jf.Item(
        id=relative_path,
        url=request_url+relative_path,
        title=page_item.p.text.strip(),
        image=page_item.img["src"],
        content_html=page_item.a.prettify(),
    )

def page_to_items(page):
    soup = bs(page.text, 'html.parser')
    page_items = soup.findAll("li", class_="music-grid-item")
    return [to_item(page_item, page.url) for page_item in page_items[:MAX_ITEMS]]

wrapper = jfw.JSONFeedWrapper("Bandcamp", BASE_URL_FORMAT, page_to_items, MAX_ITEMS)

# App for App Engine deployments.
app = wrapper.as_bottle_app()
# Target for Cloud Function deployments.
target = wrapper.as_cloud_function()
