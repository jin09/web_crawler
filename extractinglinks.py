import requests


def get_page(web_url):
    try:
        response = requests.get(web_url)
        return response.content
    except:
        print "NOT A VALID URL"


def get_url_and_pos_of_ending_quote(page):
    start_link = page.find('<a href=')
    if (start_link == -1):
        return 0, None
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


def print_all_links(webcode):
    while (1):
        url, endpos = get_url_and_pos_of_ending_quote(webcode)
        if url:
            print url
        else:
            break
        webcode = webcode[endpos + 1:]


def get_links_in_list(web_code):
    l = []
    if web_code==None:
        return l
    while (1):
        url, endpos = get_url_and_pos_of_ending_quote(web_code)
        if url:
            l.append(url)
        else:
            return l
        web_code = web_code[endpos + 1:]


def print_the_list(lis):
    for i in lis:
        print i


def return_list_of_crawled_pages(to_be_crawled):
    crawled = []
    done = []
    while to_be_crawled:

        s = to_be_crawled.pop(0)
        if(not (s in done)):
            l = get_links_in_list(get_page(s))
            crawled = crawled + l
            to_be_crawled = to_be_crawled + l

        done.append(s)

    return crawled


seed_page = input("Enter the URL that you want to crawl : ")
to_be_crawld = []
to_be_crawld.append(seed_page)
crawld = return_list_of_crawled_pages(to_be_crawld)
print_the_list(crawld)
#l = get_links_in_list(get_page('http://xkcd.com/353'))
#print_the_list(l)
# print_all_links(get_page('http://xkcd.com/353'))
