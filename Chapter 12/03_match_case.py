def http_status(status):

    match status:

        case 200:
            return "ok"
        
        case 400:
            return "Not found"
        
        case 600:
            return "Invalid server"
        
        case _:
            return "Unknown status"
        
print(http_status(200))
print(http_status(400))
print(http_status(600))
print(http_status(5))