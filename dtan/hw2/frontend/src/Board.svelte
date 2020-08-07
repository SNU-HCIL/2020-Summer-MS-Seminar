<script lang="ts">
  import Square from './Square.svelte';

  export let squares : any[];
</script>

<style>
  .game-board {
    display: table;
  }

  .board-row:after {
    clear: both;
    content: "";
    display: table-row;
    margin-top: 0px;
    margin-bottom: 0px;
  }
</style>

<div class="game-board">
  <div class="board-row">
    <Square index={0} state={squares} on:message />
    <Square index={1} state={squares} on:message />
    <Square index={2} state={squares} on:message />
  </div>
  <div class="board-row">
    <Square index={3} state={squares} on:message />
    <Square index={4} state={squares} on:message />
    <Square index={5} state={squares} on:message />
  </div>
  <div class="board-row">
    <Square index={6} state={squares} on:message />
    <Square index={7} state={squares} on:message />
    <Square index={8} state={squares} on:message />
  </div>
</div>