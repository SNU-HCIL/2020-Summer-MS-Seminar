<script lang="ts">
    import {BoardState} from './BoardState'
    import {BoardManager} from './BoardManager'
    import {onMount} from 'svelte'
    
    export const width = 3;
    export const height = 3;

    export const cell_width = 35;
    export const cell_height = 35;
    
    export const color_stroke = "black";

    let board_width = 1 + width * cell_width;
    let board_height = 1 + height * cell_height;
    
    
    const gameHistory = BoardManager.gameHistory;
    const gameStatus = BoardManager.gameStatus;

    let canvas: HTMLElement;

    gameHistory.push(new BoardState(width, height))
    
    function handleClick(event: MouseEvent){
        let x = Math.trunc((event.offsetX + 0.5) / cell_width)
        let y = Math.trunc((event.offsetY + 0.5)/ cell_height)
        let i = y * width + x

        const currState = $gameHistory.currentState()
        if($gameStatus == "Win" || currState.cells[i] != '')
            return;

        const currCells = [... currState.cells]
        currCells[i] = currState.turnOfTheFirst ? 'O' : 'X'
        
        let newState = new BoardState(width, height)
        newState.cells = currCells
        newState.turnOfTheFirst = !currState.turnOfTheFirst

        gameHistory.push(newState)
    }

    onMount( () => {
            const context = (canvas as HTMLCanvasElement).getContext('2d')
            function draw(){
                if (context == null)
                    return;
                context.clearRect(0, 0, board_width, board_height)
                
                context.beginPath();
                
                for (let x= 0; x <=board_width; x += cell_width){
                    context.moveTo(0.5 + x, 0)
                    context.lineTo(0.5 + x, board_height)
                }

                for (let y=0; y <=board_height; y += cell_height){
                    context.moveTo(0, 0.5 + y)
                    context.lineTo(board_width, 0.5 + y)
                }

                context.strokeStyle = color_stroke
                context.stroke()

                context.closePath()

                context.beginPath();

                context.font = "bold 22px Roboto";
                let d = 8;
                let k = 0;
                for (let i = 0; i < height; i+=1) {
                    for (let j = 0; j < width; j+=1) {
                        context.fillText($gameHistory.currentState().cells[k], j * cell_width + d + 1, (i + 1) * cell_height - d);
                        k++;
                    }
                }

                context.closePath();
                requestAnimationFrame(draw);
            }
            draw();
        }
    )

</script>
<canvas
    bind:this = {canvas}
    width = {board_width}
    height = {board_height}
    on:click = {handleClick}>
</canvas>