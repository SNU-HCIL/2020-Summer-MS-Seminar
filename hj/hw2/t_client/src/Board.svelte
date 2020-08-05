<script lang="ts">
    import { gameLog, State, logStatus, idStore } from "./stores"
    import { winStore, loseStore, drawStore } from "./stores"
    import { fade, blur } from "svelte/transition"
    import axios from 'axios'

    let id : string;

    idStore.subscribe(v => { id = v; } );

    let domain = "http://localhost:8000/login/";

    async function getToken() {
        await axios.get(domain, { withCredentials: true });
    }

    function getCookie(name: string): string {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }


    let cells : any;
    let currentLogStatus : number;
    let currentState : State;
    let winner : State = State.E;
    let finished : boolean = false;
    let lastLog : any;
    let isDraw : boolean = false;
    let aiThinking : boolean = false;

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

    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    async function clickCell() {
        let coorStr : string = this.id.slice(7,9);
        let coordinate : [number, number] = [parseInt(coorStr[0]), parseInt(coorStr[1])];

        // log capture

        let newState : State = currentState == State.O ? State.X : State.O;
        if(lastLog.length - 1 === currentLogStatus){
            let newBoard : any[][] = JSON.parse(JSON.stringify(lastLog[lastLog.length - 1].board));
            newBoard[coordinate[0]][coordinate[1]] = currentState;
            lastLog.push({
                    board : newBoard,
                    before_turn : newState,
            });
        }
        else {
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

        // draw case
        if(currentLogStatus == 9 && winner == State.E) {
            finished = true;
            isDraw = true;
        }
        
        if(finished) {
            let result : string = isDraw ? "draw" : (winner === State.O ? "lose" : "win");
            await getToken();
            const csrftoken : string = getCookie("csrftoken");
            const response = await axios.put(domain + "gameResult/", 
            {
                id: id,
                gameResult: result,
            },
            {
                withCredentials: true,
                headers: {
                    "X-CSRFToken" : csrftoken
                },
            });
            switch(result){
                case "win" : winStore.update(v => response.data.win);  break;
                case "lose": loseStore.update(v => response.data.lose); break;
                case "draw": drawStore.update(v => response.data.draw); break;
            }
            return;
        }
        else {
            // AI Turn (needs refactoring...)
            let board : any[][] = lastLog[lastLog.length - 1].board;
            let input : string = "";
            for(let i = 0; i < 3; i++) 
                for(let j = 0; j < 3; j++) {
                    if      (board[i][j] == 0) input += "N";
                    else if (board[i][j] == 1) input += "O";
                    else                       input += "X";
                }
            const response = await axios.get(domain + "aiTurn/" + input + "/");
            // ai thinking...
            aiThinking = true;
            await sleep(2500);
            aiThinking = false;
            // ai thinking ends
            let coordRaw : number = parseInt(response.data);
            coordinate = [Math.floor(coordRaw / 3), coordRaw % 3];
            let newState : State = currentState == State.O ? State.X : State.O;
            if(lastLog.length - 1 === currentLogStatus){
                let newBoard : any[][] = JSON.parse(JSON.stringify(lastLog[lastLog.length - 1].board));
                newBoard[coordinate[0]][coordinate[1]] = currentState;
                lastLog.push({
                        board : newBoard,
                        before_turn : newState,
                });
            }
            else {
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

            // draw case
            if(currentLogStatus == 9 && winner == State.E) {
                finished = true;
                isDraw = true;
            }
            
            if(finished) {
                let result : string = isDraw ? "draw" : (winner === State.O ? "lose" : "win");
                await getToken();
                const csrftoken : string = getCookie("csrftoken");
                const response = await axios.put(domain + "gameResult/", 
                {
                    id: id,
                    gameResult: result,
                },
                {
                    withCredentials: true,
                    headers: {
                        "X-CSRFToken" : csrftoken
                    },
                });
                switch(result){
                    case "win" : winStore.update(v => response.data.win);  break;
                    case "lose": loseStore.update(v => response.data.lose); break;
                    case "draw": drawStore.update(v => response.data.draw); break;
                }
                return;
            }

        }
    }

    function resetBoard() {
        logStatus.set(0);
        winner = State.E;
        isDraw = false;
        finished = false;
    }

</script>
<div id="board-view">
    {#if isDraw}
        <h2>Draw!!</h2>
    {:else if winner === State.E}
        <h2>{#if currentState === State.O} AI's turn {:else} Your turn {/if}</h2>
    {:else}
        <h2>{#if winner === State.O} You lose!! {:else} You win!! {/if}</h2>
    {/if}
    <div id="game-board">
        {#each cells as cell_row, i}
            <div class="cell-row">
                {#each cell_row as cell, j}
                    <button id="button_{i}{j}" on:click={clickCell} 
                            disabled={aiThinking || finished || cells[i][j] !== State.E}
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