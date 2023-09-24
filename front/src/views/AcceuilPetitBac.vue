<template style="height: 100%; max-height: 100%">
    <div class="main">
      <div class="chatAndTab">
        <div class="divChat">
          <div class="chat">
          </div>
          <div class="inputChat">
            <textarea rows="5" cols="1" id="windowChat" @keyup.enter="sendMessage" ref="inputMessage"></textarea>
            <button id="Send" @click="sendMessage">Envoyer</button>
          </div>
        </div>
        <div class="divtab">
          <table border=0 cellspacing=0 class="mainTable" id="mainTable">
            <tr>
              <th style="width: 10%"></th>
              <th>Joueurs</th>
              <th style="width: 10%">Prêt</th>
            </tr>
          </table>
        </div>
      </div>
      <button class="triggerChat" @click="openChat">Chat</button>
    </div>
</template>
  
<script>
import axios from "axios"

export default {
  name: "AcceuilPetitBac",
  data() {
    return {
      evtSource: "",
      name: JSON.parse(localStorage.getItem("player"))["login"],
      messageHistory: [],
      players: [],
      noMessage: 0,
    }
  },
  methods: {
      addline(player){
          let table = document.getElementById("mainTable")
          let line = document.createElement("tr")
          line.classList.add("line")

          let td1 = document.createElement("td")
          td1.innerText = "X"
          line.appendChild(td1)

          let td2 = document.createElement("td")
          td2.innerText = player
          line.appendChild(td2)

          let td3 = document.createElement("td")
          td3.innerText = "X"
          line.appendChild(td3)

          table.appendChild(line)
      },
      keepintouch(){
          axios.get(localStorage.getItem("urlBack") + "/getAllOnlinePlayer")
          .then((responseData) =>{
              responseData.data.forEach((element) =>{
                  this.addline(element)
              })
          })
      },
      createMessage(newMessage, side, author){
        let chat = document.getElementsByClassName("chat")[0]

        let divMessage = document.createElement("div")
        
        if(side == "left"){
          divMessage.classList.add("otherMessageContainer")
        } else {
          divMessage.classList.add("messageContainer")
        }

        console.log(divMessage)
        
        let newDivMessage = document.createElement("div")
        if (side == "right"){
          newDivMessage.classList.add("messageDiv")
        }
        else {
          newDivMessage.classList.add("otherMessage")
        }
        newDivMessage.innerText = newMessage
        let name = document.createElement("p")
        name.innerText = author

        divMessage.appendChild(name)
        divMessage.appendChild(newDivMessage)

        chat.appendChild(divMessage)
        chat.scrollTop = chat.scrollHeight;

        this.noMessage += 1;
      },
      sendMessage(){
        this.createMessage(this.$refs.inputMessage.value, "right", this.name)
        this.messageHistory.push(this.$refs.inputMessage.value)

        axios.post(localStorage.getItem("urlBack") + "/sendMessage", {"message": this.noMessage + "," + this.name + "," + this.$refs.inputMessage.value})
        .then((response) => {
          console.log(response)
          this.$refs.inputMessage.value = ""
        })
      },
      openChat(){
        let chat = document.getElementsByClassName("divChat")[0]
        chat.style.display = "flex"
        if (chat.children.length == 2) {
          const barre = document.createElement("div")
          barre.classList.add("barre")

          const cross = document.createElement("button")
          cross.classList.add("cross")
          cross.innerText = "Fermer"
          cross.onclick = function(){
            chat.style.display = "none"
          }

          barre.appendChild(cross)
          chat.insertBefore(barre, chat.firstChild)
        }
      },
      checkMessage(message) {
        return message.includes("message")
      },
      stream(){
        this.evtSource = new EventSource(localStorage.getItem("urlBack") + "/streamingData");
        this.evtSource.onopen = function() {
          console.log("event source is open")
        }
        this.evtSource.onmessage = function(event) {
          if (event.data !== ""){
            console.log(event.data)
            let newMessages = event.data.split(",")
            newMessages.forEach((element) => {
              element = element.slice(1,-1)
              let genre = element.split(";")[0]
              if (genre == "message"){
                let id = parseInt(element.split(";")[1])
                let name = element.split(";")[2]
                let message = element.split(";")[3]
                if( id > this.noMessage ){
                  if (this.name == name){
                    this.createMessage(message, "right", name)
                  }
                  else {
                    this.createMessage(message, "left", name)
                  }
                  this.messageHistory.push(message)
                }
                else {
                  let namePlayer = element.split(";")[1]
                  if (!this.players.includes(namePlayer)){
                    this.addline(namePlayer)
                    this.players.push(namePlayer)
                  }
                }
              }
            })
          }
        }.bind(this)
      },
      sendOnline(){
        axios.get(localStorage.getItem("urlBack") + "/sendOnline/" + this.name)
        .then((response) => {
          console.log(response.data)
        })
      }
  },
  async mounted() {
    let loggedIn = localStorage.getItem("loggedIn");
    if (loggedIn == "false"){
      window.location.href = "./#/login"
    }
    else {
      this.sendOnline()
      this.stream()
    }
  }
}
</script>
  
