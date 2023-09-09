<template>
    <div class="maindiv">
        <h1>S'enregistrer</h1>
        <div class="field">
            <p>Identifiant</p>
            <input id="identifiant" type="text" value="admin">
        </div>
        <div class="field">
            <p>Mot de passe</p>
            <input id="password" type="password" value="blabla">
        </div>
        <div class="field">
            <p>Email</p>
            <input id="email" type="text" value="davidneau49@gmail.com">
        </div>
        <button class="subscribe" @click="subscribe">S'enregistrer</button>
    </div>
</template>


<script>
import axios from 'axios';

export default {
    name:"registrationView",
    methods: {
        subscribe(){
            let user = {
                "login": document.getElementById("identifiant").value,
                "password": document.getElementById("password").value,
                "email": document.getElementById("email").value,
            }
            axios.post('http://127.0.0.1:5000/registration', user)
            .then((data) => {
                console.log(data)
                window.location.href = "./#/login"
            })
            .catch((err) => {
                console.log(err)
            });
        }
    }
}
</script>

<style scoped>

body, html{
    margin: 0;
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
    width: 90%;
}

.field p{
    font-size: 20px;
    font-weight: bold;
    width: 30%;
}

.field input{
    border: 1px solid black;
    font-size: 20px;
    font-weight: bold;
    width: 70%;
    padding-left: 5px;
    background-color: white;
}

.subscribe{
    background-color: hotpink;
    border-radius: 10px;
    width: 200px;
    height: 70px;
    font-size: 20px;
    font-weight: bold;
    border: 1px solid black;
}

</style>