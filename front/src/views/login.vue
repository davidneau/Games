<template>
    <div class="maindiv">
        <h1>Se connecter</h1>
        <div class="field">
            <p>Identifiant</p>
            <input id="identifiant" type="text" value="admin">
        </div>
        <div class="field">
            <p>Mot de passe</p>
            <input id="password" type="password" value="blabla">
        </div>
        <div class="ErrorMessage"></div>
        <div class="divConnected">
            <a href="./#/registration">s'enregistrer</a>
            <button class="login" @click="login">Se connecter</button>
            <button class="loginfb" @click="dialogfb = true">Se connecter <br>avec facebook</button>
        </div>
    </div>
    <div class="connectfb" v-if="dialogfb">
        <div class="banner"><span>Facebook</span> <span @click="dialogfb = false;" style="position: absolute; right: 10px; cursor: pointer;">&#10060;</span></div>
        <div class="fieldfb">
            <p>Identifiant</p>
            <input id="identifiantfb" type="text">
        </div>
        <div class="fieldfb">
            <p>Mot de passe</p>
            <input id="passwordfb" type="password">
        </div>
        <button class="loginfb" style="margin-bottom:20px" @click="loginfb">Se connecter</button>
    </div>
</template>

<script>
import axios from 'axios';

/* import axios from "axios" */

export default {
    name:"loginView",
    data() {
      return {
            dialogfb: false
        }
    },
    methods: {
        login(){
            let user = {
                "login": document.getElementById("identifiant").value,
                "password": document.getElementById("password").value,
            }
            axios.post(localStorage.getItem("urlBack") + "/login", user)
            .then((data) => {
                console.log(data)
                localStorage.setItem("loggedIn", "true")
                if(data.data !== "False"){
                    localStorage.setItem("player", JSON.stringify(user))
                    window.location.href = "/"
                }
                else {
                    document.getElementsByClassName("ErrorMessage")[0].innerText = "Mauvais identifiant ou mauvais mot de passe"
                }
            })
        },
        loginfb(){
            let user = {
                "login": document.getElementById("identifiantfb").value,
                "password": document.getElementById("passwordfb").value,
            }
            axios.post(localStorage.getItem("urlBack") + "/login", user)
            .then((data) => {
                localStorage.setItem("loggedIn", "true")
                if(data.data == "True"){
                    window.location.href = "/"
                }
                else {
                    document.getElementsByClassName("ErrorMessage")[0].innerText = "Mauvais identifiant ou mauvais mot de passe"
                }
            })
        }
    },
    mounted(){
        localStorage.setItem("loggedIn", false)
        let hasReloaded = localStorage.getItem('hasReloaded')
        console.log(hasReloaded)
        if (hasReloaded == "false"){
            localStorage.setItem('hasReloaded', true)
            location.reload()
        }
        else {
            localStorage.setItem('hasReloaded', false)}
        }
}
</script>


<style scoped>

body, html{
    margin: 0;
}

input{
    background-color: white;
}

.ErrorMessage{
    color:red;
    font-size: 20px;
}

.maindiv{
    width: 30%;
    height: 60%;
    border-radius: 10px;
    background: pink;
    position: absolute;
    top: 20%;
    left: 35%;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
}

.field{
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
    width: 60%;
}

.field p{
    font-size: 20px;
    font-weight: bold;
    width: 50%;
}

.field input{
    border: 1px solid black;
    font-size: 20px;
    font-weight: bold;
    width: 70%;
    padding-left: 5px;
    background-color: white;
}

.divConnected{
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
    width: 100%;
}

.login{
    background-color: hotpink;
    border-radius: 10px;
    width: 200px;
    height: 70px;
    font-size: 20px;
    font-weight: bold;
    border: 1px solid black;
}

.loginfb{
    background-color: #3b5998;
    height: 50px;
    font-size: 14px;
    border: 1px solid black;
    color: white;
    width: 120px
}

.banner{
    background-color: #3b5998;
    color: white;
    text-align: center;
    width: 100%;
    font-size: 30px;
}

.connectfb{
    background-color: white;
    width: 20%;
    height: 60%;
    position: absolute;
    top: 20%;
    left: 40%;
    z-index: 5;
    border: 1px solid black;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
}

.fieldfb{
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
    width: 80%;
}

.fieldfb p{
    font-size: 20px;
    font-weight: bold;
    width: 50%;
}

.fieldfb input{
    border: 1px solid black;
    font-size: 20px;
    font-weight: bold;
    width: 50%;
}

@media only screen and (max-width: 600px) {
  .maindiv {
    width: 90%;
    left: 5%;
  }
}


</style>