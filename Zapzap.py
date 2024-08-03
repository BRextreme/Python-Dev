#Titulo
#Botao Chat
    #Abre um pop-up
    #Abre um campo de texto
    #Botao para entrar no chat
        #Sumir com o titulo e o botao inicial
        #Fechar o pop-up
        #Criar o chat
        #Embaixo do chat
            #Campo de texto e botao enviar  
            #Vai aparecer a mensagem com onome de usuario

#importar flet
import flet as ft

#criar a função pricipal do sistema
def main(pagina):
    #criar
    titulo = ft.Text("Python zap")

    def mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))
        pagina.update()

    pagina.pubsub.subscribe(mensagem_tunel)#cria o tunel
    
    def entrar_chat(evento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        popup.open = False
        pagina.add(chat)
        pagina.add(linha_msn)
        entrou_chat = f"{campo_nome.value} entrou no chat"
        pagina.pubsub.send_all(entrou_chat)
        pagina.update()

    titulo_popup = ft.Text("Bem vindo")
    campo_nome = ft.TextField(label="Nome de usuário", on_submit=entrar_chat)
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)


    def enviar_mensagem(evento):
        texto = f"{campo_nome.value}: {texto_msn.value}"
        #enviar a mensagem no chat

        #enviar mensagem no tunel
        pagina.pubsub.send_all(texto)

        #limpar o campo de mensagem
        texto_msn.value = ""
        pagina.update()
    
    texto_msn = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar= ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_msn =ft.Row([texto_msn, botao_enviar])
    chat = ft.Column()

    popup = ft.AlertDialog(
        title=titulo_popup,
        content=campo_nome,
        actions=[botao_entrar])
        

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.IconButton("Chat", on_click=abrir_popup)

    #colocar
    pagina.add(titulo)
    pagina.add(botao_iniciar)



#executar o seu sistema
ft.app(main, view=ft.WEB_BROWSER) # type: ignore
