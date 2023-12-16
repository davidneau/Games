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
            referAngleText: {
                "1": -3,
                "2": -2,
                "3": -1,
                "4": 0,
                "5": 1,
                "6": 2,
                "7": 3,
                "8": 4,
                "9": 5,
                "10": 6,
                "11": -5,
                "12": -4
            },
            element: ["comet", "asteroid", "nuageDeGaz", "planeteNaine", "vide", "planeteD"]
        }
    },
    methods: {
        line(moveToX, moveToY, lineToX, lineToY, ctx){
            // Start a new Path
            ctx.beginPath();
            ctx.moveTo(moveToX, moveToY);
            ctx.lineTo(lineToX, lineToY);
            ctx.stroke();
        },
        drawElement(centerX, centerY, element){
            let canvas = this.$refs.monCanvas
            let ctx = canvas.getContext("2d")
            if(element == "comet"){
                console.log("comet")
            }
            if(element == "asteroid"){
                console.log("asteroid")
            }
            if(element == "nuageDeGaz"){
                console.log("nuageDeGaz")
            }
            if(element == "planeteNaine"){
                console.log(ctx)
                this.line(centerX + Math.cos(Math.PI * 3/4) * 10, centerY + Math.sin(Math.PI * 3/4) * 10, centerX + Math.cos(Math.PI * 3/4) * 10 + 8, centerY + Math.sin(Math.PI * 3/4) *10, ctx)
                this.line(centerX-10, centerY, centerX, centerY, ctx)
                this.line(centerX + Math.cos(Math.PI * -3/4) * 10, centerY + Math.sin(Math.PI * -3/4) * 10, centerX + Math.cos(Math.PI * -3/4) * 10 + 5, centerY + Math.sin(Math.PI * -3/4) * 10, ctx)
                ctx.arc(centerX, centerY, 10, 0, 2 * Math.PI, true)
            }
            if(element == "vide"){
                ctx.beginPath();
                this.line(centerX-10, centerY+2, centerX-10, centerY+10, ctx)
                this.line(centerX-10, centerY+10, centerX-2, centerY+10, ctx)

                this.line(centerX+2, centerY+10, centerX+10, centerY+10, ctx)
                this.line(centerX+10, centerY+10, centerX+10, centerY+2, ctx)

                this.line(centerX+10, centerY-2, centerX+10, centerY-10, ctx)
                this.line(centerX+10, centerY-10, centerX+2, centerY-10, ctx)

                this.line(centerX-2, centerY-10, centerX-10, centerY-10, ctx)
                this.line(centerX-10, centerY-10, centerX-10, centerY-2, ctx)
            }
            if(element == "planeteD"){
                for(let i=0; i<4; i++){
                    let angle = Math.PI/4 + i * Math.PI/2
                    ctx.beginPath();
                    this.line(centerX, centerY, centerX + Math.cos(angle) * 8, centerY + Math.sin(angle) * 8, ctx)
                }
                ctx.beginPath();
                ctx.arc(centerX, centerY, 10, 0, 2 * Math.PI, true)
            }
        },
        drawElements(angle) {
            let canvas = this.$refs.monCanvas
            let ctx = canvas.getContext("2d")
            for (let i=0; i<6; i++){
                ctx.beginPath();
                this.drawElement(this.centerX + Math.cos(angle) * (this.radius*i/6), this.centerY + Math.sin(angle) * (this.radius*i/6), this.element[i]);
                ctx.stroke();
            }
        },
        draw() {
            let canvas = this.$refs.monCanvas
            let ctx2 = canvas.getContext("2d")
            // Sauvegarde l'état initial du contexte
            ctx2.save();
            ctx2.clearRect(-window.innerWidth /2, 0, window.innerWidth, window.innerHeight);
            ctx2.rotate(this.angle)
            this.circle(ctx2, this.radius);
            this.circle(ctx2, this.radius + 30);
            for (let i=0; i<this.numberOfSector; i++){
                let angle = Math.PI * i / (this.numberOfSector/2)
                this.line(this.centerX, this.centerY, this.centerX + Math.cos(angle) * this.radius, this.centerY + Math.sin(angle) * this.radius, ctx2)
                let angleText = angle + (Math.PI / (this.numberOfSector/2)) / 2
                let angleTextSelf = (this.referAngleText[i+1] + 0.5) * (Math.PI / (this.numberOfSector/2))
                ctx2.translate((this.centerX + Math.cos(angleText) * (this.radius + 70)), this.centerY + Math.sin(angleText) * (this.radius + 70))
                ctx2.rotate(angleTextSelf)
                ctx2.fillText(i+1, 0, 0);
                ctx2.rotate(-(angleTextSelf))
                ctx2.translate(-((this.centerX + Math.cos(angleText) * (this.radius + 70))), -(this.centerY + Math.sin(angleText) * (this.radius + 70)))
                this.drawElements(angleText)
            }
            // Restaure l'état initial du contexte
            ctx2.restore();
        },
        circle(ctx, radius){
            ctx.beginPath();
            ctx.arc(this.centerX, this.centerY, radius, 0, 2 * Math.PI, true);
            ctx.stroke();
        },
        mouseDown(event){
            console.log("down")
            this.selected = true
            this.referX = event.touches[0]["clientX"]
        },
        mouseMove(event){
            if(this.selected) {
                this.angle -= (event.touches[0]["clientX"] - this.referX) / 100
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
            ctx.font = "48px serif";

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