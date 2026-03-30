let currentSession = null

async function createChat(){

    const res = await fetch("/new_chat")

    
    let data

    try{
        data = await res.json()
    }catch(e){
    console.log("Server returned HTML error")
    return
    }
    currentSession = data.session_id

    document.getElementById("chat-box").innerHTML=""

    loadChats()

}

async function sendMessage(){

    const input = document.getElementById("user-input")

    const message = input.value.trim()

    if(!message) return

    input.value=""

    addMessage("user",message)

    const res = await fetch("/chat",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            message:message,
            session_id:currentSession
        })
    })

    const data = await res.json()

    addMessage("bot",data.reply)

}

function addMessage(role,text){

    const chatBox = document.getElementById("chat-box")

    const div = document.createElement("div")

    div.className=role

    div.innerHTML = marked.parse(text)

    chatBox.appendChild(div)

    chatBox.scrollTop = chatBox.scrollHeight

}

async function loadChats(){

    const res = await fetch("/chats")

    const chats = await res.json()

    const list = document.getElementById("chat-list")

    list.innerHTML=""

    chats.forEach(chat=>{

        const div = document.createElement("div")

        div.className="chat-item"

        div.innerText=chat.title

        div.onclick=()=>loadChat(chat._id)

        list.appendChild(div)

    })

}

async function loadChat(id){

    currentSession=id

    const res = await fetch("/chat/"+id)

    const messages = await res.json()

    const box=document.getElementById("chat-box")

    box.innerHTML=""

    messages.forEach(msg=>{
        addMessage(msg.role,msg.message)
    })

}

window.onload=loadChats
