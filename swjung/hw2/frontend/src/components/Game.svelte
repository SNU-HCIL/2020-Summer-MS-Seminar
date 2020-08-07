<script lang="ts">
    import { onMount, beforeUpdate } from 'svelte'
    import Board from './Board.svelte'
    import Square from './Square.svelte';
    import { page } from '../store';
    import axios from 'axios';


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
    }
    let aiPlayed: number;
    
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
    }

    beforeUpdate(() => {
        
        const winner = calculateWinner(current.squares)
        if (winner) {
            status = 'Winner: ' + winner
        } else {
            status = 'Next player: ' + (xIsNext ? 'X' : 'O')
        }
    })

    function handleLogOut() {
        page.set('login');
    }
    function handleReset() {
        let index: number = 0;

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
</script>

<style>
    .game {
        display: flex;
        flex-direction: row;
    }

</style>

<div class="game">
    <button on:click={() => jumpTo(0)}> Reset </button>
    <div> {status} </div>
    <div class="game-board">
        <Board 
            squares={current.squares}
            on:click={handleClick}
         />
    </div>
    <div class="user-record">
        User Record
    </div>
</div>
