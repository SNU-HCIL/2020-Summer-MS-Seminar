<script lang="ts">
  import Board from './Board.svelte'
  import type Square from './Square.svelte';
  import { fade } from 'svelte/transition';

  let state = {
    history: [
      {
        squares: Array(9).fill(null)
      }
    ],
    stepNumber: 0,
    xIsNext: true
  };

  $: winner = calculateWinner(state.history[state.stepNumber].squares);

  function calculateWinner(squares) {
    const lines = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6]
    ];

    for (let i = 0; i < lines.length; i++) {
      const [a, b, c] = lines[i];
      if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
        return squares[a];
      }
    }

    return null;
  }

  function handleClick(event) {
    const history = state.history.slice(0, state.stepNumber + 1);
    const current = history[history.length - 1];
    const squares = current.squares.slice();

    if (calculateWinner(squares) || squares[event.detail.index]) {
      return;
    }

    squares[event.detail.index] = state.xIsNext ? "X" : "O";

    state.history = [...history, {
      squares: squares
    }];
    state.stepNumber = history.length;
    state.xIsNext = !state.xIsNext;
    //state = state;
  }

  function jumpTo(step: number) {
    state.stepNumber = step;
    state.xIsNext = (step % 2) === 0;
    //state = state;
  }
</script>

<style>
  ol {
    padding-left: 30px;
  }

  .game {
    display: flex;
    flex-direction: row;
  }

  .game-info {
    margin-left: 20px;
  }

  .current-step {
    color: #d6225e;
    border-color: #d3849e;
  }

  .other-step {
    color: #000;
  }
</style>

<div class="game">
  <div class="game-board">
    <Board
      squares={state.history[state.stepNumber].squares}
      on:message={handleClick}
    />
  </div>
  <div class="game-info">
    <div>
      {#if winner}
      {"Winner: " + winner}
      {:else}
      {"Next player: " + (state.xIsNext ? "X" : "O")}
      {/if}
    </div>
    <ol>
      {#each state.history as log, i (log)}
        <li in:fade
          class={i === state.stepNumber ? "current-step" : "other-step"}>
          <button on:click={() => jumpTo(i)}
            class={i === state.stepNumber ? "current-step" : "other-step"}>
            {i ? 'Go to move #' + i : 'Go to game start'}
          </button>
        </li>
      {/each}
    </ol>
  </div>
</div>