<script lang="ts">
    import { gameLog, State, logStatus } from "./stores"
    import { fade, blur } from "svelte/transition"


    let cells : any;
    let currentLogStatus : number;
    let currentState : State;
    let winner : State = State.E;
    let finished : boolean = false;
    let lastLog : any;
    gameLog.subscribe(v => { lastLog = v } );
    logStatus.subscribe(n => {
        currentLogStatus = n;
        cells = lastLog[n].board;
        currentState = lastLog[n].before_turn;
        winner = checkWinner();
        finished = (winner !== State.E) ? true : false;
    });

    cells = lastLog[currentLogStatus].board;


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

        let newState : State = currentState == State.O ? State.X : State.O;
        if(lastLog.length - 1 === currentLogStatus){
            console.log("NEW")
            let newBoard : any[][] = JSON.parse(JSON.stringify(lastLog[lastLog.length - 1].board));
            newBoard[coordinate[0]][coordinate[1]] = currentState;
            lastLog.push({
                    board : newBoard,
                    before_turn : newState,
            });
        }
        else {
            console.log("AFTER revert")
            console.log(lastLog);
            let newBoard : any[][] = JSON.parse(JSON.stringify(lastLog[currentLogStatus].board));
            newBoard[coordinate[0]][coordinate[1]] = currentState;
            lastLog = lastLog.slice(0, currentLogStatus+1);
            lastLog.push({
                board : newBoard,
                before_turn : newState,
            });
        }

        gameLog.update(
            v => lastLog
        );

        logStatus.update(n => n + 1)

        cells = lastLog[currentLogStatus].board;
        currentState = lastLog[currentLogStatus].before_turn;
        winner = checkWinner();
        finished = (winner !== State.E) ? true : false;
        
    }

    function resetBoard() {
        logStatus.set(0);
    }

</script>
<div id="board-view">
    {#if winner === State.E}
        <h2>Next player : {#if currentState === State.O} O {:else} X {/if}</h2>
    {:else}
        <h2>Winner is {#if winner === State.O} O {:else} X {/if}</h2>
    {/if}
    <div id="game-board">
        {#each cells as cell_row, i}
            <div class="cell-row">
                {#each cell_row as cell, j}
                    <button id="button_{i}{j}" on:click={clickCell} 
                            disabled={finished || cells[i][j] !== State.E}
                            style={finished || cells[i][j] !== State.E ? "cursor:default": "cursor:pointer"}>
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
    <div>
        <button class="reset-button" on:click={resetBoard}>Reset</button>
    </div>
</div>

<style type="text/scss">
    button {
        width: 59px;
        height: 59px;
        margin: 3px;
        padding: auto;
        border: 0px;
        border-radius: 5px;
        box-shadow: 0 5px 5px #8ec0fa inset, 0 -5px 5px #8ec0fa inset;
        background: #499af7;
        text-align: center;
        color: rgba(0, 0, 0, 1);
    }

    .cell-row {
        display: flex;
    }

    #game-board {
        display: inline-block;
    }

    #board-view {
        border-right: 1px #499af7 solid;
        height: 350px;
    }

    h2 {
		color: #03254c;
		font-size: 2em;
        font-weight: 200;
        margin: 20px;
        margin-top:8px;
        margin-bottom:20px;
        width: 200px;
    }

    .reset-button {
        margin: 20px;
        width: 188px;
        height: 31px;
        padding: auto;
        border: 0px;
        border-radius: 5px;
        background: #8ec0fa;
        text-align: center;
        color: rgba(0, 0, 0, 1);
        cursor: pointer;
    }


</style>