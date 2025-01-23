import webbrowser as wb

def webauto():
    edge_path='"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" %s'
    URLS=(  #Can replace with your workspace URLS
       " github.com",
        "youtube.com",
        "chatgpt.com",
        "geekforgeeks.org"
    )

    for url in URLS:
        print("Opening:",url)
        wb.get(edge_path).open(url)

webauto()        
