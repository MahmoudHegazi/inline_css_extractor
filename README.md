# inline_css_extractor


this is simple python tool to extract the inline css from each element, and create it's own css Xpath (cssXPath) which allowed in html unlike chrome xpath which not used in css selectors, it uses nth-child to simulate xpath, and add the css code inside each selector, this tool is simple and fast, and accurate

### why use it:
some people asks How do I convert inline CSS to external CSS automatically? you can use this tool to automatic do the task

### next updates:
if element have unique id use it's id instead of cssXPath else use cssXPath

for better understanding this is reverse of this tool:
https://templates.mailchimp.com/resources/inline-css/

# important notes:
* first you need import lxml and bs4 (BeautifulSoup)
* as this tool uses BeautifulSoup you can not work with styles/elements generated by JavaScript

this function will return soup object you can get the html or use other soup methods for example ```python encode_contents() ```


#example of use:

![image](https://github.com/MahmoudHegazi/inline_css_extractor/assets/55125302/1e3affc7-5ff4-4c4f-ad65-a35581001da2)


# after using the tool
![image](https://github.com/MahmoudHegazi/inline_css_extractor/assets/55125302/ea547456-c011-4f5c-b6f7-813545ab391d)

# generated inline css example:
![image](https://github.com/MahmoudHegazi/inline_css_extractor/assets/55125302/9066a813-5d8b-4166-90b7-880c596c1d68)




##### old example of app
```python
        source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
        soup = BeautifulSoup(source, 'lxml')
        for elm in all_elms:
                if isinstance(elm, bs4.element.Tag):
                    parent = elm.parent
                    parent_xpath = []
                    nth_num = 0
                    childs = list(elm.children)
                    if len(childs) == 0:
                        elm_style = elm.get('style')
                        if elm_style:                        
                            while parent:
                                parent_xpath.append(parent.name)
                                parent = parent.parent
                            parent_xpath.reverse()
                            simple_xpath = " ".join(parent_xpath)
                            clean_css.append("%s %s {%s}"%(simple_xpath, elm.name, elm_style))
                    else:

                        while parent and parent.name != '[document]':
                            parent_xpath.append(parent.name)
                            parent = parent.parent
                        parent_xpath.reverse()
                        simple_xpath = " ".join(parent_xpath)
                        elm_style = elm.get('style')
                        if elm.get('style'):
                            clean_css.append("%s %s {%s}"%(simple_xpath, elm.name, elm_style))

                        for i in range(len(childs)):
                            child_elm = childs[i]
                            if isinstance(child_elm, bs4.element.Tag):
                                elm_style = child_elm.get('style')
                                if elm_style:
                                    clean_css.append("%s %s:nth-child(%s){%s}"%(simple_xpath, child_elm.name, i+1 , elm_style))
```


# note:
URL used in soup from tutorial:
https://pythonprogramming.net/introduction-scraping-parsing-beautiful-soup-tutorial/
