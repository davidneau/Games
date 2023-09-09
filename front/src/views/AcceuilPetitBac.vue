<template style="height: 100%">
    <div class="main">
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
</template>
  
  <script>
  import axios from "axios"

  export default {
    name: "AcceuilPetitBac",
    data() {
      return {
        numberOfLetter: 0,
        currentLetter: "",
        lettersRemained: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
      }
    },
    methods: {
        addline(element){
            let table = document.getElementById("mainTable")
            let line = document.createElement("tr")
            line.classList.add("line")

            let td1 = document.createElement("td")
            td1.innerText = "X"
            line.appendChild(td1)

            let td2 = document.createElement("td")
            td2.innerText = element["login"]
            line.appendChild(td2)

            let td3 = document.createElement("td")
            td3.innerText = "X"
            line.appendChild(td3)

            table.appendChild(line)
        },
        keepintouch(){
            axios.get("http://127.0.0.1:5000/getAllOnlinePlayer")
            .then((responseData) =>{
                console.log(responseData.data)
                responseData.data.forEach((element) =>{
                    this.addline(element)
                })
            })
        }
    },
    async mounted() {
      let loggedIn = localStorage.getItem("loggedIn");
      if (loggedIn == "false"){
        window.location.href = "./#/login"
      }
      this.keepintouch()
    }
  }
  </script>
  
<style scoped>

body, html{
    height: 100%;
    margin: 0;
}

body div{
    height: 100%;
}

.main{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-around;
    height: 100%;
    background-color: black;
    color: pink
}

.line{
    height: 50px;
}
</style>

<style>

.divtab{
    width: 50%;
    height: 70%;
    max-height: 90%;
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
  </style>