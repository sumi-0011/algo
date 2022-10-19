def solution(phone_book):
    phone_book.sort()
    
    if len(phone_book) ==1 : return True
    for idx in range(0,len(phone_book)-1):
        prev = phone_book[idx]
        last = phone_book[idx + 1]
        if(last[0:len(prev)] == prev):
            return False   
        
    return True