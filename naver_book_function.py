def extract_info(book_list): 
  result = []
  for book in book_list: 
    title = book.find("a", {"class" : "N=a:bta.title"}).string
    img_src = book.find("div", {"class" : "thumb_type thumb_type2"}).find("img")['src']
    link = book.find("a", {"class" : "N=a:bta.title"})["href"]
    author = book.find("a", {"class" : "txt_name N=a:bta.author"}).string
    publisher = book.find("a", {"class" : "N=a:bta.publisher"}).string
    if book.find("em", {"class" : "price"}) != None: 
      price = book.find("em", {"class" : "price"}).string 
    else: 
      price = "없음"
    
    
    book_info = {
      'title' : title,
      'img_src' : img_src,
      'link' : link,
      'author' : author,
      'publisher' : publisher, 
      'price' : price
    }
    result.append(book_info)
  return result