<script>
    // import Select from 'svelte-select';
    
    let board = [["", "", ""], ["", "", ""], ["", "", ""]];
    let turn = 'X';
    let checked = [[false, false, false], [false, false, false], [false, false, false],]
    let win = null;
    let boards = [];

    function onclick(rowIndex, colIndex) {
        if(win === null) {
            if(!checked[rowIndex][colIndex]) {
                board[rowIndex][colIndex] = turn;
                let board_hist = [rowIndex, colIndex, turn]
                turn = turn === 'X' ? 'O' : 'X';
                checked[rowIndex][colIndex] = true;
                boards.push(board_hist);

                for (let i = 0; i < lines.length; i++) {
                    let result = ["", "", ""];
                    for (let j = 0; j < 3; j++) {
                        let first = parseInt(lines[i][j] / 3);
                        let second = lines[i][j] % 3
                        result[j] = board[first][second];
                    }
                    if (result[0] && result[0] === result[1] && result[0] === result[2]) {
                        win = result[0];
                    }
                }
            }
        }
    }

    function restart() {
        board = [["", "", ""], ["", "", ""], ["", "", ""]];
        turn = 'X'
        win = null;
        boards = [];
        checked = [[false, false, false], [false, false, false], [false, false, false],]
    }

    const lines = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ];

    function backToHistory() {
        if (boards.length > 0) {
            if (win == null) {
                let last = boards.length;
                board[boards[last-1][0]][boards[last-1][1]] = "";
                checked[boards[last-1][0]][boards[last-1][1]] = false;
                boards.pop();
                turn = turn === 'X' ? 'O' : 'X';
            }
        }
    }
</script>

<style>
    table {
        width: 100%;
        max-width: 800px;
        border-collapse: collapse;
        font-size: 12em;
        }
    td {
        border: 1px solid;
        text-align: center;
        height: 1.2em;
        width: 1.2em;
    }
</style>

<h2>Let's play Tic Tac Toe!</h2>

<button on:click={() =>restart()}>Restart the game!</button>

<table>
    <tbody>
        {#each board as row, rowIndex}
            <tr>
                {#each row as col, colIndex}
                    <td on:click={() => onclick(rowIndex, colIndex)}>{col}</td>
                {/each}
            </tr>
        {/each}
    </tbody>
</table>

{#if win != null}
    <h1>{win} win!</h1>
{:else}
    <h3>Now: {turn}'s turn... </h3>
{/if}

<button on:click={() => backToHistory()}>Go back to previous step!</button>