<style scoped>

body, html{
    height: 100%;
    margin: 0;
}

.main{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-around;
    height: 100%;
    max-height: 100%;
    background-color: black;
    color: pink
}

.line{
    height: 50px;
}

.divtab{
  width: 50%;
  height: 100%;
  max-height: 100%;
  border: 1px solid pink;
}

.divChat{
  width: 50%;
  height: 100%;
  max-height: 100%;
  display: flex;
  flex-direction: column;
}

.chatAndTab{
  width: 70%;
  height: 90%;
  max-height: 90%;
  display: flex;
  flex-direction: row;
  border: 1px solid pink;
}

.chat{
  width: 100%;
  max-height: 600px;
  flex: 2;
  overflow-y: auto;
  border: 1px solid pink;
}

.inputChat{
  width: 100%;
  border: 1px solid pink;
  position: relative;
  flex: 1;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-around;
}

#windowChat{
  background-color: pink;
  color: black;
  width: 70%;
  height: 70%;
  border-radius: 20px;
  padding: 10px;
}

button{
  background-color: pink;
  color: black;
  border-radius: 20px;
  height: 50px;
  width: 20%;
  font-weight: bold;
}

.mainTable{
  width: 100%;
}

.line{
  height: 60px;
}

.stop{
  height: 80%;
  width: 80%;
  color: pink;
  border: 1px solid pink;
  border-radius: 10px;
}

.mainTable tr:first-child{
  height: 80px;
}

.mainTable th{
  border: 1px solid pink;
  font-size: 24px;
}

.mainTable td{
  text-align: center;
  border: 1px solid pink;
}

.mainTable td input{
  border: 1px solid pink;
  color: black;
  background-color: pink;
  width: 80%;
}

@media only screen and (max-width: 600px) {
  .divChat {
    display: none;
    position: absolute;
    width: 100%;
    left: 0;
    background-color: black;
    height: calc(100% - 80px);
  }

  .main {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
    width: 100%;
  }

  .divtab {
    width: 100%;
  }

  .chatAndTab {
    width: 100%;
  }
}
</style>

<style>

.messageContainer{
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  margin-top: 10px;
  margin-bottom: 10px;
  margin-right: 10px;
}

.otherMessageContainer{
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-top: 10px;
  margin-bottom: 10px;
  margin-left: 10px;
}

.messageDiv{
  background-color: purple;
  color: black;
  max-width: 60%;
  border-radius: 20px 0px 20px 20px;
  padding: 10px;
  word-wrap: break-word; 
}

.otherMessage{
  background-color: palevioletred;
  color: black;
  max-width: 60%;
  border-radius: 0px 20px 20px 20px;
  padding: 10px;
}


.barre{
  border: 1px solid pink;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}

.cross{
  color: pink
}

</style>