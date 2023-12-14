<template id="main">
    <canvas ref="monCanvas" id="plateau">
        Désolé, votre navigateur ne prend pas en charge &lt;canvas&gt;.
    </canvas>
</template>

<script>
/* import axios from "axios" */

export default {
    name: "PlanetD",
    data: function ()  {
        return {
            selected: false,
            centerX: 0,
            centerY: 0,
            radius: window.innerWidth / 2 + 100,
            numberOfSector: 12,
            angle: 0,
            referX: 0,
        }
    },
    methods: {
        draw() {
            let canvas = this.$refs.monCanvas
            let ctx2 = canvas.getContext("2d")
            // Sauvegarde l'état initial du contexte
            ctx2.save();
            ctx2.clearRect(-window.innerWidth /2, 0, window.innerWidth, window.innerHeight);
            ctx2.rotate(this.angle)
            this.circle(ctx2);
            for (let i=0; i<this.numberOfSector; i++){
                let angle = Math.PI * i / (this.numberOfSector/2)
                this.line(this.centerX, this.centerY, this.centerX + Math.cos(angle) * this.radius, this.centerY + Math.sin(angle) * this.radius, ctx2)
            }
            // Restaure l'état initial du contexte
            ctx2.restore();
        },
        circle(ctx){
            ctx.beginPath();
            ctx.arc(this.centerX, this.centerY, this.radius, 0, 2 * Math.PI, true);
            ctx.stroke();
        },
        line(moveToX, moveToY, lineToX, lineToY, ctx){
            // Start a new Path
            ctx.beginPath();
            ctx.moveTo(moveToX, moveToY);
            ctx.lineTo(lineToX, lineToY);
            ctx.stroke();
        },
        mouseDown(event){
            console.log("down")
            this.selected = true
            this.referX = event.touches[0]["clientX"]
        },
        mouseMove(event){
            if(this.selected) {
                this.angle += (event.touches[0]["clientX"] - this.referX) / 100
                console.log(this.angle)
                this.draw()
                this.referX = event.touches[0]["clientX"]
            }
        },
        mouseUp(){
            console.log("up")
            this.selected = false
        },
        resizeCanvas(canvas) {
            console.log(window.innerWidth)
            canvas.width = window.innerWidth;
            canvas.height = window.innerWidth;
        },
/*         setBackground() {
            var background = new Image();
            background.src = require("../assets/galaxy.jpeg");

            // Make sure the image is loaded first otherwise nothing will draw.
            background.onload = function(){
                ctx.drawImage(background,0,0, canvas.width, canvas.height);   
            }
        }, */
        setSize(){
            window.onload = function(){
                window.addEventListener('load', this.resizeCanvas());
                window.addEventListener('resize', this.resizeCanvas());    
            }
        },
        init() {
            var canvas = this.$refs.monCanvas
            var ctx = canvas.getContext("2d")

            this.resizeCanvas(canvas)

            ctx.translate(window.innerWidth / 2, 0)

            canvas.addEventListener('touchstart', this.mouseDown);
            canvas.addEventListener('touchmove', this.mouseMove);
            canvas.addEventListener('touchend', this.mouseUp);

            console.log(this.centerX)
            console.log(this.centerY)
            console.log(this.radius)
            
            ctx.strokeStyle  = "white";

            this.draw(ctx)
        }
    },
    mounted() {
        this.init()
    }
}
</script>

<style>
#main{
    height: 100%;
    width: 100%;
}

#plateau{
    background-color: grey;
    aspect-ratio: 1 / 1;
}
</style>