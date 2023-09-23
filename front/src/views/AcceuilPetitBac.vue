<template style="height: 100%; max-height: 100%">
    <div class="main">
      <div class="chatAndTab">
        <div class="divChat">
          <div class="chat">
          </div>
          <div class="inputChat">
            <textarea rows="5" cols="1" id="windowChat" @keyup.enter="sendMessage" ref="inputMessage"></textarea>
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
        players: []
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
          
          let newDivMessage = document.createElement("div")
          if (side == "right"){
            newDivMessage.classList.add("message")
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
        },
        sendMessage(){
          this.createMessage(this.$refs.inputMessage.value, "right", this.name)
          this.messageHistory.push(this.$refs.inputMessage.value)

          axios.post(localStorage.getItem("urlBack") + "/sendMessage", {"message": this.name + "," + this.$refs.inputMessage.value})
          .then((response) => {
            console.log(response)
            this.$refs.inputMessage.value = ""
          })
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
            console.log(event.data)
            if (event.data !== ""){
              let newMessages = event.data.split(",")
              console.log(newMessages)
              console.log(this.messageHistory)
              if (newMessages.filter(this.checkMessage).length !== this.messageHistory.length){
                let noNewMessage = newMessages.length - this.messageHistory.length
                newMessages.slice(-noNewMessage).forEach((element) => {
                  element = element.substring(1, element.length - 1)
                  console.log(element)
                  if(element.split(";")[0] == "message"){
                    if (this.name == element.split(";")[1]){
                      this.createMessage(element.split(";")[2], "right", element.split(";")[1])
                    }
                    else {
                      this.createMessage(element.split(";")[2], "left", element.split(";")[1])
                    }
                    this.messageHistory.push(element.split(";")[1])
                  }
                  else {
                    let namePlayer = element.split(";")[1]
                    if (!this.players.includes(namePlayer)){
                      this.addline(namePlayer)
                      this.players.push(namePlayer)
                    }
                  }
                })
              }
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
</style>

<style scopped>

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
}

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

.message{
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

#windowChat{
  background-color: pink;
  color: black;
  width: 80%;
  height: 80%;
  position: absolute;
  top: 10%;
  left: 10%;
  border-radius: 20px;
  padding: 10px;
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
    /* display: none; */
    position: absolute;
    width: 96%;
    left: 2%;
    background-color: black;
    height: calc(95% - 64px);
  }

  .main {
    justify-content: none;
  }

  .divtab {
    width: 100%;
  }

  .chatAndTab {
    width: 100%;
  }
}
</style>