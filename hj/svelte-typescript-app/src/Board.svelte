<script lang="ts">
    import { gamePlay } from "./stores"
    import { fade } from "svelte/transition"
    // cells를 여기 binding해서 value로 바꿔줘야 밑에서 사용가능할듯!!
    // cell 정보는 어차피 여기서만 쓰니까 store로 안해도 될듯

    enum State {
        E = 0, O, X      // empty, O, X
    }

    let cells : State[][] = [      // stores the current status of game board cells
        [State.E, State.E, State.E],
        [State.E, State.E, State.E],
        [State.E, State.E, State.E]
    ];

    let currentState : State = State.O;
    let winner : State = State.E;
    let disabled : boolean = false;

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

        cells[coordinate[0]][coordinate[1]] = currentState;
        cells = cells;

        currentState = currentState == State.O ? State.X : State.O;

        winner = checkWinner();
        if (winner !== State.E) disabled = true;
        
    }

</script>

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
                <button id="button_{i}{j}" on:click={clickCell} {disabled}>
                    {#if cell != State.E}
                        <span transition:fade>
                            {#if cell == State.O}
                                O
                            {:else}
                                X
                            {/if}
                        </span>
                    {/if}
                </button>
            {/each}
        </div>
    {/each}
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
        color: rgba(0, 0, 0, 0.5)
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
    }


</style>