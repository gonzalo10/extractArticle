from sanic import Sanic
from sanic import response
import json
from newspaper import Article

app = Sanic(__name__)


@app.route('/', methods=['GET', 'POST'])
def handle_request(request):

    url = request.json.get("url")
    article = Article(url)
    article.download()
    article.parse()

    return response.json([{
        'text': article.text,
        "meta_description": article.meta_description,
        "meta_favicon": article.meta_favicon,
        "meta_img": article.meta_img,
        "meta_lang": article.meta_lang,
        "title": article.title,
        "top_image": article.top_image
    }], status=200)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8006)
