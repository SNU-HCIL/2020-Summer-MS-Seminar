<script lang="ts">
    import { onMount, beforeUpdate } from 'svelte'
    import Board from './Board.svelte'
    import Square from './Square.svelte';

    interface History {
        squares: Array<string>
    }

    let history: Array<History> = [
        {
            squares: Array(9).fill(''),
        },
    ]
    $: current = history[stepNumber];
    let xIsNext: boolean = true;
    let status: string = 'Next player: ' + (xIsNext ? 'X' : 'O');
    let stepNumber: number = 0;

    let jumpTo = (step: number): void => {
        stepNumber = step;
        xIsNext = (step %2) === 0;
        //current = history[stepNumber];
        console.log(stepNumber)
        console.log(current)
    }
    let calculateWinner = (squares: Array<string>): string => {
        const lines = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]
        for (let i = 0; i < lines.length; i++) {
            const [a, b, c] = lines[i]
            if (
                squares[a] &&
                squares[a] === squares[b] &&
                squares[a] === squares[c]
            ) {
                return squares[a]
            }
        }
        return null
    }

    let handleClick = (event): void => {
        let index: number = event.detail.index;

        history = history.slice(0, stepNumber+1);
        const tsq: Array<string> = current.squares.slice();

        if (calculateWinner(tsq) || tsq[index]) {
            return;
        }
        tsq[index] = xIsNext ? 'X' : 'O';
        xIsNext = !xIsNext;
        
        history = [...history,{
            squares: tsq
        }];
        stepNumber = history.length-1;     
        //current = history[stepNumber];
        console.log(history)

    }

    beforeUpdate(() => {
        
        const winner = calculateWinner(current.squares)
        if (winner) {
            status = 'Winner: ' + winner
        } else {
            status = 'Next player: ' + (xIsNext ? 'X' : 'O')
        }
    })
</script>

<style>
    .kbd-navigation .square:focus {
        background: #ddd;
    }

    .game {
        display: flex;
        flex-direction: row;
    }

    .game-info {
        margin-left: 20px;
    }
</style>

<div class="game">
    <div class="game-board">
        <Board 
            squares={current.squares}
            on:click={handleClick}
         />
    </div>
    <div class="game-info">
        <div>{status}</div>
        <div>
            {#each history as hist, move}
                <li>
                    <button on:click={() => jumpTo(move)}>
                        {move? 'Go to move #' + move: 'Go to game start'}
                    </button>
                </li>
            {/each}
        </div>
    </div>
</div>
