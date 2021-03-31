def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    beginIndex = (text.find(begin)+len(begin)) if text.find(begin) !=-1 else 0
    
    endIndex = text.find(end) if text.find(end) else len(text)
    print(beginIndex,endIndex)
  
    if beginIndex < endIndex: 
        return text[beginIndex:endIndex]
    return ''


print(between_markers("No [b]hi","[b]","[/b]"))


#! string.find() 找不到会返回-1  这里的-1 并不 = False