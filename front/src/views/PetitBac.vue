<template style="height: 100%">
    <div class="main">
      <div class="leftside">
        <button v-on:click = "init">Start</button>
      </div>
      <div class="divtab">
        <table border=0 cellspacing=0 class="mainTable" id="mainTable">
          <tr>
            <th style="width: 5%">Lettre</th>
            <th style="width: 15%">Prénom Fille</th>
            <th style="width: 15%">Prénom Garçon</th>
            <th style="width: 15%">Pays/Villes</th>
            <th style="width: 15%">Métiers</th>
            <th style="width: 15%">Fruits/Légumes</th>
            <th style="width: 15%">Célébrités</th>
            <th style="width: 5%">Points</th>
          </tr>
        </table>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios"

  export default {
    name: "PetitBac",
    data() {
      return {
        numberOfLetter: 0,
        currentLetter: "",
        lettersRemained: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
      }
    },
    methods: {
      init(){
        if (this.lettersRemained.length !== 0){
          this.addLine()
        }
      },
      generateRandomLetter(){
        console.log(this.lettersRemained)
        let newLetter = this.lettersRemained.charAt(Math.floor(Math.random() * this.lettersRemained.length));
        this.lettersRemained = this.lettersRemained.replace(newLetter, '');
        this.currentLetter = newLetter
        document.getElementById("Lettre" + this.numberOfLetter).children[0].innerText = newLetter
      },
      check(){
        let answer = {}
        let nol = this.numberOfLetter
        answer["Garcon"] = document.getElementById("Garcon" + nol).children[0].value
        answer["Fille"] = document.getElementById("Fille" + nol).children[0].value
        answer["PaysVilles"] = document.getElementById("PaysVilles" + nol).children[0].value
        answer["Metiers"] = document.getElementById("Metiers" + nol).children[0].value
        answer["FruitsLegumes"] = document.getElementById("FruitsLegumes" + nol).children[0].value
        answer["Celebrities"] = document.getElementById("Celebrities" + nol).children[0].value
        console.log(answer)
        axios.post("http://85.31.238.211:5000/sendAnswer", answer)
        .then((data) => {
          console.log(data)
          Object.keys(data.data).forEach(element => {
            console.log(element);
            document.getElementById(element + nol).style.backgroundColor = (data.data[element] ? "green" : "red");
          })
        })
      },
      addCell(type, parent, id, ext){
        const Cell = document.createElement(type)
        Cell.id = id
        if (!ext){
          const input = document.createElement("input")
          input.type="text"
          input.value=this.currentLetter
          Cell.appendChild(input)
        }
        else {
          const p = document.createElement("p")
          Cell.appendChild(p)
          if (id=="Points" + this.numberOfLetter){
            const button = document.createElement("button")
            button.classList.add("stop")
            button.innerText="STOP"
            button.onclick = this.check
            Cell.appendChild(button)
          }
        }
        parent.appendChild(Cell)
      },
      addLine(){
        this.numberOfLetter += 1
        console.log(this.numberOfLetter)
        const line = document.createElement("tr")
        line.classList.add("line")
        this.addCell("td", line, "Lettre" + this.numberOfLetter, true)
        document.getElementById("mainTable").appendChild(line)
        this.generateRandomLetter()
        this.addCell("td", line, "Fille" + this.numberOfLetter, false)
        this.addCell("td", line, "Garcon" + this.numberOfLetter, false)
        this.addCell("td", line, "PaysVilles" + this.numberOfLetter, false)
        this.addCell("td", line, "Metiers" + this.numberOfLetter, false)
        this.addCell("td", line, "FruitsLegumes" + this.numberOfLetter, false)
        this.addCell("td", line, "Celebrities" + this.numberOfLetter, false)
        this.addCell("td", line, "Points" + this.numberOfLetter, true)
      }
    },
    async mounted() {
      let loggedIn = localStorage.getItem("loggedIn");
      if (loggedIn == "false"){
        window.location.href = "./#/login"
      }
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
  
  .leftside{
    display: flex;
    flex-direction: row;
    align-items: center;
  }

  .leftside button{
    border: 1px solid pink;
    width: 100px;
    height: 50px;
    font-size: 20px;
    border-radius: 10px;
  }
  </style>
  
  <style>

.divtab{
    width: 80%;
    height: 90%;
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