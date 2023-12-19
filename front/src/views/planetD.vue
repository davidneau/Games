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
            refTime: 0,
            touchX: 0,
            touchY: 0,
            initialize: true,
            repere: {},
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
            referAngleText18: {
                "1": -5,
                "2": -4,
                "3": -3,
                "4": -2,
                "5": -1,
                "6": 0,
                "7": 1,
                "8": 2,
                "9": 3,
                "10": 4,
                "11": 5,
                "12": 6,
                "13": 7,
                "14": 8,
                "15": 9,
                "16": -8,
                "17": -7,
                "18": -6,
            },
            sectorCliked: "",
            elementClicked: "",
            statusElements: {},
            element: ["comet", "asteroid", "planeteNaine", "nuageDeGaz", "vide", "planeteD"],
            stars: []
        }
    },
    methods: {
        repereFill(){
            let j=0
            let List = [j]
            let ListN = []
            for (let i=2; i<8; i++){
                List.push((j + this.radius*i/8)/2)
                ListN.push(this.radius*i/8)
                j=this.radius*i/8
            }
            List.splice(1, 1);
            console.log(List)
            console.log(ListN)
            List.push(this.radius)
            this.repere = List
/*             let k=0
            this.element.forEach(element => {
                this.repere[element] = [List[k], List[k+1]]
                k = k+1
            });
            this.repere["planeteD"][1] = 100000
            console.log(this.repere)
 */        },
        line(moveToX, moveToY, lineToX, lineToY, ctx){
            // Start a new Path
            ctx.beginPath();
            ctx.moveTo(moveToX, moveToY);
            ctx.lineTo(lineToX, lineToY);
            ctx.stroke();
        },
        transformation(angle, x, y){
            let x1 = Math.cos(this.angle) * x - Math.sin(this.angle) * y
            let y1 = Math.sin(this.angle) * x + Math.cos(this.angle) * y
            let rayon = Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2))
            let newAngle = (Math.PI*2) - (Math.atan2(y1, x1) + Math.PI*2) % (Math.PI*2)
            let sector = Math.trunc(newAngle/ ((Math.PI*2)/this.numberOfSector))+1
            this.sectorCliked = sector
            let i=0
            let result = ""
            this.repere.forEach((element) => {
                if((element > rayon) && (result == "")){
                    result = this.element[i-1]
                    this.elementClicked = this.element[i-1]
                }
                i+=1
            })
            this.changeStatus()
            console.log(this.statusElements)
            return result
        },
        changeStatus(){
            console.log("sector", (this.sectorCliked+3) % this.numberOfSector)
            if (!this.initialize){
                if (this.statusElements[(this.sectorCliked+3) % this.numberOfSector][this.elementClicked] == ""){this.statusElements[(this.sectorCliked+3) % this.numberOfSector][this.elementClicked] = "cross"}
                else if (this.statusElements[(this.sectorCliked+3) % this.numberOfSector][this.elementClicked] == "cross"){this.statusElements[(this.sectorCliked+3) % this.numberOfSector][this.elementClicked] = "circle"}
                else {this.statusElements[(this.sectorCliked+3) % this.numberOfSector][this.elementClicked] = ""}
            }
        },
        drawStatus(centerX, centerY, status){
            console.log(status)
            let canvas = this.$refs.monCanvas
            let ctx = canvas.getContext("2d")
            ctx.lineWidth = 4;
            if (!this.initialize){
                if (status == "cross"){
                    console.log("drawred")
                    ctx.strokeStyle = "red"
                    for(let i=0; i<4; i++){
                        ctx.beginPath();
                        let angle = Math.PI/4 + i * Math.PI/2
                        ctx.moveTo(centerX, centerY);
                        ctx.lineTo(centerX + Math.cos(angle) * 15, centerY + Math.sin(angle) * 15);
                        ctx.moveTo(centerX, centerY);
                        ctx.stroke();
                    }
                }
                else if (status == "circle"){
                    ctx.strokeStyle = "green"
                    ctx.beginPath();
                    ctx.arc(centerX, centerY, 20, 0, 2 * Math.PI, true);
                    ctx.stroke();   
                }
            }
            ctx.lineWidth = 1;
        },
        drawElement(centerX, centerY, element, angle, numSector){
            let canvas = this.$refs.monCanvas
            let ctx = canvas.getContext("2d")

            ctx.translate(centerX, centerY)
            ctx.lineWidth = 1;
            ctx.strokeStyle = "white"

            angle += Math.PI/2
            ctx.rotate(angle)

            let oldCenterX = centerX
            let oldCenterY = centerY

            centerX=0
            centerY=0

            if(element == "comet"){
                this.line(0-4, 0-4, 0-6, 0+2, ctx)
                this.line(0-6, 0+2, 0-5, 0+2, ctx)
                this.line(0-5, 0+2, 0-8, 0+8, ctx)
                this.line(0-8, 0+8, 0-2, 0+5, ctx)
                this.line(0-2, 0+5, 0-2, 0+6, ctx)
                this.line(0-2, 0+6, 0+4, 0+4, ctx)
                ctx.arc(0, 0, 3, 0, Math.PI*2, false)
                ctx.stroke()
                ctx.arc(0, 0, 6, Math.PI/4, -3 * Math.PI/4, true)
                ctx.stroke()
            }
            if(element == "asteroid"){
                this.line(centerX-9, centerY, centerX-6, centerY-3, ctx)
                this.line(centerX-6, centerY-3, centerX-3, centerY-9, ctx)
                this.line(centerX-3, centerY-9, centerX+3, centerY-9, ctx)
                this.line(centerX+3, centerY-9, centerX+9, centerY-3, ctx)
                this.line(centerX+9, centerY-3, centerX+9, centerY, ctx)
                this.line(centerX+9, centerY, centerX, centerY+9, ctx)
                this.line(centerX, centerY+9, centerX-3, centerY+9, ctx)
                this.line(centerX-3, centerY+9, centerX-9, centerY+3, ctx)
                this.line(centerX-9, centerY+3, centerX-9, centerY, ctx)
                
                this.line(centerX+1, centerY-3, centerX+3, centerY-5, ctx)
                this.line(centerX+3, centerY-5, centerX+1, centerY-7, ctx)
                this.line(centerX+1, centerY-7, centerX-1, centerY-5, ctx)
                this.line(centerX-1, centerY-5, centerX+1, centerY-3, ctx)
                
                this.line(centerX+3, centerY+1, centerX+5, centerY+1, ctx)
                this.line(centerX+5, centerY+1, centerX+5, centerY-1, ctx)
                this.line(centerX+5, centerY-1, centerX+3, centerY-1, ctx)
                this.line(centerX+3, centerY-1, centerX+3, centerY+1, ctx)
                
                this.line(centerX-2, centerY+2, centerX, centerY+4, ctx)
                this.line(centerX, centerY+4, centerX-2, centerY+6, ctx)
                this.line(centerX-2, centerY+6, centerX-4, centerY+4, ctx)
                this.line(centerX-4, centerY+4, centerX-2, centerY+2, ctx)
                
                this.line(centerX-8, centerY-5, centerX-10, centerY-5, ctx)
                this.line(centerX-10, centerY-5, centerX-10, centerY-7, ctx)
                this.line(centerX-10, centerY-7, centerX-8, centerY-7, ctx)
                this.line(centerX-8, centerY-7, centerX-8, centerY-5, ctx)
            }
            if(element == "nuageDeGaz"){
                ctx.beginPath();
                ctx.arc(centerX-8, centerY+2, 5, -Math.PI/2, Math.PI /4, true)
                ctx.stroke();
                ctx.beginPath();
                ctx.arc(centerX-4, centerY-3, 4, -Math.PI/4, -Math.PI, true)
                ctx.stroke();
                ctx.beginPath();
                ctx.arc(centerX+2, centerY-3, 4, -Math.PI/4, -Math.PI * 3/4, true)
                ctx.stroke();
                ctx.beginPath();
                ctx.arc(centerX+8, centerY-2, 5, -3*Math.PI/4, Math.PI/2, false)
                ctx.stroke();
                ctx.beginPath();
                ctx.arc(centerX+4, centerY+3, 4, 0, Math.PI*3/4, false)
                ctx.stroke();
                ctx.beginPath();
                ctx.arc(centerX-2, centerY+3, 4, Math.PI/4, 3*Math.PI/4, false)
                ctx.stroke();
            }
            if(element == "planeteNaine"){
                ctx.lineWidth = 2;
                this.line(centerX + Math.cos(Math.PI * 3/4) * 10, 
                          centerY + Math.sin(Math.PI * 3/4) * 10, 
                          centerX + Math.cos(Math.PI * 3/4) * 10 + 5, 
                          centerY + Math.sin(Math.PI * 3/4) * 10, 
                          ctx)
                this.line(centerX + Math.cos(Math.PI * -3/4) * 10, 
                          centerY + Math.sin(Math.PI * -3/4) * 10, 
                          centerX + Math.cos(Math.PI * -3/4) * 10 + 10, 
                          centerY + Math.sin(Math.PI * -3/4) * 10, 
                          ctx)
                this.line(centerX-7, centerY, centerX + 10, centerY, ctx)
                ctx.lineWidth = 1;

                ctx.arc(centerX, centerY, 10, 0, 2 * Math.PI, true)
                ctx.stroke()
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
                ctx.stroke()
            }
            this.drawStatus(centerX, centerY, this.statusElements[numSector][element])
            ctx.rotate(-angle)
            ctx.translate(-oldCenterX, -oldCenterY)
        },
        drawElements(angle, numSector) {
            let canvas = this.$refs.monCanvas
            let ctx = canvas.getContext("2d")
            for (let i=2; i<8; i++){
                if (this.statusElements[numSector][this.element[i-2]] == undefined){this.statusElements[numSector][this.element[i-2]] = ""}
                let radius = this.radius*i/8
                ctx.beginPath();
                this.drawElement(this.centerX + Math.cos(angle) * (radius), this.centerY + Math.sin(angle) * radius, this.element[i-2], angle, numSector);
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
            ctx2.fillStyle = "white"
            this.fillTheSky()
            this.circle(ctx2, this.radius);
            this.circle(ctx2, this.radius + 30);
            for (let i=0; i<this.numberOfSector; i++){
                if (this.statusElements[i+1] == undefined){this.statusElements[i+1] = {}}
                let angle = Math.PI * i / (this.numberOfSector/2)
                this.line(this.centerX, this.centerY, this.centerX + Math.cos(angle) * this.radius, this.centerY + Math.sin(angle) * this.radius, ctx2)
                let angleText = angle + (Math.PI / (this.numberOfSector/2)) / 2
                let angleTextSelf = (this.referAngleText[i+1] + 0.5) * (Math.PI / (this.numberOfSector/2))
                ctx2.translate((this.centerX + Math.cos(angleText) * (this.radius + 70)), this.centerY + Math.sin(angleText) * (this.radius + 70))
                ctx2.rotate(angleTextSelf)
                ctx2.fillText(i+1, 0, 0);
                ctx2.rotate(-(angleTextSelf))
                ctx2.translate(-((this.centerX + Math.cos(angleText) * (this.radius + 70))), -(this.centerY + Math.sin(angleText) * (this.radius + 70)))
                this.drawElements(angleTextSelf, i+1)
            }
            console.log(this.statusElements)
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
            this.refTime = Date.now()
            this.selected = true
            this.touchX = event.touches[0]["clientX"] - window.innerWidth /2
            this.touchY = - event.touches[0]["clientY"] + 64
            this.referX = event.touches[0]["clientX"]
        },
        mouseMove(event){
            console.log(this.selected)
            if(this.selected) {
                this.angle -= (event.touches[0]["clientX"] - this.referX) / 100
                this.draw()
                this.referX = event.touches[0]["clientX"]
            }
        },
        mouseUp(){
            console.log("up")
            this.selected = false
            if((Date.now() - this.refTime) < 200) {
                this.transformation(this.angle, this.touchX, this.touchY)
                this.draw()
            }
        },
        resizeCanvas(canvas) {
            console.log(window.innerWidth)
            canvas.width = window.innerWidth;
            canvas.height = window.innerWidth;
        },
        setStars() {
            for (let i=0; i<100; i++){
                this.stars.push([Math.floor((Math.random() * this.radius * 2) - this.radius/2), Math.floor((Math.random() * this.radius * 2) - this.radius/2)])
            }
        },
        fillTheSky() {
            let canvas = this.$refs.monCanvas
            let ctx = canvas.getContext("2d")
            this.stars.forEach(element => {
                ctx.beginPath();
                ctx.fillStyle="white"
                ctx.arc(element[0], element[1], 2, 0, 2 * Math.PI);
                ctx.fill(); 
            });
        },
        setSize(){
            window.onload = function(){
                window.addEventListener('load', this.resizeCanvas());
                window.addEventListener('resize', this.resizeCanvas());    
            }
        },
        init() {
            var canvas = this.$refs.monCanvas
            var ctx = canvas.getContext("2d")

            this.repereFill()
            this.setStars()

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
            this.initialize = false;
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
    background-color: "#0f056b";
    aspect-ratio: 1 / 1;
}
</style>