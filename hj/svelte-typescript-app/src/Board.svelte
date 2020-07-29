<script lang="ts">
    import { gameLog, State, logStatus } from "./stores"
    import { fade } from "svelte/transition"


    let cells : any;
    let currentLogStatus : number;
    let currentState : State;
    gameLog.subscribe(v => { 
        logStatus.subscribe(n => {
            currentLogStatus = n;
            cells = v[n].board;
            currentState = v[n].before_turn;
        })
     });


    let winner : State = State.E;
    let finished : boolean = false;

    function checkIdentity(a : any, b : any, c : any) : boolean {
        if (a === b && b === c) return true;
        else                    return false;
    }

    function checkWinner() : State {
        // horizontal
        for(let i = 0; i < 3; i++)   
            if (checkIdentity(cells[i][0], cells[i][1], cells[i][2]) && cells[i][0] !== State.E) return cells[i][0];

        // vertical
        for(let i = 0; i < 3; i++)   
            if (checkIdentity(cells[0][i], cells[1][i], cells[2][i]) && cells[0][i] !== State.E) return cells[0][i];

        // diagonal
        if (checkIdentity(cells[0][0], cells[1][1], cells[2][2]) && cells[0][0] !== State.E) return cells[0][0];
        if (checkIdentity(cells[0][2], cells[1][1], cells[2][0]) && cells[0][2] !== State.E) return cells[0][2];

        return State.E; 
    }

    function clickCell() {
        let coorStr : string = this.id.slice(7,9);
        let coordinate : [number, number] = [parseInt(coorStr[0]), parseInt(coorStr[1])];

        // log capture

        let lastLog : any;
        gameLog.subscribe(v => { lastLog = v } );
        console.log("LASTLOG", lastLog)


        let newState : State = currentState == State.O ? State.X : State.O;
        if(lastLog.length - 1 === currentLogStatus){
            let newBoard : any[][] = JSON.parse(JSON.stringify(lastLog[lastLog.length - 1].board));
            newBoard[coordinate[0]][coordinate[1]] = currentState;
            lastLog.push({
                    board : newBoard,
                    before_turn : newState,
            });
            logStatus.update(n => n + 1)
        }
        else {
            let newBoard : any[][] = JSON.parse(JSON.stringify(lastLog[currentLogStatus].board));
            newBoard[coordinate[0]][coordinate[1]] = currentState;
            lastLog[currentLogStatus++] = {
                board : newBoard,
                before_turn : newState,
            }
        }
        
        gameLog.set(
            lastLog
        );



        cells = lastLog[currentLogStatus].board;

        winner = checkWinner();
        if (winner !== State.E) finished = true;
        
    }

</script>
<div>
    <h2>
        {#if winner === State.E}
            Next player : {#if currentState === State.O} O {:else} X {/if}
        {:else}
            Winner is {#if winner === State.O} O {:else} X {/if} 
        {/if}
    </h2>
    <div id="game-board">
        {#each cells as cell_row, i}
            <div class="cell-row">
                {#each cell_row as cell, j}
                    <button id="button_{i}{j}" on:click={clickCell} disabled={finished || cells[i][j] !== State.E}>
                        {#if cell != State.E}
                            <span transition:fade>
                                {#if cell == State.O} O {:else} X {/if}
                            </span>
                        {/if}
                    </button>
                {/each}
            </div>
        {/each}
    </div>
</div>

<style type="text/scss">
    button {
        width: 50px;
        height: 50px;
        margin: 3px;
        padding: auto;
        border: 0px;
        border-radius: 5px;
        box-shadow: 0 5px 5px #8ec0fa inset, 0 -5px 5px #8ec0fa inset;
        background: #499af7;
        text-align: center;
        color: rgba(0, 0, 0, 1)
    }

    .cell-row {
        display: flex;
    }

    #game-board {
        display: inline-block;
    }

    h2 {
		color: #03254c;
		font-size: 2em;
        font-weight: 300;
        margin: 20px;
    }


</style>