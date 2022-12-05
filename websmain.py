from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content= html_file.read()
    soup=BeautifulSoup(content, 'lxml')
    s_tags= soup.find_all('div', class_='des')
    for s_tag in s_tags:
        p_tag= s_tag.p.text
        st_tag= s_tag.strong.text
        print(p_tag)
        print(st_tag)        
    
    