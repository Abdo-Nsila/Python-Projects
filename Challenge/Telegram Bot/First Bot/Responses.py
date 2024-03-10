from datetime import datetime

def sample_response(input_text):
    message = str(input_text).lower()

    if(message in ('hello','hi')):
        return('hello user')
    
    if(message == ('time','time?')):
        now = datetime.now('')
        date_time = now.strftime('%d/%m/%Y, %H:%M:%S')
        return str(datetime)
    
    return "I don't understand you?"
