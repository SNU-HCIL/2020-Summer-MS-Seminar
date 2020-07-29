<script lang="ts">
  import Square from "./Square.svelte";
  import { fly, fade } from "svelte/transition";

  let histories = [
    {
      OXs: Array(9).fill(null),
    },
  ];
  let stepNumber: number = 0;
  let xIsNext: boolean = true;

  let current = histories[stepNumber];
  let winner = calculateWinner(current.OXs);

  function onClick(i: number) {
    const history = histories.slice(0, stepNumber + 1);
    const current = history[history.length - 1];
    const OXs = current.OXs.slice();

    if (calculateWinner(OXs) || OXs[i]) {
      return;
    }

    OXs[i] = xIsNext ? "X" : "O";

    histories = history.concat([
      {
        OXs: OXs,
      },
    ]);
    stepNumber = history.length;
    xIsNext = !xIsNext;

    update();
  }

  function moveTo(i: number) {
    stepNumber = i;
    xIsNext = stepNumber % 2 === 0;
    update();
  }

  function calculateWinner(squares) {
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

    for (let i = 0; i < lines.length; i++) {
      const [a, b, c] = lines[i];
      if (
        squares[a] && squares[a]
        === squares[b] && squares[b]
        === squares[c] && squares[c]
      ) {
        return squares[a];
      }
    }
    return null;
  }

  function update() {
    current = histories[stepNumber];
    winner = calculateWinner(current.OXs);
  }
</script>

<style>
  .board {
    position: relative;
    padding: 2em;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
  }
  .row {
    float: left;
  }
  .console {
    float: left;
  }
</style>

<div class="console">
  <div class="board">
    {#each current.OXs as OX, i}
      <div class="row">
        <Square value={OX} onClick={() => onClick(i)} />
      </div>
      {#if (i + 1) % 3 == 0}
        <div />
      {/if}
    {/each}
  </div>

  <div>

    {#if !winner}
      Next Player
      {#if xIsNext}
        <p in:fade={{ duration: 500 }}>X</p>
      {:else}
        <p in:fade={{ duration: 500 }}>O</p>
      {/if}
    {:else}
      Winner
      <p in:fade={{ duration: 500 }}>{winner}</p>
    {/if}

  </div>

  <ol>
    {#each histories as _, i}
      {#if i == 0}
        <li in:fly={{ y: 20, duration: 500 }} out:fade>
          <button on:click={() => moveTo(i)}>Go to game start</button>
        </li>
      {:else}
        <li in:fly={{ y: 20, duration: 500 }} out:fade>
          <button on:click={() => moveTo(i)}>Go to move #{i}</button>
        </li>
      {/if}
    {/each}
  </ol>
</div>
