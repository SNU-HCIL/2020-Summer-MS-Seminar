<script lang="ts">
  import Board from './Board.svelte';
  import Square from './Square.svelte';
  import { login } from './stores';
  import { fade } from 'svelte/transition';
  import { onMount } from 'svelte';
  import axios from 'axios';
  import { navigate } from 'svelte-routing';

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

  let record = {
    'total': 0,
    'win': 0,
    'draw': 0,
    'lose': 0
  };

  async function getRecord() {
    try {
      const res = await axios.get(
        'http://127.0.0.1:8000/records',
        {
          withCredentials: true
        }
      );
      if (res.status === 200) {
        record = res.data;
        console.log(res.data);
        return;
      }
    } catch (error) {
      if (error.response) {
        throw new Error(error.response);
      }
      else {
        navigate("info");
        return;
      }
    }
  }
</script>

<style>
  .game {
    display: flex;
    flex-direction: row;
  }

  .game-info {
    margin-left: 20px;
  }
</style>

<div class="game">
  <div>
    <div>
      {#if winner}
      {"Winner: " + winner}
      {:else}
      {"Next player: " + (state.xIsNext ? "X" : "O")}
      {/if}
    </div>
    <Board
      squares={state.history[state.stepNumber].squares}
      on:message={handleClick}
    />
  </div>
  <div class="game-info">
    {#await getRecord}
      <p>전적을 불러오는 중입니다...</p>
    {:then data} 
      <p>{record.total}전 {record.win}승 {record.draw}무 {record.lose}패</p>
    {:catch error}
      <p>{error}</p>
    {/await}
  </div>
</div>