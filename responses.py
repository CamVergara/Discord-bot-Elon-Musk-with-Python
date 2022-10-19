import random



def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hallo':
        return 'Ich spreche aber kein Deutsch'

    if p_message == 'hello':
        return 'Heeey, no hellos, just buy Dogecoin!'

    if p_message == 'how are you?':
        return 'I am wondering why am i a bot. I am suppose to hate them!'

    if p_message == 'what is spacex doing?':
        return 'Creating new rockets.'
    
    if p_message == 'that it is interesting':
        return 'Yes, it is.'

    if p_message == 'tell me a number':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return "`This is a help message that you can modify.`" 

    if p_message == 'thanks elon, bye!':
        return 'Bye, hope to see you again!'





    #  return 'Yeah, I don\'t know. Try typing "!help".'