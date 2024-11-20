from flask import Flask
from query import get_pages



app = Flask(__name__)

@app.route("/")
def hello():
    
    titles = []
    pages = get_pages()
    for page in pages:
        page_id = page["id"]
        props = page["properties"]
        url = page["url"]
        title = props["Name"]["title"][0]["text"]["content"]
        #published = props["Published"]["date"]["start"]
        #published = datetime.fromisoformat(published)
        if "Name" in props and "title" in props["Name"] and props["Name"]["title"]:
            title = props["Name"]["title"][0]["text"]["content"]
            titles.append(title)
    if titles:
        return ", ".join(titles)
    else:
        return "No titles found"
    


    

##app.run(host="0.0.0.0", port=3000, debug=True)