import requests
from google import genai

client = genai.Client(api_key='Minha_API')
print('Bem vindo ao resumidor de sites!')

escolha = 'S'

while escolha == 'S':

    url = input('Informe a URL do site: ')
    web = requests.get(url)

    print('\nResposta carregando...')
    
    chat = client.chats.create(model="gemini-2.5-flash")
    response = chat.send_message(f'Resuma brevemente o código HTML: {web.text}, ignore os elementos visuais e só fale sobre o conteúdo escrito do site')
    print('\n',response.text)

    escolha = input('\nDeseja continuar? (S) para sim e (N) para não: ')
    escolha = escolha.upper()

    if escolha == 'S':
         continue
    elif escolha == 'N':
        print('Programa encerrando...')
        break
    else:
        while escolha != 'S' and escolha != 'N':
            escolha = input('\nEscolha invalida, tente novamente\nDeseja continuar? (S) para sim e (N) para não:')
            escolha = escolha.upper()
            if escolha == 'N':
                 print('Programa encerrando...')
