<script lang="ts">
  import Square from './Square.svelte';

  export let squares : any[];
</script>

<style>
  .board-row:after {
    clear: both;
    content: "";
    display: table;
  }
</style>

<div>
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