import bs4
def get_elm_index(elm):
    previouses = 1
    previous_siblings = elm.find_previous_siblings()
    for elm in previous_siblings:
        if isinstance(elm, bs4.element.Tag):
            previouses += 1
    return previouses

def inline_css_extractor(soup):
    clean_css = []
    types = []
    all_elms = soup.find_all(True, recursive=True)
    internal_css = ''
    for elm in all_elms:
            if isinstance(elm, bs4.element.Tag):
                #previous
                parent = elm.parent
                parent_xpath = []
                nth_num = 0

                prevs = 0
                next = 0

                elm_style = elm.get('style')
                if elm_style:
                    del elm['style']
                    while parent and parent.name != '[document]':
                        parent_xpath.append("{}:nth-child({})".format(parent.name, get_elm_index(parent)))
                        parent = parent.parent
                    parent_xpath.reverse()
                    simple_xpath = " ".join(parent_xpath)
                    nth_index = get_elm_index(elm)

                    css_block = """%s %s:nth-child(%s) {\n    %s\n}"""%(simple_xpath, elm.name, nth_index, elm_style)
                    if css_block not in clean_css:
                        clean_css.append(css_block)
                    internal_css = """<style>\n{}\n</style>
                    """.format("\n".join(clean_css))
    
    internal_css = BeautifulSoup(internal_css, 'lxml')
    soup.head.append(internal_css)
    # you can instead of return create new file with the css and the body data without the styles attribute 
    return str(soup)
